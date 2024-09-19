# Charging Functions
from functions import agregar_insumos

# Función principal ja
def main():
    modulo = input("Introduce el nombre del módulo: ")
    actividades = {}
    
    while True:
        agregar_actividad = input("¿Deseas agregar una actividad al módulo? (sí/no): ").lower()
        if agregar_actividad == 'no':
            break
        elif agregar_actividad == 'sí':
            nombre_actividad = input("Introduce el nombre de la actividad: ")
            insumos = agregar_insumos(nombre_actividad)
            actividades[nombre_actividad] = insumos
        else:
            print("Respuesta no válida. Escribe 'sí' o 'no'.")
    
    # Mostrar el resumen del módulo, actividades e insumos
    print(f"\nMódulo: {modulo}")
    for actividad, insumos in actividades.items():
        print(f"\nActividad: {actividad}")
        for insumo, cantidad in insumos.items():
            print(f"  Insumo: {insumo}, Cantidad: {cantidad}")

if __name__ == "__main__":
    main()
