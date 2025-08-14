def match_words(words):
    counter = 0
    matching_list = []
    for word in words:
        if len(word) > 1 and word[0].lower() == word[-1].lower():
            counter += 1
            matching_list.append(word)

    print("Number of words with same last and first letters:", matching_list)
    return counter

word = ['aba', 'xyz', "12221", 'madam', 'messi']
count = match_words(word)
print("Count of matching words are:", count)