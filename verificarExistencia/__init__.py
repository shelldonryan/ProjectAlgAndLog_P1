def nomeExiste(nome, vendedores: dict):
    nomeExiste = False
    for chaveCnpj in vendedores:
        if nome == vendedores[chaveCnpj][0]:
            nomeExiste = True
        break
    return nomeExiste

def cnpjExiste(cnpj, vendedores: dict):
    cnpjExiste = False
    for chaveCnpj in vendedores:
        if cnpj == vendedores[chaveCnpj][1]:
            cnpjExiste = True
        break
    return cnpjExiste

def cpfExisteVendedor(cpf, vendedores: dict):
    cpfExiste = False
    for chaveCpf in vendedores:
        if cpf == vendedores[chaveCpf][2]:
            cpfExiste = True
        break
    return cpfExiste

def cpfExisteCliente(cpf, vendedores: dict):
    cpfExiste = False
    for chaveCpf in vendedores:
        if cpf == vendedores[chaveCpf][1]:
            cpfExiste = True
        break
    return cpfExiste


def telefoneExiste(numTelefone, vendedores: dict):
    telefoneExiste = False
    for chaveCnpj in vendedores:
        if numTelefone == vendedores[chaveCnpj][3]:
            telefoneExiste = True
        break
    return telefoneExiste

def loginExiste(nomeUsuario, vendedores: dict):
    loginExiste = False
    for chaveCnpj in vendedores:
        if nomeUsuario == vendedores[chaveCnpj][4]:
            loginExiste = True
        break
    return loginExiste

def emailExiste(email, vendedores: dict):
    emailExiste = False
    for chaveCnpj in vendedores:
        if email == vendedores[chaveCnpj][5]:
            emailExiste = True
        break
    return emailExiste

def senhaExiste(senha, vendedores: dict):
    senhaExiste = False
    for chaveCnpj in vendedores:
        if senha == vendedores[chaveCnpj][6]:
            senhaExiste = True
            break
    return senhaExiste
