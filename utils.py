import random
from time import sleep

import pyautogui
from keyboard import press

from constantes import LLAVES_MENSAJES, MENSAJES, LLAVES_MENSAJES_RESPUESTA, MENSAJES_RESPUESTA


def mover_mouse(x, y):
    pyautogui.moveTo(x, y)


def mover_mouse_desde_aqui(x, y):
    pyautogui.moveRel(x, y)


def hacer_click(x, y):
    pyautogui.click(x, y)


def escribir(mensaje: str):
    pyautogui.typewrite(mensaje)
    pyautogui.press(['enter', 'enter'])


def presionar_tecla(key: str):
    pyautogui.keyDown(key)


def mover_desplazamiento(trayectoria, accion=None, args=None):
    if args is None:
        args = [None]
    for coord in trayectoria:
        x = coord[0]
        y = coord[1]
        mover_mouse(x, y)
        if accion:
            accion(x, y, *args)


def generar_mensaje_random():
    tiempo_respuesta = random.randint(1, 3)
    sleep(tiempo_respuesta)
    total = len(LLAVES_MENSAJES)
    indice = random.randint(0, total - 1)
    llave = LLAVES_MENSAJES[indice]
    return MENSAJES[llave] + ' '


def generar_mensaje_respuesta_random():
    tiempo_respuesta = random.randint(1, 3)
    sleep(tiempo_respuesta)
    total = len(LLAVES_MENSAJES_RESPUESTA)
    indice = random.randint(0, total - 1)
    llave = LLAVES_MENSAJES_RESPUESTA[indice]
    return MENSAJES_RESPUESTA[llave] + ' '
