# Software de cálculo numérico de resistência de aterramento de múltiplas hastes
import numpy as np #biblioteca necessária pra o cálculo

x=4 #Quantidade de hastes na linha
y=2 #Quantidade de hastes na coluna
dx=3.35 #Distância entre cada haste da direção x
dy=3.4 #Distância entre cada haste da direção y
roa=300 #Resistividade
Lh=3 #Altura da haste
Dh=0.75 #Diâmetro da haste

distancias = np.zeros((x,y,x,y)) #matriz de distâncias, cada matriz contém uma matriz em cada elemento contendo as distâncias da haste ao restante das hastes
resistencias = np.zeros((x,y)) #matriz das resistências, concatena o somatório da resistência própria com a mútua
resistencia_final=0 #inicializa a variável da resistência final

for k in range(x):
    for l in range(y): #loop da matriz principal
        for i in range(x): 
            for j in range(y): #loop da matriz secundária
                distancias[k,l,i,j] = np.sqrt((dx*(i-k))**2+(dy*(j-l))**2) #cálculo das distâncias entre as hastes
                
for k in range(x):
    for l in range(y): #loop da matriz principal
        for i in range(x):
            for j in range(y): #loop da matriz secundária
                D=distancias[k,l,i,j] #extração da distância entre as hastes
                if D == 0: #resistência própria
                    resistencias[k,l] += ((roa)/(2*np.pi*Lh))*np.log((400*Lh)/(2.54*Dh)) 
                else: #resistência mútua
                    resistencias[k,l] += ((0.183*roa)/Lh)*np.log10(((np.sqrt(Lh**2+D**2)+Lh)**2-D**2)/(D**2-(np.sqrt(Lh**2+D**2)-Lh)**2))

for k in range(x):
    for l in range(y):
        resistencia_final += 1/resistencias[k,l] #soma o inverso das resistências
resistencia_final = 1 / resistencia_final #inverte para obter a resistência equivalente
print(resistencia_final) #mostra a resistência equivalente