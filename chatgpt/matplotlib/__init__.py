import matplotlib.pyplot as plt

def graphic(produtos, quantidades):
    plt.bar(produtos, quantidades)

    plt.xlabel('PRODUTOS A VENDA')
    plt.ylabel('QUANTIDADE EM ESTOQUE')

    plt.title('PRODUTOS DO VENDEDOR')

    plt.show()
