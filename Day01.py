# Dia 1.

def principal1():
    contador = 0
    print('Inicio Dia1-1')
    f1 = open("Day01_input.txt", "r")
    anterior = None
    for l1 in f1:
        if anterior is not None:
            if int(l1) > anterior:
                contador = contador + 1
                print(f"{int(l1)}>{anterior}, llevamos {contador}")
            else:
                print(f"{int(l1)}<={anterior}, llevamos {contador}")
        anterior = int(l1)
    f1.close()
    print(f"Fin Dia1-1 resultado: {contador}")

def principal2():
    contador = 0
    print(f"Inicio Dia1-2")
    with open("Day01_input.txt", "r") as f:
        content = [i.strip() for i in f.readlines()]

    for i in range(3, len(content)):
        # print(f"{linea1}")
        ultimo = int(content[i]) + int(content[i-1]) + int(content[i-2])
        anterior = int(content[i-1]) + int(content[i-2]) + int(content[i-3])
        print(f"{anterior}={content[i-1]} {content[i-2]} {content[i-3]}")
        print(f"{ultimo}={content[i]} {content[i-1]} {content[i-2]}")
        if ultimo > anterior:
            contador = contador + 1
            print(f"{ultimo}>{anterior}, llevamos {contador}")
        else:
            print(f"{ultimo}<={anterior}, llevamos {contador}")

    print(f"Fin Dia1-2 resultado: {contador}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # principal1()
    principal2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

