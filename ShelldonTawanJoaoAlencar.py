import functionsMenu
from functionsMenu import menuVendedor
from functionsVendedor import optionsLoginVendedor
import verificarExistencia
import validarDado

vendedores = {'12345678901234': ['Shelldon Ryan', '12345678901234', '12332112332', '83981955736', 'shelldon', 'shelldon@gmail.com', 'Ryan2018@', '']}
produtosNoSistema = []
option = -1

functionsMenu.mensagemInicial()
while option != 0:
    option = menuVendedor.menuInicialVendedor()

    if not option.isdigit():
        print('\nSÓ NÚMEROS NAS OPÇÕES')
        continue

    if option == '0':
        print('\nPROGRAMA ENCERRADO.')
        break

    elif option == '1':
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

        vendedores[cnpjVendedor] = [nomeDoVendedor, cnpjVendedor, cpfVendedor, telefoneVendedor, nomeUsuarioVendedor,
                                    emailDoVendedor, senhaDeUsuarioVendedor, '']
        print('\nVENDEDOR CADASTRADO COM SUCESSO!')

    elif option == '2':
        print('\n|-----ÁREA DE LOGIN-----|\n')
        login = False
        chaveParaLogin = input('DIGITE SEU CNPJ: ').strip()

        while not login:
            if len(vendedores) == 0:
                print('NENHUM USUÁRIO AINDA FOI CADASTRADO!')
                break

            if vendedores[chaveParaLogin][1] != chaveParaLogin:
                print('\nLOGIN INVÁLIDO!')
                break

            if vendedores[chaveParaLogin][1].find(chaveParaLogin) >= 0:
                senhaDoUsuario = input('SENHA: ').strip()
                login = optionsLoginVendedor.senhaAreaLoginVendedor(vendedores, senhaDoUsuario, chaveParaLogin)
        else:
            print('LOGIN EFETUADO.\n')

        if len(vendedores) != 0:
            print(f'OLÁ {vendedores[chaveParaLogin][0]}, BEM-VINDO AO SERTÃO LIVRE')

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
                optionsLoginVendedor.cadastrarProdutos(vendedores, chaveParaLogin, produtosNoSistema)

            elif optionLoginVendedor == '3':
                optionsLoginVendedor.buscarProduto(vendedores, chaveParaLogin)

            elif optionLoginVendedor == '4':
                optionsLoginVendedor.atualizarProduto(vendedores, chaveParaLogin, menuVendedor.menuAtualizarProduto())

            elif optionLoginVendedor == '5':
                optionsLoginVendedor.removerProduto(vendedores, chaveParaLogin)

            elif optionLoginVendedor == '6':
                login = optionsLoginVendedor.removerConta(vendedores, chaveParaLogin)

    else:
        print('OPÇÃO INVÁLIDA, DIGITE NOVAMENTE.')
