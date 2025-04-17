import string
from collections import Counter

def count_word_frequency(text):
   	     # Remove punctuation and convert text to lowercase
    	     translator = str.maketrans('', '', string.punctuation)
    	     text = text.translate(translator).lower()
	
              # Split the text into words
    	    words = text.split()

    	    # Count the frequency of each word
    	    word_count = Counter(words)

    	    return word_count

def main():
    # Get input from the user
    user_text = input("Enter the text you want to analyze:\n")

    # Get the word frequencies
    frequency = count_word_frequency(user_text)

    # Print the results
    print("\nWord frequencies:")
    for word, count in frequency.items():
        print(f"{word}: {count}")

if _name_ == "_main_":
    main() 
