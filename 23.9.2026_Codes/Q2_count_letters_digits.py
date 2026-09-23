text = input()

L = 0
D = 0

for i in range(0, len(text)):
    if text[i].isalpha():
        L += 1
    elif text[i].isdigit():
        D += 1

print("LETTERS", L)
print("DIGITS", D)
