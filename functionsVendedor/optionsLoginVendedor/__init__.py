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
        codProd = input('DIGITE O CÓDIGO DO PRODUTO: ')
        precoProd = input('DIGITE O VALOR DO PRODUTO: ')
        quantProd = input('DIGITE A QUANTIDADE EM ESTOQUE DO PRODUTO: ')
        descProd = input('DESCRIÇÃO DO PRODUTO: ').capitalize()


        while True:
            if not precoProd.isnumeric():
                print('APENAS VALORES NUMÉRICOS SÃO PERMITIDOS NO PREÇO!')
                precoProd = input('DIGITE O VALOR DO PRODUTO NOVAMENTE: ')
            elif not quantProd.isnumeric():
                print('APENAS VALORES NUMÉRICOS SÃO PERMITIDOS NO PREÇO!')
                quantProd = input('DIGITE A QUANTIDADE DO PRODUTO EM ESTOQUE NOVAMENTE: ')
            else:
                break

        produto.append(nomeProd)
        produto.append(codProd)
        produto.append(float(precoProd))
        produto.append(int(quantProd))
        produto.append(descProd)
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
            print(f'\nCÓDIGO DO PRODUTO: {produtoBuscado[1]}')
            print(f'\nVALOR DO PRODUTO: R$ {produtoBuscado[2]:.2f}')
            print(f'\nQUANTIDADE DO PRODUTO EM ESTOQUE: {produtoBuscado[3]}')
            print(f'\nDESCRIÇÃO DO PRODUTO: {produtoBuscado[4]}')
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
                    print(f'\nPRODUTO ACHADO: {produtoBuscado[1]}\n')
                    novoNomeProduto = input('DIGITE O NOVO NOME DO PRODUTO: ').upper()
                    produtoBuscado[0] = novoNomeProduto
                    print('NOME ATUALIZADO COM SUCESSO!')
                    break
                else:
                    print('PRODUTO NÃO ENCONTRADO.')
                    continue
            break

        elif optionAtualizarProduto == '2':
            atualizarProdutoCod = input('\nDIGITE O NOME DO PRODUTO QUE DESEJA ATUALIZAR O CÓDIGO: ').upper()
            for produtoBuscado in vendedores[loginDoUsuario][6]:
                if produtoBuscado[0].find(atualizarProdutoCod) >= 0:
                    print(f'\nPRODUTO ACHADO: {produtoBuscado[1]}\n')
                    novoCodProduto = input('DIGITE O NOVO CÓDIGO DO PRODUTO: ').upper()
                    produtoBuscado[1] = novoCodProduto
                    print('CÓDIGO ATUALIZADO COM SUCESSO!')
                    break
                else:
                    print('PRODUTO NÃO ENCONTRADO.')
                    continue
            break

        elif optionAtualizarProduto == '3':
            atualizarProdutoValor = input('\nDIGITE O NOME DO PRODUTO QUE DESEJA ATUALIZAR O VALOR: ').upper()
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
                    produtoBuscado[2] = float(novoValorProduto)
                    print('VALOR ATUALIZADO COM SUCESSO.')
                    break
                else:
                    print('PRODUTO NÃO ENCONTRADO.')
                    continue
            break

        elif optionAtualizarProduto == '4':
            atualizarProdutoQuant = input('\nDIGITE O NOME DO PRODUTO QUE DESEJA ATUALIZAR O VALOR: ').upper()
            for produtoBuscado in vendedores[loginDoUsuario][6]:
                if produtoBuscado[0].find(atualizarProdutoQuant) >= 0:
                    print(f'\nVALOR ACHADO: R$ {produtoBuscado[1]:.2f}\n')
                    novoQuantProduto = input('DIGITE A QUANTIDADE EM ESTOQUE DO PRODUTO: ')
                    while True:
                        if not novoQuantProduto.isnumeric():
                            print('APENAS VALORES NUMÉRICOS SÃO PERMITIDOS NO PREÇO!')
                            novoQuantProduto = input('DIGITE A QUANTIDADE EM ESTOQUE DO PRODUTO NOVAMENTE: ')
                        else:
                            break
                    produtoBuscado[3] = float(novoQuantProduto)
                    print('ESTOQUE ATUALIZADO COM SUCESSO.')
                    break
                else:
                    print('PRODUTO NÃO ENCONTRADO.')
                    continue
            break

        elif optionAtualizarProduto == '5':
            atualizarProdutoDesc = input('\nDIGITE O NOME DO PRODUTO QUE DESEJA ATUALIZAR: ').upper()
            for produtoBuscado in vendedores[loginDoUsuario][6]:
                if produtoBuscado[0].find(atualizarProdutoDesc) >= 0:
                    print(f'\nPRODUTO ACHADO: {produtoBuscado[1]}\n')
                    novoDescProduto = input('DIGITE A NOVA DESCRIÇÃO DO PRODUTO: ').upper()
                    produtoBuscado[4] = novoDescProduto
                    print('DESCRIÇÃO ATUALIZADA COM SUCESSO!')
                    break
                else:
                    print('PRODUTO NÃO ENCONTRADO.')
                    continue
            break

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