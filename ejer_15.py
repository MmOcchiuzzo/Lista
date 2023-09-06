from lista import Lista as ListaSimple

# Definición de la estructura de datos para un Pokémon
class Pokemon:
    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

# Definición de la estructura de datos para un entrenador Pokémon
class EntrenadorPokemon:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_perdidas = batallas_perdidas
        self.batallas_ganadas = batallas_ganadas
        self.pokemons = ListaSimple()

# Lista de entrenadores Pokémon

pokemon1 = Pokemon("Pikachu", 35, "Eléctrico", None)
pokemon2 = Pokemon("Bulbasaur", 32, "Planta", "Veneno")
pokemon3 = Pokemon("Charizard", 76, "Fuego", "Volador")

entrenador1 = EntrenadorPokemon("Ash Ketchum", 10, 5, 15)
entrenador1.pokemons.insert(pokemon1)
entrenador1.pokemons.insert(pokemon2)

entrenador2 = EntrenadorPokemon("Misty", 5, 3, 10)
entrenador2.pokemons.insert(pokemon3)

# a. Obtener la cantidad de Pokémons de un determinado entrenador
def cantidad_pokemons(entrenador_nombre):
    for i in range(entrenadores.size()):
        entrenador = entrenadores.get_element_by_index(i)[0]
        if entrenador.nombre == entrenador_nombre:
            return entrenador.pokemons.size()
    return 0

# b. Listar los entrenadores que hayan ganado más de tres torneos
def entrenadores_ganadores(torneos_minimos):
    ganadores = []
    for i in range(entrenadores.size()):
        entrenador = entrenadores.get_element_by_index(i)[0]
        if entrenador.torneos_ganados > torneos_minimos:
            ganadores.append(entrenador.nombre)
    return ganadores

# c. Encontrar el Pokémon de mayor nivel del entrenador con más torneos ganados
def pokemon_mas_poderoso():
    entrenador_mas_exitoso = None
    pokemon_mas_poderoso = None
    max_torneos_ganados = 0

    for i in range(entrenadores.size()):
        entrenador = entrenadores.get_element_by_index(i)[0]
        if entrenador.torneos_ganados > max_torneos_ganados:
            entrenador_mas_exitoso = entrenador
            max_torneos_ganados = entrenador.torneos_ganados

    if entrenador_mas_exitoso is not None:
        max_nivel_pokemon = 0
        for i in range(entrenador_mas_exitoso.pokemons.size()):
            pokemon = entrenador_mas_exitoso.pokemons.get_element_by_index(i)[0]
            if pokemon.nivel > max_nivel_pokemon:
                pokemon_mas_poderoso = pokemon
                max_nivel_pokemon = pokemon.nivel

    return entrenador_mas_exitoso, pokemon_mas_poderoso

# d. Mostrar todos los datos de un entrenador y sus Pokémos
def datos_entrenador(nombre_entrenador):
    for i in range(entrenadores.size()):
        entrenador = entrenadores.get_element_by_index(i)[0]
        if entrenador.nombre == nombre_entrenador:
            return entrenador
    return None

# e. Mostrar los entrenadores cuyo porcentaje de batallas ganadas sea mayor al 79%
def entrenadores_porcentaje_ganadas(min_porcentaje):
    buenos_entrenadores = []
    for i in range(entrenadores.size()):
        entrenador = entrenadores.get_element_by_index(i)[0]
        porcentaje_ganadas = (entrenador.batallas_ganadas / (entrenador.batallas_ganadas + entrenador.batallas_perdidas)) * 100
        if porcentaje_ganadas > min_porcentaje:
            buenos_entrenadores.append(entrenador.nombre)
    return buenos_entrenadores

# f. Los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo)
def entrenadores_con_tipos(tipo1, subtipo1, tipo2, subtipo2):
    entrenadores_con_tipos = []
    for i in range(entrenadores.size()):
        entrenador = entrenadores.get_element_by_index(i)[0]
        tiene_tipo1_subtipo1 = False
        tiene_tipo2_subtipo2 = False
        for j in range(entrenador.pokemons.size()):
            pokemon = entrenador.pokemons.get_element_by_index(j)[0]
            if pokemon.tipo == tipo1 and pokemon.subtipo == subtipo1:
                tiene_tipo1_subtipo1 = True
            if pokemon.tipo == tipo2 and pokemon.subtipo == subtipo2:
                tiene_tipo2_subtipo2 = True
        if tiene_tipo1_subtipo1 and tiene_tipo2_subtipo2:
            entrenadores_con_tipos.append(entrenador.nombre)
    return entrenadores_con_tipos

# g. El promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel(entrenador_nombre):
    for i in range(entrenadores.size()):
        entrenador = entrenadores.get_element_by_index(i)[0]
        if entrenador.nombre == entrenador_nombre:
            if entrenador.pokemons.size() > 0:
                suma_niveles = 0
                for j in range(entrenador.pokemons.size()):
                    pokemon = entrenador.pokemons.get_element_by_index(j)[0]
                    suma_niveles += pokemon.nivel
                return suma_niveles / entrenador.pokemons.size()
    return None

# h. Determinar cuántos entrenadores tienen a un determinado Pokémon
def cantidad_entrenadores_con_pokemon(pokemon_nombre):
    count = 0
    for i in range(entrenadores.size()):
        entrenador = entrenadores.get_element_by_index(i)[0]
        for j in range(entrenador.pokemons.size()):
            pokemon = entrenador.pokemons.get_element_by_index(j)[0]
            if pokemon.nombre == pokemon_nombre:
                count += 1
    return count

# i. Mostrar los entrenadores que tienen Pokémons repetidos
def entrenadores_con_pokemon_repetido():
    entrenadores_repetidos = []
    for i in range(entrenadores.size()):
        entrenador = entrenadores.get_element_by_index(i)[0]
        nombres_pokemon = []
        for j in range(entrenador.pokemons.size()):
            pokemon = entrenador.pokemons.get_element_by_index(j)[0]
            if pokemon.nombre in nombres_pokemon:
                entrenadores_repetidos.append(entrenador.nombre)
            else:
                nombres_pokemon.append(pokemon.nombre)
    return entrenadores_repetidos

# j. Determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull
def entrenadores_con_pokemon_especifico(pokemon_nombres):
    entrenadores_con_pokemon = []
    for i in range(entrenadores.size()):
        entrenador = entrenadores.get_element_by_index(i)[0]
        for j in range(entrenador.pokemons.size()):
            pokemon = entrenador.pokemons.get_element_by_index(j)[0]
            if pokemon.nombre in pokemon_nombres:
                entrenadores_con_pokemon.append(entrenador.nombre)
    return entrenadores_con_pokemon

# k. Determinar si un entrenador “X” tiene al Pokémon “Y”
def tiene_entrenador_pokemon(entrenador_nombre, pokemon_nombre):
    for i in range(entrenadores.size()):
        entrenador = entrenadores.get_element_by_index(i)[0]
        if entrenador.nombre == entrenador_nombre:
            for j in range(entrenador.pokemons.size()):
                pokemon = entrenador.pokemons.get_element_by_index(j)[0]
                if pokemon.nombre == pokemon_nombre:
                    return entrenador, pokemon
    return None, None
