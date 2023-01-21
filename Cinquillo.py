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
import operator


PALOS = 'bastos',  'copas', 'espadas', 'oros'
jugadores = int()
es_primero = int()
baraja_diccionario = {}
baraja = []
grupo_en_orden = []
PUNTUACION = (0, 1, 3, 6, 10, 15) # Ley de formación de números triangulares

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

    def mostrar_mano(self) -> str:
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
        self.es_tirada_valida = (numero == 5) or (
            numero in range(4, 6) and palo == 'oro')
        self.nombre_carta = self.palo + '_' + str(self.numero)
        # * Aquí la añadimos al diccionario
        baraja_diccionario[self.nombre_carta] = self

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
        list: El grupo que es una lista de 2, 3 o 4 jugadores (cada jugador lleva su nombre, su mano y un número para el orden)
    """
    logging.debug('Entra en crear_jugadores')
    grupo = ()
    menu = True
    while menu is True:
        try:
            jugadores = int(
                input('¿Cuantos jugadores hay (máximo 4 y 0 para salir)?: '))
            print()
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
                        print(
                            f'Dos manos creadas de {len(mano1)} y {len(mano2)} cartas para los dos jugadores')
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
                        print(
                            f'Tres manos creadas de {len(mano1)}, {len(mano2)} y {len(mano3)} cartas para los tres jugadores')
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
                        print(
                            f'Cuatro manos creadas de {len(mano1)}, {len(mano2)}, {len(mano3)} y {len(mano4)} cartas para los cuatro jugadores')
                menu = False
    return list(grupo)


def chequear_nombre_jugador(numero: str) -> str:
    """Chequeamos que el nombre de los jugadores no esta vacio

    Args:
        numero (str): numero en texto del jugador

    Returns:
        str: nombre del jugador por defecto si no ha metido ninguno: Uno, Dos, Tres o Cuatro
    """
    logging.debug('Entra en chequear_nombre_jugador')
    nombre = input('Nombre del jugador ' + numero + ': ')
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
    # ? podemos usar panel con esquinas redondeadas pero no se como poner el fondo
    # ? Panel.fit(crear_carta('2 Espadas'))
    for numero in range(1, 11):
        numero = str(numero)
        # Para la creacion de la tabla todo tiene que ser str
        table.add_row(numero,
                      crear_carta_tablero('Bastos', numero, baraja),
                      crear_carta_tablero('Copas', numero, baraja),
                      crear_carta_tablero('Espadas', numero, baraja),
                      crear_carta_tablero('Oros', numero, baraja))
    console = Console()
    console.print(table)


def crear_carta_tablero(palo: str, numero: str, baraja: list) -> str:
    """Crea cada una de las 40 cartas para que se muestren en la función crear_tablero.
    Puede retornar la carta o tres retornos de línea si la carta no esta visible

    Args:
        palo (str): Palo de la carta
        numero (str): Número de la carta
        baraja (list): Baraja donde estan atributos como si es visible

    Returns:
        str: carta para la función crear_tablero
    """
    logging.debug('Entra en crear_carta_tablero')
    paso = False
    carta_retornada = ''
    for carta in baraja:
        if carta.visible == True and carta.palo == palo.lower() and str(carta.numero) == numero:
            # print(f'{carta.visible=}')
            # print(f'{carta.palo=}')
            # print(f'{palo.lower()=}')
            # print(f'{carta.numero=}')
            # print(f'{numero=}')
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
            # * Creamos cada línea de la carta
            carta_retornada = '[reverse][bold yellow] ' + \
                numero + ' [/]' + ' '*(9-numero_longitud) + '\n'
            carta_retornada = carta_retornada + \
                '[reverse]' + ' '*palo_espacio_delante + \
                palo + ' '*palo_espacio_detras + '\n'
            carta_retornada = carta_retornada + \
                ' ' * (9-(numero_longitud)) + \
                '[reverse][bold yellow] ' + numero + ' [/]' + '\n'
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
    """Pide y analiza la entrada del usuario para tirar una carta.
    carta_usuario es list(numero: int, palo: str)

    Returns:

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
        carta_usuario = input(
            '¿Qué carta quieres poner en la mesa (número y palo)? ')
        if carta_usuario == '':
            errores('vacio')
            paso_longuitud = False
        else:
            carta_usuario = carta_usuario.lower()
            carta_usuario = carta_usuario.split()
            # * Analizamos los criterios físicos
            paso_longuitud = analizar_longitud(carta_usuario)
            if paso_longuitud == True:
                paso_contenido, carta_usuario = analizar_contenido(carta_usuario)
                # * Analizamos los criterios lógicos, solo si los criterios físicos son True
                if paso_contenido == True:
                    paso_esta_en_mano = analizar_pertenece_mano(carta_usuario, jugador_activo_mano)
                    if paso_esta_en_mano == True:
                        paso_tirada_valida, baraja = analizar_tirada_valida(carta_usuario, jugador_activo_mano)
                        if paso_tirada_valida == True:
                            paso_visibilidad = analizar_visibilidad(carta_usuario, baraja)
                            if paso_visibilidad == True:
                                print()
                                print(
                                    f'{jugador_activo_nombre} la tirada es válida (se muestra en la siguiente pantalla)')
                                # * Eliminamos la carta
                                jugador_activo_mano = eliminar_carta(
                                    carta_usuario, jugador_activo_mano)
                                paso_jugada = True
    return baraja, jugador_activo_mano


def jugada_ia(jugador_activo_mano: list, tirada_IA: list):
    """Ejecuta la tirada de la IA

    Args:
        jugador_activo_mano (list):
        tirada_IA (list): Tirada de la IA

    Returns:
        baraja: list
        jugador_activo_mano: list
    """
    logging.debug('Entra en jugada_AI')
    paso_tirada_valida, baraja = analizar_tirada_valida(
        tirada_IA, jugador_activo_mano)
    paso_visibilidad = analizar_visibilidad(tirada_IA, baraja)
    print()
    print(f'La tirada es válida (se muestra en la siguiente pantalla)')
    # * Eliminamos la carta
    jugador_activo_mano = eliminar_carta(tirada_IA, jugador_activo_mano)
    return baraja, jugador_activo_mano


def analizar_visibilidad(carta_usuario, baraja) -> bool:
    """Analizamos si la carta ya esta en la mesa.
    Si no esta, pero la va a colocar en la jugada actual cambia el valor de carta.visible = True

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
    por_encima = str
    por_debajo = str
    for carta in mano:
        # * Cuando encontramos la carta en la mano
        if carta.numero == carta_usuario[0] and carta.palo == carta_usuario[1]:
            if carta.es_tirada_valida == True:
                paso_tirada_valida = True
                # * Actualizamos en estado de las carta anterior y posterior
                # creamos los nombres a buscar
                if carta_usuario[0] == 10:
                    por_encima = carta_usuario[1] + '_' + str(carta_usuario[0])
                else:
                    por_encima = carta_usuario[1] + \
                        '_' + str(carta_usuario[0]+1)
                if carta_usuario[0] == 1:
                    por_debajo = carta_usuario[1] + '_' + str(carta_usuario[0])
                else:
                    por_debajo = carta_usuario[1] + '_' + str(carta_usuario[0]-1)
            else:
                errores('tirada_no_valida')
    # * Recorremos el diccionario buscando las dos cartas a modificar
    for carta in baraja:
        if carta.nombre_carta == por_encima or carta.nombre_carta == por_debajo:
            carta.es_tirada_valida = True
    logging.info(f'{paso_tirada_valida=}')
    return paso_tirada_valida, baraja


def analizar_longitud(carta_usuario) -> bool:
    """Analizamos la longuitud de la cadena. Si hay un 'de' lo elimina

    Args:
        carta_usuario (list): _description_

    Returns:
        Bool: True si es correcto: si tiene 2 elementos
    """
    logging.debug('Entra en analizar_longitud')
    paso_longuitud = True
    if len(carta_usuario) == 1:
        errores('corto')
        paso_longuitud = False
    if len(carta_usuario) > 2:
        if carta_usuario[1] == 'de' and len(carta_usuario) == 3:
            carta_usuario.pop(1)
            paso_longuitud = True
        else:
            errores('largo')
            paso_longuitud = False
    logging.info(f'{paso_longuitud=}')
    return paso_longuitud


def analizar_contenido(carta_usuario):
    """Analizamos el contenido: que existe un número y un palo y
    unfificamos el número de salida de carta_usario a 8, 9 y 10 para que sea un int

    Args:
        carta_usuario (list): la entrada del usuario

    Returns:
        paso_contenido: True si hay un número y un palo
    """
    logging.debug('Entra en analizar_contenido')
    match carta_usuario[0]:
        case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | \
                'sota' | 'caballo' | 'rey' | 'sotas' | 'caballos':
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
    # ? opción 1) recorro toda la mano
    for carta in mano:
        if carta_usuario == carta.nombre_carta:
            paso_pertenece_mano = True
    if paso_pertenece_mano == False:
        errores('carta_no_mano')
    # ? opción 2) diccionario con todas las cartas
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
        mano_bastos.append(carta.solo_numero()
                           ) if carta.palo == 'bastos' else None
        mano_copas.append(carta.solo_numero()
                          ) if carta.palo == 'copas' else None
        mano_espadas.append(carta.solo_numero()
                            ) if carta.palo == 'espadas' else None
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
    print(f'  -Número de cartas: {len(mano_jugador)}')


def eliminar_carta(carta_usuario, jugador_activo_mano) -> list:
    """Eliminamos la carta de la mano del jugador

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
        if numero >= 1 and numero <= 7:
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
    print()
    return es_posible


def ganador_jugada(jugador_activo_nombre: str) -> None:
    """Mostramos el texto del fin del juego cuando hay un ganador

    Args:
        jugador_activo_nombre (str): Nombre del jugados
    """
    logging.debug('Entra en ganador_jugada')
    print()
    cadena = '*  ' + jugador_activo_nombre.upper() + ' has ganado la partida  *'
    print('*'*len(cadena))
    print(cadena)
    print('*'*len(cadena))


def IA(mano: list) -> list:
    """Versión 2.2
    Nivel medio: Versión sin dificultar el juego a los oponentes.
    El nivel alto seria teniendo en cuenta como dificultar el juego a los oponentes.
    Si HAY huecos entre medias:
        puntos = puntos final - puntos inicia - cartas nuestras entre medias
    si NO HAY huecos entre medias
        puntos = 0

    Args:
        mano (list): _description_
    """
    logging.debug('Entra en IA')
    #* Agrupamos la mano por palos
    mano_bastos = []
    mano_copas = []
    mano_espadas = []
    mano_oros = []
    for carta in mano:
        mano_bastos.append(carta.solo_numero()) if carta.palo == 'bastos' else None
        mano_copas.append(carta.solo_numero()) if carta.palo == 'copas' else None
        mano_espadas.append(carta.solo_numero()) if carta.palo == 'espadas' else None
        mano_oros.append(carta.solo_numero()) if carta.palo == 'oros' else None
    mano_bastos.sort()
    mano_copas.sort()
    mano_espadas.sort()
    mano_oros.sort()
    # * Recorremos toda la mano para ver si es posible la tirada y si lo es aplicamos la IA
    # * Creamos un diccionario con key = tirada y value = valor_tirada
    mano_activa = []
    resumen_tirada = {}
    valor_tirada = 0
    for carta in mano:
        if carta.es_tirada_valida == True:
            # * Seleccionamos la mano activa según la carta que sea
            match carta.palo:
                case 'bastos':
                    mano_activa = mano_bastos
                case 'copas':
                    mano_activa = mano_copas
                case 'espadas':
                    mano_activa = mano_espadas
                case 'oros':
                    mano_activa = mano_oros
            try:
                # * Implementación de la IA
                print(mano_activa)
                pasos = max(mano_activa) - min(mano_activa) + 1
                valor_tirada = pasos + len(mano_activa)
            except:
                print(
                    f'Error en este punto: {max(mano_activa)=} // {min(mano_activa)=}')
                pasos = 0
            
            if pasos == len(mano_activa):
                print('Esta en este punto')
                valor_tirada = 0
            # * Añadimos valor_tirada al diccionario
            key_carta = str(carta.numero) + ' ' + carta.palo
            resumen_tirada_temp = {key_carta : valor_tirada}
            resumen_tirada.update(resumen_tirada_temp)
    # * Ordenamos el diccionario
    resumen_tirada_ordenados = sorted(
        resumen_tirada.items(), key=operator.itemgetter(1), reverse=True)
    print(f'Puntos de cada tirada: {resumen_tirada_ordenados}')
    # * Pasamos de diccionario (solo el primer resultado) a lista
    tirada_ai = []
    tirada_ai = resumen_tirada_ordenados[0][0].split()
    tirada_ai = int(tirada_ai[0]), tirada_ai[1]
    tirada_ai = list(tirada_ai)
    return tirada_ai


# * *********************
# * Empieza la aplicación
# * *********************
if __name__ == '__main__':
    os.system('clear')
    print('Bienvenido al Cinquillo')
    print('-'*23)
    print('''
Instrucciones de la aplicación:
1) Primero tenemos que introducir el número de jugadores.
2) Después hay que introducir el nombre de cada jugador.
   Si quieres que algún (o algunos) jugador(es) sea (o sean) la Inteligencia Artificial escribe de nombre "IA" seguido del nombre que quieres
   usar para esa Inteligencia Artificial, por ejemplo: "AI iMac", "IA Ex Machina" o "IA Her".\n
          ''')

# todo para implementar en el menú
    """
3) Hay dos niveles disponibles (solamente si usas la IA, claro):
   1) Básico: La IA solo se preocupa en intentar ganar,
   2) Avanzado: No solo intententa ganar, si no que, además, intentara entorpecer que otros ganen.
    """
    # * Creamos las carta, la baraja y los jugadores
    for palo in PALOS:
        for numero in range(1, 11):
            Carta(palo, numero)
    for carta in baraja_diccionario.values():
        baraja.append(carta)
    grupo = crear_jugadores(baraja)

    # * Recorrer los datos
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
    print(f'{jugador_en_curso.nombre} tienes el "5 de oros" y empezara a jugar')
    print()

    # * Creamos el grupo por orden (grupo_en_orden)
    # de primero al final
    primero = jugador_en_curso.numero
    for i in range(primero-1, len(grupo)):
        grupo_en_orden.append(grupo[i])
    # del comienzo al primero
    for i in range(0, primero-1):
        grupo_en_orden.append(grupo[i])

    # * Eliminamos carta de la mano
    jugador_en_curso.mano.remove(baraja_diccionario['oros_5'])

    # * Mostrar mano
    print(f'Mano actual (después de tirar el "5 de oros") es:')
    mostar_estado(jugador_en_curso.mano)

    pausa()

    # * Hacemos circular la lista de jugadores (grupo_en_orden). Uso: next(grupo_en_orden).nombre
    grupo_en_orden = cycle(grupo_en_orden)
    # nos saltamos el primero porque ha jugado de forma manual
    jugador_activo = next(grupo_en_orden)

    # * Ciclo del juego, solo se sale cuando hay un ganador
    ganador = False

    while ganador == False:
        jugador_activo = next(grupo_en_orden)
        jugador_activo_nombre = jugador_activo.nombre
        jugador_activo_mano = jugador_activo.mano
        print('Mesa de juego:')
        crear_tablero(baraja)
        print()

        if jugador_activo_nombre[0:2].upper() == 'IA':
            print(f'Va a tirar "{jugador_activo_nombre}". En su mano tiene:')
        else:
            print(f'{jugador_activo_nombre} te toca tirar. En tu mano tienes:')
        mostar_estado(jugador_activo_mano)

        print()

        es_posible = es_posible_tirar(jugador_activo_mano)
        if es_posible == True:
            # * Discriminamos que tipo de jugador que es: la IA o humano
            if jugador_activo_nombre[0:2].upper() == 'IA':
                # Es la IA
                tirada_ia = IA(jugador_activo_mano)
                print(
                    f'"{jugador_activo_nombre}" ha pensado en esta tirada: {tirada_ia[0]} {str(tirada_ia[1])}')
                baraja, jugador_activo_mano = jugada_ia(jugador_activo_mano, tirada_ia)
            else:
                # Es humano
                baraja, jugador_activo_mano = jugada(baraja, jugador_activo_mano, jugador_activo_nombre)
        else:
            if jugador_activo_nombre[0:2].upper() == 'IA':
                # Es la IA
                print('Upps, la IA no puede tirar ninguna carta, tiene que pasar')
            else:
                # Es humano
                print('Upps, no puedes tirar ninguna carta, tienes que pasar')


        # * Tratamos el ganador del juego
        if len(jugador_activo_mano) == 0:
            ganador_jugada(jugador_activo_nombre)
            ganador = True
            break

        pausa()

print()
print('Fin del juego')
