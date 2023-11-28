def mult(x, y):
    print(x, 'x', y)
    return x * y


def sum(x, y):
    print(x, '+', y)
    return x + y


def sub(x, y):
    print(x, '-', y)
    return x - y


def div(x, y):
    print(x, '/', y)
    return x / y


def main():
    try:
        global num1
        num1 = (int(input('Digite o primeiro numero: ')))
        global num2
        num2 = (int(input('Digite o segundo numero: ')))
        print('\n')

    except:
        print(" ")
        print('Digite um numero valido')
        print(" ")
        main()

    global selecao

    def selecao():
        print('Selecione ua operação:\n ')

        print('[1]ADIÇÃO: ')
        print('[2]SUBTRAÇÃO: ')
        print('[3]MULTIPLICAÇÃO: ')
        print('[4]DIVISÃO: ')
        print('\n')

        selecao_numero = 0

        try:
            selecao_numero = (int(input()))
            print(f'Voce selecionou a opção[{selecao_numero}]')
            print('\n')

        except:
            print('Digite uma operação válida')
            selecao()

        if selecao_numero == 0 or selecao_numero >= 5:
            print('Digite uma operação valida!')
            selecao()

        if selecao_numero == 1:
            print(sum(num1, num2))
        elif selecao_numero == 2:
            print(sub(num1, num2))
        elif selecao_numero == 3:
            print(mult(num1, num2))
        elif selecao_numero == 4:
            print(div(num1, num2))


main()
selecao()
