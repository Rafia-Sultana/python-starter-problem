def find_longest_word(sentence):
words = sentence.split()
longest = max(words, key=len)
return longest
print(find_longest_word("Machine learning is fascinating"))