import csv
import random
from datetime import datetime, timedelta

# Definir los valores permitidos
temperatura_permitida = (15.0, 22.0)
distancia_detector_permitida = (0.5, 2.0)
distancia_cabeza_permitida = (0.5, 1.0)
angulo_inclinacion_permitido = range(0, 46)
dispositivos_permitidos = [f"{num}{alpha}" for num in range(1, 8) for alpha in ['I', 'E']]
turnos_permitidos = ["Mañana", "Tarde", "Noche"]
colores_cabello_permitidos = ["castaño", "negro", "marron claro"]
formas_rostro_permitidas = ["redondo", "ovalado", "diamante", "cuadrado", "triangular v", "triangular a", "rectangular", "alargado", "corazon"]
tipos_piel_permitidos = range(1, 7)
formas_cejasi_permitidas = ["arqueadas", "angulo marcado", "forma de s", "redondas", "rectas"]
tipos_nariz_permitidas = ["recta", "aguileña", "silla de montar", "gibal nasal", "pinocho", "levantada", "aplastad"]
uso_accesorios_permitidos = ["lentes", "capucha", "gorra", "mascarilla"]  # Lista de posibles accesorios
climas_permitidos = ["Soleado", "nublado", "lluvioso"]
corriente_viento_permitidos = ["debil", "mediana", "fuerte"]
estado_lectura_permitidos = ["exitoso", "fallido"]
generos_permitidos = ["Masculino", "Femenino"]
colores_ojos_permitidos = ["negro", "marron oscuro", "marron claro", "otro"]
tamaño_cabello = ["corto", "mediano", "largo"]


# Función para generar una marca temporal aleatoria
def generar_marca_temporal():
    inicio = datetime.now() - timedelta(days=365)
    random_datetime = inicio + timedelta(days=random.randint(0, 365), seconds=random.randint(0, 86400))
    return random_datetime.strftime("%d/%m/%Y %H:%M:%S")

# Función para generar accesorios usados
def generar_accesorios():
    accesorios_usados = random.sample(uso_accesorios_permitidos, random.randint(0, 4))  # Escoger de 0 a 4 accesorios
    return ", ".join(accesorios_usados) if accesorios_usados else ""  # Devolver como cadena separada por comas

# Función para generar filas de datos aleatorios
def generar_fila():
    return [
        generar_marca_temporal(),  # Marca temporal
        random.randint(17,30),      #Edad
        round(random.uniform(1.5, 2.0), 2),  # Estatura en metros
        round(random.uniform(50.0, 100.0), 1),  # Peso en kilogramos
        random.randint(1, 5),  # Número de intentos para reconocimiento
        round(random.uniform(5.0, 30.0), 1),  # Tiempo total que tomó el reconocimiento
        random.randint(100, 1000),  # Intensidad de luz en luxes
        round(random.uniform(*temperatura_permitida), 1),  # Temperatura en C°
        round(random.uniform(*distancia_detector_permitida), 2),  # Distancia entre detector y persona
        round(random.uniform(*distancia_cabeza_permitida), 2),  # Distancia de cabeza a cámara
        random.choice(angulo_inclinacion_permitido),  # Ángulo de inclinación
        random.choice(dispositivos_permitidos),  # Dispositivo
        random.choice(turnos_permitidos),  # Turno del registro
        random.choice(colores_cabello_permitidos),  # Color de cabello
        random.choice(formas_rostro_permitidas),  # Forma del rostro
        random.choice(tipos_piel_permitidos),  # Tipo de piel
        random.choice(formas_cejasi_permitidas),  # Forma de cejas
        random.choice(tipos_nariz_permitidas),  # Tipo de nariz
        generar_accesorios(),  # Accesorios usados (lentes, capucha, gorra, mascarilla)
        random.choice(climas_permitidos),  # Clima
        random.choice(corriente_viento_permitidos),  # Corriente del viento
        random.choice(estado_lectura_permitidos),  # Estado de la lectura
        random.choice(generos_permitidos),  # Género
        random.choice(colores_ojos_permitidos),  # Color de ojos
        random.choice(["claro", "oscura"]), # Color de ropa
        random.choice(tamaño_cabello)  # Tamaño de cabello
    ]

# Nombre del archivo CSV
archivo_csv = "datos_reconocimiento.csv"

# Columnas del archivo CSV
columnas = [
    "Marca temporal",
    "Edad",
    "Estatura en metros",
    "Peso en kilogramos",
    "Numero de intentos para reconocimiento",
    "Tiempo total que tomo el reconocimiento en segundos",
    "Intensidad de luz en luxes",
    "Temperatura en C°",
    "Distancia entre el detector y la persona en metros",
    "Distancia de la parte superior de cabeza hasta la camara",
    "Angulo de inclinación-sexagesimales",
    "Dispositivo",
    "Turno del registro",
    "Color de cabello",
    "Forma del rostro",
    "Tipo de piel",
    "Forma de cejas",
    "Tipo de nariz",
    "Accesorios en la cabeza-rostro",  # Nueva columna que incluye lentes, capucha, gorra, mascarilla
    "Clima",
    "Corriente del viento",
    "Estado de la lectura",
    "Género",
    "Color de ojos",
    "Color de ropa",
    "Tamaño de cabello",
]

# Crear el archivo CSV y escribir los datos
with open(archivo_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(columnas)  # Escribir las cabeceras
    for _ in range(200):  # Generar 200 filas de datos
        writer.writerow(generar_fila())

print(f"Archivo {archivo_csv} generado exitosamente.")
