sentence = input('Enter a sentence: ')

words = sentence.split()
total_words = len(words)

longest_word = max(words, key=len)
longest_length = len(longest_word)

uppercase = sentence.upper()
lowercase = sentence.lower()
titlecase = sentence.title()
reversed_sentence = sentence[::-1]

print('Total_words:', total_words)
print('Longest_words:', longest_word, f'({longest_length} letters)')
print('Uppercase:', uppercase)
print('Lowercase:', lowercase)
print('Title case:', titlecase)
print('reversed:', reversed_sentence)