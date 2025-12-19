text = input("So'z kiriting: ")

katta_harf_soni = 0
 
for i in text:
    if i.isupper():
        katta_harf_soni += 1

print(katta_harf_soni)        