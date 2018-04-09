#Задані числа a, n. Вирахувати а в ступені n! Рішення оформити у вигляді фукції power(a, n).
def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res

print(power(float(input()), int(input())))
