import random

secret = random.randint(1000,9999)
urunish_soni = 0
jami_urunish = 7

while urunish_soni < jami_urunish:
    find = int(input("Pin codni kiriting: "))
    urunish_soni += 1

    if find > secret:
        print("Juda katta son! ")

    elif find < secret:
        print("Juda kichik son! ") 

    else:
        print("Topdingiz, tabriklaymiz: ") 

        break

else:
    print(f"Urunishlar soni tugadi, Pin code = {secret}")
