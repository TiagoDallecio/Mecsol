import numpy as np

nos=[]
ligas=[]
forcas=[]
apoios=[]
def main(): 
    escolha=menu()
    adiciona(escolha,nos,ligas)
    print(nos)


def menu():
    print("Para adicionar nós digite 1","\nPara ligar os nós digite 2","\nPara adicionar forças digite 3",
          "\nPara selecionar os apoios digite 4 ")
    escolha=input()
    return escolha

def adiciona(escolha,nos,ligas):
    continuar='1'
    if escolha=="1":
        i=0
        while continuar=='1':
            i+=1
            x,y=input(f"Digite as coordenadas do nó {i} ")
            print('coordenada x:',x)
            print('coordenada y:',y)
            nos.append(x)
            nos.append(y)
            print(nos)
            for v in enumerate(nos) :
                print(v)
            continuar=input("Para adiconar outro nó digite 1")
        main()
    
    if escolha=="2":
        n1=[]
        n2=[]
        while continuar=="1":
            print(nos)
            h1,h2=input("Digite os nós que deseja conectar, na ordem")
            for i,v in enumerate(nos):
                if i==int(h1)-1:
                    n1.append(nos[i])
                    n1.append(nos[i+1])
                if i==int(h2)-1:
                    n2.append(nos[i])
                    n2.append(nos[i+1])
                
            print(n1,n2)
            ligas.append([n1,n2])
            print(ligas)
            main()
    if escolha=="3":
        while continuar=="1":
            n,f,theta=input("Escolha o nó que deseja aplicar a força,seu módulo e seu ângulo de inclinação(em graus) com o eixo x:")
            theta=60*(np.pi)/180
            fx=float(f) *(np.cos(theta))
            fy=float(f)* (np.sin(theta))
            forcas.append([n,fx,fy])
            print(forcas)
            print(forcas[0])
            continuar=input("Para adiconar outra força digite 1")

    if escolha=="4":
        while continuar=="1":
            a=input("Esolha o tipo de apoio que deseja adicionar: \nApoio móvel\nApoio fixo\nSuperapoio\n")
            apoios.append(a)
            print(apoios)
            menu()

main()