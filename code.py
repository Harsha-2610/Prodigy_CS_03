import re

def check_password_strength(password):
    # Define criteria
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    specialchar_error = re.search(r"[ !@#$%&'()*+,-./[\\\]^_`{|}~\"":;<=>?]", password) is None

    # Evaluate strength
    password_ok = not (length_error or digit_error or uppercase_error or lowercase_error or specialchar_error)

    # Provide feedback
    if password_ok:
        return "Password is strong."
    else:
        errors = []
        if length_error:
            errors.append("Password should be at least 8 characters.")
        if digit_error:
            errors.append("Password should contain at least one digit.")
        if uppercase_error:
            errors.append("Password should contain at least one uppercase letter.")
        if lowercase_error:
            errors.append("Password should contain at least one lowercase letter.")
        if specialchar_error:
            errors.append("Password should contain at least one special character (!@#$%&'()*+,-./[\\]^_`{|}~\"\":;<=>?")

        return "Password is weak. " + " ".join(errors)

# Example usage:
password = input("Enter your password: ")
strength = check_password_strength(password)
print(strength)
