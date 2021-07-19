# Sistemas Operativos Simulación - 3


### Contexto:


Se está trabajando en una estructura de nube. Se calcula que en promedio los usuarios guardan en Discos Duros un promedio de 7000 Megas.
Por otro lado su servicio necesita saber cuánta memoria física agregar a la infraestructura nueva para que siga creciendo.
Si usted agrega menos de 7000 megas al día, irá mal pues ya va perdiendo para el día siguiente.
Debido a situaciones contractuales y de horas extra, el personal puede agregar hasta un 40% más de memoria al día; PERO si ya la memoria disponible supera los 28000 MEGAS, solo puede agregar un 31%. 


---

#### 1. Modele matemáticamente cuanta es la cantidad de mínima de memoria necesaria para garantizar que cada día tendrá más memoria de la consumida por los usuarios, es decir siempre crecerá. Asuma que los 7000 megas al día de consumo son FIJOS 


1.1 Se demostró por razonamiento lógico que la cantidad mínima necesaria de memoria para garantizar que el espacio disponible SIEMPRE siga creciendo es de 17,501 megas.

1.2 El razonamiento se hizo a base de la siguiente propuesta: se necesita que el valor n multiplicado por el porcentaje de 40% siempre sea mayor a 7,000, ya que un número menor provocaría que el consumo de memoría decrezca a lo largo del tiempo. Con el fin de demostrar la validéz de esta propuesta se realizó lo siguiente:



1.2.1 Se hizo un programa en Python que procesara dichos cálculos y obtenimos que con 1,000 días y con una cantidad de memoría inicial de 17,501, el comportamiento del crecimiento fue:

![Modelo 17501](https://user-images.githubusercontent.com/65442367/126081000-0402ea9f-ceae-464e-8ac2-563db92fd667.png)


1.2.2 Por otro lado, se probó con una memoría incial de 17,500 y con 1,000 días, lo cual dió como resultado una línea estática:



![17500](https://user-images.githubusercontent.com/65442367/126081092-914d6e38-bc72-45d0-a0a8-84b5583cbb0d.png)




1.2.3 Por último, se hizo el mismo escenario de 1,000 días, pero ahora con 17,499 megas de memoría disponible y obtuvimos el siguiente resultado: 


![174999](https://user-images.githubusercontent.com/65442367/126081134-044ee9ec-a851-4426-a7a7-41cee4f6d350.png)

#### Por lo tanto, queda demostrado visualmente que la cantidad mínima necesaría para que el almacenamiento siempre crezca es de 17,501 megas



#### 2. ¿Puede establecer un modelo matemática que determina dicha cantidad en función del consumo diario? (suponiendo que dicho consumo es fijo)

2.1 Con el fin de desarrollar una solución inteligente con reutilización en el futuro, se desarrolló un modelo de Machine Learning (regresión lineal simple) para predecir la variable objetivo (cantidad de memoria mínima para asegurar el crecimeinto constante).

2.2 Entrenamiento del algoritmo:

![test](https://user-images.githubusercontent.com/65442367/126112181-ff4f4f20-4cc9-4f37-8ecd-2855a74a568b.png)


2.3 Prueba del algoritmo:

![train](https://user-images.githubusercontent.com/65442367/126112193-f03c85a9-2c44-4905-b05d-90a0a1a19a74.png)


