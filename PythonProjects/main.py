import requests

token = "fc8db1cafc433d281111a5324fe627b0"
host =  'https://api.pokemonbattle.me:9104'

response = requests.post('https://api.pokemonbattle.me:9104/pokemons' , 
                         headers = {"Content_Type" : "application/json" , "trainer_token" : token } , 
                         json = 
    {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"

})

print(response.text)


response_change_name = requests.patch('https://api.pokemonbattle.me:9104/pokemons' , 
                         headers = {"Content_Type" : "application/json" , "trainer_token" : token } ,
                         json = {
    "pokemon_id": "2783",
    "name": "pokemon",
})

print(response_change_name.text)


response_pokemon = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball' , 
                         headers = {"Content_Type" : "application/json" , "trainer_token" : token } ,
                         json = {
    "pokemon_id": "2813"
})

print(response_pokemon.text)

















