from marketplaces import marketplaces
from categories import categorias
from subcategories import subcategorias

def menu():
    options = ['Listar Marketplaces', 'Listar Categorias', 'Listar Subcategorias', 'Sair']

    print('\nMenu: ')

    for i, option in enumerate(options):
        print(f'[{i+1}] - {option}')

    op = int(input('Selecione uma das opções abaixo: '))
    return op


while True:
    try:
        op = menu()
        if op == 1:
            print(marketplaces())
        elif op == 2:
            print(categorias())
        elif op == 3:
            print(subcategorias())
        elif op == 4:
            exit(0)
        else:
            print('Opção indisponível. Tente novamente.')
    except ValueError:
        print('Opção indisponível. Tente novamente.')