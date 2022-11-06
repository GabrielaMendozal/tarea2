import requests
import json

#Opc#ión 1: Listar pokemons por generación. 
# Se ingresa alguna generación (1, 2, 3, ..) y 
# se listan todos los pokemon respectivos.
def get_generation(id):
    url = f'https://pokeapi.co/api/v2/generation/{id}'

    #args = {'id':id} if id else {}

    response = requests.get(url)
   #....
    #print(response.status_code)
    if response.status_code == 200:
    
        data = response.json()
        #print(data)
        results = data['pokemon_species']
        
        if results: 
            for pokemon in results:
                name = pokemon['name']
                print(name)

#if __name__ == '__main__':

   # url = 'https://pokeapi.co/api/v2/generation/=${id}'
id = int(input("Escribe el id de la generacion de pokemon a listar: "))

get_generation(id)
    


#Opción 2: Listar pokemons por forma. 
# Se ingresa alguna forma (deben sugerir valores) y
#  se listan todos los pokemons respectivos.
#Opción 3: Listar pokemons por habilidad.
# Se deben sugerir opciones a ingresar para interactuar.
#Opción 4: Listar pokemons por habitat. Se deben sugerir
# opciones a ingresar para interactuar.
#Opción 5: Listar pokemons por tipo. Se deben sugerir
#  opciones a ingresar para interactuar.