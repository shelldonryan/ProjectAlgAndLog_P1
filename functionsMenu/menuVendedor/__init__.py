
def menuInicialVendedor():
    print('\n|------QUAL AÇÃO DESEJA FAZER?------|')
    print('1 - CADASTRAR VENDEDOR')
    print('2 - FAZER LOGIN')
    print('0 - VOLTAR')
    optionVendedor = input('\nDIGITE A OPÇÃO DESEJADA: ')
    return optionVendedor


def menuLoginVendedor():
    print('\nQUAL OPÇÃO DESEJA?\n')
    print('1 - ATUALIZAR A SENHA DO LOGIN DO VENDEDOR')
    print('2 - CADASTRAR PRODUTO')
    print('3 - BUSCAR PRODUTO')
    print('4 - ATUALIZAR PRODUTO')
    print('5 - REMOVER PRODUTO')
    print('0 - SAIR DA CONTA')
    print('6 - REMOVER CONTA\n')
    optionLoginVendedor = input('DIGITE A OPÇÃO QUE DESEJA REALIZAR: ')
    return optionLoginVendedor


def menuAtualizarProduto():
    print('\n------OPÇÕES------')
    print('1 - ATUALIZAR NOME')
    print('2 - ATUALIZAR O CÓDIGO')
    print('3 - ATUALIZAR O PREÇO')
    print('4 - ATUALIZAR O ESTOQUE')
    print('5 - ATUALIZAR A DESCRIÇÃO')
    print('0 - VOLTAR PARA A PÁGINA INICIAL')
    optionAtualizarProduto = input('\nDIGITE A OPÇÃO DESEJADA: ')
    return optionAtualizarProduto

