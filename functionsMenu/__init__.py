def mensagemInicial():
    print('\n                     |------------ BEM VINDO AO SERTÃO LIVRE ------------|\n')
    print('ESPERO QUE ESTE PROGRAMA ATENDA A TODAS AS SUAS NECESSIDADES E FACILITE A GESTÃO DO SEU NEGÓCIO.'.center(99))
    print('ESTOU À DISPOSIÇÃO PARA ESCLARECER QUAISQUER DÚVIDAS E OUVIR SEUS FEEDBACKS PARA MELHORIAS FUTURAS.\n')

def menuInicial():
    print('\n|------QUAL ÁREA DESEJA ACESSAR------|')
    print('1 - ÁREA DO VENDEDOR')
    print('2 - ÁREA DO CLIENTE')
    print('0 - ENCERRAR PROGRAMA')
    optionInicial = input('\nDIGITE A OPÇÃO DESEJADA: ')
    return optionInicial