def fib(n): # n - номер останнього числа фібаначі в послідовності яку потрібно отримати
    if n < 0:
        return []
    if n == 0:
        return [0]
    result = [0, 1]

    for i in range(2, n + 1):
        next = result[i - 1] + result[i - 2]
        result.append(next)
    return result


k = int(input("How many numbers do you want to see: "))
numbers = fib(k-1)
print(numbers)




