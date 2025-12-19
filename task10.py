n = int(input("Son kiriting: "))

start = 1

while start <= n:

    if start % 3 == 0 and start % 5 == 0:
        print("FizzBuzz")

    elif start % 3 == 0:
        print("Fizz")

    elif start % 5 == 0:
        print("Buzz")

    else:
        print(start)

    start += 1