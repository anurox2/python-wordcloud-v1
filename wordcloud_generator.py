#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import wordcloud

## Reading the filename from user input arguments
if(sys.argv[1].split(".")[1] != 'txt'):
    print("Please select a text (.txt) file")
    exit(0)
else:
    input_file = open(sys.argv[1])
    text_contents = input_file.read()


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "in", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # Removing new line characters
    file_contents = file_contents.replace("\n", " ")

    # Removing non-alphabet characters
    for char in file_contents:
        if(char.isalpha() == False and char != " "):
            file_contents = file_contents.replace(char, "")

    # Removing punctuations
    for char in punctuations:
        file_contents = file_contents.replace(char, "")

    # Removing double spaces and converting to a word list
    file_contents = file_contents.replace("  ", " ").lower().split(" ")

    # Removing stopwords
    for word in uninteresting_words:
        try:
            while word in file_contents:
                file_contents.remove(word)
        except:
            print(word, "not found in the input")

    # Getting word count and storing in a dictionary
    frequencies = {}
    for word in file_contents:
        frequencies[word] = file_contents.count(word)
    
    # Generating a wordcloud object
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

myimage = calculate_frequencies(text_contents)
plt.imshow(myimage, interpolation='nearest')
plt.axis('off')
plt.show()