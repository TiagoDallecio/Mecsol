import numpy as np
import sys
import time

nos=[]
ligas=[]
forcas=[]
apoios=[]
fr=[]    
nos_visitados=[]
def main():
    escolha=menu()
    if escolha=="5":
        calculo()
    adiciona(escolha,nos,ligas)


def menu(): # menu de seleção de 'operações'
    print("Para adicionar nós digite 1","\nPara ligar os nós existentes digite 2","\nPara adicionar forças digite 3",
          "\nPara opções de apoios digite 4","\nPara consultar as forças digite 5","\nPara sair digite 6")
    escolha=input("=> ")
    return escolha

def adiciona(escolha,nos,ligas): # função chamada pelo menu que executa a opção selecionada
    continuar='1'
    if escolha=="1": # implementação de nós por meio de um sistema de coordenadas x,y
        i=0
        while continuar=='1':
            i+=1
            print("Para voltar para o menu digite 'sair' \n")
            x=input(f"Digite a coordenadas 'x' do nó {i} => ")
            if x =='sair':
                break
            y=input(f"Digite a coordenadas 'y' do nó {i} => ")
            if y =='sair':
                break
            print('\ncoordenada x:',x)
            print('coordenada y:',y)
            n=[x,y]
            if n in nos:
                print("\nEsse nó ja existe na treliça!!\n")
                i-=1
                time.sleep(2)
                continuar=input("Para adiconar outro nó digite 1 => ")
                
            else:
                nos.append(n)
           
                print(nos)
                for v in enumerate(nos) :
                    print(v)
                continuar=input("Para adicionar outro nó digite 1 => ")
        main()
    
    if escolha == "2" and len(nos) > 1: # validação do número de elementos presentes na lista de nós
        n1 = []
        n2 = []
        barra=[]
        while continuar == "1": # caso passe pela validação, cria um loop para o menu de criação de barras entre os nós
            print(nos)  
            print("\nDigite 'sair' em qualquer um dos campos para voltar ao menu\n")
            print("Digite os nós que deseja conectar, na ordem")

            h1 = input("Nó inicial: ")
            if h1 == 'sair':
                main()
                break

            h2 = input("Nó final: ")
            if h2 == 'sair':
                main()
                break

            h1, h2 = int(h1), int(h2) 
            for i, v in enumerate(nos):
                if i == h1 - 1:
                    n1.append(nos[i])
                if i == h2 - 1:
                    n2.append(nos[i])
                    
            if float(n2[0][0])-float(n1[0][0])!=0:
                tg=(float(n2[0][1])-float(n1[0][1]))/(float(n2[0][0])-float(n1[0][0]))
                ang=np.arctan(tg)
            else:
                ang=np.pi/2
            barra=[h1-1,h2-1,ang]
            print((ang*180)/np.pi)
            print(n1, n2)
            viga = np.sqrt((float(n2[0][0])-float(n1[0][0]))**2 + (float(n2[0][1])-float(n1[0][1]))**2) # conta que cálcula o tamanho da barra gerada ao ligar dois nós 
            ligas.append(barra)     # matriz das barras
            print(ligas)
            print(f"\nUma barra foi gerada entre os nós {h1} e {h2}!")
            print(f"\nTamanho da barra gerada: {viga}\n")
            time.sleep(2)
            continuar = input("Para criar mais uma barra digite 1 => ")
        main()
    elif escolha == "2" and len(nos) < 1: # caso não passe pela validação, retorna um aviso e redireciona para o menu principal
        print("\nÉ preciso ter, no mínimo, 2 nós para usar essa opção\n")
        time.sleep(2)
        main()
    if escolha=="3": # menu de inserção de forças
        while continuar=="1":
            if len(nos) > 0: # validação da quantidade de nós presentes na lista
                print("\nDigite 'sair' para voltar ao menu\n")
                n=input("Escolha o nó em que deseja aplicar a força: ") #ver com o mauritz
                if n == 'sair':
                    break
                f=input("Módulo da força: ")
                theta=input("Ângulo de inclinação(em graus) da força com o eixo x: ")
                s,d=input("Qual a direção e o sentido da força? (d,e)(c,b): ")
                theta=float(theta)*(np.pi)/180 # conversão do angulo (graus para radianos)
                if d=="c" and s=="d": # diferentes validações para determinar o sinal das forças
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


                forcas.append([n,fx,fy]) # adiciona, respectivamente, o módulo, componente em x e em y da força na lista 'forcas'
                print(forcas)
                print(forcas[0])
                continuar=input("Para adicionar outra força digite 1 ")
            else: # caso não passe pela validação, retorna mensagem e redireciona para o menu principal
                print("\nÉ preciso ter pelo menos um nó para declarar uma força.\n")
                time.sleep(2)
                main()
                break
        main()

    if escolha == "4": # menu de inserção de apoios
        while continuar=="1":
            if len(nos) > 0: # validação do número de nós na lista, necessário pelo menos um para a inserção do apoio
                print("\nDigite 'sair' para voltar ao menu\n")
                a=input("Esolha o tipo de apoio que deseja adicionar : \n1-Apoio móvel\n2-Apoio fixo\n3-Engastamento\n ")
                if a == 'sair':
                    main()
                    break
                else:
                    a = int(a) 
                n=input("Em que nó ele se encontra? ")
                erro=0
                num_nos=len(nos)
                if int(n)>num_nos:
                    print("Esse nó não existe!!")
                    continuar=input("Para adicionar outro apoio digite 1 => ")
                else:
                    for i,ap in enumerate(apoios):
                        if ap[0]==n:
                            r=input("Já existe um apoio nesse nó! Deseja sobrescrever?(sim/nao) \n")
                            erro=1
                            if r=='nao':
                                continuar=input("Para adicionar outro apoio digite 1 => ")
                            elif r=='sim':
                                apoios[i]=[n,a] # caso passe pela validação, insere o apoio escolhido e o nó selecionado na lista de apoios 
                                print(apoios)
                                continuar=input("Para adicionar outro apoio digite 1 => ")
                    if erro==0:
                        apoios.append([n,a]) # caso passe pela validação, insere o apoio escolhido e o nó selecionado na lista de apoios
                        print(apoios)
                        continuar=input("Para adicionar outro apoio digite 1 => ")
                
                
            
            else: # caso não passe pela validação, redireciona para o menu principal com uma mensagem
                print("\nÉ preciso ter pelo menos um nó para posicionar um apoio.\n")
                time.sleep(2)
                main()
                break
        main()
    
    if escolha =="6": # créditos
        print("\n\nFeito por Tiago Oliveira Dallecio, Mauricio Lasca Gonçales e Murilo Alves Croce\nEngenharia De Computação\nPUC-Campinas 2023\n\n")
        sys.exit()
def calculo(): # função para o cálculo de forças 
    fx=0
    fy=0
    coord=[]
    dist=[]
    vet=[]
    nó=0
    momento=0
    countx=0
    county=0
    for i,n in enumerate(nos):    
        for f in forcas:
            if int(f[0])==i+1 and isinstance(f[1], float):
                fx=fx+f[1]
                fy=fy+f[2]  #resultante das forças
        
        fr.append([i,fx,fy])
        fx=0
        fy=0
    num_nos=len(nos)
    num_barras=len(ligas)
    matriz_forcas=np.zeros((2*num_nos,2*num_nos))
    vetor_carga_nos=np.zeros(2*num_nos)
    
    for no,modulo in enumerate(nos):
        for f in fr:
            if int(f[0])==no and f[1] is not None :
                vetor_carga_nos[2*no]=f[1]
                matriz_forcas[2*no,2*no]=1

            if int(f[0])==no and f[2] is not None:
                vetor_carga_nos[2*no+1]=f[2]
                matriz_forcas[2*no+1,2*no+1]=1
    
        for i,l in enumerate(ligas):
            no_i=l[0]
            no_f=l[1]
            cos=np.cos(l[2])
            sen=np.sin(l[2])

            #considerando que o eixo x segue a orientação da barra
            #força x
            matriz_forcas[2*no_i, 2*i] = cos
            matriz_forcas[2*no_i, 2*i + 1] = sen
            #força y
            matriz_forcas[2*no_i+1, 2*i] = -sen
            matriz_forcas[2*no_i+1, 2*i + 1] = cos
            #força x nof
            matriz_forcas[2*no_f, 2*i] = -cos
            matriz_forcas[2*no_f, 2*i + 1] = -sen
            #força y
            matriz_forcas[2*no_i+1, 2*i] = sen
            matriz_forcas[2*no_i+1, 2*i + 1] = -cos

            #ainda nao da certo


            solucao=np.linalg.solve(matriz_forcas, vetor_carga_nos)
        
        forcas_barras = solucao[:2*num_nos]
        print(vetor_carga_nos)
        print(matriz_forcas)
        print(solucao)
        print(forcas_barras)

    
    """ 
    for ap in apoios:
        vet.append(ap[1])
    print(fr)
    ap=max(vet, key=int)    #maior numero de variaveis entre os apoios
    for a in apoios:
        if a[1]==ap:                #momento é um produto vetorial
            nó=a[0]
    """
    for i,n in enumerate(nos):
        if i+1==int(nó):             #coloca as coordenadas do nó na variável nó
            coordnó=n 
        
        for f in forcas:
            if int(f[0])==i+1:
                coord.append(n)
               
    print(coord)
    print(coordnó)
    
                        #resolver questão do módulo
      
    for c in coord:         #achando as distâncias das forças com o apoio
        x=int(c[0])-int(coordnó[0])
        y=int(c[1])-int(coordnó[1])
        dist.append([x,y])

    for i,f in enumerate(forcas):   #componente da força no vetor m                           
        m=[]                        #produto vetorial do vetor das forças com o vetor das distâncias
        m.append(f[1])
        m.append(f[2])
        momento=momento+np.cross(m,dist[i])
    
    print(momento)

        
    print(dist)        
    print(fr)
    main()
            
            
main()