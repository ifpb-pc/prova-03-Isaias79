def q1(cidades):
    cidade_maior = []

    for i in range(len(cidades.keys())):
        valor_1 = list(cidades.keys())[i]
        if cidades[valor_1] >= 100:
            cidade_maior.append(valor_1) 
        
    return cidade_maior


def q2(lista1, lista2):    
    Soma = 0
    Maior = []
    
    for i in range(len(lista1)):
        if lista1[i] > 0:
            Soma = lista1[i] + Soma
            Maior.append(lista1[i])
        elif lista2[i] > 0:
            Soma = lista2[i] + Soma
            Maior.append(lista2[i])
        sorte = sorted(Maior)  
    
    return Soma, sorte

def q3(valores):
    lista = []
    lista_impar = []
    lista_par = []  

    def ler_valores():    
        while True:
            num = int(input('Digite um número: '))
            if num == 0:
                break
            else:
                lista.append(num)

        processa_lista(lista)

    def processa_lista(valores):
        for i in range(len(lista)):
            if lista[i] % 2 == 0 or lista[i] == 0:
                lista_par.append(lista[i])
            else:
                lista_impar.append(lista[i])
                
    ler_valores()
    print(lista_par, lista_impar)

def q4(valores):

    lista = []
    nova_lista = []
    nova_lista_1 = []

    def organizar_alturas():
        for i in range(len(lista)):
            nova_lista.append('{:.2f}'.format(lista[i]))
        
        sorte = sorted(nova_lista)
        nova_lista_1.append(sorte[1])
        nova_lista_1.append(sorte[2])
        nova_lista_1.append(sorte[0])

        print(nova_lista_1)

    def ler_03_alturas():
        for i in range(3):
            num = int(input('Digite um número: '))
            lista.append(num)
        print(lista)
        organizar_alturas()

    ler_03_alturas()

def main():
    # Teste as questões que você desenvolveu manualmente:
    idades = {
        "João Pessoa": 432,
        "Campina Grande": 325,
        "Santa Rita": 68,
        "Patos": 289,
        "Bayeux": 54,
        "Sousa": 178,
        "Cajazeiras": 201,
        "Cabedelo": 45,
        "Guarabira": 122,
        "Areia": 177,
    }
    resultado = q1(idades)
    print("q1:", resultado)


    lista1 = [3, -5, 12, 0, -8, 7]
    lista2 = [-2, 10, -1, 6, -4, 9]
    resultado = q2(lista1, lista2)
    print("q2:", resultado)



if __name__ == "__main__":
    main()


