def enter():
    i = input("Enter a number: ")
    match i[0:2]:
        case '0b':
            base = '2'
            n = i[2::]
        case '0o':
            base = '8'
            n = i[2::]
        case '0x':
            base = '16'
            n = i[2::]
        case _:
            n, base = i.split('x') if 'x' in i else (i, '10')

    while any(x not in '0123456789ABCDEF' or '0123456789ABCDEF'.find(x) >= int(base) for x in n):
        print("Wrong input try again!")
        return enter()

    to_base = input("To which base you want to convert your little number? (2 <= number <= 16): ")
    while not to_base.isdigit() or int(to_base) < 2 or int(to_base) > 16:
        print("Wrong base try again!")
        return enter()
    return from_dec(to_dec(n, base), int(to_base))

def from_dec(n, base):
    a = '0123456789ABCDEF'
    binary = ''
    while n != 0:
        binary = a[n % base] + binary
        n = n // base
    return binary if binary else 0

def to_dec(n, base):
    return sum(int(base)**x * '0123456789ABCDEF'.find(y) for x, y in enumerate(reversed(n)))


while True:
    print("Your little number but in another base:", enter())
    if input("Another one? (y/n): ") != 'y':
        break