
#Definir

import csv
import matplotlib.pyplot as plt





def Reader_SimRBS(File):
    """
    Input: "file.phsp" ;
    Output: list of lists w/ k energy and respective count
    """
    with open(File, "r") as file:
        reader = csv.reader(file, delimiter=",", skipinitialspace=True)
        data = list(reader) #transforma cada linha do ficheiro numa lista.

    
    energy= []
    for i in range(2,len(data[7])-1): #i=elementos da linha 6
        if float(data[7][i])!=0:
            energy.append(float(data[7][i])) #lista a
        #x = len(aux[i]) -1 #x= comprimento da linha
    print(len(energy))



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


#Plot_SimRBS("Detector.phsp","Lead")

#Reader_SimRBS("EnergyDepAtPhantom.csv")
Reader_SimRBS("Case1BinnedByIncidentTrackEnergy.csv")







