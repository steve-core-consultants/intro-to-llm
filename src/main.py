"""
Activity - Working with LLMs

TODO: Import the packages from utils
TODO: Read the example_text.txt file
TODO: Perform any necessary cleaning
TODO: Create a summarization of data/example_text.txt
TODO: Try playing with the arguments of the bullet_point_summary function or adding your own text :)
"""
# Import packages (these are how installed packages work as well)
from utils.clean_text import clean_text
from utils.bullet_point_summary import bullet_point_summary

# Read the example_text.txt file via open
with open("../data/example_text.txt", "r") as file:
    raw_text = file.readlines()[0]

# Apply the clean_text function
# Its best practice to unit test your functions to account for any edge cases -
# example of this can be found in ../test/test_my_function.py
cleaned_text = clean_text(raw_text)

# Write the cleaned_text to a file within ../data/ to compare with example_text.txt
with open("../data/cleaned_text.txt", "w") as file:
    file.write(cleaned_text)

# Apply bullet_point_summary function to the cleaned_text
summary = bullet_point_summary(cleaned_text)

# Evaluate the output - is it what you expected?
print(summary)
