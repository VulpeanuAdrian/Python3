import collections

s = "alas"


def hang(s):
    counter = 0
    q = []
    list(s)
    while(counter < 11):
            # you have 10 attemps
        if(collections.Counter(s) == collections.Counter(q)):
            return print("Your win")
        elif counter == 10:
            return print("You lost")
        else:
            q.append(input("please enter a letter:"))
            counter += 1


hang(s)
