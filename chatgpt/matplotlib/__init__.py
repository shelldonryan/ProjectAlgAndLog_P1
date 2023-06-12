import matplotlib.pyplot as plt

#Dados fictícios dos produtos e suas quantidades vendidas
produtos = ['CARRO', 'MOTO', 'BICICLETA', 'CARROÇA']
quantidades = [2, 1, 10, 6]

#Criar o gráfico de barras
plt.bar(produtos, quantidades)

#Configurar os rótulos dos eixos
plt.xlabel('PRODUTOS A VENDA')
plt.ylabel('QUANTIDADE EM ESTOQUE')

#Configurar o título do gráfico
plt.title('PRODUTOS DO VENDEDOR')

#Exibir o gráfico
plt.show()
