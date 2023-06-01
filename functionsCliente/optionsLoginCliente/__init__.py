def usuarioAreaLogin (clientes: dict):
    loginDoCliente = input('ENTRE COM SEU CNPJ: ').strip()
    for cnpj in clientes:
        while True:
            if loginDoCliente != clientes[cnpj][1]:
                print('\nLOGIN INVÁLIDO!')
                loginDoCliente = input('DIGITE O CNPJ NOVAMENTE: ').strip()
            else:
                break
        return loginDoCliente

def senhaAreaLogin(clientes: dict, senha):
    for cnpj in clientes:
        while True:
            if senha != clientes[cnpj][5]:
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

def removerConta(clientes: dict):
    remocaoConta = input('DIGITE O CNPJ DA SUA CONTA PARA REMOVER: ').strip()
    for cnpj in clientes:
        while True:
            if remocaoConta != clientes[cnpj][1]:
                print('\nESSE CNPJ NÃO FOI ENCONTRADO')
                remocaoConta = input('DIGITE O CNPJ NOVAMENTE: ').strip()
            else:
                break
    verification = False

    while not verification:
        print('\nPRECISAMOS VERIFICAR SE É VOCÊ MESMO!')
        senhaDoUsuario = input('DIGITE SUA SENHA: ').strip()
        for cnpj in clientes:
            if senhaDoUsuario != clientes[cnpj][5]:
                print('\nSENHA INVÁLIDA!')
                print('\nTENTE NOVAMENTE.')
                continue
            else:
                print('\nDIGITE Y - SIM OU N - NÃO')
                pergSeguranca = input('\nDESEJA REALMENTE EXCLUIR SUA CONTA? ').upper()
                if pergSeguranca == 'Y':
                    clientes.pop(remocaoConta)
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