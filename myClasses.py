class Drone:
    def __init__(self, posicao_x=0, posicao_y=0, inclinacao=0,p_mot_EF = 0, p_mot_DF=0, p_mot_ET=0, p_mot_DT=0):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.inclinacao = inclinacao
        self.p_mot_EF = p_mot_EF
        self.p_mot_DF = p_mot_DF
        self.p_mot_ET = p_mot_ET
        self.p_mot_DT = p_mot_DT
    
    def sensor_frontal(self, mapa): #Valores do Lidar frontal
        distancias = []
        pos_x = self.posicao_x
        pos_y = self.posicao_y

        for x, valor in enumerate(mapa[pos_y]):
            if valor == 1:
                distancia = x - pos_x
                if distancia >= 0: #Considera apenas obstáculos na frente do drone
                    distancias.append(distancia)
        
        if (distancias != None):
            return min(distancias)
        else:
            return "Erro no sensor"
    
    def sensor_altura(self, mapa):
        distancias = []

        for y in range(len(mapa)):
            if mapa[y][self.posicao_x] == 1:
                distancia = abs(y - self.posicao_y)
                distancias.append(distancia)
        
        try:
            if (distancias != None):
                return min(distancias)
            else:
                return "Erro no sensor"
        except ValueError:
            return self.posicao_y #Se não houver obstáculos, retorna a altura atual do drone

    def throttle_up(self, mapa):
        self.p_mot_EF = 100
        self.p_mot_DF = 100
        self.p_mot_ET = 100
        self.p_mot_DT = 100
        print(f"Throttle up, Potências dos motores: EF={self.p_mot_EF}%, DF={self.p_mot_DF}%, ET={self.p_mot_ET}%, DT={self.p_mot_DT}%")
        print()

        mapa[self.posicao_y][self.posicao_x] = 0 #Limpa a posição anterior
        self.posicao_y += 1 #Move o drone para cima
        mapa[self.posicao_y][self.posicao_x] = "X" #Marca a nova posição do drone no mapa

        self.p_mot_EF = 50
        self.p_mot_DF = 50
        self.p_mot_ET = 50
        self.p_mot_DT = 50
        print(f"Throttle estabilizado, Potências dos motores: EF={self.p_mot_EF}%, DF={self.p_mot_DF}%, ET={self.p_mot_ET}%, DT={self.p_mot_DT}%")
        print()
    
    def throttle_down(self, mapa):
        self.p_mot_EF = 20
        self.p_mot_DF = 20
        self.p_mot_ET = 20
        self.p_mot_DT = 20
        print(f"Throttle down, Potências dos motores: EF={self.p_mot_EF}%, DF={self.p_mot_DF}%, ET={self.p_mot_ET}%, DT={self.p_mot_DT}%")
        print()

        mapa[self.posicao_y][self.posicao_x] = 0 #Limpa a posição anterior
        self.posicao_y -= 1 #Move o drone para baixo
        mapa[self.posicao_y][self.posicao_x] = "X" #Marca a

        self.p_mot_EF = 50
        self.p_mot_DF = 50
        self.p_mot_ET = 50
        self.p_mot_DT = 50
        print(f"Throttle estabilizado, Potências dos motores: EF={self.p_mot_EF}%, DF={self.p_mot_DF}%, ET={self.p_mot_ET}%, DT={self.p_mot_DT}%")
        print()
    
    def pitch_front(self, mapa):
        self.p_mot_EF = 50
        self.p_mot_DF = 50
        self.p_mot_ET = 80
        self.p_mot_DT = 80
        print(f"Sem obstáculo na frente, se movendo... Pitch-Front, Potência dos motores: EF={self.p_mot_EF}%, DF={self.p_mot_DF}%, ET={self.p_mot_ET}%, DT={self.p_mot_DT}%")
        print()

        mapa[self.posicao_y][self.posicao_x] = 0 #Limpa a posição anterior
        self.posicao_x += 1 #Move o drone para frente
        mapa[self.posicao_y][self.posicao_x] = "X" #Marca a nova posição do drone no mapa

        self.p_mot_EF = 50
        self.p_mot_DF = 50
        self.p_mot_ET = 50
        self.p_mot_DT = 50
        print(f"Pitch estabilizado, Potências dos motores: EF={self.p_mot_EF}%, DF={self.p_mot_DF}%, ET={self.p_mot_ET}%, DT={self.p_mot_DT}%")
        print()

    def print_mapa(self, mapa):
        for linha in reversed(mapa):
            for elemento in linha:
                print(elemento, end= " ")
            print()
        print()

    def initialize(self, mapa, variacao_altura, variacao_sensor_altura):
        self.posicao_x = 0
        self.posicao_y = 0
        mapa[self.posicao_y][self.posicao_x] = "X"

        self.print_mapa(mapa)

        print(f"Potências dos motores: EF={self.p_mot_EF}%, DF={self.p_mot_DF}%, ET={self.p_mot_ET}%, DT={self.p_mot_DT}%")
        variacao_altura.append(self.posicao_y)
        variacao_sensor_altura.append(self.sensor_altura(mapa))
        print(f"Posição inicial: ({self.posicao_x}, {self.posicao_y}), Lidar Frontal: {self.sensor_frontal(mapa)}m, Lidar Altura: {self.sensor_altura(mapa)}m")
        print()
        input("Pressione Enter para iniciar a decolagem...")
        print("----------------------------------")
    
    def takeOff(self, mapa):
        print(f"Decolando...")
        self.throttle_up(mapa)
        self.throttle_up(mapa)
        self.print_mapa(mapa)
        print(f"Posição atual: ({self.posicao_x}, {self.posicao_y}), Lidar Frontal: {self.sensor_frontal(mapa)}m, Lidar Altura: {self.sensor_altura(mapa)}m")
        print()
        input("Pressione Enter para continuar...")
        print("----------------------------------")
    
    def ver_mov_front(self, mapa, variacao_altura, variacao_sensor_altura):
        print(f"LiDAR frontal: {self.sensor_frontal(mapa)}m, verificando movimento frontal...")
        if (self.sensor_frontal(mapa) is not None) and (self.sensor_frontal(mapa) > 1):
            self.pitch_front(mapa)
        elif (self.sensor_frontal(mapa) <= 1):
            print(f"Obstáculo detectado na frente, subindo...")
            self.throttle_up(mapa)
        else:
            print("Erro com o sensor LiDAR, distancia frontal desconhecida.")
        
        if (self.sensor_altura(mapa) < 2): #Manter altura sempre 2m
            print(f"Altura baixa detectada, subindo...")
            self.throttle_up(mapa)
        elif (self.sensor_altura(mapa) > 2) and (self.sensor_frontal(mapa) > 1) and (mapa[self.posicao_y-1][self.posicao_x+1] != 1):
            print(f"Altura alta detectada, descendo...")
            self.throttle_down(mapa)
        else:
            print()
        
        self.print_mapa(mapa)
        variacao_altura.append(self.posicao_y)
        variacao_sensor_altura.append(self.sensor_altura(mapa))
        print(f"Posição atual: ({self.posicao_x}, {self.posicao_y}), Lidar Frontal: {self.sensor_frontal(mapa)}m, Lidar Altura: {self.sensor_altura(mapa)}m")
        print()
        input("Pressione Enter para continuar...")
        print("----------------------------------")
    
    def land(self, mapa, variacao_altura, variacao_sensor_altura):
        print(f"Posição final alcançada, pousando...")
        while self.posicao_y > 0: #Throttle down até y=0
            self.throttle_down(mapa)
        
        self.p_mot_EF = 0
        self.p_mot_DF = 0
        self.p_mot_ET = 0
        self.p_mot_DT = 0

        self.print_mapa(mapa) #Printa o mapa

        variacao_altura.append(self.posicao_y)
        variacao_sensor_altura.append(self.sensor_altura(mapa))
        print(f"Desligando... Potências dos motores: EF={self.p_mot_EF}%, DF={self.p_mot_DF}%, ET={self.p_mot_ET}%, DT={self.p_mot_DT}%")
        print(f"Posição final: ({self.posicao_x}, {self.posicao_y}), Lidar Frontal: {self.sensor_frontal(mapa)}m, Lidar Altura: {self.sensor_altura(mapa)}m")
        print()
        print("Simulação finalizada.")
        input("Pressione Enter para finalizar...")