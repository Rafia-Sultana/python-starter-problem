from collections import Counter
rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'
clean_list = []

for ch in rhyme:
    if ch.isalnum():
        clean_list.append(ch)

joined_string = ''.join(clean_list).lower()

char_counts = Counter(joined_string)

print(char_counts.most_common(1)[0][0])



