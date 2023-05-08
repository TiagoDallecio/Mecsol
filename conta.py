import numpy as np

nos=[]
ligas=[]
forcas=[]
apoios=[]
fr=[]
def main(): 
    escolha=menu()
    adiciona(escolha,nos,ligas)



def menu():
    print("Para adicionar nós digite 1","\nPara ligar os nós existentes digite 2","\nPara adicionar forças digite 3",
          "\nPara opções de apoios digite 4","\nPara consultar as forças digite 5","\nPara sair digite 6")
    escolha=input("=> ")
    if escolha=="5":
        print("ola")
        calculo()
    return escolha

def adiciona(escolha,nos,ligas):
    continuar='1'
    if escolha=="1":
        i=0
        while continuar=='1':
            i+=1
            x,y=input(f"Digite as coordenadas do nó {i} => ")
            print('coordenada x:',x)
            print('coordenada y:',y)
            nos.append([x,y])
            
            print(nos)
            for v in enumerate(nos) :
                print(v)
            continuar=input("Para adiconar outro nó digite 1")
        main()
    
    if escolha == "2" and len(nos) > 1:
        n1 = []
        n2 = []
        while continuar == "1":
            print(nos)
            h1, h2 = input("Digite os nós que deseja conectar, na ordem => ")
            h1, h2 = int(h1), int(h2)
            for i, v in enumerate(nos):
                if i == h1 - 1:
                   n1.append(nos[0])
                if i == h2 - 1:
                    n2.append(nos[1])   
            print(n1, n2)
            viga = np.sqrt((float(n2[0][0])-float(n1[0][0]))**2 + (float(n2[0][1])-float(n1[0][1]))**2)
         
            ligas.append([n1, n2])
            print(f'{ligas}')

            print(f"Tamanho da viga gerada: {viga}")
            main()
    elif escolha == "2" and len(nos) < 1:
        print("É preciso ter, no mínimo, 2 nós para usar essa opção")
    if escolha=="3":
        while continuar=="1":
            n,f,theta=input("Escolha o nó em que deseja aplicar a força, módulo da mesma e seu ângulo de inclinação(em graus) com o eixo x: ") #ver com o mauritz
            s,d=input("Qual a direção e o sentido da força? (v,h)(c,b,d,e)")
            theta=60*(np.pi)/180
            if d=="c" and s=="d":
                fx=float(f) *(np.cos(theta))
                fy=float(f) *(np.sin(theta))
            elif d=="c" and s=="e":
                fx=float(f) *(-np.cos(theta))
                fy=float(f)* (np.sin(theta))
            elif d=="b" and s=="d":
                fx=float(f) *(np.cos(theta))
                fy=float(f)* (-np.sin(theta))
            else:
                fx=float(f) *(-np.cos(theta))
                fy=float(f)* (-np.sin(theta))


            forcas.append([n,fx,fy])
            print(forcas)
            print(forcas[0])
            continuar=input("Para adicionar outra força digite 1 ")
        main()

    if escolha=="4":
        while continuar=="1":
            a=input("Esolha o tipo de apoio que deseja adicionar: \nApoio móvel\nApoio fixo\nEngastamento\n")
            apoios.append(a)
            print(apoios)
            main()

    if escolha =="6":
        print("\n\nFeito por Tiago Oliveira Dallecio, Mauricio Lasca Gonçalves e Murilo Alves Croce\nEngenharia De Computação\nPUC-Campinas 2023\n\n")
        return 0
def calculo():
    fx=0
    fy=0
    for i,n in enumerate(nos):    
        for f in forcas:
            if int(f[0])==i+1:
                fx=fx+f[1]
                fy=fy+f[2]
            
        fr.append([i+1,fx,fy])
    print(fr)
    main()
            
      
main()