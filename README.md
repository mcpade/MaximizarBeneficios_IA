# MaximizarBeneficios_IA

## Caso Práctico: Ejemplo de uso del muestreo de Thompson para maximización de beneficios de un negocio de venta online

### Problema a resolver

Imaginemos un negocio minorista en línea que tiene millones de clientes. Estos clientes son solo personas que compran algunos
productos en el sitio web de vez en cuando y se los entregan en casa (como Amazon). El negocio está funcionando bien, pero
la junta directiva ha decidido tomar algún plan de acción para maximizar aún más los ingresos. Este plan consiste en ofrecer
a los clientes la opción de suscribirse a un plan premium, que les dará algunos beneficios como precios reducidos, ofertas
especiales, etc. Este plan premium se ofrece a un precio anual de 100 dólares y el objetivo de este negocio minorista en línea
es, por supuesto, conseguir que el máximo de clientes se suscriba a este plan premium. Descubrir la mejor estrategia a
implementar hará que el negocio maximice sus ingresos adicionales.

En este caso práctico enfrentaremos 9 estrategias diferentes, y nuestra IA no tendrá idea de cuál es la mejor, y absolutamente
ninguna información previa sobre ninguna de sus tasas de conversión. Estas estrategias fueron elaboradas de forma cuidadosa e
inteligente por el equipo de marketing, y cada una de ellas tiene el mismo objetivo: convertir al mayor número de clientes al
plan premium. Las 9 estrategias son todas diferentes: tienen diferentes formas, diferentes paquetes, diferentes
anuncios y diferentes ofertas especiales para convencer y persuadir a los clientes a suscribirse al plan premium. Por supuesto,
el equipo de marketing no tiene idea de cuál de estas 9 estrategias es la mejor. 

En lugar enviar un correo electrónico a sus 100 millones de clientes que sería costoso y correrían el riesgo de acabar en spam,
se buscará la mejor estrategia a través del aprendizaje en línea.

¿Qué es el aprendizaje en línea? Consistirá en implementar una estrategia cada vez que un cliente navegue por el sitio web
del negocio para pasar el rato o comprar algunos productos. Mientras el cliente navega por el sitio web, de repente recibirá
un anuncio emergente, sugiriéndole que se suscriba al plan premium. Y para cada cliente que navega por el sitio web, solo se
implementará una de las 9 estrategias. Luego, el usuario elegirá, o no, tomar medidas y suscribirse al plan premium. Si el
cliente se suscribe, es un éxito, de lo contrario, es un fracaso. Cuantos más clientes hagan esto, más comentarios recibiremos
y tendremos una mejor idea de cuál es la mejor estrategia. Por supuesto, no lo resolveremos manualmente, 
visualmente o con algunas matemáticas simples. Implementaremos el algoritmo más inteligente que descubra cuál
es la mejor estrategia en el menor tiempo posible. 

#### Simulación

Para simular este Caso Práctico, asumiremos que estas estrategias tienen las siguientes tasas de conversión. En una situación de la vida real no tendríamos idea de cuáles serían estas tasas de conversión. Solo las conocemos aquí para fines de simulación, solo para que podamos verificar al final que nuestra IA logra descubrir la mejor estrategia, que según la tabla siguiente es la estrategia número 7 (la que tiene la tasa de conversión más alta).

  
Strategy | Conversion Rate
---------| ----------------
1        | 0.05
2        | 0.13
3        | 0.09
4        | 0.16
5        | 0.11
6        | 0.04
7        | 0.20
8        | 0.08
9        | 0.01

### Definición del entorno

Tenemos que definir las recompensas para construir nuestra matriz de recompensas, donde cada fila corresponde a un usuario que está implementando una estrategia, y cada columna corresponde a una de las 9 estrategias. Por lo tanto, dado que realmente ejecutaremos este experimento de aprendizaje en línea en 10.000 clientes, esta matriz de recompensas tendrá 10.000 filas y 9 columnas. Luego, cada celda obtendrá un 0 si el cliente no se suscribe al plan premium después de ser abordado por la estrategia seleccionada, y un 1 si el cliente se suscribe después de ser abordado por la estrategia seleccionada. Y los valores en la celda son exactamente, las recompensas.

La matriz de recompensas solo está aquí para la simulación, y en la vida real no tendríamos una matriz de recompensas. Simplemente simularemos 10.000 clientes siendo abordados sucesivamente por una de las 9 estrategias, y gracias a la matriz de recompensas simularemos la decisión del cliente de suscribirse sí o no al plan premium. Si la celda correspondiente a un cliente específico y una estrategia seleccionada específica tiene un 1, eso simulará una conversión por parte del cliente al plan premium, y si la celda tiene un 0, simulará un rechazo. 

El muestreo de Thompson recopilará los comentarios de si cada uno de estos clientes se suscribe al plan premium  y, gracias a su poderoso algoritmo, descubrirá rápidamente la estrategia con la tasa de conversión más alta. Esta será la estrategía que habrá que implementar en los millones de clientes, maximizando así los ingresos de la compañía.

### Solución IA

La solución de IA que determinará la mejor estrategia se llama muestreo de Thompson. Es, con diferencia, el mejor modelo para ese tipo de problemas en esta rama de Aprendizaje en línea de Inteligencia Artificial. En resumen, cada vez que un nuevo cliente se conecta al sitio web, esa es una nueva ronda n y seleccionamos una de nuestras 9 estrategias para intentar una conversión (suscripción al plan premium). El objetivo es seleccionar la mejor estrategia en cada ronda, y entrenar durante muchas rondas. 

### Implementación: "thomson_sampling.py"

Al implementar el muestreo de Thompson, también implementaremos el algoritmo de selección aleatoria, que simplemente seleccionará una estrategia aleatoria en cada ronda. Este será nuestro punto de referencia para evaluar el rendimiento de nuestro modelo de muestreo de Thompson. Por supuesto, el muestreo de Thompson y el algoritmo de selección aleatoria competirán en la misma simulación, es decir, utilizando la misma matriz de recompensas. Y al final, una vez realizada la simulación completa, evaluaremos el rendimiento de Thompson Sampling calculando el rendimiento relativo, definido por la siguiente fórmula:

Rendimiento Rel =  (Recompensa Muestro Thompson) - (Recompensa Selección
Al implementar el muestreo de Thompson, también implementaremos el algoritmo de selección aleatoria, que simplemente seleccionará una estrategia aleatoria en cada ronda. Este será nuestro punto de referencia para evaluar el rendimiento de nuestro modelo de muestreo de Thompson. Por supuesto, el muestreo de Thompson y el algoritmo de selección aleatoria competirán en la misma simulación, es decir, utilizando la misma matriz de recompensas. Y al final, una vez realizada la simulación completa, evaluaremos el rendimiento de Thompson Sampling calculando el rendimiento relativo, definido por la siguiente fórmula:

Rendimiento Relativo = (Recompensa Muestro de Thomson) - (Recompensa Selección Aleatoria) / (Recompensa Selección Aleatoria * 100

