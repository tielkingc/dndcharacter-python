import random
stre = 0
dex = 0
con = 0
inte = 0
wis = 0
cha = 0

he_score = random.randint(0, 7)
sta = [stre, dex, con, inte, wis, cha]
sta[he_score] += 1

print(sta[he_score])
