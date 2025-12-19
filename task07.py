max_son = int(input("Sonni kiriting: "))

for i in range(4):
    son = int(input("Keyingi sonnni kiritning: "))
    if son > max_son:
        max_son = son       

print(max_son)