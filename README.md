## Trabajando
Script para hackear tiempo.

## Uso

Instalar dependencias

```shell script
  $ pip install -r requirements.txt
```
Ejecutar y a trabajar XD

```shell script
  $ python trabando.py
```

## Cambiar accion


En `trabajando.py`

```python
    mover_desplazamiento(
            trayectoria=DESPLAZAMIENTO_DISCORD, # Desplazamiento
            accion=escribir_discord,  # Accion
            args=[
                generar_mensaje_respuesta_random()
            ]
        )
```