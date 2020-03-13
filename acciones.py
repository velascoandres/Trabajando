from keyboard import press
from utils import hacer_click, escribir, presionar_tecla
from pynput.keyboard import Key, Controller

keyboard = Controller()


def navegar_node_modules(x, y, mensaje):
    if y == 430:
        hacer_click(x, y)
        hacer_click(x, y)
    if x == 100:
        hacer_click(x, y)
        escribir(mensaje)
        # keyboard.press(Key.enter)


def escribir_discord(x, y, mensaje):
    if y == 1100:
        hacer_click(x, y)
        escribir(mensaje)
        # keyboard.press(Key.enter)
