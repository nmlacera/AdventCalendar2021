# Dia 1.

def principal1():
    x = 0
    y = 0
    print('Inicio Dia2-1')
    f1 = open("Day02_input.txt", "r")
    for l1 in f1:
        direccion, pasos = l1.split(' ')
        if direccion == 'up':
            y = y - int(pasos)
        if direccion == 'down':
            y = y + int(pasos)
        if direccion == 'forward':
            x = x + int(pasos)
    f1.close()
    print(f"Fin Dia2-1 resultado: x{x} y{y} = {x*y}")


def principal2():
    x = 0
    y = 0
    aim = 0
    print('Inicio Dia2-2')
    f1 = open("Day02_input.txt", "r")
    for l1 in f1:
        direccion, pasos = l1.split(' ')
        if direccion == 'up':
            aim = aim - int(pasos)
        if direccion == 'down':
            aim = aim + int(pasos)
        if direccion == 'forward':
            x = x + int(pasos)
            y = y + (aim*int(pasos))
    f1.close()
    print(f"Fin Dia2-2 resultado: x{x} y{y} = {x*y}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # principal1()
    principal2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

