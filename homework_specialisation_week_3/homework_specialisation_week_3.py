"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you cab generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""


def generate_phrase(characters, phrase):
    count = 0
    if len(characters) < len(phrase):
        return False
    elif len(phrase)==0 and len(characters)>0:
        return Trye
    else:
        for i in phrase:
            for j in characters:
                if i==j:
                    count = count + 1
                    break
    if count==len(phrase):
        return True
    else:
        return False

