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

def telefoneExiste(numTelefone, vendedores: dict):
    telefoneExiste = False
    for chaveCnpj in vendedores:
        if numTelefone == vendedores[chaveCnpj][2]:
            telefoneExiste = True
        break
    return telefoneExiste

def loginExiste(nomeUsuario, vendedores: dict):
    loginExiste = False
    for chaveCnpj in vendedores:
        if nomeUsuario == vendedores[chaveCnpj][3]:
            loginExiste = True
        break
    return loginExiste

def emailExiste(email, vendedores: dict):
    emailExiste = False
    for chaveCnpj in vendedores:
        if email == vendedores[chaveCnpj][4]:
            emailExiste = True
        break
    return emailExiste

def senhaExiste(senha, vendedores: dict):
    senhaExiste = False
    for chaveCnpj in vendedores:
        if senha == vendedores[chaveCnpj][5]:
            senhaExiste = True
            break
    return senhaExiste
