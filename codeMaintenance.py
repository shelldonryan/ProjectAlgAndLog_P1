from time import sleep
import functionsMenu
from functionsMenu import menuVendedor, menuCliente
from functionsVendedor import optionsLoginVendedor
from functionsCliente import optionsLoginCliente
import verificarExistencia
import validarDado

vendedores = {}
clientes = {}

optionInicial = -1
while optionInicial != 0:
    functionsMenu.mensagemInicial()
    optionInicial = functionsMenu.menuInicial()

    if optionInicial == '1':

        optionVendedor = -1
        while optionVendedor != 0:
            optionVendedor = menuVendedor.menuInicialVendedor()

            if not optionVendedor.isdigit():
                print('\nSÓ NÚMEROS NAS OPÇÕES')
                continue

            if optionVendedor == '0':
                print('\nRETROCEDENDO PÁGINA...')
                sleep(2)
                break

            elif optionVendedor == '1':
                print('\nPRECISAREMOS DE ALGUNS DADOS SEUS PARA A REALIZAÇÃO DO CADASTRO, INFORME-OS A SEGUIR ->')

                nomeDoVendedor = input('QUAL É O SEU NOME COMPLETO? ').strip().title()

                nomeExiste = verificarExistencia.nomeExiste(nomeDoVendedor, vendedores)
                if nomeExiste:
                    print('\nESSE NOME JÁ FOI USADO EM UM CADASTRO ANTERIOR.')
                    continue

                nomeDoVendedor = validarDado.validarNome(nomeDoVendedor)

                cnpj = input('\nINFORME SEU CNPJ: ').strip()

                cnpjExiste = verificarExistencia.cnpjExiste(cnpj, vendedores)

                if cnpjExiste:
                    print('\nESSE CNPJ JÁ FOI USADO ANTERIORMENTE.')
                    continue

                cnpj = validarDado.validarCnpj(cnpj)

                telefone = input('\nINFORME SEU NÚMERO DE TELEFONE COM DDD: ')

                telefoneExiste = verificarExistencia.telefoneExiste(telefone, vendedores)

                if telefoneExiste:
                    print('\nESSE NÚMERO DE TELEFONE JÁ FOI USADO ANTERIORMENTE.')
                    continue

                telefone = validarDado.validarTelefone(telefone)

                nomeUsuario = input('\nCRIE SEU NOME DE USUÁRIO: ').strip()

                loginExiste = verificarExistencia.loginExiste(nomeUsuario, vendedores)

                if loginExiste:
                    print('\nESSE NOME DE USUÁRIO JÁ FOI USADO EM UM CADASTRO ANTERIOR.')
                    continue

                nomeUsuario = validarDado.validarUsuario(nomeUsuario)

                print('\nEX: renegadelha@gmail.com')
                emailDoUsuario = input('CADASTRE O SEU EMAIL: ').strip()

                emailExiste = verificarExistencia.emailExiste(emailDoUsuario, vendedores)

                if emailExiste:
                    print('ESSE EMAIL JÁ ESTÁ SENDO USADO.')
                    continue

                emailDoUsuario = validarDado.validarEmail(emailDoUsuario)

                senhaDeUsuario = input('\nCADASTRE SUA SENHA: ').strip()

                senhaExiste = verificarExistencia.senhaExiste(senhaDeUsuario, vendedores)

                if senhaExiste:
                    print('\nESSA SENHA JÁ EXISTE.')
                    continue

                senhaDeUsuario = validarDado.validarSenha(senhaDeUsuario)

                vendedores[cnpj] = [nomeDoVendedor, cnpj, telefone, nomeUsuario, emailDoUsuario, senhaDeUsuario, '']
                print('\nVENDEDOR CADASTRADO COM SUCESSO!')

            elif optionVendedor == '2':
                print('\n|-----ÁREA DE LOGIN-----|\n')
                login = False
                chaveParaLogin = ''
                while not login:
                    if len(vendedores) == 0:
                        print('NENHUM VENDEDOR AINDA FOI CADASTRADO!')
                        break

                    loginDoVendedor = optionsLoginVendedor.usuarioAreaLogin(vendedores)
                    chaveParaLogin = loginDoVendedor

                    senhaDoUsuarioVendedor = input('SENHA: ').strip()

                    login = optionsLoginVendedor.senhaAreaLogin(vendedores, senhaDoUsuarioVendedor)
                else:
                    print('LOGIN EFETUADO.\n')

                if len(vendedores) != 0:
                    print(f'OLÁ VENDEDOR {vendedores[chaveParaLogin][0]}, BEM-VINDO AO SERTÃO LIVRE')

                while login:

                    optionLoginVendedor = menuVendedor.menuLoginVendedor()

                    if not optionLoginVendedor.isdigit():
                        print('DIGITE APENAS NÚMEROS.')
                        continue

                    if optionLoginVendedor == '0':
                        print('CONTA ENCERRADA.')
                        login = False
                        break

                    elif optionLoginVendedor == '1':
                        optionsLoginVendedor.atualizarSenha(vendedores, chaveParaLogin)

                    elif optionLoginVendedor == '2':
                        optionsLoginVendedor.cadastrarProdutos(vendedores, chaveParaLogin)

                    elif optionLoginVendedor == '3':
                        optionsLoginVendedor.buscarProduto(vendedores, chaveParaLogin)

                    elif optionLoginVendedor == '4':
                        optionsLoginVendedor.atualizarProduto(vendedores, chaveParaLogin, menuVendedor.menuAtualizarProduto())

                    elif optionLoginVendedor == '5':
                        optionsLoginVendedor.removerProduto(vendedores, chaveParaLogin)

                    elif optionLoginVendedor == '6':
                        optionsLoginVendedor.removerConta(vendedores)

            else:
                print('OPÇÃO INVÁLIDA, DIGITE NOVAMENTE.')

    elif optionInicial == '2':

        optionCliente = -1
        while optionCliente != 0:
            optionCliente = menuCliente.menuInicialCliente()

            if not optionCliente.isdigit():
                print('\nSÓ NÚMEROS NAS OPÇÕES')
                continue

            if optionCliente == '0':
                print('\nRETROCEDENDO PÁGINA...')
                sleep(2)
                break

            if optionCliente == '1':
                print('\nPRECISAREMOS DE ALGUNS DADOS SEUS PARA A REALIZAÇÃO DO CADASTRO, INFORME-OS A SEGUIR ->')

                nomeDoCliente = input('QUAL É O SEU NOME COMPLETO? ').strip().title()

                nomeExiste = verificarExistencia.nomeExiste(nomeDoCliente, clientes)
                if nomeExiste:
                    print('\nESSE NOME JÁ FOI USADO EM UM CADASTRO ANTERIOR.')
                    continue

                nomeDoCliente = validarDado.validarNome(nomeDoCliente)

                cnpjCliente = input('\nINFORME SEU CNPJ: ').strip()

                cnpjExiste = verificarExistencia.cnpjExiste(cnpjCliente, clientes)

                if cnpjExiste:
                    print('\nESSE CNPJ JÁ FOI USADO ANTERIORMENTE.')
                    continue

                cnpjCliente = validarDado.validarCnpj(cnpjCliente)

                telefoneCliente = input('\nINFORME SEU NÚMERO DE TELEFONE COM DDD: ')

                telefoneExiste = verificarExistencia.telefoneExiste(telefoneCliente, clientes)

                if telefoneExiste:
                    print('\nESSE NÚMERO DE TELEFONE JÁ FOI USADO ANTERIORMENTE.')
                    continue

                telefoneCliente = validarDado.validarTelefone(telefoneCliente)

                nomeUsuarioCliente = input('\nCRIE SEU NOME DE USUÁRIO: ').strip()

                loginExiste = verificarExistencia.loginExiste(nomeUsuarioCliente, clientes)

                if loginExiste:
                    print('\nESSE NOME DE USUÁRIO JÁ FOI USADO EM UM CADASTRO ANTERIOR.')
                    continue

                nomeUsuarioCliente = validarDado.validarUsuario(nomeUsuarioCliente)

                print('\nEX: renegadelha@gmail.com')
                emailDoCliente = input('CADASTRE O SEU EMAIL: ').strip()

                emailExiste = verificarExistencia.emailExiste(emailDoCliente, vendedores)

                if emailExiste:
                    print('ESSE EMAIL JÁ ESTÁ SENDO USADO.')
                    continue

                emailDoCliente = validarDado.validarEmail(emailDoCliente)

                senhaDeUsuarioCliente = input('\nCADASTRE SUA SENHA: ').strip()

                senhaExiste = verificarExistencia.senhaExiste(senhaDeUsuarioCliente, vendedores)

                if senhaExiste:
                    print('\nESSA SENHA JÁ EXISTE.')
                    continue

                senhaDeUsuarioCliente = validarDado.validarSenha(senhaDeUsuarioCliente)

                clientes[cnpjCliente] = [nomeDoCliente, cnpjCliente, telefoneCliente, nomeUsuarioCliente, emailDoCliente,
                                  senhaDeUsuarioCliente, '']
                print('\nVENDEDOR CADASTRADO COM SUCESSO!')
                print(clientes)

            if optionCliente == '2':
                print('\n|-----ÁREA DE LOGIN-----|\n')
                login = False
                chaveParaLogin = ''
                while not login:
                    if len(clientes) == 0:
                        print('NENHUM CLIENTE AINDA FOI CADASTRADO!')
                        break

                    loginDoCliente = optionsLoginCliente.usuarioAreaLogin(clientes)
                    chaveParaLogin = loginDoCliente

                    senhaDoUsuarioCliente = input('SENHA: ').strip()

                    login = optionsLoginCliente.senhaAreaLogin(clientes, senhaDoUsuarioCliente)
                else:
                    print('LOGIN EFETUADO.\n')

                if len(clientes) != 0:
                    print(f'OLÁ CLIENTE{clientes[chaveParaLogin][0]}, BEM-VINDO AO SERTÃO LIVRE')

                while login:
                    optionLoginCliente = menuCliente.menuLoginCliente()

                    if not optionLoginCliente.isdigit():
                        print('DIGITE APENAS NÚMEROS.')
                        continue

                    if optionLoginCliente == '0':
                        print('CONTA ENCERRADA.')
                        login = False
                        break

                    elif optionLoginCliente == '1':
                        optionsLoginCliente.atualizarSenha(clientes, chaveParaLogin)

                    elif optionLoginCliente == '6':
                        optionsLoginCliente.removerConta(clientes)

    elif optionInicial == '0':
        print('\nPROGRAMA ENCERRADO')
        break