s = input('Введіть вираз для обчислення: ')
for operator in ('+', '-', '*', '/'):
    a, op, b = s.partition(operator)
    if op:
        break
if op:
    a = int(a)
    b = int(b)
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a / b)
else:
    print('Невідома операція')
