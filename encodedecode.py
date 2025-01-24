# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

import random
import string

class SecretCode:
    def __init__(self, message):
        self.message = message

    def encode_word(self, word):
        if len(word) <= 3:
            return word[::-1]
        else:
            first_letter_removed = word[1:] + word[0]
            random_chars_start = ''.join(random.choices(string.ascii_letters, k=3))
            random_chars_end = ''.join(random.choices(string.ascii_letters, k=3))
            return random_chars_start + first_letter_removed + random_chars_end

    def decode_word(self, word):
        if len(word) < 3:
            return word[::-1]
        else:
            without_random_chars = word[3:-3]  # Remove the random characters
            return without_random_chars[-1] + without_random_chars[:-1]

    def encode_message(self):
        try:
            words = self.message.split()
            return ' '.join(self.encode_word(word) for word in words)
        except Exception as e:
            return f"Error during encoding: {e}"

    def decode_message(self):
        try:
            words = self.message.split()
            return ' '.join(self.decode_word(word) for word in words)
        except Exception as e:
            return f"Error during decoding: {e}"

def main():
    try:
        mode = input("Do you want to code or decode? ").strip().lower()
        message = input("Enter your message: ").strip()
        secret_code = SecretCode(message)

        if mode == "code":
            result = secret_code.encode_message()
        elif mode == "decode":
            result = secret_code.decode_message()
        else:
            raise ValueError("Invalid mode selected!")

        print("Result:", result)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
