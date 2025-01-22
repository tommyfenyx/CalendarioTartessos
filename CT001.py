# Definir los días de la semana
DIAS_SEMANA = ["Amadei", "Soldei", "Tredei", "Vishnudei", "Liberdei", "Kidei"]

# Definir los meses
MESES = [
    "Farvardín", "Ordibehesht", "Jordad", "Tir", 
    "Mordad", "Sahjrivar", "Mehr", "Aabán", 
    "Azar", "Dey", "Bahmæn", "Esfand"
]

# Diccionario para los primeros días del ciclo de 8 años
PRIMEROS_DIAS_CICLO = {
    0: "Kidei",  # Corresponde al año 1408, 1416, etc. (año % 8 == 0)
    1: "Liberdei",  # Corresponde al año 1401, 1409, etc. (año % 8 == 1)
    2: "Vishnudei",  # Corresponde al año 1402, 1410, etc. (año % 8 == 2)
    3: "Tredei",  # Corresponde al año 1403, 1411, etc. (año % 8 == 3)
    4: "Tredei",  # Corresponde al año 1404, 1412, etc. (año % 8 == 4)
    5: "Soldei",  # Corresponde al año 1405, 1413, etc. (año % 8 == 5)
    6: "Amadei",  # Corresponde al año 1406, 1414, etc. (año % 8 == 6)
    7: "Kidei"  # Corresponde al año 1407, 1415, etc. (año % 8 == 7)
}

# Función para determinar si un año es bisiesto según el sistema de Omar Khayyam
def es_bisiesto_khayyam(year):
    # Calcular el índice dentro del ciclo de 2820 años, usando 457 como año de referencia
    indice_ciclo = (year - 457) % 2820

    # Definición de los períodos dentro del ciclo de 2820 años
    periodos = [
        (128, 7),  # 21 períodos de 128 años con 7 años bisiestos cada uno
        (29, 7),   # 1 período de 29 años con 7 años bisiestos
        (33, 8),   # 3 períodos de 33 años con 8 años bisiestos cada uno
        (132, 7),  # 1 período de 132 años con 7 años bisiestos
        (33, 8),   # 2 períodos de 33 años con 8 años bisiestos cada uno
        (37, 9)    # 1 período de 37 años con 9 años bisiestos
    ]

    # Recorrer los períodos para encontrar el año correcto
    for periodo in periodos:
        if indice_ciclo < periodo[0]:
            return (indice_ciclo > 1) and ((indice_ciclo - 1) % 4 == 0)
        else:
            indice_ciclo -= periodo[0]

    return False

# Función para obtener el primer día del año
def obtener_primer_dia(year):
    indice_ciclo = (year - 1401) % 8
    if indice_ciclo == 7:
        indice_ciclo = 0
    else:
        indice_ciclo += 1

    primer_dia_actual = PRIMEROS_DIAS_CICLO[indice_ciclo]
    return primer_dia_actual

# Función para generar el calendario de un año dado
def generar_calendario(year):
    es_bisiesto_year = es_bisiesto_khayyam(year)
    
    # Duración de los meses (en días)
    DURACION_MESES = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
    
    if es_bisiesto_year:
        DURACION_MESES[-1] = 30  # Esfand tiene 30 días en años bisiestos
    else:
        DURACION_MESES[-1] = 29  # Esfand tiene 29 días en años no bisiestos
    
    # Generar el calendario
    calendario = {}
    dia_actual = DIAS_SEMANA.index(obtener_primer_dia(year))
    
    for mes_idx, mes in enumerate(MESES):
        dias_mes = DURACION_MESES[mes_idx]
        calendario[mes] = []
        
        for dia in range(1, dias_mes + 1):
            calendario[mes].append(DIAS_SEMANA[dia_actual])
            dia_actual = (dia_actual + 1) % len(DIAS_SEMANA)
    
    return calendario

# Función principal para interactuar con el usuario
def main():
    try:
        year = int(input("Introduce el año del calendario del Reino de Tartessos: "))
        
        print(f"El año {year} {'es' if es_bisiesto_khayyam(year) else 'no es'} bisiesto.")
        print(f"El primer día del año {year} es {obtener_primer_dia(year)}.")
        
        calendario = generar_calendario(year)
        
        print("\nCalendario:")
        for mes, dias in calendario.items():
            print(f"\n{mes}:")
            for i, dia in enumerate(dias, start=1):
                print(f"{i}: {dia}", end=" ")
                if i % 6 == 0:  # Salto de línea cada 6 días para mejor lectura
                    print()
            print()
            
    except ValueError:
        print("Por favor, introduce un año válido.")

if __name__ == "__main__":
    main()
