import getpass
print("Quer jogar?")
cont = input()
if cont == "sim":
    print("-------------------BEM VINDOS AO PEDRA, PAPEL, TESOURA-------------------")
    print("- LEGENDA -")
    print("p - Pedra")
    print("a - Papel")
    print("t - Tesoura")
    pontosplay1 = 0
    pontosplay2 = 0
    while cont == "sim":
        obj1 = getpass.getpass(prompt='Digite seu objeto PLAYER 1: ', stream=None)
        obj2 = getpass.getpass(prompt='Digite seu objeto PLAYER 2: ', stream=None)
        if obj1 == obj2:
            print("empate")
        elif ((obj1 == "p")and(obj2 == "t")) or ((obj1 == "a")and(obj2 == "p")) or ((obj1 == "t")and(obj2 == "a")):
            print("PLAYER 1 WIN")
            pontosplay1 = pontosplay1 + 1 
        elif ((obj2 == "p")and(obj1 == "t")) or ((obj2 == "a")and(obj1 == "p")) or ((obj2 == "t")and(obj1 == "a")):
            print("PLAYER 2 WIN")
            pontosplay2 = pontosplay2 + 1
        print("Quer continuar jogando? ")
        cont = input()
print("Tchau")
print("PLAYER 1 |",pontosplay1, "x", pontosplay2, "| PLAYER 2")
