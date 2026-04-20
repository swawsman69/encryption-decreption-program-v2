import string
import json
import os # We'll use this to check if the file exists

def fetch_saved_key(filename='last_key.json'):
    """
    Fetches the key (a list of characters) from a JSON file.
    """
    if not os.path.exists(filename):
        print(f"Error: The key file '{filename}' was not found.")
        return None

    try:
        # Open the file in read mode ('r')
        with open(filename, 'r') as f:
            # Use json.load() to read the JSON data back into a Python list
            loaded_key = json.load(f)
            print(f" Key successfully loaded from {filename}")
            return loaded_key
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filename}'. Is the file corrupted?")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return None

# --- Main execution block ---

# 1. Call the function to fetch the key
ENCRYPTION_KEY = fetch_saved_key()

# 2. Use the fetched key (ENCRYPTION_KEY)
if ENCRYPTION_KEY is not None:
    chars = " " + string.punctuation + string.digits + string.ascii_letters
#DECRYPT
cipher_text = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = ENCRYPTION_KEY.index(letter)
    plain_text += chars[index]

print(f"encrypted message: {cipher_text}")
print(f"original message : {plain_text}")