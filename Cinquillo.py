#!/usr/bin/env python
# -*- coding: utf-8 -*-
# /

# ! CUIDADO
# todo por hacer
# ? aviso
# * explicación

import os
from pprint import pprint
import random
import logging
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import readchar
from itertools import cycle



PALOS = 'bastos',  'copas', 'espadas', 'oros'
jugadores = int()
es_primero = int()
baraja_diccionario = {}
baraja = []
grupo_en_orden = []


# * Configuración de logging
logging.basicConfig(level=logging.WARNING,
                    format='-%(levelname)-8s [Línea: %(lineno)-4s Función: %(funcName)-18s] %(message)s')
# logging.debug('Mensaje de traza')
# logging.info('Mensaje Informativo, algo funciona como se espera') # INFO
# logging.warning('Peligro') # WARNING
# logging.error('Error')


class Jugador:
    """Clase de Jugador

    Returns:
        _type_: _description_
    """
    logging.debug('Se crea Jugador')
    def __init__(self, nombre, mano, numero):
        self.nombre = nombre
        self.mano = mano
        self.numero = numero

    def __str__(self) -> str:
        return f'{self.nombre}'

    def mostrar_mano(self):
        return self.mano

    def es_primero(self) -> bool:
        if baraja_diccionario['oros_5'] in self.mano:
            return True
        return False

    def todos_los_datos(self):
        print()
        print(f'Nombre del jugador: {self.nombre}')
        print('---------------------')
        print(f' -mano: {self.mano}')
        print(f' -{self.numero=}')
        print(f' -{self.es_primero()=}')


class Carta:
    """Clase que crea cada carta

    Returns:
        _type_: _description_
    """
    logging.debug('Se crea una Carta')
    def __init__(self, palo, numero):
        self.numero = numero
        self.palo = palo
        self.visible = False
        self.es_tirada_valida = (numero == 5) or (numero in range(4, 6) and palo == 'oro')
        self.nombre_carta = self.palo + '_' + str(self.numero)
        baraja_diccionario[self.nombre_carta] = self # * aquí lo añadimos al diccionario

    def __str__(self) -> str:
        return f'{self.nombre_carta} || Visible: {self.visible} || es_tirada_valida: {self.es_tirada_valida})'

    def __getitem__(self, item):
        if item == "palo":
            return self.palo
        elif item == "numero":
            return self.numero
        else:
            return None

    def __setitem__(self, key, value):
        if key == "palo":
            self.palo = value
        elif key == "numero":
            self.numero = value

    def palo_numero(self) -> str:
        return f'{self.palo}_{self.numero}'

    def solo_numero(self) -> int:
        numero = int(self.numero)
        return numero


def crear_jugadores(baraja: list) -> list:
    """Función que crea los jugadores y sus manos

    Args:
        baraja (list): entra la lista de las 40 cartas

    Returns:
        list: El grupo que es una lista de 2, 3 o 4 jugadores (cada jugador lleva su nombre, su mano y un número para le orden)
    """
    logging.debug('Entra en crear_jugadores')
    grupo = ()
    menu = True
    while menu is True:
        try:
            jugadores = int(input('¿Cuantos jugadores hay (máximo 4 y 0 para salir)?: '))
        except:
            print('Por favor, introduce un valor numérico')
        else:
            if jugadores > 4:
                    print('Tienen que ser menos de 4 jugadores')
                    menu = True
            if jugadores == 0:
                    print('Salir del juego')
                    exit()
            if jugadores == 1:
                    print('Tu solo no puedes jugar. Un consejo: necesitas amigos 😀')
                    menu = True
            if jugadores >= 2 and jugadores <= 4:
                print(f'Introduce el nombre de los {jugadores} jugadores')
                print(f'Si quieres que algún (o algunos) jugador(es) sea la máquina pon de nombre "0"')
                random.shuffle(baraja)
                match jugadores:
                    case 2:
                        nombre1 = chequear_nombre_jugador('Uno')
                        nombre2 = chequear_nombre_jugador('Dos')
                        mano1 = []
                        mano2 = []
                        mano1 = baraja[0:20]
                        mano2 = baraja[20:40]
                        jugador_uno = Jugador(nombre1, mano1, 1)
                        jugador_dos = Jugador(nombre2, mano2, 2)
                        grupo = jugador_uno, jugador_dos
                        print()
                        print(f'Dos manos creadas de {len(mano1)} y {len(mano2)} cartas para los dos jugadores')
                    case 3:
                        nombre1 = chequear_nombre_jugador('Uno')
                        nombre2 = chequear_nombre_jugador('Dos')
                        nombre3 = chequear_nombre_jugador('Tres')
                        mano1 = []
                        mano2 = []
                        mano3 = []
                        mano1 = baraja[0:14]
                        mano2 = baraja[14:27]
                        mano3 = baraja[27:40]
                        jugador_uno = Jugador(nombre1, mano1, 1)
                        jugador_dos = Jugador(nombre2, mano2, 2)
                        jugador_tres = Jugador(nombre3, mano3, 3)
                        grupo = jugador_uno, jugador_dos, jugador_tres
                        print()
                        print(f'Tres manos creadas de {len(mano1)}, {len(mano2)} y {len(mano3)} cartas para los tres jugadores')
                    case 4:
                        nombre1 = chequear_nombre_jugador('Uno')
                        nombre2 = chequear_nombre_jugador('Dos')
                        nombre3 = chequear_nombre_jugador('Tres')
                        nombre4 = chequear_nombre_jugador('Cuatro')
                        mano1 = []
                        mano2 = []
                        mano3 = []
                        mano4 = []
                        mano1 = baraja[0:10]
                        mano2 = baraja[10:20]
                        mano3 = baraja[20:30]
                        mano4 = baraja[30:40]
                        jugador_uno = Jugador(nombre1, mano1, 1)
                        jugador_dos = Jugador(nombre2, mano2, 2)
                        jugador_tres = Jugador(nombre3, mano3, 3)
                        jugador_cuatro = Jugador(nombre4, mano4, 4)
                        grupo = jugador_uno, jugador_dos, jugador_tres, jugador_cuatro
                        print()
                        print(f'Cuatro manos creadas de {len(mano1)}, {len(mano2)}, {len(mano3)} y {len(mano4)} cartas para los cuatro jugadores')
                menu = False
    return list(grupo)


def chequear_nombre_jugador(numero: str) -> str:
    """Chequeamos que el nombre dle jugados no esta vacio

    Args:
        numero (str): numero en texto del jugador

    Returns:
        str: nombre del jugador por defecto si no ha metido ninguno: Uno, Dos, Tres o Cuatro
    """
    logging.debug('Entra en chequear_nombre_jugador')
    nombre = input('Nombre del jugador '+ numero +': ')
    if not nombre:
        print(f'No puede estar sin nombre, te llamaremos {numero}')
        nombre = numero
    return nombre


def crear_tablero(baraja) -> None:
    """Genera el tablero con las cartas

    Args:
        baraja (list): baraja con las cartar
    """
    logging.debug('Entra en crear_tablero')
    table = Table()
    table.add_column('Número', justify='center', width=7)
    table.add_column('Bastos', width=11)
    table.add_column('Copas',  width=11)
    table.add_column('Espadas', width=11)
    table.add_column('Oros', width=11)
    #? podemos usar panel con esquinas redondeadas pero no se como poner el fondo
    #? Panel.fit(crear_carta('2 Espadas'))
    for numero in range(1,11):
        numero = str(numero)
        # * para la creacion de la tabla todo tiene que ser str
        table.add_row(numero, \
                      crear_carta_tablero('Bastos', numero, baraja),
                      crear_carta_tablero('Copas', numero, baraja),
                      crear_carta_tablero('Espadas', numero, baraja),
                      crear_carta_tablero('Oros', numero, baraja))
    console = Console()
    console.print(table)


def crear_carta_tablero(palo: str, numero: str, baraja: list) -> str:
    """_summary_

    Args:
        palo (str): _description_
        numero (str): _description_
        baraja (list): _description_

    Returns:
        str: _description_
    """
    logging.debug('Entra en crear_carta_tablero')
    paso = False
    carta_retornada = ''
    for carta in baraja:
        if carta.visible == True and carta.palo == palo.lower() and str(carta.numero) == numero:
            numero_longitud = len(str(numero))
            palo_longitud = len(str(palo))
            palo_espacio_delante = int(round((10-palo_longitud)/2))
            numero = str(numero)
            # * Este código se usa para mostar en las cartas el texto de Sota, Caballo o Rey
            # match numero:
            #     case '8':
            #         numero = 'Sota'
            #     case '9':
            #         numero = 'Caballo'
            #     case '10':
            #         numero = 'Rey'
            palo_espacio_detras = 11 - palo_longitud - palo_espacio_delante
            # * creamos cada línea de la carta
            carta_retornada = '[reverse][bold yellow] ' + \
                numero + ' [/]' + ' '*(9-numero_longitud) + '\n'
            carta_retornada = carta_retornada + '[reverse]' + ' '*palo_espacio_delante + palo + ' '*palo_espacio_detras + '\n'
            carta_retornada = carta_retornada + \
                ' ' * (9-(numero_longitud)) + '[reverse][bold yellow] ' + numero + ' [/]' + '\n'
            # esta variable seria (esta a medias) si usamos la opción de panel
            # carta_retornada = f'[bold] ' + numero + '[/bold]' + ' '*(10-numero_longitud) + \
                # '\n' + ' ' + palo + '  ' + '\n' + '[bold]     ' + numero + ' [/bold]'
            paso = True
        if paso == False:
            carta_retornada = '\n\n\n'
    return carta_retornada


def pausa() -> None:
    """Realiza una pausa hasta pulsar una tecla
    """
    logging.debug('Entra en pausa')
    print()
    print('Pulsa cualquier tecla para continuar...')
    pausa = readchar.readkey()
    os.system('clear')


def jugada(baraja: list, jugador_activo_mano: list, jugador_activo_nombre):
    """Analiza la entrada del usuario para tirar una carta

    Returns:
        list: carta_usuario(numero: int, palo: str)
    """
    logging.debug('Entra en jugada')
    paso_jugada = False
    paso_longuitud = False
    paso_contenido = False
    paso_visibilidad = False
    paso_esta_en_mano = False
    paso_tirada_valida = False
    carta_usuario = []
    while paso_jugada is False:
        carta_usuario = input('¿Qué carta quieres poner en el mesa (número y palo)? ')
        if carta_usuario == '':
            errores('vacio')
            paso_longuitud = False
        else:
            carta_usuario = carta_usuario.lower()
            carta_usuario = carta_usuario.split()
            # * Analizamos los criterios físicos
            paso_longuitud = analizar_longitud(carta_usuario)
            paso_contenido, carta_usuario = analizar_contenido(carta_usuario)
            # * Analizamos los criterios lógicos, solo entra si los criterios físicos son True
            if paso_longuitud == True and paso_contenido == True:
                paso_esta_en_mano = analizar_pertenece_mano(
                    carta_usuario, jugador_activo_mano)
                if paso_esta_en_mano == True:
                    paso_tirada_valida, baraja = analizar_tirada_valida(
                        carta_usuario, jugador_activo_mano)
                    if paso_tirada_valida == True:
                        paso_visibilidad = analizar_visibilidad(carta_usuario, baraja)
            # * Repasamos que las 3 condiciones que quedan son True para aceptar la jugada
            if  paso_visibilidad == True and paso_esta_en_mano == True and paso_tirada_valida == True:
                print()
                print(
                    f'{jugador_activo_nombre} la tirada es válida (se muestra en la siguiente pantalla)')
                # * Eliminamos la carta
                jugador_activo_mano = eliminar_carta(carta_usuario, jugador_activo_mano)
                paso_jugada = True
    return baraja, jugador_activo_mano


def analizar_visibilidad(carta_usuario, baraja) -> bool:
    """Analizamos si la carta ya esta en la mesa

    Args:
        carta_usuario (list): _description_
        baraja (list de objetos que son las cartas): _description_

    Returns:
        paso_visibilidad: True/False
    """
    logging.debug('Entra en analizar_visibilidad')
    paso_visibilidad = False
    for carta in baraja:
        if carta.numero == int(carta_usuario[0]) and carta.palo == carta_usuario[1]:
            if carta.visible == True:
                errores('carta_usada')
                paso_visibilidad = False
            else:
                carta.visible = True
                paso_visibilidad = True
    logging.info(f'{paso_visibilidad=}')
    return paso_visibilidad


def analizar_tirada_valida(carta_usuario: list, mano: list):
    """Analizamos si es posible tirar esa carta, o sea, si está por encima o por debajo de las que estan en la mesa.
    También actualizamos el estado del atributo es_tirada_valida a True para la carta anterior y para la posterior
    Args:
        carta_usuario (list): _description_

    Returns:
        paso_tirada_valida: True/False
        baraja: lista de cartas
    """
    logging.debug('Entra en analizar_tirada_valida')
    paso_tirada_valida = False
    for carta in mano:
        #print(f'{carta.numero=} y {carta.palo=}, el tipo de carta.numero es {type(carta.numero)=}')
        if carta.numero == carta_usuario[0] and carta.palo == carta_usuario[1]: # o sea cuando encontramos la carta en la mano
            if carta.es_tirada_valida == True:
                paso_tirada_valida = True
                # * Actualizamos en estado de las carta anterior y posterior
                # creamos los nombres a buscar
                if carta_usuario[0] == 10:
                    por_encima = carta_usuario[1] + '_' + str(carta_usuario[0])
                else:
                    por_encima = carta_usuario[1] + '_' + str(carta_usuario[0]+1)
                if carta_usuario[0] == 1:
                    por_debajo = carta_usuario[1] + '_' + str(carta_usuario[0])
                else:
                    por_debajo = carta_usuario[1] + '_' + str(carta_usuario[0]-1)
                # recorremos el diccionario buscando las dos cartas a modificar
                for carta in baraja:
                    if carta.nombre_carta == por_encima or carta.nombre_carta == por_debajo:
                        carta.es_tirada_valida = True
            else:
                errores('tirada_no_valida')
    logging.info(f'{paso_tirada_valida=}')
    return paso_tirada_valida, baraja


def analizar_contenido(carta_usuario):
    """Analizamos el contenido, o sea que hay un numero y un palo

    Args:
        carta_usuario (list): la entrada del usuario

    Returns:
        paso_contenido: True si hay un número + un palo
    """
    logging.debug('Entra en analizar_contenido')
    match carta_usuario[0]:
        case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | \
            'sota' | 'caballo' | 'rey' | 'sotas' | 'caballos' :
            if carta_usuario[0] == 'sota' or carta_usuario[0] == 'sotas':
                carta_usuario[0] = 8
            if carta_usuario[0] == 'caballo' or carta_usuario[0] == 'caballos':
                carta_usuario[0] = 9
            if carta_usuario[0] == 'rey':
                carta_usuario[0] = 10
            carta_usuario[0] = int(carta_usuario[0])
            paso_contenido_numero = True
        case _:
            errores('numeros')
            paso_contenido_numero = False
    match carta_usuario[1]:
        case 'bastos' | 'copas' | 'espadas' | 'oros':
            paso_contenido_texto = True
        case _:
            errores('palos')
            paso_contenido_texto = False
    if paso_contenido_numero == True and paso_contenido_texto == True:
        paso_contenido = True
    else:
        paso_contenido = False
    logging.info(f'{paso_contenido=}')
    return paso_contenido, carta_usuario


def analizar_longitud(carta_usuario) -> bool:
    """Analizamos la longuitud de la cadena. Si hay un 'de' lo elimina.

    Args:
        carta_usuario (list): _description_

    Returns:
        Bool: True si es correcto, si tiene 2 elementos
    """
    logging.debug('Entra en analizar_longitud')
    paso_longuitud = True
    if len(carta_usuario) == 1:
        errores('corto')
        paso_longuitud = False
    if carta_usuario[1] == 'de':
        carta_usuario.pop(1)
        paso_longuitud = True
    if len(carta_usuario) > 2:
        errores('largo')
        paso_longuitud = False
    logging.info(f'{paso_longuitud=}')
    return paso_longuitud


def analizar_pertenece_mano(carta_usuario: str, mano: list) -> bool:
    """Analizamos si la carta pertenece a su mano

    Args:
        carta_usuario (str): _description_
        mano (list): _description_

    Returns:
        paso_pertenece_mano: True si la carta esta dentro de su mano
    """
    logging.debug('Entra en analizar_pertenece_mano')
    paso_pertenece_mano = False
    carta_usuario = carta_usuario[1]+'_'+str(carta_usuario[0])
    # opción 1) recorro toda la mano
    for carta in mano:
        if carta_usuario == carta.nombre_carta:
            paso_pertenece_mano = True
    if paso_pertenece_mano == False:
        errores('carta_no_mano')
    # opción 2) diccionario con todas las cartas
    # if baraja_diccionario[carta_usuario] in jugador_en_curso.mano:
    #     paso_pertenece_mano = True
    # if paso_pertenece_mano == False:
    #     errores('carta_no_mano')
    #     paso_pertenece_mano = False
    # print(f'{paso_pertenece_mano=}')
    logging.info(f'{paso_pertenece_mano=}')
    return paso_pertenece_mano


def errores(mensaje_mostrado) -> None:
    """Generamos elmensaje de salida si hay un error en la entrada de la jugada

    Args:
        mensaje_mostrado (str): tipo de error
    """
    logging.debug('Entra en errores')
    match mensaje_mostrado:
        case 'palos':
            print('Creo que el palo esta mal')
        case 'numeros':
            print('Creo que el número esta mal')
        case 'corto':
            print('Solo hay una palabra')
        case 'largo':
            print('Hay muchas palabras')
        case 'vacio':
            print('No has escrito nada')
        case 'carta_usada':
            print('Es carta ya esta en la mesa')
        case 'carta_no_mano':
            print('Esa carta no esta en tu mano, o ya ha sido usada. No la puedes usar')
        case 'tirada_no_valida':
            print('Esa carta no la puedes usar. Tiene que ser una carta por arriba o por abajo de las cartas mostradas')
        case _:
            print('Error en general en la entrada de la jugada')


def mostar_estado(mano_jugador) -> None:
    """Mostramos el panel de distirbución de las cartas de la mano

    Args:
        mano_jugador (_type_): Mano del jugador en curso
    """
    logging.debug('Entra en mostar_estado')
    mano_bastos = []
    mano_copas = []
    mano_espadas = []
    mano_oros = []
    for carta in mano_jugador:
        mano_bastos.append(carta.solo_numero()) if  carta.palo == 'bastos' else None
        mano_copas.append(carta.solo_numero()) if carta.palo == 'copas' else None
        mano_espadas.append(carta.solo_numero()) if carta.palo == 'espadas' else None
        mano_oros.append(carta.solo_numero()) if carta.palo == 'oros' else None
    mano_bastos.sort()
    mano_bastos = str(cambio_nombre(mano_bastos))[1:-1]
    mano_copas.sort()
    mano_copas = str(cambio_nombre(mano_copas))[1:-1]
    mano_espadas.sort()
    mano_espadas = str(cambio_nombre(mano_espadas))[1:-1]
    mano_oros.sort()
    mano_oros = str(cambio_nombre(mano_oros))[1:-1]
    print(f'  Bastos: {mano_bastos}')
    print(f'  Copas: {mano_copas}')
    print(f'  Espadas: {mano_espadas}')
    print(f'  Oros: {mano_oros}')
    print(f'  Número de cartas: {len(mano_jugador)}')


def eliminar_carta(carta_usuario, jugador_activo_mano) -> list:
    """Eliminanos la carta de la mano del jugador

    Args:
        numero (int): numero de la carta
        palo (str): palo

    Returns:
        lista de objetos (cartas del usuario)
    """
    logging.debug('Entra en eliminar_carta')
    carta_usuario = carta_usuario[1]+'_'+str(carta_usuario[0])
    for carta in jugador_activo_mano:
        if carta_usuario == carta.nombre_carta:
            jugador_activo_mano.remove(carta)
    return jugador_activo_mano


def cambio_nombre(mano: list) -> list:
    """Función que usamos para cambiar el número por texto en las figuras: 8, 9 y 10.
    La usamos solo para mostar la mano en pantalla

    Args:
        mano (list): lista de cada palo

    Returns:
        list: Lista con la cartas según se ven
    """
    logging.debug('Entra en cambio_nombre')
    mano_temp = []
    for numero in mano:
        if numero >= 1 and numero <=7:
            mano_temp.append(numero)
        if numero == 8:
            numero = '8 Sota'
            mano_temp.append(numero)
        if numero == 9:
            numero = '9 Caballo'
            mano_temp.append(numero)
        if numero == 10:
            numero = '10 Rey'
            mano_temp.append(numero)
    return mano_temp


def es_posible_tirar(mano: list) -> bool:
    """Vemos si es posible tirar esa carta

    Args:
        mano (list): mano actual

    Returns:
        bool: True/False si es posible la tirada
    """
    logging.debug('Entra en es_posible_tirar')
    es_posible = False
    for carta in mano:
        if carta.es_tirada_valida == True:
            es_posible = True
        # paso_tirada_valida, baraja = analizar_tirada_valida(carta_usuario, mano)
        # es_posible = True if paso_tirada_valida == True else False
        # if paso_tirada_valida == True:
        #     es_posible = True
    print()
    return es_posible


def ganador_jugada(jugador_activo_nombre: str) -> None:
    """Mostramos el texto del fin del juego cuando hay un ganador

    Args:
        jugador_activo_nombre (str): Nombre del jugados
    """
    logging.debug('Entra en ganador_jugada')
    print()
    cadena = '*  ' + jugador_activo_nombre + ' has ganado la partida  *'
    print('*'*len(cadena))
    print(cadena)
    print('*'*len(cadena))






# * *********************
# * Empieza la aplicación
# * *********************

if __name__ == '__main__':
    os.system('clear')
    print('Bienvenido al Cinquillo')
    print('-'*23)
    print()

    # * Creamos la baraja y los jugadores
    for palo in PALOS:
        for numero in range(1,11):
            Carta(palo, numero)
    for carta in baraja_diccionario.values():
        baraja.append(carta)
    grupo = crear_jugadores(baraja)

    # * Recorre los datos
    # for carta in baraja_diccionario.keys():
    #     print(carta)
    # for carta in baraja_diccionario.values():
    #     print(carta)

    # * Actualizamos el valor de tirada_valida y visible a las que lo son por defecto y la primera tirada, 5 de oros
    baraja_diccionario['bastos_5'].es_tirada_valida = True
    baraja_diccionario['copas_5'].es_tirada_valida = True
    baraja_diccionario['espadas_5'].es_tirada_valida = True
    baraja_diccionario['oros_4'].es_tirada_valida = True
    baraja_diccionario['oros_5'].es_tirada_valida = True
    baraja_diccionario['oros_5'].visible = True
    baraja_diccionario['oros_6'].es_tirada_valida = True

    pausa()

    print('Mesa de juego:')
    print()
    crear_tablero(baraja)

    print()

    # * Analizamos quien empieza
    for i in range(0, len(grupo)):
        primero = grupo[i].es_primero()
        if primero == True:
            es_primero = i
    jugador_en_curso = grupo[es_primero]
    print(f'{jugador_en_curso.nombre} tienes el "5 de oros" y vas a empezar a jugar')
    print()

    # * Creamos el grupo por orden (grupo_en_orden)
    # de primero al final
    primero = jugador_en_curso.numero
    for i in range(primero-1, len(grupo)):
        grupo_en_orden.append(grupo[i])
    # del comienzo al primero
    for i in range(0, primero-1):
        # print(f'{i=}')
        grupo_en_orden.append(grupo[i])

    # * Eliminamos carta de la mano
    jugador_en_curso.mano.remove(baraja_diccionario['oros_5'])

    # * Mostrar mano
    print(f'Tu mano actual (después de tirar el "5 de oros") es:')
    mostar_estado(jugador_en_curso.mano)

    pausa()

    # for jugador in grupo:
    #     pprint(jugador.todos_los_datos)

    # * Hacemos circular la lista (grupo_en_orden). Uso: next(grupo_en_orden).nombre
    grupo_en_orden = cycle(grupo_en_orden)
    # nos saltamos el primero porque lo hemos hecho manualmente
    jugador_activo = next(grupo_en_orden)

    # * Ciclo del juego, el primer jugador no esta porque lo hemos desarrollado manualmente
    # * Solo se sale cuando hay un ganador
    ganador = False

    while ganador == False:
        jugador_activo = next(grupo_en_orden)
        jugador_activo_nombre = jugador_activo.nombre
        jugador_activo_mano = jugador_activo.mano
        print('Mesa de juego:')
        crear_tablero(baraja)
        print()

        print(f'{jugador_activo_nombre} te toca tirar. En tu mano tienes:')
        # print(f'{id(jugador_activo.mano)=}')
        mostar_estado(jugador_activo_mano)
        # print(f'{id(jugador_activo.mano)=}')
        # print(f'{jugador_activo_nombre=} - {id(jugador_activo_mano)=}')

        print()

        es_posible = es_posible_tirar(jugador_activo_mano)
        if es_posible == True:
            baraja, jugador_activo_mano = jugada(
                baraja, jugador_activo_mano, jugador_activo_nombre)
        else:
            print('Upps, no puedes tirar ninguna carta, tienes que pasar')

        # * Tratamos el ganador del juego
        if len(jugador_activo_mano) == 0:
            ganador = True
            break

        pausa()

    ganador_jugada(jugador_activo_nombre)

