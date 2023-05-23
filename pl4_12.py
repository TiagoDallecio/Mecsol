import matplotlib.pyplot as plt
import math

# Lista para armazenar as coordenadas e os nomes das linhas
linhas_x = []
linhas_y = []
nomes_linhas = []

while True:
    # Solicita as coordenadas e o nome da linha ao usuário
    print("Digite as coordenadas da linha (x1, y1, x2, y2) ou digite 'sair' para sair")
    coordenadas = input("Coordenadas: ")

    # Verifica se o usuário deseja sair do programa
    if coordenadas.lower() == "sair":
        break

    # Separa as coordenadas
    x1, y1, x2, y2 = map(float, coordenadas.split(","))

    # Armazena as coordenadas e o nome da linha nas listas
    linhas_x.append([x1, x2])
    linhas_y.append([y1, y2])
    nomes_linhas.append(input("Nome da linha: "))

# Cria um novo gráfico
plt.figure()

# Plota as linhas no gráfico e adiciona o nome a cada linha
for i in range(len(linhas_x)):
    plt.plot(linhas_x[i], linhas_y[i], label=nomes_linhas[i])

# Calcula e exibe o ângulo entre as linhas que se tocam
for i in range(len(linhas_x) - 1):
    # Obtém as coordenadas das duas linhas adjacentes
    x1, x2 = linhas_x[i], linhas_x[i+1]
    y1, y2 = linhas_y[i], linhas_y[i+1]

    # Calcula o ângulo entre as linhas usando o produto escalar
    angulo_radianos = math.acos(
        ((x1[1]-x1[0])*(x2[1]-x2[0]) + (y1[1]-y1[0])*(y2[1]-y2[0])) /
        (math.hypot(x1[1]-x1[0], y1[1]-y1[0]) * math.hypot(x2[1]-x2[0], y2[1]-y2[0]))
    )

    # Converte o ângulo de radianos para graus
    angulo_graus = math.degrees(angulo_radianos)

    # Exibe o ângulo entre as linhas
    print(f"Ângulo entre a linha {nomes_linhas[i]} e a linha {nomes_linhas[i+1]}: {angulo_graus:.2f} graus")

# Obtém os limites mínimos e máximos dos eixos x e y
xmin = min(min(linhas_x))
xmax = max(max(linhas_x))
ymin = min(min(linhas_y))
ymax = max(max(linhas_y))

# Calcula a margem para os eixos x e y
margin_x = abs(xmax - xmin) * 0.1
margin_y = abs(ymax - ymin) * 0.1

# Define os limites dos eixos x e y com margem de 2 números
plt.xlim(xmin - 2 - margin_x, xmax + 2 + margin_x)
plt.ylim(ymin - 2 - margin_y, ymax + 2 + margin_y)

# Define os rótulos dos eixos x e y
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adiciona uma grade no gráfico
plt.grid(True)

# Exibe a legenda com o nome das linhas
plt.legend()

# Mostra o gráfico
plt.show()
