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
    print("Para adicionar nós digite 1","\nPara ligar os nós digite 2","\nPara adicionar forças digite 3",
          "\nPara selecionar os apoios digite 4 ","\n Para encontrar as forças digite 5 ")
    escolha=input()
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
            x,y=input(f"Digite as coordenadas do nó {i} ")
            print('coordenada x:',x)
            print('coordenada y:',y)
            nos.append([x,y])
            
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
                    n1.append(nos[0])
                    n1.append(nos[1])
                if i==int(h2)-1:
                    n2.append(nos[0])
                    n2.append(nos[1])
                
            print(n1,n2)
            ligas.append([n1,n2])
            print(ligas)
            main()
    if escolha=="3":
        while continuar=="1":
            n,f,theta=input("Escolha o nó que deseja aplicar a força,seu módulo e seu ângulo de inclinação(em graus) com o eixo x:")
            s,d=input("Qual o sentido da força e direrçao da forca? (c,b)(d,e)")
            theta=60*(np.pi)/180
            if s=="c" and d=="d":
                fx=float(f) *(np.cos(theta))
                fy=float(f) *(np.sin(theta))
            elif s=="c" and d=="e":
                fx=float(f) *(-np.cos(theta))
                fy=float(f)* (np.sin(theta))
            elif s=="b" and d=="d":
                fx=float(f) *(np.cos(theta))
                fy=float(f)* (-np.sin(theta))
            else:
                fx=float(f) *(-np.cos(theta))
                fy=float(f)* (-np.sin(theta))


            forcas.append([n,fx,fy])
            print(forcas)
            print(forcas[0])
            continuar=input("Para adiconar outra força digite 1")
        main()

    if escolha=="4":
        while continuar=="1":
            a=input("Esolha o tipo de apoio que deseja adicionar: \nApoio móvel\nApoio fixo\nSuperapoio\n")
            apoios.append(a)
            print(apoios)
            main()
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