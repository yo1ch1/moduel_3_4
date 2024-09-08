def single_root_word(root_word, *other_words):
    same_words =[]
    n = 0
    r = root_word.lower()
    o = list(other_words)
    o_1 = [x.lower() for x in o]
    for i in other_words:
        if r in o_1[n] or o_1[n] in r:
            same_words.append(other_words[n])
        n += 1
    return same_words


result1 = single_root_word('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_word('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
