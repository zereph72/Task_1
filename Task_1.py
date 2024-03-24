a = int(input("Enter a: "))
b = int(input("Enter b: "))

if a < b:
    step = 1
    b += 1
else:
    step = -1

    b -= 1

for number in range(a, b, step):
    is_prime = True
    for num in range(2, number // 2):
        if number % num == 0:
            is_prime = False
            break

    if is_prime:
        print("number:", number)

# 5 + -1
