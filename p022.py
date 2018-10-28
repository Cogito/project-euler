import csv


def name_score(name):
    return sum(1 + ord(letter) - ord('A') for letter in name)


print(name_score("COLIN"))

with open("p022_names.txt") as file:
    names = csv.reader(file).next()
    names = sorted(names)
    print(sum(num * name_score(name) for num, name in enumerate(names, start=1)))

