# Maximiación de beneficios de una empresa de venta online con el Muestreo de Thomson

#Importar las librerías

import numpy as np
import matplotlib.pyplot as plt
import random

#Configuraciónn de los parámetros

#número total de rondas --> número de clientes
N = 10000

#nÃºmero de estrategias
d = 9


#Creación de la simulación, como no estamos en producción voy a simular
#unos ratios de conversión. No tenemos datos de clientes reales. Estos ratios
#de conversión es precisamente lo que tendremos que calcular en producción
#viendo los usuarios que se han convertido con cada estrategia

#conversion_rate = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

conversion_rate = [0.05, 0.13, 0.09, 0.16, 0.11, 0.04, 0.20, 0.08, 0.01]

#Inicializo el array a ceros
X = np.array(np.zeros([N,d]))

#Rellenamos la simulación. Voy a ir generando números aleatorios entre 0 y 1
#y comparando con el ratio de conversión. Si estoy por debajo serí­a un 1 y 
#por encima un 0. Así­ podrí­amos hacer la simulación. A recordar que estos datos
#se tendrí­an que obtener en producción tras analizar las respuestas de los
#usuarios a las estrategias 

for i in range(N):   #recorro las filas
    for j in range (d):   #recorro las columnas por cada fila
        if np.random.rand()<conversion_rate[j]:
            X[i,j]=1
            

#Implementación de la Selección Aleatoria y el Muestreo de Thompson

#estrategia seleccionada de forma aleatoria para cada usuario
strategies_selected_rs =[]
#estrategia seleccionada por el muestreo de Thompson para cada usuario
strategies_selected_ts =[]            

#Recompensas de la selección aleatoria y el muestreo de Thomson
total_reward_rs=0
total_reward_ts=0

#Conteo de recompensas para cada estrategia, empiezan con todo a cero
number_of_rewards_1 = [0]*d   #Lista con d ceros
number_of_rewards_0 = [0]*d


#Para las curvas de arrepentimiento
acumul_rewards_rs=[0]*d
regret_rs=[]

acumul_rewards_ts=[0]*d
regret_ts=[]



#Por cada ronda n
for n in range(0,N):
    
    #Selección aleatoria
    
    #Selección aleatoria de estrategia
    strategy_rs=random.randrange(d)    #Escojo una de las 9
    strategies_selected_rs.append(strategy_rs)   #La añado
    #Recompensa de la selección de estrategia aleatoria
    reward_rs = X[n,strategy_rs]
    #Actualizo el total de recompensa
    total_reward_rs += reward_rs
    
    #Para representar la curva de arrepentimiento
    #diferencia entre la mejor estrategia y el modelo utilizado con 
    #con respecto a las rondas
    
    #Cálculo de la mejor estrategia: el máximo de las recompensas acumuladas
    #en todas las diferentes estrategias.
    
    for i in range(d):
        #Acumulo recompensa por cada estrategia
        acumul_rewards_rs[i] += X[n,i] 
        
    
    #Me quedo con el valor máximo
    max_rewards_rs=max(acumul_rewards_rs)  
    
    #Arrepentimiento
    
    regret_rs.append(max_rewards_rs-total_reward_rs)
    
    
    

    
    
    #Muestreo de Thompson
    #PASO 1: seleccionar para cada iteración el valor aleatorio que deberí­a seguir 
    #la distribución teta (n) para el anuncio i en la ronda n
    #Extración aleatoria de una distribución Beta que tenga como parámetros
    #N1(n)+1 y N0(n)+1
    #Python trae la distribución beta de serie 
    
    #Ir mirando el algoritmo
    max_random = 0
    strategy_ts = 0
    for i in range(0,d):   #recorremos cada estrategia para sacar el valor aleatorio de la distribución Beta
        
        #Extración de valores aleatorios
        random_beta = random.betavariate(number_of_rewards_1[i]+1,number_of_rewards_0[i]+1)
       
        #PASO 2: seleccionamos la estrategia que maximiza el random_beta
        if random_beta>max_random:
            max_random = random_beta
            strategy_ts = i
            
    #PASO 3: Actualizar los contadores de recompensas    

    reward_ts = X[n,strategy_ts]
    if reward_ts==1:
        number_of_rewards_1[strategy_ts]+=1
    else:
        number_of_rewards_0[strategy_ts]+=1
        
    #Actualizo la lista de estrategias seleccionadas    
    strategies_selected_ts.append(strategy_ts)    
    #Actualizo la recompensa
    total_reward_ts += reward_ts    
    
    
    
    #Para representar la curva de arrepentimiento
    #diferencia entre la mejor estrategia y el modelo utilizado con 
    #con respecto a las rondas
    
    #Cálculo de la mejor estrategia: el máximo de las recompensas acumuladas
    #en todas las diferentes estrategias.
    
    for i in range(d):
        #Acumulo recompensa por cada estrategia
        acumul_rewards_ts[i] += X[n,i] 
        
    
    #Me quedo con el valor máximo
    max_rewards_ts=max(acumul_rewards_ts)  
    
    #Arrepentimiento
    
    regret_ts.append(max_rewards_ts-total_reward_ts)
    


#Calcular el retorno relativo y absoluto (comparación de selección aleatorio y muestreo de Thompson)


#Suponomos que el precio de la subsripción son 100 $, esto es lo que ganaría
absolute_return = (total_reward_ts - total_reward_rs)*100

relative_return = (total_reward_ts - total_reward_rs)/total_reward_rs *100 #porcentaje

print ("Rendimiento Absoluto: {:.0f} $".format(absolute_return))
print ("Rendimiento Relativo: {:.0f} %".format(relative_return))


#Representación del histograma de selecciones

plt.hist(strategies_selected_ts)    
plt.title("Histograma de Selecciones")
plt.xlabel("Estrategia")
plt.ylabel("Numero de veces que se ha seleccionado la estrategia")
plt.show()


#Representación de la curva de arrepentimiento de la estrategia aleatoria

plt.plot(regret_rs)   
plt.title("Curva de arrepentimiento estrategia aleatoria")
plt.xlabel("Rondas")
plt.ylabel("Arrepentimiento")
plt.show()

#Representación de la curva de arrepentimiento del muestreo de Thompson

plt.plot(regret_ts)   
plt.title("Curva de arrepentimiento muestreo de Thompson")
plt.xlabel("Rondas")
plt.ylabel("Arrepentimiento")
plt.show()



























        



