def criarRelatorio(produtos, vendedor, chave):
    nome_arquivo = "relatorio.txt"
    titulo = f' RELATÓRIO DE PRODUTOS DO VENDEDOR {[vendedor][chave][0]}'
    try:

        with open(nome_arquivo, "w") as arquivo:
            arquivo.write(f'{titulo}\n\n')

            for produto in produtos:
                linha = f"\nNome: {produto[0]}\nPreço: R${produto[2]}\nQuantidade: {produto[1]}\n\n"
                arquivo.write(linha)

        print(f"O relatório foi criado com sucesso no arquivo '{nome_arquivo}'.")

    except IOError:
        print("Ocorreu um erro ao criar o relatório.")