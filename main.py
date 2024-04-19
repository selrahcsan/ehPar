def eh_par(numero):
    """
    Determina se um número dado é par ou ímpar.

    Args:
        numero (int): O número de entrada.

    Returns:
        str: 'par' se o número for par, 'ímpar' se o número for ímpar.
    """
    resultado = 'par' if numero % 2 == 0 else 'ímpar'
    return resultado


def valida_numero():
    while True:
        try:
            numero = int(input('Digite um número: '))
            print(f'O número é {eh_par(numero)}.')
            break
        except ValueError:
            print('Digite um valor válido.')


if __name__ == "__main__":
    valida_numero()
