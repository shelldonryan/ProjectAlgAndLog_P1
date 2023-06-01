def menuInicialCliente():
    print('\n|------QUAL AÇÃO DESEJA FAZER?------|')
    print('1 - CADASTRAR CLIENTE')
    print('2 - FAZER LOGIN')
    print('0 - VOLTAR')
    optionCliente = input('\nDIGITE A OPÇÃO DESEJADA: ')
    return optionCliente

def menuLoginCliente():
    print('\nQUAL OPÇÃO DESEJA?\n')
    print('1 - ATUALIZAR A SENHA DO LOGIN DO CLIENTE')
    print('2 - BUSCAR PRODUTO')
    print('3 - LISTA DE COMPRAS')
    print('3 - CONSULTA DE DESCRIÇÃO')
    print('0 - SAIR DA CONTA')
    print('6 - REMOVER CONTA\n')
    optionLoginCliente = input('DIGITE A OPÇÃO QUE DESEJA REALIZAR: ')
    return optionLoginCliente