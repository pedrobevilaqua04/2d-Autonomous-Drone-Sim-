from myClasses import Drone
import plotext as plt # pyright: ignore[reportMissingImports]

# Simulador de Drone para primeira capacitação
# Simulador com  interface 2d, dois sensores Lidar, um sensor de posição e com potencias dos motores
print()
print("Simulador de Drone - Pedro Horta - 2026.01")
print()

drone = Drone(0, 0, 0, 0, 0, 0, 0) # Cria uma instância do drone na posição (10, 21)
mapa = [[0 for _ in range(22)] for _ in range(10)] # Cria um mapa de 10 linhas e 25 colunas
# index de 0 a 9 para as linhas e de 0 a 24 para as colunas
variacao_altura = []
variacao_sensor_altura = []
tempo = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
for i in range(0, 4):
        for j in range(8, 16):
            mapa[i][j] = 1 # Adiciona obstáculos no mapa,da coordenada x = 8 a 15 e da coordenada y = 0 a 3

for i in range(0, 10):
    mapa[i][21] = 1 # Parede final do mapa, coordenada x = 24


# def sensor_frontal(matriz):
#     global posicao_x, posicao_y
#     # Calcula as distâncias horizontais de X até todos os 1 na mesma linha
#     distancias = []

#     for x, valor in enumerate(matriz[posicao_y]):
#         if valor == 1:
#             distancia = x - posicao_x
#             if distancia >= 0: # Considera apenas obstáculos à frente do drone
#                 distancias.append(distancia)

#     if (distancias != None):
#         return min(distancias)
#     else:
#         return "Erro no sensor"

# def sensor_altura(matriz):
#     global posicao_x, posicao_y
#     # Calcula as distâncias verticais de X até todos os 1 na mesma coluna
#     distancias = []

#     for y in range(len(matriz)):
#         if matriz[y][posicao_x] == 1:
#             distancia = abs(y - posicao_y)
#             distancias.append(distancia)

#     try:
#         if (distancias != None):
#             return min(distancias)
#         else:
#             return "Erro no sensor"
#     except ValueError:
#         return posicao_y # Se não houver obstáculos na vertical, retorna a altura atual do drone (distância até o chão)

# def inicializacao():
#     global lidar_frontal, lidar_altura, posicao_x, posicao_y, p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT, coordenadas, mapa
#     mapa[posicao_y][posicao_x] = "X" # Posição inicial do drone

#     for linha in reversed(mapa):
#         for elemento in linha:
#             print(elemento, end=" ") # Printa a matriz do mapa, 0 serão espaços vazios e 1 serão obstáculos
#         print()
#     print()
#     print(f"Potências dos motores: EF={p_mot_EF}%, DF={p_mot_DF}%, ET={p_mot_ET}%, DT={p_mot_DT}%")
#     lidar_frontal = sensor_frontal(mapa)
#     lidar_altura = sensor_altura(mapa) # Sensor com o valor da distância frontal até um obstáculo
#     variacao_altura.append(posicao_y)
#     variacao_sensor_altura.append(lidar_altura)
#     print(f"Posição inicial: ({posicao_x}, {posicao_y}), Lidar Frontal: {lidar_frontal}m, Lidar Altura: {lidar_altura}m")
#     print()
#     input("Pressione Enter para iniciar a decolagem...")
#     print("----------------------------------")

# def takeOff(): # Decolar
#     global lidar_frontal, lidar_altura, posicao_x, posicao_y, p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT, coordenadas, mapa

#     p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT = 100, 100, 100, 100 # Potência máxima para decolagem (Subir)
#     print(f"Decolando... Throttle-Up, Potências dos motores: EF={p_mot_EF}%, DF={p_mot_DF}%, ET={p_mot_ET}%, DT={p_mot_DT}%")
#     print()

#     mapa[posicao_y][posicao_x] = 0 # Limpa a posição atual do drone no mapa
#     posicao_y += 2
#     mapa[posicao_y][posicao_x] = "X" # Atualiza a posição do drone no mapa (Sobe 2)
#     lidar_altura = sensor_altura(mapa) # Sensor com o valor da altura
#     lidar_frontal = sensor_frontal(mapa) # Sensor com o valor da distância frontal até um obstáculo
#     p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT = 50, 50, 50, 50 # Potência de estabilização

#     for linha in reversed(mapa):
#         for elemento in linha:
#             print(elemento, end=" ") # Printa o mapa
#         print()
#     print()

#     variacao_altura.append(posicao_y)
#     variacao_sensor_altura.append(lidar_altura)
#     print(f"Estabilizando... Potências dos motores: EF={p_mot_EF}%, DF={p_mot_DF}%, ET={p_mot_ET}%, DT={p_mot_DT}%")
#     print(f"Posição atual: ({posicao_x}, {posicao_y}), Lidar Frontal: {lidar_frontal}m, Lidar Altura: {lidar_altura}m")
#     print()
#     input("Pressione Enter para continuar...")
#     print("----------------------------------")

# def ver_mov_front(): # Movimentação do drone com base nos sensores
#     global lidar_frontal, lidar_altura, posicao_x, posicao_y, p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT, coordenadas, mapa
    
#     lidar_altura = sensor_altura(mapa) # Atualiza o valor do sensor de altura
#     lidar_frontal = sensor_frontal(mapa) # Atualiza o valor do sensor frontal

#     if (lidar_frontal is not None) and (lidar_frontal > 1):
#         p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT = 50, 50, 80, 80 # Potencia para ir para frente (eixo X)
#         print(f"Sem obstáculo na frente, se movendo... Pitch-Front, Potência dos motores: EF={p_mot_EF}%, DF={p_mot_DF}%, ET={p_mot_ET}%, DT={p_mot_DT}%")
#         print()

#         mapa[posicao_y][posicao_x] = 0 # Limpa a posição atual do drone no mapa
#         posicao_x += 1 # Move 1 no x
#         mapa[posicao_y][posicao_x] = "X" # Atualiza posição do Drone
#         lidar_frontal = sensor_frontal(mapa) # Atualiza o valor do sensor frontal
#         lidar_altura = sensor_altura(mapa) # Atualiza o valor do sensor de altura
        
#         p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT = 50, 50, 50, 50 # Potencia de estabilização
#     elif (lidar_frontal <= 1):
#         p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT = 80, 80, 80, 80 # Potencia para subir suavemente
#         print(f"Obstáculo detectado na frente, subindo... Throttle-Up, Potência dos motores: EF={p_mot_EF}%, DF={p_mot_DF}%, ET={p_mot_ET}%, DT={p_mot_DT}%")
#         print()

#         mapa[posicao_y][posicao_x] = 0 # Limpa a posição atual do Drone
#         posicao_y += 1 # Sobe 1 no y
#         mapa[posicao_y][posicao_x] = "X" # Atualiza posição do Drone
#         lidar_frontal = sensor_frontal(mapa) # Atualiza o valor do sensor frontal
#         lidar_altura = sensor_altura(mapa) # Atualiza o valor do sensor de altura

#         p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT = 50, 50, 50, 50 # Potencia de estabilização
        
#     else:
#         print("Erro com o sensor LiDAR, distância de parede frontal desconhecida.")
    
#     lidar_frontal = sensor_frontal(mapa) # Atualiza o valor do sensor frontal
#     lidar_altura = sensor_altura(mapa) # Atualiza o valor do sensor de altura
    
#     if (lidar_altura < 2): # Manter a altura sempre 2m
#         p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT = 80, 80, 80, 80 # Potencia para subir suavemente
#         print(f"Altura baixa detectada, subindo... Throttle-Up, Potência dos motores: EF={p_mot_EF}%, DF={p_mot_DF}%, ET={p_mot_ET}%, DT={p_mot_DT}%")
#         print()

#         mapa[posicao_y][posicao_x] = 0 # Limpa a posição atual do Drone
#         posicao_y += 1 # Sobe 1 no y
#         mapa[posicao_y][posicao_x] = "X" # Atualiza posição do Drone
#         lidar_frontal = sensor_frontal(mapa) # Atualiza o valor do sensor frontal
#         lidar_altura = sensor_altura(mapa) # Atualiza o valor do sensor de altura

#         p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT = 50, 50, 50, 50 # Potencia de estabilização
#     elif (lidar_altura > 2) and (lidar_frontal >  1) and (mapa[posicao_y-1][posicao_x+1] != 1):
#         p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT = 20, 20, 20, 20 # Potencia para descer suavemente
#         print(f"Altura alta detectada, descendo... Throttle-Down, Potência dos motores: EF={p_mot_EF}%, DF={p_mot_DF}%, ET={p_mot_ET}%, DT={p_mot_DT}%")
#         print()

#         mapa[posicao_y][posicao_x] = 0 # Limpa a posição atual do Drone
#         posicao_y -= lidar_altura - 2 # Desce a diferença entre a altura atual e a altura ideal (2)
#         mapa[posicao_y][posicao_x] = "X" # Atualiza posição do Drone
#         lidar_frontal = sensor_frontal(mapa) # Atualiza o valor do sensor
#         lidar_altura = sensor_altura(mapa) # Atualiza o valor do sensor de altura

#         p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT = 50, 50, 50, 50 # Potencia de estabilização
#     else:
#         print()
    
#     for linha in reversed(mapa):
#         for elemento in linha:
#             print(elemento, end=" ") # Printa o mapa
#         print()
#     print()

#     variacao_altura.append(posicao_y)
#     variacao_sensor_altura.append(lidar_altura)
#     print(f"Estabilizando... Potências dos motores: EF={p_mot_EF}%, DF={p_mot_DF}%, ET={p_mot_ET}%, DT={p_mot_DT}%")
#     print(f"Posição atual: ({posicao_x}, {posicao_y}), Lidar Frontal: {lidar_frontal}m, Lidar Altura: {lidar_altura}m")
#     print()
#     input("Pressione Enter para continuar...")
#     print("----------------------------------")
    
# def land(): # Pousar
#     global lidar_frontal, lidar_altura, posicao_x, posicao_y, p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT, coordenadas, mapa

#     p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT = 20, 20, 20, 20 # Potência para pousar (Descer)
#     print(f"Posição final alcançada, pousando... Throttle-Down, Potências dos motores: EF={p_mot_EF}%, DF={p_mot_DF}%, ET={p_mot_ET}%, DT={p_mot_DT}%")
#     print()

#     lidar_altura = sensor_altura(mapa) # Atualiza o valor do sensor de altura
#     mapa[posicao_y][posicao_x] = 0 # Limpa a posição atual do drone no mapa
#     posicao_y -= lidar_altura # Desce até o chão
#     mapa[posicao_y][posicao_x] = "X" # Atualiza a posição do drone no mapa
#     lidar_frontal = sensor_frontal(mapa) # Atualiza o valor do sensor frontal
#     lidar_altura = sensor_altura(mapa) # Atualiza o valor do sensor de
#     p_mot_EF, p_mot_DF, p_mot_ET, p_mot_DT = 0, 0, 0, 0 # Potência zero para motores desligados

#     for linha in reversed(mapa):
#         for elemento in linha:
#             print(elemento, end=" ") # Printa o mapa
#         print()
#     print()

#     variacao_altura.append(posicao_y)
#     variacao_sensor_altura.append(lidar_altura)
#     print(f"Desligando... Potências dos motores: EF={p_mot_EF}%, DF={p_mot_DF}%, ET={p_mot_ET}%, DT={p_mot_DT}%")
#     print(f"Posição final: ({posicao_x}, {posicao_y}), Lidar Frontal: {lidar_frontal}m, Lidar Altura: {lidar_altura}m")
#     print()
#     print("Simulação finalizada.")
#     input("Pressione Enter para finalizar...")

def graficos():
    global variacao_altura, variacao_sensor_altura, tempo
    plt.plot(tempo, variacao_altura)
    plt.title("Variação de Altura do Drone ao Longo do Tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Altura (m)")
    plt.show()

    plt.plot(tempo, variacao_sensor_altura)
    plt.title("Variação do Sensor de Altura do Drone ao Longo do Tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Altura do Sensor (m)")
    plt.show()

def dar_mortal():

     drone.inclinacao, drone.p_mot_EF, drone.p_mot_DF, drone.p_mot_ET, drone.p_mot_DT = 0, 20, 20, 100, 100 # Potência para dar o mortal (Giro no eixo X)
     print(f"Dando mortal... Pitch-Front bem forte, Potências dos motores: EF={drone.p_mot_EF}%, DF={drone.p_mot_DF}%, ET={drone.p_mot_ET}%, DT={drone.p_mot_DT}%")
     print()
     drone.inclinacao += 180 # Seria o sensor de inclinação do Drone
     print(f"Inclinação atual no meio do mortal: {drone.inclinacao}°")
     print()
     drone.inclinacao += 180
     print(f"Inclinação atual no final do mortal: {drone.inclinacao}°")
     print()
     drone.p_mot_EF, drone.p_mot_DF, drone.p_mot_ET, drone.p_mot_DT = 50, 50, 50, 50 # Potência de estabilização
     print(f"Voltando a estabilizar após o mortal... Potências dos motores: EF={drone.p_mot_EF}%, DF={drone.p_mot_DF}%, ET={drone.p_mot_ET}%, DT={drone.p_mot_DT}%")
     print(f"Inclinação final normalizada: {drone.inclinacao % 360}°")
     print()
     input("Pressione Enter para continuar...")
     print("----------------------------------")

drone.initialize(mapa, variacao_altura, variacao_sensor_altura)
drone.takeOff(mapa)
while drone.posicao_x != 20: #Realizar leitura de sensores e movimentos enquanto o drone não chegar na parede final
    drone.ver_mov_front(mapa, variacao_altura, variacao_sensor_altura)
dar_mortal()
drone.land(mapa, variacao_altura, variacao_sensor_altura)
print("Gerando gráficos de variação de altura...")
graficos()