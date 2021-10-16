# Implementação de algoritmos de Ordenação em python

def burbleSorte(tabela):
    anterior = 0
    proximo = 0
    y = 0   
    
    while(y < len(tabela)):


        for i in range(len(tabela)):

            if i + 1 < len(tabela) and tabela[i] > tabela[i + 1]:
                
                anterior = tabela[i + 1]
                proximo = tabela[i]

                tabela[i + 1] = proximo
                tabela[i] = anterior    
                
            i+= 1             
                     
        y += 1
        i = 0


def SelectionSort(tabela):
    menor = 0
    tabela2 = []
    y = 0
    numero = 0

    while len(tabela) > 0:

        numero = tabela[y]

        for i in range(len(tabela)):
            
            if  numero <= tabela[i]:
                menor+= 1


        if menor == len(tabela):
            tabela2.append(numero)
            tabela.remove(numero)
            menor = 0                
            y += 1
        
        else:
            menor = 0
            y+= 1

        if y >= len(tabela):
            y = 0        

    return tabela2


def quickSort(tabela,inicio = 0,fim = None):

    if fim is None:
        fim = len(tabela) - 1

    if inicio < fim:
        p = partion(tabela,inicio,fim)
        quickSort(tabela,inicio,p - 1)
        quickSort(tabela,p + 1,fim)

    return tabela    

def partion(tabela,inicio,fim):
    pivo = tabela[fim]  
    i = inicio

    for j in range(inicio,fim):
        if tabela[j] <= pivo:
            tabela[j],tabela[i] = tabela[i],tabela[j]
            i+= 1

    tabela[i],tabela[fim]= tabela[fim],tabela[i]
    return i    


tabela = [5,8,7,4,6,9,1,3]


print(quickSort(tabela))
