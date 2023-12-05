from password_generator import PasswordGenerator
from api_client import APIClient

def main():
    api_client = APIClient()
    password_generator = PasswordGenerator()

    while True:
        num_passwords = int(input("Enter the number of passwords to be created (max 50): "))
        words = api_client.get_random_words(num_passwords)

        passwords = [password_generator.generate(word) for word in words]
        print("\n".join(passwords))

        choice = input("\n1. Create password again\n2. Exit\nChoose an option: ")
        if choice == '2':
            break
        elif choice not in ['1', '2']:
            print("Warning: Invalid option selected. The program will now close.")
            break

if __name__ == "__main__":
    main()