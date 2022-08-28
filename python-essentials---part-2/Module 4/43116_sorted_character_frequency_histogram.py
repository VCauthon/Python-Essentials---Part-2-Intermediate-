"""

    Estimated time > 15-30 minutes
    Level of difficulty >Medium
    Prerequisites > 4.3.1.15

    Objectives:
        improve the student's skills in operating with files (reading/writing)
        using lambdas to change the sort order.

    Scenario:
        The previous code needs to be improved. It's okay, but it has to be better.

    Your task is to make some amendments, which generate the following results:
        the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
        the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)
        Assuming that the input file contains just one line filled with:

    Examble > cBabAa
    the expected output should look as follows:
        a -> 3
        b -> 2
        c -> 1

    Tip: Use a lambda to change the sort order.

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

    #

    # Checks that the letter is not a breakline or a space
    if letter not in [" ", "\n"]:

        # Checks if the current character exist
        if not letter in letter_counter.keys():
            letter_counter[letter.lower()] = 0

        # Increase the counter by 1
        letter_counter[letter.lower()] += 1

reader.close()

# Creates the file where all the data will be saved
stream_writer = open(os.path.join(os.getcwd(), "43116_result.txt"), 'wt')

# Shows the results
for character in sorted(letter_counter.keys(), key=lambda x: letter_counter[x], reverse=True):
    stream_writer.write(character + "->" + str(letter_counter[character]) + "\n")

# Close all streams
stream_writer.close()
