def senhaAreaLoginVendedor(dicionario: dict, senha, chaveparalogin):
    while True:
        if senha != dicionario[chaveparalogin][6]:
            print('\nSENHA INVÁLIDA!')
            senha = input('DIGITE A SUA SENHA NOVAMENTE: ').strip()
        else:
            login = True
            break
    return login

def atualizarSenha(vendedores: dict, loginDoUsuario):
    confirmarSenha = input('SENHA ATUAL: ').strip()

    while True:
        if confirmarSenha != vendedores[loginDoUsuario][6]:
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
                vendedores[loginDoUsuario][6] = novaSenha
                print('\nSENHA ALTERADA COM SUCESSO!')
                break

            elif pergSeguranca == 'N':
                print('\nMUDANÇA CANCELADA.')
                break

            else:
                print("\nÉ NECESSÁRIO DIGITAR 'Y' OU 'N'.")
                print('DIGITE A SUA NOVA SENHA NOVAMENTE.')
                continue

def cadastrarProdutos(vendedores: dict, loginDoUsuario, lista: list):
    produtos = []
    quantProdutos = int(input('\nDIGITE QUANTOS PRODUTOS DESEJA CADASTRAR: '))

    for i in range(0, quantProdutos,):
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
        produto.append(loginDoUsuario)
        produtos.append(produto)

        print('\nPRODUTO(s) CADASTRADO(s).')
        continue
    vendedores[loginDoUsuario][7] = produtos
    lista.append(produtos)

def buscarProduto(vendedores, loginDoUsuario):
    buscarProduto = input('DIGITE O NOME DO PRODUTO QUE DESEJA BUSCAR: ').upper()
    busca = False

    for produtoBuscado in vendedores[loginDoUsuario][7]:
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
            for produtoBuscado in vendedores[loginDoUsuario][7]:
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
            for produtoBuscado in vendedores[loginDoUsuario][7]:
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
            for produtoBuscado in vendedores[loginDoUsuario][7]:
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
            for produtoBuscado in vendedores[loginDoUsuario][7]:
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
            for produtoBuscado in vendedores[loginDoUsuario][7]:
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

    for produtoBuscado in vendedores[loginDoUsuario][7]:
        if produtoBuscado[0].find(remocaoProduto) >= 0:
            removidos.append(produtoBuscado)

    for produtosParaRemover in removidos:
        removidos.remove(produtosParaRemover)
        print('PRODUTO REMOVIDO COM SUCESSO.')

    if len(removidos) == 0:
        print('\nPRODUTO NÃO ENCONTRADO!')


def removerConta(vendedores, chaveParaLogin):
    chaveParaRemover = input('DIGITE O CNPJ DA SUA CONTA PARA REMOVER: ').strip()
    while True:
        if chaveParaRemover != vendedores[chaveParaLogin][1]:
            print('\nESSE CNPJ NÃO FOI ENCONTRADO')
            chaveParaRemover = input('DIGITE O CNPJ NOVAMENTE: ').strip()
        else:
            break
    verification = False

    while not verification:
        print('\nPRECISAMOS VERIFICAR SE É VOCÊ MESMO!')
        senhaDoUsuario = input('DIGITE SUA SENHA: ').strip()
        if senhaDoUsuario != vendedores[chaveParaLogin][6]:
            print('\nSENHA INVÁLIDA!')
            print('\nTENTE NOVAMENTE.')
            continue
        else:
            print('\nDIGITE Y - SIM OU N - NÃO')
            pergSeguranca = input('\nDESEJA REALMENTE EXCLUIR SUA CONTA? ').upper()
            if pergSeguranca == 'Y':
                vendedores.pop(chaveParaRemover)
                print('\nCONTA EXCLUÍDA.')
                return False
                break

            elif pergSeguranca == 'N':
                print('\nREMOÇÃO CANCELADA.')
                return True
                break

            else:
                print("\nÉ NECESSÁRIO DIGITAR 'Y' OU 'N'.\n")
                print('TENTE NOVAMENTE.')
                continue