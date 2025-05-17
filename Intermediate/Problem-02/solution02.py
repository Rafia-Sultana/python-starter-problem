def group_words(words):
    grouped = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in grouped:
           grouped[sorted_word].append(word)
        else:
           grouped[sorted_word] = [word]

    result = list(grouped.values())
    return result

words = ["bat", "tab", "cat", "act"]
print(group_words(words))




