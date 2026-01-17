def raqam_yigindi(n):
    s = 0
    while n > 0:
        raqam = n % 10
        s += raqam
        n = n // 10
    return s
print(raqam_yigindi(108))

def katta_q(names):
    natija = []
    for i in names:
        natija.append(i.capitalize())
    return natija
names = ['alfred', 'tabitha', 'william', 'arla']
print(katta_q(names))

def baholar(scores):
    return list(filter(lambda i: i > 75, scores))
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
print(baholar(scores))

def palindromlar(words):
    x = []
    for word in words:
        lo_wor = word.lower()
        if lo_wor == lo_wor[::-1]:
            x.append(word)
    return x
words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
print(palindromlar(words))

matn = input("matn kiriting ")
i,x = 0,""
while i < len(matn):
    if matn[i].lower() == 'e':
        x += "3"
    else:
        x += matn[i]
    i += 1
print(x)

matn = input("Matn kiriting: ")
x = ""
i = 0
while i < len(matn):
    if matn[i] != ' ':
        x += matn[i]
    i += 1
print(f"matn {x}")

raqamlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kara = []
for i in raqamlar:
    kara.append(i * 2)
print(kara)