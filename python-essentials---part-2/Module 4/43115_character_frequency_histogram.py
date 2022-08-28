"""

    Estimated time
    30-60 minutes

    Level of difficulty > Medium

    Objectives:
        improving the student's skills in operating with files (reading)
        using data collections for counting numerous data.

    Scenario:
        A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text.
        Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

    Your task is to write a program which:
        asks the user for the input file's name;
        reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
        prints a simple histogram in alphabetical order (only non-zero counts should be presented)
        Create a test file for the code, and check if your histogram contains valid results.

    Assuming that the test file contains just one line filled with:
        aBc
        samplefile.txt

    the expected output should look as follows:
        a -> 1
        b -> 1
        c -> 1
        output

    Tip: We think that a dictionary is a perfect data collection medium for storing the counts. The letters may be keys while the counters can be values.

"""
import os.path
from os import strerror

# Dictionary with all the results
letter_counter = {}
reader = None

# Set a STREAM to the file and read all the data
try:
    reader = open(os.path.join(os.getcwd(), '43115_text.txt'),
                mode='r')

except IOError as Error:
    print("Error detected opening the file", strerror(Error.errno), sep=" ")

# Reads all the text character by character
for letter in reader.read():

    # Checks that the letter is not a breakline or a space
    if letter not in [" ", "\n"]:

        # Checks if the current character exist
        if not letter in letter_counter.keys():
            letter_counter[letter.lower()] = 0

        # Increase the counter by 1
        letter_counter[letter.lower()] += 1

# Shows the results
for character in letter_counter.keys():
    print(character, "->", letter_counter[character], sep=" ")
