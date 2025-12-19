text = input("Matn kiriting: ") # salom

teskari = ""
harf = len(text) - 1    # 5-1 = 4

while harf >= 0:
    teskari += text[harf]
    harf -= 1

print(teskari)    
