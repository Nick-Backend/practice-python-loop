def add(a,b):
    result = a + b
    return  result

def ayir(a,b):
    result = a - b
    return  result

def kop(a,b):
    result = a * b
    return  result

def bul(a,b):
    result = a / b
    return  result

def main():
    a = int(input("A:  "))
    b = int(input("B:  "))
    amal = input("Amal: (+) (-) (*) (/)")

    if amal == "+":
        result = add(a,b)

    elif amal == "-":
        result = ayir(a,b)

    elif amal == "*":
        result = kop(a,b)

    elif amal == "/":
        result = bul(a,b)

    print(result)

main()        
        