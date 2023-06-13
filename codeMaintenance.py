from time import sleep
import functionsMenu
from functionsMenu import menuVendedor, menuCliente
from functionsVendedor import optionsLoginVendedor
from functionsCliente import optionsLoginCliente
import verificarExistencia
import validarDado
from chatgpt.matplotlib import graphic
from vizualizarRelatorio import criarRelatorio

vendedores = {}
clientes = {}
produtosNoSistema = []

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

                cnpjVendedor = input('\nINFORME SEU CNPJ: ').strip()

                cnpjExiste = verificarExistencia.cnpjExiste(cnpjVendedor, vendedores)

                if cnpjExiste:
                    print('\nESSE CNPJ JÁ FOI USADO ANTERIORMENTE.')
                    continue

                cnpjVendedor = validarDado.validarCnpj(cnpjVendedor)

                cpfVendedor = input('\nINFORME SEU CPF: ').strip()

                cpfExiste = verificarExistencia.cpfExisteVendedor(cpfVendedor, vendedores)

                if cpfExiste:
                    print('\nESSE CNPJ JÁ FOI USADO ANTERIORMENTE.')
                    continue

                cpfVendedor = validarDado.validarCpf(cpfVendedor)

                telefoneVendedor = input('\nINFORME SEU NÚMERO DE TELEFONE COM DDD: ')

                telefoneExiste = verificarExistencia.telefoneExiste(telefoneVendedor, vendedores)

                if telefoneExiste:
                    print('\nESSE NÚMERO DE TELEFONE JÁ FOI USADO ANTERIORMENTE.')
                    continue

                telefoneVendedor = validarDado.validarTelefone(telefoneVendedor)

                nomeUsuarioVendedor = input('\nCRIE SEU NOME DE USUÁRIO: ').strip()

                loginExiste = verificarExistencia.loginExiste(nomeUsuarioVendedor, vendedores)

                if loginExiste:
                    print('\nESSE NOME DE USUÁRIO JÁ FOI USADO EM UM CADASTRO ANTERIOR.')
                    continue

                nomeUsuarioVendedor = validarDado.validarUsuario(nomeUsuarioVendedor)

                print('\nEX: renegadelha@gmail.com')
                emailDoVendedor = input('CADASTRE O SEU EMAIL: ').strip()

                emailExiste = verificarExistencia.emailExiste(emailDoVendedor, vendedores)

                if emailExiste:
                    print('ESSE EMAIL JÁ ESTÁ SENDO USADO.')
                    continue

                emailDoVendedor = validarDado.validarEmail(emailDoVendedor)

                senhaDeUsuarioVendedor = input('\nCADASTRE SUA SENHA: ').strip()

                senhaExiste = verificarExistencia.senhaExiste(senhaDeUsuarioVendedor, vendedores)

                if senhaExiste:
                    print('\nESSA SENHA JÁ EXISTE.')
                    continue

                senhaDeUsuarioVendedor = validarDado.validarSenha(senhaDeUsuarioVendedor)

                vendedores[cnpjVendedor] = [nomeDoVendedor, cnpjVendedor, cpfVendedor, telefoneVendedor,
                                            nomeUsuarioVendedor, emailDoVendedor, senhaDeUsuarioVendedor, []]
                produtosNoSistema.append([cpfVendedor])
                print('\nVENDEDOR CADASTRADO COM SUCESSO!')

            elif optionVendedor == '2':
                print('\n|-----ÁREA DE LOGIN-----|\n')
                login = False
                chaveParaLogin = input('DIGITE SEU CNPJ: ').strip()

                cnpjExiste = verificarExistencia.cnpjExiste(chaveParaLogin, vendedores)

                if not cnpjExiste:
                    print('\nESSE CNPJ NÃO EXISTE.')
                    continue

                chaveParaLogin = validarDado.validarCnpj(chaveParaLogin)

                while not login:
                    if len(vendedores) == 0:
                        print('NENHUM USUÁRIO AINDA FOI CADASTRADO!')
                        break

                    if vendedores[chaveParaLogin][1].find(chaveParaLogin) >= 0:
                        senhaDoUsuario = input('SENHA: ').strip()
                        login = optionsLoginVendedor.senhaAreaLoginVendedor(vendedores, senhaDoUsuario, chaveParaLogin)
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
                        print('\nCONTA ENCERRADA.')
                        print('\nRETROCEDENDO PÁGINA...')
                        sleep(2)
                        login = False
                        break

                    elif optionLoginVendedor == '1':
                        optionsLoginVendedor.atualizarSenha(vendedores, chaveParaLogin)

                    elif optionLoginVendedor == '2':
                        optionsLoginVendedor.cadastrarProdutos(vendedores, chaveParaLogin, produtosNoSistema)
                        pergTawan = input('\nDESEJA VER O GRÁFICO DE BARRA? ( Y \ N ) ').upper()

                        if pergTawan == 'Y':
                            produtosParaGrafico = []
                            for produtoParaGrafico in vendedores[chaveParaLogin][7]:
                                produtosParaGrafico.append(produtoParaGrafico[0])
                            quantidadesParaGrafico = []
                            for produtoParaGrafico in vendedores[chaveParaLogin][7]:
                                quantidadesParaGrafico.append(produtoParaGrafico[3])

                            graphic(produtosParaGrafico, quantidadesParaGrafico)
                        else:
                            continue

                        pergTawan2 = input('\nDESEJA VER O RELATÓRIO? ( Y \ N ) ').upper()

                        if pergTawan == 'Y':
                            criarRelatorio(vendedores[chaveParaLogin][7], vendedores, chaveParaLogin)
                        else:
                            continue

                    elif optionLoginVendedor == '3':
                        optionsLoginVendedor.buscarProduto(vendedores, chaveParaLogin)

                    elif optionLoginVendedor == '4':
                        atualizar = False
                        while not atualizar:
                            atualizar = optionsLoginVendedor.atualizarProduto(vendedores, chaveParaLogin,
                                                                              menuVendedor.menuAtualizarProduto(),
                                                                              produtosNoSistema)

                    elif optionLoginVendedor == '5':
                        optionsLoginVendedor.removerProduto(vendedores, chaveParaLogin, produtosNoSistema)

                    elif optionLoginVendedor == '6':
                        login = optionsLoginVendedor.removerConta(vendedores, chaveParaLogin)

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

                cpfCliente = input('\nINFORME SEU CPF: ').strip()

                cpfExiste = verificarExistencia.cpfExisteCliente(cpfCliente, clientes)

                if cpfExiste:
                    print('\nESSE CPF JÁ FOI USADO ANTERIORMENTE.')
                    continue

                cpfCliente = validarDado.validarCpf(cpfCliente)

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

                emailExiste = verificarExistencia.emailExiste(emailDoCliente, clientes)

                if emailExiste:
                    print('ESSE EMAIL JÁ ESTÁ SENDO USADO.')
                    continue

                emailDoCliente = validarDado.validarEmail(emailDoCliente)

                senhaDeUsuarioCliente = input('\nCADASTRE SUA SENHA: ').strip()

                senhaExiste = verificarExistencia.senhaExiste(senhaDeUsuarioCliente, clientes)

                if senhaExiste:
                    print('\nESSA SENHA JÁ EXISTE.')
                    continue

                senhaDeUsuarioCliente = validarDado.validarSenha(senhaDeUsuarioCliente)

                clientes[cpfCliente] = [nomeDoCliente, cpfCliente, telefoneCliente, nomeUsuarioCliente, emailDoCliente,
                                        senhaDeUsuarioCliente, []]
                print('\nVENDEDOR CADASTRADO COM SUCESSO!')

            if optionCliente == '2':
                print('\n|-----ÁREA DE LOGIN-----|\n')
                login = False
                chaveParaLogin = input('DIGITE SEU CPF: ').strip()

                chaveParaLogin = validarDado.validarCpf(chaveParaLogin)

                cpfExiste = verificarExistencia.cpfExisteCliente(chaveParaLogin, clientes)

                if not cpfExiste:
                    print('\nESSE CPF NÃO EXISTE.')
                    continue

                while not login:
                    if len(clientes) == 0:
                        print('NENHUM CLIENTE AINDA FOI CADASTRADO!')
                        break

                    if clientes[chaveParaLogin][1].find(chaveParaLogin) >= 0:
                        senhaDoUsuario = input('SENHA: ').strip()
                        login = optionsLoginCliente.senhaAreaLoginCliente(clientes, senhaDoUsuario, chaveParaLogin)
                else:
                    print('LOGIN EFETUADO.\n')

                if len(clientes) != 0:
                    print(f'OLÁ CLIENTE {clientes[chaveParaLogin][0]}, BEM-VINDO AO SERTÃO LIVRE')

                while login:
                    optionLoginCliente = menuCliente.menuLoginCliente()

                    if not optionLoginCliente.isdigit():
                        print('DIGITE APENAS NÚMEROS.')
                        continue

                    if optionLoginCliente == '0':
                        print('CONTA ENCERRADA.')
                        print('\nRETROCEDENDO PÁGINA...')
                        sleep(2)
                        login = False
                        break

                    elif optionLoginCliente == '1':
                        optionsLoginCliente.atualizarSenha(clientes, chaveParaLogin)

                    elif optionLoginCliente == '2':
                        buscar = False
                        while not buscar:
                            buscar = optionsLoginCliente.buscarProduto(produtosNoSistema,
                                                                       clientes,
                                                                       menuCliente.menuBuscarProduto(),
                                                                       chaveParaLogin)

                    elif optionLoginCliente == '3':
                        optionsLoginCliente.listaDeCompras(clientes, chaveParaLogin)

                    elif optionLoginCliente == '6':
                        login = optionsLoginCliente.removerConta(clientes, chaveParaLogin)

    elif optionInicial == '0':
        print('\nPROGRAMA ENCERRADO')
        break
