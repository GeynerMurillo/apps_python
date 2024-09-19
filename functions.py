def agregar_insumos(actividad):
    insumos = {}
    while True:
        nombre_insumo = input(f"Introduce el nombre del insumo para '{actividad}' (o 'salir' para terminar): ")
        if nombre_insumo.lower() == 'salir':
            break
        cantidad = input(f"Introduce la cantidad de '{nombre_insumo}': ")
        insumos[nombre_insumo] = cantidad
    return insumos