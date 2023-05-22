import matplotlib.pyplot as plt

# Dados de exemplo
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Cria um novo gráfico
plt.figure()

# Plota os pontos no gráfico
plt.plot(x, y, 'ro')

# Define os limites dos eixos x e y
plt.xlim(0, 6)
plt.ylim(0, 12)

# Define os rótulos dos eixos x e y
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adiciona uma grade no gráfico
plt.grid(True)

# Mostra o gráfico
plt.show()
