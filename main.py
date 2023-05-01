def mu_reverse_letters(mu_sentence):
    # Split the sentence into individual words
    mu_words = mu_sentence.split()

    # Reverse the order of letters within each word
    mu_reversed_words = [mu_word[::-1] for mu_word in mu_words]

    # Join the reversed words back together into a sentence
    mu_reversed_sentence = " ".join(mu_reversed_words)

    # Return the reversed sentence
    return mu_reversed_sentence


# Prompt the user for input
mu_sentence = input("Enter a sentence: or a word 🥽 ")

# Reverse the order of letters in each word of the sentence
mu_reversed_sentence = mu_reverse_letters(mu_sentence)

# Print the reversed sentence
print("Reversed sentence:", mu_reversed_sentence)
