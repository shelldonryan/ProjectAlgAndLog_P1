import matplotlib.pyplot as plt
# create the dataset

data = {'Mesa': 20, 'cadeira': 15, 'Corda': 30, 'Cortina': 35}
courses = list(data.keys())
values = list(data.values())

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(courses, values, color='marrom', width=0.4)

plt.xlabel("Produtos")
plt.ylabel("Quantidade")
plt.title("Sertão Livre")
plt.show()
