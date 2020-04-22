import random

country = open('data/text/chosen_country.txt', "r")
choise = list()

for i in country.read().replace(',', ' ').split():
    if '_' in i:
        choise.append(i)
    else:
        choise.append(i)
print("Глобус остановился..", "Вы летите в прекрасную страну {}".format(choise[random.randrange(len(choise))]), sep="\n")