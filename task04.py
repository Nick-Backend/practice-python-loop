import random

secret = random.randint(1, 20 + 1)

while True:
    find = int(input("Sonni toping: "))

    if secret == find:
        print("Topding! ")

        break
    elif 1 <= find <= 20:
        print("Topolmading! ")

    else:
        print("Noto'g'ri son: ")  


