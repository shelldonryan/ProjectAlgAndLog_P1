import re
def validarNome(nome):
    while True:
        listaNomes = nome.split()

        if len(listaNomes) < 2:
            print('\nPRECISAMOS DO SEU NOME COMPLETO.')
            nome = input('DIGITE NOVAMENTE SEU NOME COMPLETO: ').capitalize()
        else:
            break

    return nome

def validarCnpj(cnpj):
    while True:
        if not cnpj.isdigit() or len(cnpj) != 14:
            print('CNPJ INVÁLIDO! DEVE TER 14 CARACTERES.')
            cnpj = input('\nDIGITE NOVAMENTE SEU CNPJ: ')
        else:
            break
    return cnpj

def validarCpf(cpf):
    while True:
        if not cpf.isdigit() or len(cpf) != 11:
            print('CPF INVÁLIDO! DEVE TER 11 CARACTERES.')
            cpf = input('\nDIGITE NOVAMENTE SEU CPF: ')
        else:
            break
    return cpf

def validarTelefone(telefone):
    while True:
        if not telefone.isdigit() or len(telefone) != 11:
            print('FORMATO DE NÚMERO INVÁLIDO!')
            telefone = input('\nDIGITE NOVAMENTE O SEU TELEFONE: ')
        else:
            break
    return telefone

def validarUsuario(usuario):
    while True:
        teste = usuario.split()
        if not usuario.islower() or len(usuario) <= 5:
            print('\nUSE APENAS LETRAS MINÚSCULAS, COM NO MÍNIMO 6 CARACTERES.')
            usuario = input('DIGITE NOVAMENTE SEU NOME DE USUÁRIO: ')

        else:
            break
    return usuario

def validarEmail(email):
    padraoCaracteres = r"[a-z0-9._%+-]{3,}@[a-z0-9.-]+\.[a-z]{2,}$"

    while True:
        if not re.match(padraoCaracteres, email):
            print('\nFORMATO DE EMAIL INVÁLIDO.')
            email = input('CADASTRE O SEU E-MAIL NOVAMENTE: ').strip()
        else:
            break
    return email

def validarSenha(senha):
    while True:
        if len(senha) < 8:
            print('\nA SENHA DEVE CONTER NO MÍNIMO 8 CARACTERES E UM CAARACTERE ESPECIAL ex:@.')
            senha = input('CADASTRE SUA SENHA: ').strip()
        else:
            break

    while True:
        if len(senha) < 8:
            print('\nA SENHA DEVE CONTER NO MÍNIMO 8 CARACTERES E UM CAARACTERE ESPECIAL ex:@.')
            senha = input('CADASTRE SUA SENHA: ').strip()
        else:
            break

    while True:
        if senha.isalnum():
            print('\nDEVE CONTER AO MENOS UM CARACTERE ESPECIAL E 8 DÍGITOS.')
            senha = input('CADASTRE SUA SENHA: ').strip()
        else:
            break

    return senha