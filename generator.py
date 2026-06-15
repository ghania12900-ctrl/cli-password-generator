import argparse
import secrets
import string
import sys


def generate_password(length=12, count=1, no_symbols=False, exclude_chars=""):
    # Define default character pools
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation if not no_symbols else ""

    # Combine pools
    all_characters = letters + digits + symbols

    # Remove any characters the user wants to exclude
    if exclude_chars:
        all_characters = "".join(
            [c for c in all_characters if c not in exclude_chars]
        )

    # Safety check: If they excluded too many characters
    if not all_characters:
        print(
            "Error: No characters available to generate a password. Reduce your exclusions.",
            file=sys.stderr,
        )
        sys.exit(1)

    # Generate the passwords
    passwords = []
    for _ in range(count):
        password = "".join(secrets.choice(all_characters) for _ in range(length))
        passwords.append(password)

    return passwords


def main():
    parser = argparse.ArgumentParser(
        description="Secure CLI Password Generator"
    )

    # Set up the command line flags (-l, --count, --no-symbols, --exclude)
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=12,
        help="Length of the password (default: 12)",
    )
    parser.add_argument(
        "--count",
        type=int,
        default=1,
        help="Number of passwords to generate (default: 1)",
    )
    parser.add_argument(
        "--no-symbols",
        action="store_true",
        help="Generate password without special symbols",
    )
    parser.add_argument(
        "--exclude",
        type=str,
        default="",
        help='Characters to exclude (e.g., "0O1lI")',
    )

    args = parser.parse_args()

    # Generate and print the passwords
    results = generate_password(
        length=args.length,
        count=args.count,
        no_symbols=args.no_symbols,
        exclude_chars=args.exclude,
    )

    for pwd in results:
        print(pwd)


if __name__ == "__main__":
    main()