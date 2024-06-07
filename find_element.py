def finder(sentences):
    for i in range(len(sentences)):
        if sentences[i] == "a" or sentences[i] == "b":
            sentences = sentences.replace(sentences[i], " ")
    print(sentences)

finder(input("enter the word: "))
