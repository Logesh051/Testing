numbers = input().split(",")

for number in numbers:
    decimal = int(number, 2)

    if decimal % 5 == 0:
        print(number)
