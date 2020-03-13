from acciones import navegar_node_modules, escribir_discord
from constantes import DESPLAZAMIENTO_WEBSTORM, DESPLAZAMIENTO_DISCORD
from desplazamiento import generar_ruta_constante
from utils import mover_desplazamiento, hacer_click, generar_mensaje_random, generar_mensaje_respuesta_random


def trabajar(tiempo_limite):
    mi_ruta = generar_ruta_constante(100, 35, 12, 'H')
    tiempo_actual = 0
    while True:
        tiempo_actual = tiempo_actual + 1
        if tiempo_actual == tiempo_limite:
            break
        mover_desplazamiento(
            trayectoria=DESPLAZAMIENTO_DISCORD,
            accion=escribir_discord,
            args=[
                generar_mensaje_random()
            ]
        )


trabajar(20)
