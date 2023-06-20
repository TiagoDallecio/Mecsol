import numpy as np
import sys
import time
import matplotlib.pyplot as plt

def intersect(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    den = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
    if den == 0:
        return False

    t = ((x1 - x3)*(y3 - y4) - (y1 - y3)*(x3 - x4)) / den
    u = -((x1 - x2)*(y1 - y3) - (y1 - y2)*(x1 - x3)) / den

    if 0 <= t <= 1 and 0 <= u <= 1:
        return True
    else:
        return False

nos=[]
ligas=[]
forcas=[]
apoios=[]
fr=[]    
nos_visitados=[]
def main():
    escolha=menu()
    if escolha=="5":
        calcular_forcas(nos, forcas, ligas)
    adiciona(escolha,nos,ligas)


def menu(): # menu de seleção de 'operações'
    print("\n---Exibição e cálculo de treliças---\n\n")
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
            # Verificação de interseção de barras
            intersection = False

            for i in range(len(ligas)):
                line1 = [(float(nos[ligas[i][0]][0]), float(nos[ligas[i][0]][1])),
                         (float(nos[ligas[i][1]][0]), float(nos[ligas[i][1]][1]))]
                line2 = [(float(n1[0][0]), float(n1[1][0])),
                         (float(n2[0][0]), float(n2[1][0]))]
                
                if (line1[0] == line2[0] or line1[0] == line2[1] or
                    line1[1] == line2[0] or line1[1] == line2[1]):
                    continue
                
                if intersect(line1, line2):
                    intersection = True
                    break

            if intersection:
                print("Verifique o input, intersecção de barras detectada")
                time.sleep(2)
                break
            else:
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
                n=input("Escolha o nó em que deseja aplicar a força: ") 
                if n == 'sair':
                    break
                f=input("Módulo da força: ")
                theta=input("Ângulo de inclinação(em graus) da força com o eixo x: ")
                s,d=input("Qual é o sentido da força? (d,e)(c,b): ")
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


def calcular_forcas(nos, forcas, ligas):
    fx = np.zeros(len(nos))
    fy = np.zeros(len(nos))
    for f in forcas:
        no, x, y = f
        fx[int(no)-1] += float(x)
        fy[int(no)-1] += float(y)

    num_nos = len(nos)
    num_barras = len(ligas)
    matriz_forcas = np.zeros((2 * num_nos, 2 * num_barras))
    vetor_carga_nos = np.zeros(2 * num_nos)

    for i, (no_i, no_f, angulo) in enumerate(ligas):
        no_i -= 1
        no_f -= 1
        cos = np.cos(angulo)
        sen = np.sin(angulo)

        # força x
        matriz_forcas[2 * no_i, 2 * i] = cos
        matriz_forcas[2 * no_i, 2 * i + 1] = sen
        matriz_forcas[2 * no_f, 2 * i] = -cos
        matriz_forcas[2 * no_f, 2 * i + 1] = -sen

        # força y
        matriz_forcas[2 * no_i + 1, 2 * i] = -sen
        matriz_forcas[2 * no_i + 1, 2 * i + 1] = cos
        matriz_forcas[2 * no_f + 1, 2 * i] = sen
        matriz_forcas[2 * no_f + 1, 2 * i + 1] = -cos

    for no, (x, y) in enumerate(zip(fx, fy)):
        vetor_carga_nos[2 * no] = x
        vetor_carga_nos[2 * no + 1] = y

    print(matriz_forcas)
    print(num_nos)
    print(num_barras)
    matriz_forcas = np.where(np.abs(matriz_forcas) < 1e-10, 0, matriz_forcas)
    print(matriz_forcas)

    determinante = np.linalg.det(matriz_forcas)

    if abs(determinante) < 1e-10:
        solucao = np.linalg.lstsq(matriz_forcas, vetor_carga_nos, rcond=None)
        solucao = solucao[0]  # Acesso ao resultado da solução
    else:
        solucao = np.linalg.solve(matriz_forcas, vetor_carga_nos)

    for no in range(num_nos):
        forca_x = solucao[2 * no]  # Acessar o elemento correto da solução
        forca_y = solucao[2 * no + 1]  # Acessar o elemento correto da solução
        print(f"No {no+1}: Força X = {forca_x}N, Força Y = {forca_y}N")

'''


'''

            
main()