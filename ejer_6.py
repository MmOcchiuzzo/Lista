from lista import Lista as ListaSimple

class Superheroe:
    def __init__(self, nombre, anio_aparicion, casa, biografia):
        self.nombre = nombre
        self.anio_aparicion = anio_aparicion
        self.casa = casa
        self.biografia = biografia

# Lista de superhéroes
superheroes=[
    Superhero("Linterna Verde",1940,"DC","Traje"),
    Superhero("Wolverine",1974,"Marvel","Traje"),
    Superhero("Star Lord",1976, "Marvel","Armadura"),
    Superhero("Dr. Strange",1963,"DC","Traje"),
    Superhero("Capitana Marvel", 1968, "Marvel", "Traje"),
    Superhero("Mujer Maravilla", 1941, "DC","Armadura"),
    Superhero("Flash",1940,"DC","Traje"),
    Superhero("Iron Man", 1963, "Marvel", "Armadura"),
    Superhero("Thor", 1962, "Marvel", "Armadura"),
    Superhero("Vision",1968,"Marvel", "Traje"),
    ]

# a. Eliminar el nodo que contiene la información de Linterna Verde
superheroes = [heroe for heroe in superheroes if heroe.nombre != "Linterna Verde"]

# b. Mostrar el año de aparición de Wolverine
for heroe in superheroes:
    if heroe.nombre == "Wolverine":
        print(f"Año de aparición de Wolverine: {heroe.año_aparicion}")

# c. Cambiar la casa de Dr. Strange a Marvel
for heroe in superheroes:
    if heroe.nombre == "Dr. Strange":
        heroe.casa = "Marvel"

# d. Mostrar el nombre de aquellos superhéroes que en su biografía mencionan la palabra "traje" o "armadura"
for heroe in superheroes:
    if "traje" in heroe.biografia or "armadura" in heroe.biografia:
        print(f"Superhéroe con traje o armadura: {heroe.nombre}")

# e. Mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
for heroe in superheroes:
    if heroe.anio_aparicion < 1963:
        print(f"Nombre: {heroe.nombre}, Casa: {heroe.casa}")

# f. Mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
for heroe in superheroes:
    if heroe.nombre in ["Capitana Marvel", "Mujer Maravilla"]:
        print(f"{heroe.nombre} pertenece a la casa {heroe.casa}")

# g. Mostrar toda la información de Flash y Star-Lord
for heroe in superheroes:
    if heroe.nombre in ["Flash", "Star-Lord"]:
        print(f"Nombre: {heroe.nombre}, Año de aparición: {heroe.anio_aparicion}, Casa: {heroe.casa}, Biografía: {heroe.biografia}")

# h. Listar los superhéroes que comienzan con la letra B, M y S
letras_iniciales = ["B", "M", "S"]
for heroe in superheroes:
    if heroe.nombre[0] in letras_iniciales:
        print(f"Superhéroe que comienza con {heroe.nombre[0]}: {heroe.nombre}")

# i. Determinar cuántos superhéroes hay de cada casa de cómic
casa_counts = {"Marvel": 0, "DC": 0}
for heroe in superheroes:
    casa_counts[heroe.casa] += 1

for casa, count in casa_counts.items():
    print(f"Superhéroes de la casa {casa}: {count}")



