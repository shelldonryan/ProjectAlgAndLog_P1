from time import sleep
import functionsMenu
from functionsMenu import menuVendedor, menuCliente
from functionsVendedor import optionsLogin, validarDado, verificarExistencia

vendedores = {}



functionsMenu.mensagemInicial()

optionInicial = -1
while optionInicial != 0:

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
                        print('NENHUM USUÁRIO AINDA FOI CADASTRADO!')
                        break

                    loginDoUsuario = optionsLogin.usuarioAreaLogin(vendedores)
                    chaveParaLogin = loginDoUsuario

                    senhaDoUsuario = input('SENHA: ').strip()

                    login = optionsLogin.senhaAreaLogin(vendedores, senhaDoUsuario)
                else:
                    print('LOGIN EFETUADO.\n')

                if len(vendedores) != 0:
                    print(f'OLÁ {vendedores[chaveParaLogin][0]}, BEM-VINDO AO SERTÃO LIVRE')

                while login:

                    optionLoginVendedor = menuVendedor.menuLoginVendedor()

                    if not optionLoginVendedor.isdigit():
                        print('DIGITE APENAS NÚMEROS.')
                        continue

                    if optionLoginVendedor == '6':
                        print('CONTA ENCERRADA.')
                        login = False
                        break

                    elif optionLoginVendedor == '1':
                        optionsLogin.atualizarSenha(vendedores, chaveParaLogin)

                    elif optionLoginVendedor == '2':
                        optionsLogin.cadastrarProdutos(vendedores, chaveParaLogin)

                    elif optionLoginVendedor == '3':
                        optionsLogin.buscarProduto(vendedores, chaveParaLogin)

                    elif optionLoginVendedor == '4':
                        optionsLogin.atualizarProduto(vendedores, chaveParaLogin, menuVendedor.menuAtualizarProduto())

                    elif optionLoginVendedor == '5':
                        optionsLogin.removerProduto(vendedores, chaveParaLogin)

                    elif optionLoginVendedor == '7':
                        optionsLogin.removerConta(vendedores)

            else:
                print('OPÇÃO INVÁLIDA, DIGITE NOVAMENTE.')

    elif optionInicial == '2':
        optionCliente = menuCliente.menuInicialCliente()

    elif optionInicial == '0':
        print('\nPROGRAMA ENCERRADO')
        break