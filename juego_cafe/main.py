import pygame
import random
from pygame import mixer
pygame.init() ## inicializando el juego

######################################
pantalla = pygame.display.set_mode((1200, 700))## estableciendo el tamaño de la pnatalla
fondo = pygame.image.load("cafe.png") ## cargando la imagen que queremos de fondo para nuestra cafeteria
fondo = pygame.transform.scale(fondo,(1200,700)) ## estableciendo la imagen que cargamos antes como fondo
######################################

pygame.display.set_caption("Cafecito")
icono = pygame.image.load("logo_cafe.png")
pygame.display.set_icon(icono)

## 1ero mande a llamar a todas las imagenes de los monitos a una lista, la lista "clientes"
clientes = ['cliente_1.png','cliente_2.png','cliente_3.png','cliente_4.png','cliente_5.png','cliente_6.png','cliente_7.png','cliente_8.png','cliente_9.png','cliente_10.png',
            'cliente_11.png','cliente_12.png','cliente_13.png','cliente_14.png','cliente_15.png','cliente_16.png','cliente_17.png','cliente_18.png','cliente_19.png','cliente_20.png',
            'cliente_21.png','cliente_22.png','cliente_23.png','cliente_24.png','cliente_25.png']
lista_personita = [] ## luego cree una lista vacia donde voy a ir mentiendo las imagenes ya cargadas de los monitos

## luego creamos este for, que nos va a ayudar a cargar la imagen de los clientes, que sea visual
## para ello necesitamos el indice i, que nos va ayudar a ir avanzando en la lista de las iamgenes "clientes"
for i, cliente in enumerate(clientes, start=1): ## ademas necesitamos decir que empezaremos por el cliente 1
    personita = pygame.image.load(f'cliente_{i}.png') ## aqui podemos ir poniedo el indice i para recorrer cada elemento de la lista y cragarlo de forma correcta
    lista_personita.append(personita) ## luego a cada personita ya cargada, la vamos a agregar a una lista "lista_personita"

## luego para poder obtener a 3 clientes al azar utilice el metodo "sample" de la libreria "random", para que elija 3 al azar sin repetir
grupo_clientes = random.sample(lista_personita,3)

altura_barra = 470 ## calculo que la altura de la barra, comienza en el pixel "470"
largo_barra = 1200 ## como el cliente va a entrar desde el lado derecho de la pantalla, eso comienza en el pizel 1200
y_cliente = altura_barra - personita.get_height() ## y decimos que la posición en y del cliente va a ser igual a la altura de la barra, menos los pixeles de la imagen de la personita
x_cliente = largo_barra - personita.get_width() ## la posisción del cliente en x, es el largo de la ventana, menos los pixeles que tenga de ancho la imagen del cliente
velocidad_cliente = 3 ## aqui tenemos la velocidad con la que queremos que avence el cliente
x_cliente -= velocidad_cliente ## la posición del cliente se va a ir modificando, cada que le restemos 3 pixeles a los 1200

cola_clientes = list(grupo_clientes) ## aqui estoy metiendo a mi lista de grupoclientes a otra lista
cliente_actual = cola_clientes.pop(0)

if x_cliente < 230:
    if cola_clientes:
        cliente_actual = cola_clientes.pop(0)
        y_cliente = altura_barra - cliente_actual.get_height()
        x_cliente = largo_barra -cliente_actual.get_width()
    else:
        grupo_clientes = random.sample(lista_personita, 3)
        cola_clientes = list(grupo_clientes)
        cliente_actual = cola_clientes.pop(0)
        y_clientes = altura_barra - cliente_actual.get_height()
        x_cliente = largo_barra - cliente_actual.get.width()

#### tenemos a "ejecutando" con un valor boooleano, cuando lo cambiemos a False, salimos del juego
## nos ayuda a mentener viva la ventana
ejecutando = True
while ejecutando: ##pero mientras la varieble "ejecutando" tenga un valor verdadero, vamos a ejecutar las diferentes funciones del juego, mantiene la ventana viva

    pantalla.blit(fondo,(0,0))## aqui estamos pegando la imagen que cargamos para el fondo en la ventana

    pygame.display.update() ## con ayuda del metodo ".update()" vamos a actualizar loq ue podemos ver en nuestra pantalla
###########
    #A continuación tenemos un bucle for que nos ayuda a obtener el evento que el usuario esta ejecutando y al que vamos a corresponder
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False


pygame.quit()