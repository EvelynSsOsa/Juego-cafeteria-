import pygame ## esta libreria es la que nos ayuda a poder cargar elementos a nuestro juego, así como imagene, darke un tamaño a la pantalla
import random ## esta libreria nos sirve para poder selecionar clientes al azar ademas de que su orden tambien sea al azar
from pygame import mixer ## esta nos sirve para poder cardarle la musiquita al juego
pygame.init() ## inicializando el juego

######################################
pantalla = pygame.display.set_mode((1200, 700))## estableciendo el tamaño de la pnatalla
fondo = pygame.image.load("conmenu.png") ## cargando la imagen que queremos de fondo para nuestra cafeteria
fondo = pygame.transform.scale(fondo,(1200,700)) ## estableciendo la imagen que cargamos antes como fondo
######################################
mixer.music.load('cafeteria.mp3')##Carga el archivo de sonido cafeteria.mp3 en la memoria
mixer.music.set_volume(0.4) ## este es volumen que tendrá la musica, el 0.4 indica que el volumen del juego esta en un 40% del 100%
mixer.music.play(-1) ## se coloca el parametro menos uno, para que la musica se repita
######################################## #####################################  ###############################

pygame.display.set_caption("Cafecito")# nombre/ titulo de la ventana
icono = pygame.image.load("logo_cafe.png") ## cargamos adecuadamente la imagen que queremos utilizar como icono de la aplicación
pygame.display.set_icon(icono) ## y en esta linea con ayuda de ".set_icon()" pasamos a la varibele "icono" como parametro, para que sea cargada

#################################     #################################     #################################
## y bueno en estas linea estoy cargando las reacciones de los clientes, una monedita para poder ir viendo cuanto dinerito llevamos
## y ademas estoy elegiendo la fuente que vamos a utilizar para poder dar las indicaciones
corazon = pygame.image.load("rico.png")##
corazon = pygame.transform.scale(corazon,(70,70)) ## ajiste de medida

asco = pygame.image.load("wakalaa.png")
asco = pygame.transform.scale(asco,(70,70)) ## ajuste de medida

monedita = pygame.image.load("monedita.png")
monedita = pygame.transform.scale(monedita, (40, 40)) ## aqui estamos ajustando el tamaño de cada uno de estos archivos

fuente = pygame.font.SysFont("Arial", 30)## esta es la linea donde selecionamos la fuente y el tamaño de la letra

#################################     #################################     #################################
## en las siguientes lineas tenemos cargadas los archivos de imagen de los botones y pues tambien podemos darle un tamaño a cada uno
jugar = pygame.image.load("jugar.png")
jugar = pygame.transform.scale(jugar, (90, 60))## en la variable jugar guardamos el archivo de imagen

pausa = pygame.image.load("pausa.png")
pausa = pygame.transform.scale(pausa, (90, 65))## en la variable pause  guardamos el archivo de imagen

score = pygame.image.load("score.png")
score = pygame.transform.scale(score,(90,65))## en la variable score guardamos el archivo de imagen

salir = pygame.image.load("salir.png")
salir = pygame.transform.scale(salir, (90, 60))## en la variable salir guardamos el archivo de imagen

#################################     #################################     #################################

burbuja = pygame.image.load("burbujititaa.png")## aqui estamos cargando la imagen de la burbujita
burbuja = pygame.transform.scale(burbuja,(140,140)) ## aquí le estoy dando un tamaño a la burbujita de texto

###lista de comiditas, aqui solo mandamos a llamar a los archivos de las imagenes que antes, cagar al proyecto
comidas = ['huevo.png', 'pastelito.png', 'paycrema.png', 'paymora.png', 'leche.png', 'panrosita.png',
           'coctel.png', 'pastelchoco.png', 'sopita.png', 'payuva.png', 'pancajeta.png',
           'rolefresa.png', 'panajo.png', 'latee.png', 'refresco.png', 'panque.png', 'pokiiis.png']

lista_comiditas = [] ## luego creamos una lista vacia, que es en donde iremos almacenando las imagenes ya cargadas completamente
## para que poder verlas en la pantalla

## luego con ayuda del ciclo for decimos que por cada comida/elemento que haya en la lista "comidas", podemos ajustar el tamaño de esa imagen
## y agregarla a la lista vacia "lista_comiditas"
for comida in comidas:
    img_comida = pygame.image.load(comida)## tomaremos la imagen actual de la iteración y la vamos a cargar
    img_comida = pygame.transform.scale(img_comida,(60,60)) ## luego vamos a darle un tamaño adecuado a nuestra imagen
    lista_comiditas.append(img_comida) ## y vamos a ir agregandola a lista vacia

orden = random.sample(lista_comiditas,3) ## con ayuda de "random.sample" si le pasamos como parametro "lista_comiditas" y un 3 indicamos que
## queremos que de esa lista "lista_comiditas", nos pase 3 comidas sin repetición, entonces en la variable orden tenemos guardados 3 elementos/ comiditas
cola_orden = list(orden) ## liego metemos a orden en uns lista

## esta función nos ayuda a poder sacar uno de los elementos de la lista, saca el 1ero y por eso pasamos siempre el indice 0
def iniciar_orden():
    global cola_orden,orden_actual
    orden_actual = cola_orden.pop(0) ## esta linea nos ayuda a obtener la orden del cliente

#################################     #################################     #################################
## 1ero mande a llamar a todas las imagenes de los monitos a una lista, la lista "clientes"
clientes = ['cliente_1.png','cliente_2.png','cliente_3.png','cliente_4.png','cliente_5.png','cliente_6.png','cliente_7.png','cliente_8.png','cliente_9.png','cliente_10.png',
            'cliente_11.png','cliente_12.png','cliente_13.png','cliente_14.png','cliente_15.png','cliente_16.png','cliente_17.png','cliente_18.png','cliente_19.png','cliente_20.png',
            'cliente_21.png','cliente_22.png','cliente_23.png','cliente_24.png','cliente_25.png']
lista_personita = [] ## luego cree una lista vacia donde voy a ir mentiendo las imagenes ya cargadas de los monitos

## luego creamos este for, que nos va a ayudar a cargar la imagen de los clientes, que sea visualisan
## para ello necesitamos el indice i, que nos va ayudar a ir avanzando en la lista de las iamgenes "clientes"
for i, cliente in enumerate(clientes, start=1): ## ademas necesitamos decir que empezaremos por el cliente 1
    personita = pygame.image.load(f'cliente_{i}.png') ## aqui podemos ir poniedo el indice i para recorrer cada elemento de la lista y cragarlo de forma correcta
    personita = pygame.transform.scale(personita, (100, 150))  # aqui le etsamos dnado el mismo ancho y largo a cada uan de las imagenes
    lista_personita.append(personita) ## luego a cada personita ya cargada, la vamos a agregar a una lista "lista_personita"

## luego para poder obtener a 3 clientes al azar utilice el metodo "sample" de la libreria "random", para que elija 3 al azar sin repetir
grupo_clientes = random.sample(lista_personita,3)

cola_clientes = list(grupo_clientes) ## luego en la variable "cola_clientes" metemos a nuestros 3 clientes selecionados al azar, en una lista

altura_barra = 485 ## calculo que la altura de la barra, comienza en el pixel "485"
largo_barra = 1200 ## como el cliente va a entrar desde el lado derecho de la pantalla, eso comienza en el pizel 1200
velocidad_cliente = 0.6 ## aqui tenemos la velocidad con la que queremos que avence el cliente
#################################     #################################     #################################
altura_burbuja = 350 ## considerando que desde la parte superior de la pantalla empieza con el pixel 0 y mientras mas profundo sea mas aumenta la cantidad de pixeles, tomando en cuenta
##altura de la barra, junto con el torso de los clientes calculo que las burbujas de texto deben de estar a esta altura 350, para que quede justo arriba de su cabeza
largo_burbuja = 1200 ## la burbuja de texto vendra junto con el cliente, entonces en el eje x de la burbujita tambien se  inicializa en 1200
velocidad_burbuja = 0.6 ## aquí tenemos la misma velocidad con la que avanzara el cliente, para la nubecita

## luego tenemos esta función que nos ayuda a dibujar bien la posisción de la burbuja en la pantalla
def iniciar_burbuja():## para ello usamos como global las variables que ya tienen un valor fijo y que no ira cambiando conforme se ejecute el juego
    global altura_burbuja, largo_burbuja, x_burbuja, y_burbuja,mostrar_burbuja
    x_burbuja = largo_burbuja + burbuja.get_width() ## entonces decimos que la posición  de la burbuja en x, es igual a la burbuja en el pixel 1200 + el ancho en pixeles de la burbuja
    ## lo que nos terminado dando como resultado, la poscición exacata en el eje x de la burbuja
    ## si decimos que la pantalla mide 1200 pixeles ya aprte le sumas el ancho de la burbuja, quiere decir que desde que el cliente aparece del lado derecho, ya traeria la burbuja con sigo,
    ## por eso aquí se suma el ancho de la burbuja, y no se resta, para que la burbuja vaya a la para del cliente
    y_burbuja = altura_burbuja - burbuja.get_height() ## entonces decimos que la posición  de la burbuja en y, es igual a la bubruja en el pixel 350 - el largo en pixeles de la burbuja
    ## lo que nos terminado dando como resultado, la poscición exacata en el eje y de la burbuja
    ## aquí se resta la altura de la burbuja, por que tomando en cuenta que si se genera a partir del pixel 350, si es más larga se disminuye el numero de pixeles, ya que la imagen
    # esta más cerca del borde superior de la pantalla
    mostrar_burbuja = True ## este es un parametro que cambiara, a False cuando el cliente haya recibido su pedido

#######tenemos una función pra inicializar a las personitas/ clientes:
## para ello pasamos parametros globales, que nos ayudaran a ir tomando los valores de afuera,

def iniciar_cliente():
    global cliente_actual, cola_clientes, x_cliente, y_cliente, largo_barra, altura_barra, reaccion## tenemos a "cola_clientes" como variable global, la utilizaremos en la siguiente linea
    cliente_actual = cola_clientes.pop(0) ## decimos que el cliente actual, lo obtendremos sacando al inidce 0
    x_cliente = largo_barra + cliente_actual.get_width() ## decimos que el cliente en x, sera igual al largo_barra más el ancho de pixeles del cliente actual
    ## creando así el efecto de que el cliente va aentrando poco a poco a la cafeteria
    y_cliente = altura_barra -cliente_actual.get_height() ## y buena la posisción del cliente en y, es la altura_barra - la altura de pixeles del cliente_actual, se resta por que los pixeles disminuyen
    reaccion = None ## este es un parametro que luego tomara un valor, cuando ya sea entregada la orden
    apurado = False ## e igual aqui es un paremtro que luego cambiara a True, cuando el cliente ya hay recibido su orden

## el movimiento del cliente incluye muchas varibales, pues el cliente al moverse, trae una nube par su orden, trae su orden, una reacción, a el mismo con sus posisciones y
def movimiento_cliente():
    global cliente_actual, cola_clientes, grupo_clientes, x_cliente, y_cliente, x_burbuja, y_burbuja, x_comi, y_comi,cola_orden, reaccion, apurado
    if apurado:## decimos que si la variable apurado es "True"
        x_cliente -= 1.7 ## vamos a ir restando en el eje x del cliente en -1.7 , así va a dar la ilusión de que avanza mas rapido por que ya recibio su orden
        x_burbuja -= 1.7 ## hacemos el mismo movimiento con la burbuja
    else:## decimo que si apurado es False:
        x_cliente -= velocidad_cliente ## el cliente en el eje x se sguira moviendo a una velocidad normal, pues aun no a recibido su orden
        x_burbuja -= velocidad_burbuja ## y pasa lo mismo con la burbuja

    if x_cliente < 250: ## decimos que si la posicicón del cliente es menor a 250 pixeles
        apurado = False ## apurado estara en estado Flase, lo que queire decir que el cliente aun no recibe su orden
        if cola_clientes:## y que si aun tenemos a personitas, en la cola (es importante recordar que nosotros vamos selecionando de 3 clientes en 3 clientes)
           iniciar_cliente()## continuemos inicializando al siguiente cliente
           iniciar_burbuja() ## asu burbujita
           iniciar_orden()## y su orden de comidita
        else: ## en dado caso de no tener a personitas
            grupo_clientes = random.sample(lista_personita, 3) ## tomamos al azar 3 personitas de la lista "lista_personita=[]"
            cola_clientes = list(grupo_clientes)## creamos a nuestro lista donde metemos a nuestros 3 clientes, eso lo logramos pasando como parametro la variable "grupo_clientes"
            iniciar_cliente() ## e inicializamos al cliente, obetenmos a nuestro cliente
            iniciar_burbuja() ## inicializamos la burbujita
            orden = random.sample(lista_comiditas, 3) ## volvemos a selecionar 3 ordenes al azar
            cola_orden = list(orden) ## pasamos como parametro a orden, para poder obtener la orden por medio del indice que marque la lista
            iniciar_orden() ## y madamos a llamar a la función "iniciar_orden", que nos ayuda a obtener la ordne por indice
    # La comidita se posiciona DENTRO de la burbuja
    x_comi = x_burbuja + (burbuja.get_width() // 4)  # centrada horizontalmente
    y_comi = y_burbuja + (burbuja.get_height() // 4)  # centrada verticalmente

    pantalla.blit(cliente_actual, (int(x_cliente),int(y_cliente))) ## aquí estamos mostradno al cliente actual en pantalla y pasasmos como cordenada las posiciones en x y en y
    ## como las reacciones del cliente al final del dia tiene que ver con el movimiento del cliente, tambien esto viene dentro del movimiento del cliente, y vaya la variable
    ## reacción solo tomara un valor "correcto" o "incorrecto" segun se haya elegido la comidita en el menu
    if reaccion == "correcto":## decimos que si la racción del cliente es igual a correcto
        pantalla.blit(corazon, (int(x_cliente), int(y_cliente) - 50)) ## queremos ver en pantalla la carita de corazones, le restamos -50 pixeles para uqe la carita no quede
        ##encima del cliente
    elif reaccion == "incorrecto": ## y en dado caso de que la reacción sea incorrecta,
        pantalla.blit(asco, (int(x_cliente), int(y_cliente) - 50)) ## queremos mostrar en pantalla la carita de asco,  le restamos -50 pixeles para uqe la carita no quede
        ##encima del cliente
    if mostrar_burbuja: ## si aun no hemos selecionado niguna comidita queremos que se siga mostrando la burbujita con la comidita/ orden
        pantalla.blit(burbuja, (int(x_burbuja), int(y_burbuja))) ## entonces dibujamos en pantalla la burbuja en el eje x y en el eje y
        pantalla.blit(orden_actual,(int(x_comi), int(y_comi))) ## y la orden actual, en la burbujita

iniciar_cliente() ## madamos a llamar al cliente
iniciar_burbuja() ## a la bujita tambien
iniciar_orden() ## tambien se inicializa la orden
### aquí habra algunas variables, que tendran estados establecidos por default, pero van a ir cambiando, segun las acciones del juego
mostrar_burbuja = True ## la burbujita se muestra desde el cimienzo, para poder ver la orden
comida_seleccionada = None ## este nos va a ayudar a resalatar la comidita selecionada del menu, como al comienzo del juego no tenemos selecinado nada, esta en estado "None"
reaccion = None ## como el cliente al comienzo del juego no tendrá ninguna reacción, porque no le hemos entregado su orden, se inicializa en "None"
moneda = 0 ## al principio del juego, como no hemos vendido nada se inicializa a las monedas en 0
apurado = False ## como el cleinte al inicio del juego, no ha recibido su orden, pues no se apura a vazar mas rapido en el eje x, por eso apurado esta en False, cuando esta en "True",ya se mueve rapido
pantalla_congelada = None ## este toma un valor en "None" porque el juego no se a puesto en pausa, pero basicamente si su valor cambia a "True" si se detiene el juego
estado_juego = "jugando" ## esta variable va de la mano con la anterior, pues es un estado del juego, que nos ayuda a regresar a jugar
#### tenemos a "ejecutando" con un valor boooleano, cuando lo cambiemos a False, salimos del juego
## nos ayuda a mentener viva la ventana
ejecutando = True ## y bueno esta basicmnete nos sirve para poder iniciar el juego, decimos que mientras este en "True" el juego se ejecute
while ejecutando: ##pero mientras la varieble "ejecutando" tenga un valor verdadero, vamos a ejecutar las diferentes funciones del juego, mantiene la ventana viva

    pantalla.blit(fondo,(0,0))## aqui estamos pegando la imagen que cargamos para el fondo en la ventana

    if estado_juego == "jugando": ## decimos que si el estado del juego es "jugando"
        movimiento_cliente() ## vamos a llamar a la función de moviemiento de cliente
        ## dibujamos el menú de comiditas abajo
        for i, comida in enumerate(lista_comiditas):
            columna = i % 9  # 9 comidas por columna, cada que llegamos a 9, volvera al indice 0
            fila = i // 9  # entonces se crea una nueva fila

            x_menu = 15 + columna * 80 ## con el 15 me estoy separando 15 pixeles del borde izquierdo de la pantalla, ahi suma la columna, y por cada columna habra 80 pixeles de separación
            y_menu = 555 + fila * 75  #decimos que el menu comenzara en el pixel 555 en el eje y, por cada iteración vamos a ir sumando uno de los cuadritos y de sepraci+on tendra 75 pixeles

            # si es la seleccionada una de las comiditas, el cuadrito se vera  más oscuro
            if i == comida_seleccionada: ## aquí la variable "comida_selecionada" ya tomo un valor, y dependiendo el indice de esa comida
                pygame.draw.rect(pantalla, (50, 25, 10), (x_menu, y_menu, 65, 65))  # ← vamos a hacer mas obscuro el color del cuadrito
                # Color marrón muy oscuro (casi negro) - Cuadrito relleno, los 65 son el tamaño de cada uno de los cuadritos
                pygame.draw.rect(pantalla, (20, 10, 5), (x_menu, y_menu, 65, 65), 3)
                # Color marrón extremadamente oscuro - solo el borde de 3px,      los 65 son el tamaño de cada uno de los cuadritos
            else: ## si esa comidita/cuadrito no esta selecinado entonces los colores seran:
                pygame.draw.rect(pantalla, (101, 67, 33), (x_menu, y_menu, 65, 65))
                # Color marrón café medio - Cuadrito relleno,         los 65 son el tamaño de cada uno de los cuadritos
                pygame.draw.rect(pantalla, (60, 30, 10), (x_menu, y_menu, 65, 65), 3)
                # Color marrón más oscuro - solo el borde

            # dibujamos el menu, con ayuda de las variables que creamos antes de menu_x y menu_y, que nos indican en donde comienza, la fila o columna, junto con la sepración por cuadrito
            pantalla.blit(comida, (x_menu + 2, y_menu + 2)) ## se le suma un "+2" para que las comiditas queden centradas en el cuadrito, tanto vertical como horizontalmente

    elif estado_juego == "pausa": ## decimos que si el estado del juego es pausa
        pantalla.blit(pantalla_congelada, (0, 0))  # vamos a mostrar en pantalla la imagen congelada que tomamos en la linea 274 (ESTA LINEA PUEDE IR VARENADO)
        texto_pausa = fuente.render("PAUSA", True, (255, 255, 255)) ## aqui solo le damos color a las letras
        pantalla.blit(texto_pausa, (550, 300))  ## en medio de todo el juego escribimos "PAUSA"

    elif estado_juego == "score": ## si el estado del juego es score
        pantalla.blit(pantalla_congelada, (0, 0))  # vovemos a cogelar el juego, mostramos la fototio que se toma en la linea 274(ESTA LINEA PUEDE IR VARENADO)

        ## título, creamos las diferentes fuentes que queremos
        fuente_grande = pygame.font.SysFont("Arial", 60, bold=True) ## una letra arial tamaño 60 y en negritas
        fuente_chica = pygame.font.SysFont("Arial", 35) ## y una letra arial tamaño 35
## entonces mandamos a llamar a la fuente c¿que creamos antes y por medio de ".render" escribimos lo que queramos con esta fuete que creamos antes "fuente_grande"
        titulo = fuente_grande.render("¡Fin del turno!", True, (255, 215, 0))## ademas de pasrle un color a las letras
        pantalla.blit(titulo, (400, 150)) ## por me dio de la variable "titulo" que nos guarda el texto que queremos, junto con la fuente y el color lo pasamos como parametro a
        ## pantalla.blit y ya solo le damos la cordenadas en donde queremos que salga ese texto

        ## monedita y puntuación
        ## "monedita" es el archivo de imagen, literalmente el dibujito
        ## "moneda" es el contador
        ## no confundir porque si represnetan cosas diferentes
        pantalla.blit(monedita, (470, 280)) ##presentamos a la monedita en pantalla junto con las cordenadas de en donde queremos que se vea
        ## es importante recordar que la variable moneda es contador, de cuanto dinero llevamos, entonces en la variable "resultado" estamos
        resultado = fuente_grande.render(f"${moneda}", True, (255, 255, 255))## mandando a llamar a la fuente que creamos antes y sacando en pantalla cuantas monedas fueron
        ##en total y el color del texto
        pantalla.blit(resultado, (530, 275))## por ultimo mostramos en pantalla la variable resultado, que contiene cuantas monedas se obtuvo, junto con la fuente de los numeros y el color
        ## ya solo agregamos como parametro las cordenadas de en donde queremos que salgan en pantalla

        ## mensaje según la cantidad de monedas que hagamos
        if moneda >= 50: #decimos que si la cantidad de monedas que reunimos antes de apretar al boton score son más de 50 monedas
            mensaje = fuente_chica.render("¡Excelente trabajo!", True, (100, 255, 100))
            ##mandaremos a llamar a la fuente pequeña para poder escribir en pantalla  ""¡Excelente trabajo!"" y ya  por último pasamos como parametro el color de las letras que queremos
        elif moneda >= 20: ## decimos que si la cantidad de monedas es mayor a 20
            mensaje = fuente_chica.render("¡Buen trabajo!", True, (255, 255, 100)) ## pasa lo mismo que la linea de arriba la 240, solo que esta tendra otro mensajito
        else: ## y si las monedas son menos de 20
            mensaje = fuente_chica.render("¡Puedes mejorar!", True, (255, 100, 100)) ## hacemos lo mismo que en la linea 240 y 243, solo que con otro mensaje
        pantalla.blit(mensaje, (430, 380))## por ultimo pasamos a pantalla el mensaje que corresponda según las minedas que hayamos reunido antes de presionar el boton de score

        ## y bueno tenemos un ultimo letrerito , en donde mandamos a llamar a la duente chica que creamos antes
        cerrar = fuente_chica.render("Presiona play para jugar y off para salir", True, (200, 200, 200))
        ## pasamos como parametro el texto que queremos que colocar, junto con el color de la fuente
        pantalla.blit(cerrar, (400, 500)) ## por ultimo pasamos a la pantalla, el letrerito que creamos antes en la variable "cerra" y damos las cordenadas donde queremos que se muestre el letrerito en pantalla
    elif estado_juego == "salir": ## si el estado del juego es salir
        ejecutando = False #3 la variable "ejecutando" toma el valor de "False"

################################# ##################################### ####################################
        ## buebo ahora vamos a mandar a llamar a los botones que cargamos antes y les vamos a dar diferentes cordenadas en nuestra pantalla
    pantalla.blit(jugar, (800, 555))  # play va a seer uno de nuesro 1eros botnes
    pantalla.blit(pausa, (900, 555))  # pause sera el segundo boton
    pantalla.blit(score, (1000,555)) ## score sera el terecero de nuestro botones
    pantalla.blit(salir, (1100, 555))  # off  sera el último de nuestro botones y el que más acercano esta a la esquina/ birde derecho de nuestra ventana/ pantalla

    ######## cuenta moneditas en tiempo real
    pantalla.blit(monedita, (20, 20)) ## aqui madamos a llamar al archivo de imagen de la moneda, que es monedita y pasamos las cordenadas que queremos para veral en pantalla
    texto_moneda = fuente.render(f"${moneda}", True, (255, 255, 255))## este variable "texto_moneda" nos ayuda a sacaber cuantas llevamos y el color de los nuemros
    pantalla.blit(texto_moneda, (70, 25)) ## decimos que pantalla queremos ver el texto de la moneda

    pygame.display.update() ## esta linea nos ayuda a actualizar lo que vemos en la ventana del juego

## este bucle de aquí nos va ayudar a determinar, por cada evento que hacer o como responder a la solicitud del ususario
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: ## este evento nos indica que si el evento es un quit, es decir que presionamos la tecla "command" y "@" nos saca
            ejecutando = False ## y ahora ejcutando es "Falso" nos saca del bucle "While"
        if evento.type == pygame.MOUSEBUTTONDOWN:## decimos que si el evento fue presionar una tecla del mouse, entonces
            mouse_x, mouse_y = pygame.mouse.get_pos() ## vamos a obetener la posición de donde hicimos click, tanto en el eje x y en el eje de las y
            ## tenemos diferentes condicionales que nos indican que hacer dependiendo de la posición
            # decimos que para el boton de jugar
            ## decimos que si el clcik esta entre un pixel menor a 800 y menor al pixel 1160 en x
            ## y que si el click se encuntra entre el pixel menor a 555 y menor a 615
            if 800 < mouse_x < 1160 and 555 < mouse_y < 615:
                estado_juego = "jugando" ## el estado del juego sera "jugando", podemos ver lo que sucede en la linea 189 a la 213

            # botón pausa, cuando el jugador presiona el boton de pasua, es decir que el click cae entre los siguientes pixeles
            ## en x es un pixel menor entre  900 y 1160
            ## y en y decimos que en un pixel menor entre 555 y 685
            if 900 < mouse_x < 1160 and 555< mouse_y < 685:
                estado_juego = "pausa" ## el estado del juego cambia a pausa
                pantalla_congelada = pantalla.copy() ## y en la variable "pantalla_congelada" tenemos una foto del ultimo movimiento en el juego
                ## en lineas mas arriba vemos como se acciona, para ser especificos en la linea 214 a la 218

                # Boton Score -> Cuando el click cae entre las cordenadas de un pixel menor entre 1000 y 1160 en el eje de las y
                ## y entre las cordenadas de pixel menores a 555 y 755
            if 1000 < mouse_x < 1160 and 555 < mouse_y < 755:
                estado_juego = "score" ## el estado del juego cambia a score y podemos ver que pasa, cuando se presiona este boton en la linea 219 a la 254

                # botón salir -> Cuando el click cae entre las cordenadas de piexel menor a 1100 y 1160 en el eje de las y
                ## entre las cordenadas de pixel menores entre el 555 y 825
            if 1100 < mouse_x < 1160 and 555 < mouse_y < 825:
                estado_juego = "salir" ## el estado del juego es salir, y podemos ver como reacciona este evento en la linea 255 a la 256

            for i, comida in enumerate(lista_comiditas): ## dibujamos el menú de comiditas abajo
                columna = i % 9 # 9 comidas por columna, cada que llegamos a 9, volvera al indice 0
                fila = i // 9 # entonces se crea una nueva fila
                x_menu = 15 + columna * 80  ## con el 15 me estoy separando 15 pixeles del borde izquierdo de la pantalla, ahi suma la columna, y por cada columna habra 80 pixeles de separación
                y_menu = 555 + fila * 75 #decimos que el menu comenzara en el pixel 555 en el eje y, por cada iteración vamos a ir sumando uno de los cuadritos y de sepraci+on tendra 75 pixeles

                # Si la coordenada X del mouse está ENTRE el borde izquierdo y derecho del cuadrito
                # Y la coordenada Y del mouse está ENTRE el borde superior e inferior del cuadrito
                if x_menu < mouse_x < x_menu + 65 and y_menu < mouse_y < y_menu + 65: ## este solo nos sirve para ver si seleciono uno de los cuadritos, pero aun no verificamos si fue el cuadrito correcto
                    if comida == orden_actual: ## entonces para eso verficamos si comida (vendría represntando el cuadrito selecionado) es igual a la orden actual (en la linea 75 podemos ver como se seleciona una orden actual)
                        print("correcto!") ## se imrime en consola corecto
                        mostrar_burbuja = False ## la variable mostrar burbuja cambia a "False"
                        comida_seleccionada = i ## si comida seleccionada toma el valor de un indice, entonces se va a colorear de otro color ese indice/ cuadrito/ comidita, linea 200
                        reaccion = "correcto" ## en la linea 161, podemos ver que si la reaccion toma un valor "correcto" vamos a traer a la crita con corazones
                        apurado = True ## decimos que si la variable "apurado" cambia de valor a "True", pues ya se entrego la orden, entonces la velocidad con la que avanza el cliente aumenta
                        ## lo podemos ver en la linea 133 a 138
                        moneda += 5 ## desimos que el contador de moneda ira aumentando 5 monedas cada que hagamos una entrega correcta
                        sonido_colision = mixer.Sound('bien.wav') ## mandamos a llamr el sonido, que selecinamos para esta acción
                        sonido_colision.play() ## y luego solo reproducuimos el sonido, por medio del metodod ".play"

                    else: ## si la comidita/ cuadrito/ indice selecionado no es igual a la orden actual... entonces:
                        print("incorrecto!") ## en mi terminal se va a imprimir "incorrecto!"
                        mostrar_burbuja = False ## tambien se deja de mostrar la burbuja
                        comida_seleccionada = i ## se colorea el cuadrito de la comidita
                        reaccion = "incorrecto" ## madamos a llamar a la reacción de la carita verde, esto se ve en la linea 164
                        apurado = True ## decimos que si la variable "apurado" cambia de valor a "True", pues ya se entrego la orden, entonces la velocidad con la que avanza el cliente aumenta
                        ## lo podemos ver en la linea 133 a 138
                        moneda -= 5 ## si la orden actual no corresponde con la comidita selccionada, vamos a restar 5 monedas al contador "monedas"
                        sonido_colision = mixer.Sound('mal.wav') ## mandamos a llamar el sonido selecionado para esta acción
                        sonido_colision.play() ## y lo reproducimos


pygame.quit() ## con esta linea dejamos el juego y se cierra la ventana