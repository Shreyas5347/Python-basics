def translator(phrase):
    word=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                word=word+"G"
            else:
                word=word+"g"
        else:
            word=word+letter
    return word
print(translator(input("enter the phrase :")))
