import json  # in order to import json data
from difflib import get_close_matches  # in order to similar words

data = json.load(open("data.json"))


def translate(word):
    '''Function created in order to return the input from the user'''
    if word[0] != word.upper()[
        0] or word.upper() != word:  # In case of words that start with capital letter or acronyms
        word = word.lower()
    if word in data:  # transform the word to lower cases(json dic key's are lower cases)
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        user_input = input(
            "Did you mean {0}? Enter Y if Yes,or N if no:\n".format(get_close_matches(word, data.keys())[0]))
        if user_input == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif user_input == "N":
            return "The word does not exist.Please double check it."
        else:
            return "The only variant possible is Y or N"
    else:
        return "It's a mistype.The word does not exist."  # if a misstypo is made return this message


word = input("Enter word: ")  # Get the user input

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
