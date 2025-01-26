# Simple Caesar Cipher Program

def encrypt(text, shift):
    """Encrypt a message using Caesar Cipher."""
    result = ""
    for char in text:
        if char.isalpha():  # Process only letters
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char  # Keep non-letters unchanged
    return result


def decrypt(text, shift):
    """Decrypt a message using Caesar Cipher."""
    return encrypt(text, -shift)  # Decryption is just reverse encryption


# Main program
print("Welcome to the Simple Caesar Cipher Program!")

while True:
    print("\nWhat would you like to do?")
    print("1: Encrypt a message")
    print("2: Decrypt a message")
    print("3: Exit")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        print("Encrypted message:", encrypt(message, shift))
    elif choice == "2":
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        print("Decrypted message:", decrypt(message, shift))
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
