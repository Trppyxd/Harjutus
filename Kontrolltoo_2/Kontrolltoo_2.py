
##########################################
##################3#######################
##########################################

a = [11, 15, 6, 13, 13, 25, 32, 11, 20, 5, 31, 16, 32, 29, 11, 13, 3, 29, 28, 24]
# a on esimene list, selles on 20 arvu
b = [5, 19, 16, 4, 12, 7, 2, 28, 34, 29, 29, 36, 6, 8, 24, 18, 31, 7, 1, 7]
# b on teine list, selles on 21 arvu

# 1)
sarnasedArvud = (set(a)&set(b))
# set(a)&set(b) Leiab sarnased arvud nende kahe listi vahel (uhisosa)
print("Sarnased arvud on: ", sarnasedArvud)
# voib ka print ("Sarnased arvud on: ", (set(a)&set(b))

#2)
ab = (list(set(a+b)))
# (list(set(a+b))) Teeb kaks listi uue(paneb kaks listi kokku)
# (max(ab)) Votab uue listi suurima integeri(arvu)
print('Kahe listi suurim arv on: ', max(ab))

#3)
print('Kahe listi vaikseim arv on: ', min(ab))

#4)
arvudA = (len(a))
arvudB = (len(b))

sumA = (sum(a))
sumB = (sum(b))

print("Esimese listi keskmine on: ", sumA / arvudA)
print("Teise listi keskmine on: ", sumB / arvudB)

#5)
arvudAB = (len(ab))

sumAB = (sum(ab))

print("Molema listi keskmine on: ", sumAB / arvudAB)

##########################################
##########################################
##########################################
'''
Klassis ma kogematta ei laadinud githubi algset KTd ulesse, selleparast ma tegin uue faili.
'''
