import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&* etc).")

    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, score, feedback


def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check: ")

    strength, score, feedback = check_password_strength(password)

    print(f"\nStrength: {strength} ({score}/6)")

    if feedback:
        print("\nSuggestions to improve:")
        for tip in feedback:
            print(f"- {tip}")
    else:
        print("\nGreat! This is a strong password.")


if __name__ == "__main__":
    main()
