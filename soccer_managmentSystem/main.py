from tabulate import tabulate
import os
os.system('cls') or None

class Time:
    def __init__(self, nome, pg, gm, gs, s, v, ga):
        self.__nome = str(nome)
        self.__pg = int(pg)
        self.__gm = int(gm)
        self.__gs = int(gs)
        self.__s = int(s)
        self.__v = int(v)
        self.__ga = float(ga)
    
    def getnome(self):
        return self.__nome
    def setnome(self, nome):
        self.__nome = nome
        
    def getpg(self):
        return self.__pg
    def setpg(self, pg):
        self.__pg = pg

    def getgm(self):
        return self.__gm
    def setgm(self, gm):
        self.__gm = gm
    
    def getgs(self):
        return self.__gs
    def setgs(self, gs):
        self.__gs = gs
    
    def gets(self):
        return self.__s
    def sets(self, s):
        self.__s = s

    def getv(self):
        return self.__v
    def setv(self, v):
        self.__v = v

    def getga(self):
        return self.__ga
    def setga(self, ga):
        self.__ga = ga

    def cadastrarTime(self):
        arq = open('listaTimes.txt', 'r')
        linhas = arq.readlines()
        arq.close()
        count = len(linhas)
        
        if count >= 6:
            print('\nFoi atingido o número máximo de times inscritos para este campeonato.')
            return
        
        while True:
            self.setnome(input('\nInforme o nome do time que deseja cadastrar no campeonato: ').capitalize())
            arq = open('listaTimes.txt', 'a')
            arq.write(f'{self.getnome()}, {self.getpg()}, {self.getgm()}, {self.getgs()}, {self.gets()}, {self.getv()}, {self.getga()}\n')
            arq.close()
            
            count += 1
            if count < 6:
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

class Campeonato:
    def __init__(self, times):
        self.times = times
        self.partidas = []
    
    def simularPartidas(self):
        for partida in self.partidas:
            time1, time2 = partida
            print(f"Digite o placar da partida entre {time1.getnome()} e {time2.getnome()}:")
            placar1 = int(input(f"{time1.getnome()}: "))
            placar2 = int(input(f"{time2.getnome()}: "))
            time1.setgm(time1.getgm() + placar1)
            time1.setgs(time1.getgs() + placar2)
            time2.setgm(time2.getgm() + placar2)
            time2.setgs(time2.getgs() + placar1)
            if placar1 > placar2:
                time1.setv(time1.getv() + 1)
                time2.sets(time2.gets() + 1)
            elif placar2 > placar1:
                time2.setv(time2.getv() + 1)
                time1.sets(time1.gets() + 1)
            else:
                time1.sets(time1.gets() + 1)
                time2.sets(time2.gets() + 1)

    def mostrarTabela(self):
        tabela = []
        for time in self.times:
            tabela.append([time.getnome(), time.getpg(), time.getgm(), time.getgs(), time.gets(), time.getv(), time.getga()])

            headers = ["Time", "PG", "GM", "GS", "S", "V", "GA"]
            print(tabulate(tabela, headers=headers, tablefmt="grid"))


class Menu:
    def __init__(self):
        self.times = self.carregarTimes()
        self.campeonato = Campeonato(self.times)

        while True:
            print('\nCampeonato dos Pernetas')
            print('Digite o número da opção que deseja acessar!\n')
            print('1 - Cadastrar time.')
            print('2 - Visualizar tabela.')
            print('3 - Simular partidas.')
            print('\n4 - Sair do sistema')

            opcao = int(input('\n'))
            if opcao == 1:
                self.cadastrarTime()
                continue

            elif opcao == 2:
                self.campeonato.mostrarTabela()
                print('\nVoltar para o menu? (S / N)')
                voltar = input().upper()
                if voltar == 'S':
                    continue
                else:
                    break

            elif opcao == 3:
                self.campeonato.simularPartidas()
                continue
            
            elif opcao == 4:
                print('\nCampeonato dos Pernetas agradece sua participação.')
                print('Até breve!')
                break

    def carregarTimes(self):
        arq = open('listaTimes.txt', 'r')
        linhas = arq.readlines()
        arq.close()
        times = []
        for linha in linhas:
            dados = linha.strip().split(', ')
            times.append(Time(*dados))
        return times

    def cadastrarTime(self):
        count = len(self.times)
        if count >= 6:
            print('\nFoi atingido o número máximo de times inscritos para este campeonato.')
            return
        while True:
            nome = input('\nInforme o nome do time que deseja cadastrar no campeonato: ').capitalize()
            arq = open('listaTimes.txt', 'a')
            arq.write(f'{nome}, 0, 0, 0, 0, 0, 0\n')
            arq.close()
            self.times.append(Time(nome, 0, 0, 0, 0, 0, 0))
            count += 1
            if count < 6:
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

    def lerTimes(self):
        for time in self.times:
            print(f"{time.getnome()}, {time.getpg()}, {time.getgm()}, {time.getgs()}, {time.gets()}, {time.getv()}, {time.getga()}")


if __name__ == "__main__":
    menu = Menu()
    
