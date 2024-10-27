import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

# Initialize the main application window
class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking Tool")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Initialize variables
        self.image_path = None
        self.watermark_type = tk.StringVar(value="text")
        self.watermark_text = tk.StringVar()
        self.logo_path = None

        # Set up the GUI components
        self.setup_gui()

    def setup_gui(self):
        # Frame for image display
        self.image_frame = tk.Frame(self.root, width=600, height=400, bg="grey")
        self.image_frame.pack(pady=20)

        self.image_label = tk.Label(self.image_frame)
        self.image_label.pack()

        # Frame for controls
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)

        # Button to upload image
        upload_btn = tk.Button(control_frame, text="Upload Image", command=self.upload_image)
        upload_btn.grid(row=0, column=0, padx=10)

        # Radio buttons to select watermark type
        text_rb = tk.Radiobutton(control_frame, text="Text Watermark", variable=self.watermark_type, value="text")
        text_rb.grid(row=0, column=1, padx=10)

        logo_rb = tk.Radiobutton(control_frame, text="Logo Watermark", variable=self.watermark_type, value="logo")
        logo_rb.grid(row=0, column=2, padx=10)

        # Entry for text watermark
        self.text_entry = tk.Entry(control_frame, textvariable=self.watermark_text, width=30)
        self.text_entry.grid(row=1, column=0, columnspan=3, pady=10)
        self.text_entry.insert(0, "Enter watermark text here")

        # Button to upload logo
        self.logo_btn = tk.Button(control_frame, text="Upload Logo", command=self.upload_logo)
        self.logo_btn.grid(row=2, column=0, padx=10, pady=10)
        self.logo_btn.config(state=tk.DISABLED)  # Disabled by default

        # Button to add watermark
        add_watermark_btn = tk.Button(control_frame, text="Add Watermark", command=self.add_watermark)
        add_watermark_btn.grid(row=2, column=2, padx=10, pady=10)

        # Update the UI based on watermark type selection
        self.watermark_type.trace("w", self.update_ui)

    def update_ui(self, *args):
        if self.watermark_type.get() == "logo":
            self.text_entry.config(state=tk.DISABLED)
            self.logo_btn.config(state=tk.NORMAL)
        else:
            self.text_entry.config(state=tk.NORMAL)
            self.logo_btn.config(state=tk.DISABLED)

    def upload_image(self):
        # Open a file dialog to select an image
        filetypes = (
            ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"),
            ("All files", "*.*")
        )
        filepath = filedialog.askopenfilename(title="Select Image", filetypes=filetypes)
        if filepath:
            self.image_path = filepath
            self.display_image(filepath)

    def display_image(self, path):
        # Display the selected image in the GUI
        img = Image.open(path)
        img.thumbnail((600, 400))
        self.tk_image = ImageTk.PhotoImage(img)
        self.image_label.config(image=self.tk_image)

    def upload_logo(self):
        # Open a file dialog to select a logo image
        filetypes = (
            ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"),
            ("All files", "*.*")
        )
        filepath = filedialog.askopenfilename(title="Select Logo", filetypes=filetypes)
        if filepath:
            self.logo_path = filepath
            messagebox.showinfo("Logo Uploaded", "Logo has been successfully uploaded!")

    def add_watermark(self):
        if not self.image_path:
            messagebox.showerror("No Image", "Please upload an image first.")
            return

        try:
            base_image = Image.open(self.image_path).convert("RGBA")
            watermark_layer = Image.new("RGBA", base_image.size, (0,0,0,0))
            draw = ImageDraw.Draw(watermark_layer)

            if self.watermark_type.get() == "text":
                text = self.watermark_text.get()
                if not text:
                    messagebox.showerror("No Text", "Please enter watermark text.")
                    return
                # Define font and size
                try:
                    font = ImageFont.truetype("arial.ttf", 144)
                except IOError:
                    # Fallback to default font if arial.ttf is not found
                    font = ImageFont.load_default()
                    messagebox.showwarning("Font Warning", "Arial font not found. Using default font.")

                # Calculate text size using textbbox
                bbox = draw.textbbox((0, 0), text, font=font)
                textwidth = bbox[2] - bbox[0]
                textheight = bbox[3] - bbox[1]

                # Position the text at the bottom right
                x = base_image.width - textwidth - 10
                y = base_image.height - textheight - 10

                # Debugging: Print positions and sizes
                print(f"Image size: {base_image.width}x{base_image.height}")
                print(f"Text size: {textwidth}x{textheight}")
                print(f"Watermark position: ({x}, {y})")

                # Add outline (optional)
                outline_range = 2
                for adj in range(-outline_range, outline_range +1):
                    for adj_y in range(-outline_range, outline_range +1):
                        if adj != 0 or adj_y !=0:
                            draw.text((x + adj, y + adj_y), text, font=font, fill=(0,0,0,200))  # Black outline

                # Add text to watermark layer with increased opacity
                draw.text((x, y), text, font=font, fill=(255,255,255,200))  # Less transparent white text

            elif self.watermark_type.get() == "logo":
                if not self.logo_path:
                    messagebox.showerror("No Logo", "Please upload a logo image.")
                    return
                logo = Image.open(self.logo_path).convert("RGBA")
                # Resize logo
                logo_size = (100, 100)
                logo.thumbnail(logo_size, Image.ANTIALIAS)
                # Position the logo at the bottom right
                x = base_image.width - logo.width - 10
                y = base_image.height - logo.height - 10

                # Debugging: Print positions
                print(f"Logo size: {logo.width}x{logo.height}")
                print(f"Logo position: ({x}, {y})")

                # Paste the logo onto the watermark layer
                watermark_layer.paste(logo, (x, y), logo)

            # Combine the watermark with the base image
            watermarked_image = Image.alpha_composite(base_image, watermark_layer)

            # Save the watermarked image
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"),
                                                                ("JPEG files", "*.jpg *.jpeg"),
                                                                ("All files", "*.*")],
                                                     title="Save Watermarked Image")
            if save_path:
                watermarked_image = watermarked_image.convert("RGB")  # Convert back to RGB
                watermarked_image.save(save_path)
                messagebox.showinfo("Success", f"Watermarked image saved at {save_path}")
                self.display_image(save_path)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
