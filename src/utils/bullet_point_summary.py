"""
To use the transformers package please type the below into your terminal:
pip install transformers

If you're receiving an error for installing the dependencies for transformers package please run the following in your terminal:
pip install --only-binary :all: transformers
"""
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


def bullet_point_summary(text, max_input_length=1024, min_summary_length=30, max_summary_length=300):
    """
    Generate a bullet-point summary of a given text using the BART large CNN model.

    Parameters:
        text (str): The text to be summarized.
        max_input_length (int): The maximum number of tokens for the input text. Default is 1024.
        min_summary_length (int): The minimum number of tokens for the summary. Default is 30.
        max_summary_length (int): The maximum number of tokens for the summary. Default is 300.

    Returns:
        str: A string containing the bullet-point summary.

    Notes:
        - The function uses the 'facebook/bart-large-cnn' pre-trained model.
        - The summary will be early-stopped if it reaches a sensible conclusion before hitting the max length.
    """

    # Initialize the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-large-cnn")

    # Tokenize the input text and generate summary ids
    inputs = tokenizer([text], max_length=max_input_length, return_tensors="pt", truncation=True)
    summary_ids = model.generate(
        inputs.input_ids,
        num_beams=4,
        min_length=min_summary_length,
        max_length=max_summary_length,
        early_stopping=True
    )

    # Decode and print the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    # Split the summary into sentences to make bullet points
    summary_sentences = summary.split('. ')

    # Convert to bullet points
    bullet_points = "\n- ".join(summary_sentences)

    return f"- {bullet_points}"

