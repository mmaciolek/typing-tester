import random

# List of phrases for the type checker to choose from. Make this import from a text document.
PHRASES = ["The cow jumped over the moon."]
# Main loop.
while True:
    # Select a phrase from the list of phrases.
    phrase = random.choices(PHRASES)[0]
    user_input = input(f"Please type:\n"
                       f"{phrase}\n")
    # If the user input is exactly the same as the selected phrase, print a message and move on to the next phrase.
    # Else, analyze the input versus the selected phrase.
    if user_input == phrase:
        print("Well done! 100% Correct.")
    else:
        # Split the strings into individual words.
        phrase_words = phrase.split(" ")
        user_words = user_input.split(" ")
        # For each word in the phrase, compare against each word in the input and print the results.
        for i in range(len(phrase_words)):
            try:
                if phrase_words[i] == user_words[i]:
                    print(f"{phrase_words[i]} => {user_words[i]}")
                else:
                    print(f"{phrase_words[i]} =/> {user_words[i]}")
            except IndexError:
                # Print an error message if the number of words in each string does not match.
                print("Word counts do not match.")
                break
