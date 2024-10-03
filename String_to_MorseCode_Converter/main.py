'''
Morse Code Converter: This is a simple text-based program that converts any string input from the user into Morse Code.
It translates letters, numbers, and certain punctuation marks based on a predefined dictionary, and outputs the corresponding
Morse Code for the input. If an unsupported character is encountered, it marks it with a placeholder.
'''

# Step 1: A dictionary mapping letters, numbers, and some punctuation marks to their Morse code equivalents
morse_code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': ' '  # Space is represented as a space in Morse Code
}

def string_to_morse(input_string):
    '''
    Converts the input string to Morse Code by looking up each character in the morse_code_dict.
    Unsupported characters will be replaced by a placeholder '[?]'.
    '''

    # Step 2: Converting the string to lowercase to ensure it matches our dictionary keys
    input_string = input_string.lower()

    # Step 3: Initializing an empty list to store the Morse Code translation
    morse_translation = []

    # Iterating over each character in the input string
    for char in input_string:
        if char in morse_code_dict:  # If the character exists in our Morse Code dictionary,
            morse_translation.append(morse_code_dict[char])  # Append its Morse Code to the list
        else:
            # Mark unsupported characters  with [?] as a placeholder
            morse_translation.append('[?]')

    # Step 4: Joining the Morse Code list into a single string with spaces between the letters
    return ' '.join(morse_translation)

def main():
    '''
    The main function that runs the program in a loop, allowing the user to input strings to be converted
    into Morse Code. It continues until the user types 'exit' to quit.
    '''
    print("Welcome to the Morse Code Converter!")  # Starting message

    while True:
        # Step 5: Asking the user for input
        user_input = input("Enter a string to convert to Morse Code (or 'exit' to quit): ")

        # Checking if the user wants to exit the program
        if user_input.lower() == 'exit':
            print("Thank you for using the Morse Code Converter!")  # Exit message
            break

        # Step 6: Converting the input string to Morse Code using the string_to_morse function
        morse_output = string_to_morse(user_input)

        # Step 7: Displaying the Morse Code translation to the user
        print(f"Morse Code: {morse_output}\n")  # Print the converted Morse Code

# Calling the main function to run the program
main()
