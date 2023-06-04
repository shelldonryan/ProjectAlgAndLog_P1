from time import sleep
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

def buscarProduto(lista: list, menu, chaveParaLogin):
    while True:
        optionBuscarProduto = menu

        if not optionBuscarProduto.isdigit():
            print('SÓ NÚMEROS NAS OPÇÕES.')
            break

        if optionBuscarProduto == '1':
            buscarProduto = input('\nDIGITE O NOME DO PRODUTO QUE DESEJA BUSCAR: ').upper()
            buscado = False

            for v in range(0, len(lista)):
                for produtoBuscado in lista:
                    if produtoBuscado[0].find(buscarProduto) >= 0:
                        print('-=-' * 20)
                        print(f'NOME DO PRODUTO: {produtoBuscado[0].capitalize()}')
                        print(f'\nCÓDIGO DO PRODUTO: {produtoBuscado[1]}')
                        print(f'\nVALOR DO PRODUTO: R$ {produtoBuscado[2]:.2f}')
                        print(f'\nQUANTIDADE DO PRODUTO EM ESTOQUE: {produtoBuscado[3]}')
                        print(f'\nDESCRIÇÃO DO PRODUTO: {produtoBuscado[4]}')
                        print('-=-' * 20)
                        buscado = True

            if not buscado:
                print('\nPRODUTO NÃO ENCONTRADO.')
                break
            #else:



        elif optionBuscarProduto == '2':
            buscarProduto = input('\nDIGITE A DESCRIÇÃO DO PRODUTO QUE DESEJA BUSCAR: ').capitalize()

            for v in range(0, len(lista)):
                for produtoBuscado in lista[v]:
                    if produtoBuscado[4].find(buscarProduto) >= 0:
                        print('-=-' * 20)
                        print(f'NOME DO PRODUTO: {produtoBuscado[0].capitalize()}')
                        print(f'\nCÓDIGO DO PRODUTO: {produtoBuscado[1]}')
                        print(f'\nVALOR DO PRODUTO: R$ {produtoBuscado[2]:.2f}')
                        print(f'\nQUANTIDADE DO PRODUTO EM ESTOQUE: {produtoBuscado[3]}')
                        print(f'\nDESCRIÇÃO DO PRODUTO: {produtoBuscado[4]}')
                        print('-=-' * 20)
            else:
                print('\nPRODUTO NÃO ENCONTRADO.')
                break

        elif optionBuscarProduto == '0':
            print('\nVOLTANDO AO MENU PRINCIPAL...')
            sleep(2)
            busca = True
            return busca

def listaDeCompras(lista: dict, chaveParaLogin):
    if len(lista[chaveParaLogin][6]) == 0:
        print('VOCÊ NÃO REALIZOU NENHUMA COMPRA!')


    for compras in lista[chaveParaLogin][6]:
            print('-=-' * 20)
            print(f'NOME DO PRODUTO: {compras[0].capitalize()}')
            print(f'\nCÓDIGO DO PRODUTO: {compras[1]}')
            print(f'\nVALOR DO PRODUTO: R$ {compras[2]:.2f}')
            print(f'\nQUANTIDADE DO PRODUTO EM ESTOQUE: {compras[3]}')
            print(f'\nDESCRIÇÃO DO PRODUTO: {compras[4]}')
            print('-=-' * 20)


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