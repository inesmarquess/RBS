
#Definir

import csv
import matplotlib.pyplot as plt





def Reader_SimRBS(File):
    """
    Input: "file.phsp" ;
    Output: list of lists w/ k energy and respective count
    """
    with open(File, "r") as file:
        reader = csv.reader(file, delimiter="\n", skipinitialspace=True)
        data = list(reader) #transforma cada linha do ficheiro numa lista.
    
    aux = []
    kenergy_aux= []
    for i in range(len(data)): #i=linha
        aux.append(data[i][0].split())
        x = len(aux[i]) -1 #x= comprimento da linha
        kenergy_aux.append(float(aux[i][x])) #lista com as energias cineticas de cada linha do ficheiro
    
    kenergy=sorted(kenergy_aux)
    counts_k=[]
    for k in kenergy: #Para cada elemento k procura-se quantas vezes existe em kenergy atraves do i
        counts=0 #numero de vezes em que o for encontra i=k
        for i in kenergy:
            if float(k)==float(i):
                counts=counts+1
        
        if [k, counts] not in counts_k:
            counts_k.append([k, counts]) #lista de listas com as contagens para os respetivos valores de energia
    return counts_k


def Plot_SimRBS(File,Label):
    """
    
    
    """
    coord=Reader_SimRBS(File)
    y=[]
    x=[]
    for i in range(len(coord)): #separa a lista yield_k em coordenadas x e y
        y.append(coord[i][1]) 
        x.append(coord[i][0])

    plt.scatter(x,y)
    plt.title(Label)
    plt.xlabel('Channel')
    plt.ylabel('Counts')
    plt.show()


Plot_SimRBS("Target.phsp","Lead")








