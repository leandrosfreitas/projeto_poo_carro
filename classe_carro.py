class Carro:
    def __init__(self, modelo, ano, cor, vel_max):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0  # Corrigido para velocidade
        self.vel_max = vel_max
        
    def imprima(self):
        if self.velocidade == 0:
            print("%s %s %d" % (self.modelo, self.cor, self.ano))
        elif self.velocidade < self.vel_max:
            print("%s %s indo a %d km/h" % (self.modelo, self.cor, self.velocidade))
        else:
            print("%s %s indo muito rápido!" % (self.modelo, self.cor))
            
    def acelere(self, velocidade):
        self.velocidade = velocidade  # Corrigido para velocidade
        if self.velocidade > self.vel_max:
            self.velocidade = self.vel_max
        self.imprima()
    
    def pare(self):
        self.velocidade = 0  # Corrigido para velocidade
        self.imprima()

def main():
    carro1 = Carro('March', 2012, 'Prata', 80)
    carro2 = Carro('Logan', 2017, 'Branco', 95)
    
    carro1.acelere(40)
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)
    
main()