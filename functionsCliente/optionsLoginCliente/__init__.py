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

def buscarProduto(lista: list, functionMenu):
    global buscarProduto, busca
    while True:
        optionBuscarProduto = functionMenu

        if not optionBuscarProduto.isdigit():
            print('SÓ NÚMEROS NAS OPÇÕES.')
            continue

        if optionBuscarProduto == '1':
            busca = False
            while busca:
                buscarProduto = input('DIGITE O NOME DO PRODUTO QUE DESEJA BUSCAR: ').upper()

                for v in range(0, len(lista)):
                    for produtoBuscado in lista[v]:
                        if produtoBuscado[0].find(buscarProduto) >= 0:
                            print(f'\nNOME DO PRODUTO: {produtoBuscado[0].capitalize()}')
                            print(f'\nCÓDIGO DO PRODUTO: {produtoBuscado[1]}')
                            print(f'\nVALOR DO PRODUTO: R$ {produtoBuscado[2]:.2f}')
                            print(f'\nQUANTIDADE DO PRODUTO EM ESTOQUE: {produtoBuscado[3]}')
                            print(f'\nDESCRIÇÃO DO PRODUTO: {produtoBuscado[4]}')
                            busca = True
                    if not busca:
                        print('PRODUTO NÃO ENCONTRADO.')

        elif optionBuscarProduto == '2':
            busca = False
            while busca:
                buscarProduto = input('DIGITE A DESCRIÇÃO DO PRODUTO QUE DESEJA BUSCAR: ').upper()

                for v in range(0, len(lista)):
                    for produtoBuscado in lista[v]:
                        if produtoBuscado[4].find(buscarProduto) >= 0:
                            print(f'\nNOME DO PRODUTO: {produtoBuscado[0].capitalize()}')
                            print(f'\nCÓDIGO DO PRODUTO: {produtoBuscado[1]}')
                            print(f'\nVALOR DO PRODUTO: R$ {produtoBuscado[2]:.2f}')
                            print(f'\nQUANTIDADE DO PRODUTO EM ESTOQUE: {produtoBuscado[3]}')
                            print(f'\nDESCRIÇÃO DO PRODUTO: {produtoBuscado[4]}')
                            busca = True
                    if not busca:
                        print('PRODUTO NÃO ENCONTRADO.')

def removerConta(clientes: dict, chaveParaLogin):
    chaveParaRemover = input('DIGITE O CNPJ DA SUA CONTA PARA REMOVER: ').strip()
    while True:
        if chaveParaRemover != clientes[chaveParaLogin][1]:
            print('\nESSE CNPJ NÃO FOI ENCONTRADO')
            chaveParaRemover = input('DIGITE O CNPJ NOVAMENTE: ').strip()
        else:
            break
    verification = False

    while not verification:
        print('\nPRECISAMOS VERIFICAR SE É VOCÊ MESMO!')
        senhaDoUsuario = input('DIGITE SUA SENHA: ').strip()
        if senhaDoUsuario != clientes[chaveParaLogin][6]:
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