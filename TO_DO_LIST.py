import os   
lista_de_compras = []

while True:
    print('Escolha uma opção:')
    input_usuario = input('[i]nserir [a]pagar [l]listar [s]air: ').lower()
    # aqui o usuario escolhe a ação que deseja fazer

    if input_usuario == 'i':
        item = input('Digite o item que deseja inserir: ')
        lista_de_compras.append(item)
        # insere o item na lista

    elif input_usuario == 'a':
        print('Lista de compras:')
        for indice, item in enumerate(lista_de_compras, 1):  # começa mostrando do 1
            print(f'{indice}: {item}')
        try:
            indice_digitado = int(input('Digite o número do item que deseja apagar: '))
            lista_de_compras.pop(indice_digitado - 1)  # ajusta para índice real (0)
        except (ValueError, IndexError):
            print('Índice inválido. Tente novamente.')
        # apaga o item da lista conforme o índice digitado pelo usuário

    elif input_usuario == 'l':
        os.system('cls')
        if len(lista_de_compras) == 0:
            print('A lista de compras está vazia.')
            continue
        print('Lista de compras:')
        for indice, item in enumerate(lista_de_compras, 1):  # começa do 1
            print(f'{indice}: {item}')
        # lista os itens da lista de compras

    elif input_usuario == 's':
        os.system('cls')
        print('Saindo do programa...')
        break

    else:
                print('Opção inválida. Tente novamente.')
# fim do codigo