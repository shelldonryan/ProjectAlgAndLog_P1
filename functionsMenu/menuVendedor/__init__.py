def mensagemInicial():
    print('\n                     |------------ BEM VINDO AO SERTÃO LIVRE ------------|\n')
    print('ESPERO QUE ESTE PROGRAMA ATENDA A TODAS AS SUAS NECESSIDADES E FACILITE A GESTÃO DO SEU NEGÓCIO.'.center(99))
    print('ESTOU À DISPOSIÇÃO PARA ESCLARECER QUAISQUER DÚVIDAS E OUVIR SEUS FEEDBACKS PARA MELHORIAS FUTURAS.\n')


def menuInicial():
    print('\n|------QUAL AÇÃO DESEJA FAZER?------|')
    print('1 - CADASTRAR VENDEDOR')
    print('2 - FAZER LOGIN')
    print('0 - VOLTAR')
    option = input('\nDIGITE A OPÇÃO DESEJADA: ')
    return option


def menuLogin():
    print('\nQUAL OPÇÃO DESEJA?\n')
    print('1 - ATUALIZAR A SENHA DO LOGIN DO VENDEDOR')
    print('2 - CADASTRAR PRODUTO')
    print('3 - BUSCAR PRODUTO')
    print('4 - ATUALIZAR PRODUTO')
    print('5 - REMOVER PRODUTO')
    print('6 - SAIR DA CONTA')
    print('7 - REMOVER CONTA\n')
    optionLogin = input('DIGITE A OPÇÃO QUE DESEJA REALIZAR: ')
    return optionLogin


def menuAtualizarProduto():
    print('\n------OPÇÕES------')
    print('1 - ATUALIZAR NOME')
    print('2 - ATUALIZAR O PREÇO')
    print('0 - VOLTAR PARA A PÁGINA INICIAL')
    optionAtualizarProduto = input('\nDIGITE A OPÇÃO DESEJADA: ')
    return optionAtualizarProduto

