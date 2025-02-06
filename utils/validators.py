from django.core.exceptions import ValidationError

def check_fullname(fullname):
    # Split the name into parts
    parts = fullname.split()

    # Ensure there are exactly two parts (first name and surname)
    if len(parts) != 2:
        raise ValidationError(f"{fullname} must contain both a first name and a surname.")

    surname, name = parts

    # Ensure both parts contain only letters
    if not surname.isalpha() or not name.isalpha():
        raise ValidationError(f"{fullname} must only contain letters.")


    return fullname

def clean_spaces(text):
    # Remove leading/trailing spaces and reduce multiple spaces to a single space
    if isinstance(text, str):  # Only apply to strings
        return ' '.join(text.split()).title()
    return text
