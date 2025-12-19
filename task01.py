text = input("Matn kiriting: ")

unlilar = "a,e,i,o,u"
unli_soni = 0

for i in text:
    if i in unlilar:
        unli_soni += 1

print(unli_soni)        