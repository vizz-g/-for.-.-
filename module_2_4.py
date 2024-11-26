numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prims = []
not_prims = []
print(numbers)
for i in range(len(numbers)):
    is_prime = True
    n = numbers[i]
    if n < 2:
        continue
    else:
        k = n ** (1 / 2)
    for j in range(2, int(k+1)):
        if n % j == 0:
            is_prime = False
            break
    if not is_prime:
        not_prims.append(n)
    else:
        prims.append(n)
print(prims)
print(not_prims)