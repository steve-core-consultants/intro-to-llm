import re
import string


def clean_text(text):
    """
        Cleans the input text by performing the following operations:
        1. Convert to lowercase
        2. Remove punctuation
        3. Strip leading and trailing white spaces
        4. Remove special characters
        5. Remove digits

        Parameters:
            text (str): The input string to be cleaned.

        Returns:
            str: The cleaned string.
    """

    if text is None:
        raise ValueError("Input text should not be None")

    if not text.strip():
        raise ValueError("Input text should not be empty")

    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    text = text.strip()
    text = re.sub(r'[!@#$%^&*(),.?":{}|<>]', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', re.sub(r'\d', '', text))

    return text
