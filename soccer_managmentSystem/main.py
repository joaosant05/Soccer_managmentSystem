from tabulate import tabulate
import os
os.system('cls') or None

class Time: #Classe Time
    def __init__(self, nome, pg, gm, gs, s, v, ga):
        self.__nome = str(nome)
        self.__pg = int(pg)
        self.__gm = int(gm)
        self.__gs = int(gs)
        self.__s = int(s)
        self.__v = int(v)
        self.__ga = float(ga)
        
    # get e set para nome do time
    def getnome(self):
        return self.__nome
    def setnome(self, nome):
        self.__nome = nome
    
    # get e set para pontos do time    
    def getpg(self):
        return self.__pg
    def setpg(self, pg):
        self.__pg = pg

    # get e set para gols marcados do time
    def getgm(self):
        return self.__gm
    def setgm(self, gm):
        self.__gm = gm
 
    # get e set para gols sofridos do time
    def getgs(self):
        return self.__gs
    def setgs(self, gs):
        self.__gs = gs
    
    # get e set para saldo de gols do time
    def gets(self):
        return self.__s
    def sets(self, s):
        self.__s = s

    # get e set para número de vitórias do time
    def getv(self):
        return self.__v
    def setv(self, v):
        self.__v = v

    # get e set para gols por partida do time
    def getga(self):
        return self.__ga
    def setga(self, ga):
        self.__ga = ga

class Campeonato: # Classe do campeonato
    def __init__(self, times):
        self.times = times
        self.partidas = []
        self.iniciarPartidas()

    # Cria uma lista de partidas e evita que jogos repetidos aconteçam. EX: A vs B, B vs A
    def iniciarPartidas(self): 
        for i in range(len(self.times)):
            for j in range(i + 1, len(self.times)):
                self.partidas.append((self.times[i], self.times[j]))

    # Solicita o placar para as partidas existentes na lista de partidas criada.
    def simularPartidas(self): 
        for partida in self.partidas:
            time1, time2 = partida
            print(f"\n{time1.getnome()} vs {time2.getnome()}")
            gol_time1 = int(input(f"Gols do {time1.getnome()}: "))
            gol_time2 = int(input(f"Gols do {time2.getnome()}: "))

            # Atualiza os dados dos times
            self.atualizarResultado(time1, gol_time1, gol_time2)
            self.atualizarResultado(time2, gol_time2, gol_time1)

            # Atualiza o arquivo listaTimes.txt
            self.atualizarArquivoTimes()

    # Faz o cálculo de dados para cada partida simulada.
    def atualizarResultado(self, time, gol_marcados, gol_sofridos): 
        time.setpg(time.getpg() + (3 if gol_marcados > gol_sofridos else (1 if gol_marcados == gol_sofridos else 0)))
        time.setgm(time.getgm() + gol_marcados)
        time.setgs(time.getgs() + gol_sofridos)
        time.sets(time.gets() + (gol_marcados - gol_sofridos))
        time.setv(time.getv() + (1 if gol_marcados > gol_sofridos else 0))
        time.setga(time.getgm() / (time.getv() + (1 if time.getv() == 0 else 0)))

    # Atualiza os dados após as partidas no arquivo txt
    def atualizarArquivoTimes(self): 
        arq = open('listaTimes.txt', 'w')
        for time in self.times:
            arq.write(f"{time.getnome()}, {time.getpg()}, {time.getgm()}, {time.getgs()}, {time.gets()}, {time.getv()}, {time.getga()}\n")
        arq.close()
        
    # Mostra tabela do campeonato
    def mostrarTabela(self): 
        tabela = []
        headers = ["Time", "PG", "GM", "GS", "S", "V", "GA"]
        for time in self.times:
            tabela.append([time.getnome(), time.getpg(), time.getgm(), time.getgs(), time.gets(), time.getv(), time.getga()])

        # Ordena a tabela pela quantidade de pontos ganhos e saldo de gols
        tabela_ordenada = sorted(tabela, key=lambda x: (x[1], x[4]), reverse=True)
        
        print(tabulate(tabela_ordenada, headers=headers, tablefmt="grid"))

class Menu: # Classe Menu
    def __init__(self):
        self.times = self.carregarTimes()
        self.campeonato = Campeonato(self.times)
        
        # Roda em looping o sistema
        while True: 
            print('\nCampeonato dos Pernetas')
            print('Digite o número da opção que deseja acessar!\n')
            print('1 - Cadastrar time.')
            print('2 - Visualizar tabela.')
            print('3 - Simular partidas.')
            print('\n4 - Sair do sistema')

            opcao = int(input('\n'))
            
            # Opção de cadastro de time
            if opcao == 1: 
                self.cadastrarTime()
                continue

            # Opção de visualizar tabela
            elif opcao == 2: 
                self.campeonato.mostrarTabela()
                print('\nVoltar para o menu? (S / N)')
                voltar = input().upper()
                if voltar == 'S':
                    continue
                else:
                    print('\nCampeonato dos Pernetas agradece sua participação.')
                    print('Até breve!')
                    break

            # Opção de cadastrar partidas
            elif opcao == 3: 
                self.campeonato.simularPartidas()
            
            # Opção encerrar o sistema
            elif opcao == 4: 
                print('\nCampeonato dos Pernetas agradece sua participação.')
                print('Até breve!')
                break
                
    # Cria array com times existentes na lista de times
    def carregarTimes(self): 
        arq = open('listaTimes.txt', 'r')
        linhas = arq.readlines()
        arq.close()
        times = []
        for linha in linhas:
            dados = linha.strip().split(', ')
            times.append(Time(*dados))
        return times

    # Método para criar um time no arquivo txt
    def cadastrarTime(self): 
        # Verifica número máximo de times no campeonato
        count = len(self.times)
        if count >= 4:
            print('\nFoi atingido o número máximo de times inscritos para este campeonato.')
            return
        
        # Cadastra time zerado na lista para o campeonato
        while True:
            nome = input('\nInforme o nome do time que deseja cadastrar no campeonato: ').capitalize()
            arq = open('listaTimes.txt', 'a')
            arq.write(f'{nome}, 0, 0, 0, 0, 0, 0\n')
            arq.close()
            self.times.append(Time(nome, 0, 0, 0, 0, 0, 0))
            count += 1
            if count < 4:
                print('\nDeseja adicionar mais um time?')
                print('S / N')
                x = input().capitalize()
                if x == 'S':
                    continue
                else:
                    break
            else:
                print('Foi atingido o número máximo de times inscritos para este campeonato.')
                break

if __name__ == "__main__":
    menu = Menu()