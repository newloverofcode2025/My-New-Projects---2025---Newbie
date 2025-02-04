import secrets
import string
import argparse
from typing import List

def generate_password(length: int, exclude_ambiguous: bool) -> str:
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    if exclude_ambiguous:
        ambiguous_chars = 'l1O0'
        letters = ''.join([char for char in letters if char not in ambiguous_chars])
        digits = ''.join([char for char in digits if char not in ambiguous_chars])
        symbols = ''.join([char for char in symbols if char not in ambiguous_chars])

    all_chars = letters + digits + symbols

    # Ensure the password contains at least one character from each set
    required_chars = [
        secrets.choice(letters),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Generate remaining characters securely
    remaining_length = length - len(required_chars)
    additional_chars = [secrets.choice(all_chars) for _ in range(remaining_length)]

    # Shuffle to avoid predictable patterns
    password_chars: List[str] = required_chars + additional_chars
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

def main():
    parser = argparse.ArgumentParser(description="Generate secure passwords")
    parser.add_argument("-l", "--length", type=int, default=12,
                        help="Password length (minimum 4)")
    parser.add_argument("-x", "--exclude-ambiguous", action="store_true",
                        help="Exclude ambiguous characters (e.g., l, 1, O, 0)")
    args = parser.parse_args()

    # Enforce minimum length
    final_length = max(args.length, 4)
    password = generate_password(final_length, args.exclude_ambiguous)
    
    print(f"\n🔒 Generated Password ({final_length} characters):")
    print(f"   {password}\n")

if __name__ == "__main__":
    main()