# Name: Ariana Fafach
# Date: 3/19/2026
# Title: Program #2: Word Separator


# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13


def word_separator(sentence):

    # Starts new_sentence with the first letter of the user's sentence without changing it.
    new_sentence = sentence[0]
    #    Add your logic here

    # For loop iterates over each letter of the user's sentence, skipping the first one.
    for i in range (1, len(sentence)):

        # Test if the letter is uppercase, and if it is, change it to lower case and add a space before it. Add it onto new_sentence.
        if sentence[i].isupper() == True:
            new_sentence += ' ' + sentence[i].lower()
        
        # If the letter is not uppercase, add it to new_sentence without changing it.
        else:
            new_sentence += sentence[i]
    
    # Test if the sentence already has punctuation. If not, add a period.
    if sentence[-1] != '.' and sentence[-1] != '!' and sentence[-1] != '?':
        new_sentence += '.'
    
    # Return new_sentence and strip all leading and trailing whitespaces.
    return new_sentence.strip()

# Example usage
if __name__=="__main__":

    # Get user input:
    sentence = input("Enter a sentence in which all of the words run together, but the first letter of each word is uppercase:  ")

    new_sentence = word_separator(sentence)

    print(new_sentence)
