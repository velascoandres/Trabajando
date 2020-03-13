def generar_ruta_constante(const_x, const_y, total, tipo='H'):
    ruta = []
    acumulador_y = 0
    acumulador_x = 0
    for contador in range(0, total):
        if tipo == 'V':
            acumulador_x = const_x
            acumulador_y = acumulador_y + const_y
        if tipo == 'H':
            acumulador_y = const_y
            acumulador_x = acumulador_x + const_x
        if tipo == 'D':
            acumulador_x = acumulador_x + const_x
            acumulador_y = acumulador_y + const_y

        ruta.append([acumulador_x, acumulador_y])
    return ruta
