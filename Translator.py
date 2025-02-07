# How to build a basic translator in python
# This translator takes in a string i.e (a phrase or word) and translate it into a different language

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter

    return translation

print(translate(input("Enter a phrase: ")))