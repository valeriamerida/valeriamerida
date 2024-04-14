
def encode(password):
    encoded_password = ""
    for digit in password:
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password

def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        decoded_digit = (int(digit) - 3+10) % 10
        decoded_password += str(decoded_digit)
    return decoded_password

def main():
    while True:
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
            print()
            print()
        elif choice == "2":
            if not encoded_password:
                print("Please encode a password.")
            else:
                print(f"The encoded password is: {encoded_password}, and the original password is {decode(encoded_password)}")
                print()
                print()
        elif choice == "3":
            break
if __name__ == "__main__":
    main()



