from time import sleep
#from chatgpt.openai import consultarchatgpt
def senhaAreaLoginCliente(dicionario: dict, senha, chaveparalogin):
    while True:
        if senha != dicionario[chaveparalogin][5]:
            print('\nSENHA INVÁLIDA!')
            senha = input('DIGITE A SUA SENHA NOVAMENTE: ').strip()
        else:
            login = True
            break
    return login

def atualizarSenha(clientes: dict, loginDoUsuario):
    confirmarSenha = input('SENHA ATUAL: ').strip()

    while True:
        if confirmarSenha != clientes[loginDoUsuario][5]:
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
                clientes[loginDoUsuario][5] = novaSenha
                print('\nSENHA ALTERADA COM SUCESSO!')
                break

            elif pergSeguranca == 'N':
                print('\nMUDANÇA CANCELADA.')
                break

            else:
                print("\nÉ NECESSÁRIO DIGITAR 'Y' OU 'N'.")
                print('DIGITE A SUA NOVA SENHA NOVAMENTE.')
                continue

def buscarProduto(lista: list, lista2: list, menuBuscarProduto, chaveParaLogin):
    while True:
        optionBuscarProduto = menuBuscarProduto

        if not optionBuscarProduto.isdigit():
            print('SÓ NÚMEROS NAS OPÇÕES.')
            break

        if optionBuscarProduto == '1':
            buscarProduto = input('\nDIGITE O NOME DO PRODUTO QUE DESEJA BUSCAR: ').upper()
            buscado = False

            for v in range(0, (len(lista))):
                for produtoBuscado in lista[v]:
                    if produtoBuscado[0].find(buscarProduto) >= 0:
                        print('-=-' * 20)
                        print(f'NOME DO PRODUTO: {produtoBuscado[0].capitalize()}')
                        print(f'\nCÓDIGO DO PRODUTO: {produtoBuscado[1]}')
                        print(f'\nVALOR DO PRODUTO: R$ {produtoBuscado[2]:.2f}')
                        print(f'\nQUANTIDADE DO PRODUTO EM ESTOQUE: {produtoBuscado[3]}')
                        print(f'\nINFORMARÇÕES DO PRODUTO: {produtoBuscado[4]}')
                        print('-=-' * 20)
                        buscado = True
            #print(f'\nDESCRIÇÃO DO PRODUTO: {consultarchatgpt(buscarProduto)}')

            if not buscado:
                print('\nPRODUTO NÃO ENCONTRADO.')
                break
            if buscado:
                pergConfirmar = input('DESEJA COMPRAR ALGUM PRODUTO? (Y OR N) ->  ').upper()
                if pergConfirmar == 'Y':
                    print('\n---ÁREA DE COMPRA---')
                    codeProdutoComprar = input('\nDIGITE O CÓDIGO DO PRODUTO QUE DESEJA REALIZAR A COMPRA: ')
                    quantDaCompra = int(input('QUANTOS PRODUTOS DESEJA COMPRAR? '))
                    validar = True

                    for i in range(0, (len(lista))):
                        for produtoBuscado in lista[i]:
                            if codeProdutoComprar in produtoBuscado[1]:
                                if produtoBuscado[5] == lista2[chaveParaLogin][1]:
                                    print('\nO VENDEDOR NÃO PODE COMPRAR O PRÓRPIO PRODUTO!')
                                    validar = False

                    listaDeCompra = lista2[chaveParaLogin][6]
                    verificationProduto = False
                    if validar:
                        for produtoCliente in listaDeCompra:
                            if codeProdutoComprar == produtoCliente[1]:
                                verificationProduto = True

                        for v in range(0, (len(lista))):
                            for produtoBuscado in lista[v]:
                                produtoComprado = []
                                if codeProdutoComprar == produtoBuscado[1]:
                                    if produtoBuscado[3] < quantDaCompra or produtoBuscado[3] == 0:
                                        print('QUANTIDADE INSUFICIENTE EM ESTOQUE!')
                                    elif verificationProduto:
                                        for produtoCliente in listaDeCompra:
                                            produtoCliente[3] += quantDaCompra
                                            produtoBuscado[3] -= quantDaCompra
                                            print(f'\nPRODUTO COMPRADO COM SUCESSO')
                                    else:
                                        produtoComprado.append(produtoBuscado[0].capitalize())
                                        produtoComprado.append(produtoBuscado[1])
                                        produtoComprado.append(produtoBuscado[2])
                                        produtoComprado.append(quantDaCompra)
                                        produtoComprado.append(produtoBuscado[4])
                                        listaDeCompra.append(produtoComprado)
                                        produtoBuscado[3] -= quantDaCompra
                                        print('\nPRODUTO COMPRADO COM SUCESSO')

                break

        elif optionBuscarProduto == '2':
            buscarProduto = input('\nDIGITE A DESCRIÇÃO DO PRODUTO QUE DESEJA BUSCAR: ').capitalize()
            buscado = False
            nomeProdutoBuscado = []

            for v in range(0, len(lista)):
                for produtoBuscado in lista[v]:
                    if produtoBuscado[4].find(buscarProduto) >= 0:
                        print('-=-' * 20)
                        nomeProdutoBuscado.append(produtoBuscado[0])
                        print(f'NOME DO PRODUTO: {produtoBuscado[0].capitalize()}')
                        print(f'\nCÓDIGO DO PRODUTO: {produtoBuscado[1]}')
                        print(f'\nVALOR DO PRODUTO: R$ {produtoBuscado[2]:.2f}')
                        print(f'\nINFORMAÇÕES DO PRODUTO: {produtoBuscado[4]}')
                        print('-=-' * 20)
                        buscado = True
            # print(f'\nDESCRIÇÃO DO PRODUTO: {consultarchatgpt(nomeProdutoBuscado[0])}')

            if not buscado:
                print('\nPRODUTO NÃO ENCONTRADO.')
                break
            if buscado:
                pergConfirmar = input('DESEJA COMPRAR ALGUM PRODUTO? (Y OR N) ->  ').upper()
                if pergConfirmar == 'Y':
                    print('\n---ÁREA DE COMPRA---')
                    codeProdutoComprar = input('\nDIGITE O CÓDIGO DO PRODUTO QUE DESEJA REALIZAR A COMPRA: ')
                    quantDaCompra = int(input('QUANTOS PRODUTOS DESEJA COMPRAR? '))
                    validar = True

                    for i in range(0, (len(lista))):
                        for produtoBuscado in lista[i]:
                            if codeProdutoComprar in produtoBuscado[1]:
                                if produtoBuscado[5] == lista2[chaveParaLogin][1]:
                                    print('\nO VENDEDOR NÃO PODE COMPRAR O PRÓRPIO PRODUTO!')
                                    validar = False

                    listaDeCompra = lista2[chaveParaLogin][6]
                    verificationProduto = False
                    if validar:
                        for i in range(len(listaDeCompra)):
                            for produtoCliente in listaDeCompra[i]:
                                if codeProdutoComprar == produtoCliente[1]:
                                    verificationProduto = True

                        for v in range(0, (len(lista))):
                            for produtoBuscado in lista[v]:
                                produtoComprado = []
                                if codeProdutoComprar == produtoBuscado[1]:
                                    if produtoBuscado[3] < quantDaCompra or produtoBuscado[3] == 0:
                                        print('QUANTIDADE INSUFICIENTE EM ESTOQUE!')
                                    elif verificationProduto:
                                        for i in range(len(listaDeCompra)):
                                            for produtoCliente in listaDeCompra[i]:
                                                produtoCliente[3] += quantDaCompra
                                                produtoBuscado -= quantDaCompra
                                                print(f'\nPRODUTO COMPRADO COM SUCESSO')
                                    else:
                                        produtoComprado.append(produtoBuscado[0].capitalize())
                                        produtoComprado.append(produtoBuscado[1])
                                        produtoComprado.append(produtoBuscado[2])
                                        produtoComprado.append(quantDaCompra)
                                        produtoComprado.append(produtoBuscado[4])
                                        listaDeCompra.append(produtoComprado)
                                        produtoBuscado[3] -= quantDaCompra
                                        print('\nPRODUTO COMPRADO COM SUCESSO')

            break

        elif optionBuscarProduto == '0':
            print('\nVOLTANDO AO MENU PRINCIPAL...')
            sleep(2)
            busca = True
            return busca

def listaDeCompras(lista: dict, chaveParaLogin):
    if len(lista[chaveParaLogin][6]) == 0:
        print('VOCÊ NÃO REALIZOU NENHUMA COMPRA!')

    nomeProdutoListado = []
    for compras in lista[chaveParaLogin][6]:
        print('-=-' * 20)
        print(f'NOME DO PRODUTO: {compras[0].capitalize()}')
        nomeProdutoListado.append(compras[0])
        print(f'\nCÓDIGO DO PRODUTO: {compras[1]}')
        print(f'\nVALOR DO PRODUTO: R$ {compras[2]:.2f}')
        print(f'\nQUANTIDADE COMPRADA: {compras[3]} {str(compras[0]).capitalize()}')
        print(f'\nINFORMAÇÕES DO PRODUTO: {compras[4]}')
        print('-=-' * 20)
        #print(f'\nDESCRIÇÃO DO PRODUTO: {consultarchatgpt(nomeProdutoListado[0])}')

def removerConta(clientes: dict, chaveParaLogin):
    chaveParaRemover = input('DIGITE O CPF DA SUA CONTA PARA REMOVER: ').strip()
    while True:
        if chaveParaRemover != clientes[chaveParaLogin][1]:
            print('\nESSE CPF NÃO FOI ENCONTRADO')
            chaveParaRemover = input('DIGITE O CPF NOVAMENTE: ').strip()
        else:
            break
    verification = False

    while not verification:
        print('\nPRECISAMOS VERIFICAR SE É VOCÊ MESMO!')
        senhaDoUsuario = input('DIGITE SUA SENHA: ').strip()
        if senhaDoUsuario != clientes[chaveParaLogin][5]:
            print('\nSENHA INVÁLIDA!')
            print('\nTENTE NOVAMENTE.')
            continue
        else:
            print('\nDIGITE Y - SIM OU N - NÃO')
            pergSeguranca = input('\nDESEJA REALMENTE EXCLUIR SUA CONTA? ').upper()
            if pergSeguranca == 'Y':
                clientes.pop(chaveParaRemover)
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