list1 = ["PHP", "Java", "Dotnet", "Dotnet", "Python", "Python", "Java", "Python", "Java"]


def most_rep_words(li):
    words = {}
    for word in li:
        if word in words.keys():
            words[word] += 1
        else:
            words[word] = 1
    # print(words)
    most_rep = max(words.values())
    f_words = []
    for word,count in words.items():
        if count == most_rep:
            most_rep = count
            f_words.append(word)
    print("Most rep.words : ", f_words)
most_rep_words(list1)


