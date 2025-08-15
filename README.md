 Password-Checker

 🔐 Password Strength Checker using Python

A simple Python script to check the strength of a password based on:
- Length
- Uppercase and lowercase letters
- Digits
- Special characters
- Common password check using `rockyou.txt`

 📌 Features:
- Checks for whitespace, length, and character diversity.
- Detects common passwords if `rockyou.txt` is available.
- Gives a strength score from **1/5** to **5/5** with remarks.
- Loops for multiple checks until the user exits.

 🛡 Common password attacks:
**Brute Force Attack** – Tries every possible combination of characters until the correct password is found. Very slow for long, complex passwords.  
**Dictionary Attack** – Tries passwords from a precompiled list of common words or leaked passwords. Faster than brute force but fails against unique, complex passwords.

 🔑 How password complexity affects security:
Longer passwords take exponentially more time to brute-force.  
Mixing uppercase, lowercase, digits, and special characters increases possible combinations, making attacks slower.  
Avoid common words or predictable patterns to reduce dictionary attack success.
