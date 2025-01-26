word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "{}"
word6 = "so"
word7 = "far!"

language = input("Enter a programming language: ")
sentence = f"{word1} {word2} {word3} {word4} {word5.format(language)} {word6} {word7}"
print(sentence)