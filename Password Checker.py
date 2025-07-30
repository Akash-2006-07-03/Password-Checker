import string
import getpass

def passwd_checker():
    password = getpass.getpass("Enter your password: ")
    strength = up = low = dig = spe = 0
    remark = ''
    issues = []

    # Check for whitespace
    if any(c.isspace() for c in password):
        print("❌ There should not be any whitespaces. Try again.")
        return

    # Check length
    if len(password) < 8:
        print("❌ Password too short. Must be at least 8 characters.")
        return

    # Check against common passwords
    try:
        with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as f:
            common = f.read().splitlines()
            if password in common:
                print("❌ This is a common password. Try again.")
                return
    except FileNotFoundError:
        print("⚠️ rockyou.txt not found. Skipping common password check.")

    # Count character types
    for c in password:
        if c in string.ascii_uppercase:
            up += 1
        elif c in string.ascii_lowercase:
            low += 1
        elif c in string.digits:
            dig += 1
        elif c in string.punctuation:
            spe += 1

    # Check character type issues
    if up < 1:
        issues.append("❌ At least one uppercase letter required.")
    else:
        strength += 1

    if low < 1:
        issues.append("❌ At least one lowercase letter required.")
    else:
        strength += 1

    if dig < 1:
        issues.append("❌ At least one digit required.")
    else:
        strength += 1

    if spe < 1:
        issues.append("❌ At least one special character required.")
    else:
        strength += 1

    # Add extra strength if long password
    if len(password) > 10:
        strength += 1

    # Show all issues if any
    if issues:
        print("\n🔍 Password Issues:")
        for i in issues:
            print(i)
        return

    # Remarks based on strength
    if strength == 1:
        remark = "❌ Bad password, change it ASAP!"
    elif strength == 2:
        remark = "⚠️ Your password is not good."
    elif strength == 3:
        remark = "🙂 Quite good, but could be stronger."
    elif strength == 4:
        remark = "👍 Good password."
    elif strength == 5:
        remark = "💪 Very strong password!"

    # Final output
    print(f"\n✅ Password Strength: {strength}/5")
    print(f"📝 Remark: {remark}\n")


# Main loop
if __name__ == '__main__':
    while True:
        passwd_checker()
        choice = input("🔁 Do you want to try another password? (y/n): ").strip().lower()
        if choice == 'n':
            print("👋 Exiting. Stay secure!")
            break
        elif choice != 'y':
            print("⚠️ Invalid choice! Please enter 'y' or 'n'.")
