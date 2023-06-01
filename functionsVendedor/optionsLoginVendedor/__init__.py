def senhaAreaLogin(vendedores: dict, senha):
    for cnpj in vendedores:
        while True:
            if senha != vendedores[cnpj][5]:
                print('\nSENHA INVÁLIDA!')
                senha = input('DIGITE A SUA SENHA NOVAMENTE: ').strip()
            else:
                login = True
                break
        return login

def usuarioAreaLogin (vendedores: dict):
    loginDoUsuario = input('ENTRE COM SEU CNPJ: ').strip()
    for cnpj in vendedores:
        while True:
            if loginDoUsuario != vendedores[cnpj][1]:
                print('\nLOGIN INVÁLIDO!')
                loginDoUsuario = input('DIGITE O CNPJ NOVAMENTE: ').strip()
            else:
                break
        return loginDoUsuario

def atualizarSenha(vendedores: dict, loginDoUsuario):
    confirmarSenha = input('SENHA ATUAL: ').strip()

    while True:
        if confirmarSenha != vendedores[loginDoUsuario][5]:
            print('\nSENHA INVÁLIDA!')
            confirmarSenha = input('DIGITE SUA SENHA ATUAL NOVAMENTE: ')
        else:
            novaSenha = input('SENHA NOVA: ').strip()
            while True:
                if len(novaSenha) < 8:
                    print('\nA SENHA DEVE CONTER NO MÍNIMO 8 CARACTERES.')
                    novaSenha = input('DIGITE SUA SENHA ATUAL NOVAMENTE: ').strip()
                else:
                    break

            while True:
                if novaSenha.isalnum():
                    print('\nDEVE CONTER AO MENOS UM CARACTERE ESPECIAL ex:@')
                    novaSenha = input('DIGITE SUA SENHA ATUAL NOVAMENTE: ').strip()
                else:
                    break

            print('DIGITE Y - SIM OU N - NÃO')
            pergSeguranca = input('\nDESEJA REALMENTE ALTERAR A SENHA? ').upper()
            if pergSeguranca == 'Y':
                vendedores[loginDoUsuario][5] = novaSenha
                print('\nSENHA ALTERADA COM SUCESSO!')
                break

            elif pergSeguranca == 'N':
                print('\nMUDANÇA CANCELADA.')
                break

            else:
                print("\nÉ NECESSÁRIO DIGITAR 'Y' OU 'N'.")
                print('DIGITE A SUA NOVA SENHA NOVAMENTE.')
                continue

def cadastrarProdutos(vendedores: dict, loginDoUsuario):
    produtos = []
    quantProdutos = int(input('\nDIGITE QUANTOS PRODUTOS DESEJA CADASTRAR: '))

    for i in range(0, quantProdutos):
        produto = []
        nomeProd = input('\nDIGITE O NOME DO PRODUTO: ').upper()
        precoProd = input('DIGITE O VALOR DO PRODUTO: ')

        while True:
            if not precoProd.isnumeric():
                print('APENAS VALORES NUMÉRICOS SÃO PERMITIDOS NO PREÇO!')
                precoProd = input('DIGITE O VALOR DO PRODUTO NOVAMENTE: ')
            else:
                break

        produto.append(nomeProd)
        produto.append(float(precoProd))
        produtos.append(produto)
        print('\nPRODUTO(s) CADASTRADO(s).')
        continue
    vendedores[loginDoUsuario][6] = produtos

def buscarProduto(vendedores, loginDoUsuario):
    buscarProduto = input('DIGITE O NOME DO PRODUTO QUE DESEJA BUSCAR: ').upper()
    busca = False

    for produtoBuscado in vendedores[loginDoUsuario][6]:
        if produtoBuscado[0].find(buscarProduto) >= 0:
            print(f'\nNOME DO PRODUTO: {produtoBuscado[0].capitalize()}')
            print(f'VALOR DO PRODUTO: R$ {produtoBuscado[1]:.2f}')
            busca = True

    if not busca:
        print('PRODUTO NÃO ENCONTRADO.')


def atualizarProduto(vendedores, loginDoUsuario, functionMenu):
    while True:
        optionAtualizarProduto = functionMenu

        if not optionAtualizarProduto.isdigit():
            print('SÓ NÚMEROS NAS OPÇÕES.')
            continue

        if optionAtualizarProduto == '1':
            atualizarProdutoNome = input('\nDIGITE O NOME DO PRODUTO QUE DESEJA ATUALIZAR: ').upper()
            for produtoBuscado in vendedores[loginDoUsuario][6]:
                if produtoBuscado[0].find(atualizarProdutoNome) >= 0:
                    print(f'\nPRODUTO ACHADO: {produtoBuscado[0]}\n')
                    novoNomeProduto = input('DIGITE O NOVO NOME DO PRODUTO: ').upper()
                    produtoBuscado[0] = novoNomeProduto
                    print('PRODUTO ATUALIZADO COM SUCESSO!')
                    break
            else:
                print('PRODUTO NÃO ENCONTRADO.')
                continue

        elif optionAtualizarProduto == '2':
            atualizarProdutoValor = input(
                '\nDIGITE O NOME DO PRODUTO QUE DESEJA ATUALIZAR O VALOR: ').upper()
            for produtoBuscado in vendedores[loginDoUsuario][6]:
                if produtoBuscado[0].find(atualizarProdutoValor) >= 0:
                    print(f'\nVALOR ACHADO: R$ {produtoBuscado[1]:.2f}\n')
                    novoValorProduto = input('DIGITE O NOVO PREÇO DO PRODUTO: ')
                    while True:
                        if not novoValorProduto.isnumeric():
                            print('APENAS VALORES NUMÉRICOS SÃO PERMITIDOS NO PREÇO!')
                            novoValorProduto = input('DIGITE O VALOR DO PRODUTO NOVAMENTE: ')
                        else:
                            break
                    produtoBuscado[1] = float(novoValorProduto)
                    print('VALOR ATUALIZADO COM SUCESSO.')
                    break

            else:
                print('\nPRODUTO NÃO ENCONTRADO.')
                continue

        elif optionAtualizarProduto == '0':
            break


def removerProduto(vendedores, loginDoUsuario):
    remocaoProduto = input('DIGITE O NOME DO PRODUTO QUE DESEJA REMOVER: ').upper()
    removidos = []

    for produtoBuscado in vendedores[loginDoUsuario][6]:
        if produtoBuscado[0].find(remocaoProduto) >= 0:
            removidos.append(produtoBuscado)

    for produtosParaRemover in removidos:
        removidos.remove(produtosParaRemover)
        print('PRODUTO REMOVIDO COM SUCESSO.')

    if len(removidos) == 0:
        print('\nPRODUTO NÃO ENCONTRADO!')


def removerConta(vendedores):
    remocaoConta = input('DIGITE O CNPJ DA SUA CONTA PARA REMOVER: ').strip()
    for cnpj in vendedores:
        while True:
            if remocaoConta != vendedores[cnpj][1]:
                print('\nESSE CNPJ NÃO FOI ENCONTRADO')
                remocaoConta = input('DIGITE O CNPJ NOVAMENTE: ').strip()
            else:
                break
    verification = False

    while not verification:
        print('\nPRECISAMOS VERIFICAR SE É VOCÊ MESMO!')
        senhaDoUsuario = input('DIGITE SUA SENHA: ').strip()
        for cnpj in vendedores:
            if senhaDoUsuario != vendedores[cnpj][5]:
                print('\nSENHA INVÁLIDA!')
                print('\nTENTE NOVAMENTE.')
                continue
            else:
                print('\nDIGITE Y - SIM OU N - NÃO')
                pergSeguranca = input('\nDESEJA REALMENTE EXCLUIR SUA CONTA? ').upper()
                if pergSeguranca == 'Y':
                    vendedores.pop(remocaoConta)
                    print('\nCONTA EXCLUÍDA.')
                    verification = True
                    login = False
                    break

                elif pergSeguranca == 'N':
                    print('\nREMOÇÃO CANCELADA.')
                    verification = True
                    break

                else:
                    print("\nÉ NECESSÁRIO DIGITAR 'Y' OU 'N'.\n")
                    print('TENTE NOVAMENTE.')
                    continue