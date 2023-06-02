import requests

token = '9344decd7b1e960c4e79e91bf94fdc43'
host = 'https://pokemonbattle.me:9104'


create_pok = requests.post(f'{host}/pokemons', headers={'Content-Type':'application/json', 'trainer_token': token}, json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})

print(create_pok.status_code, create_pok.text, create_pok.json() )

name_pok = requests.put(f'{host}/pokemons', headers={'Content-Type':'application/json', 'trainer_token': token}, json={
    "pokemon_id": "12729",
    "name": "booba",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})
print(name_pok.status_code, name_pok.text, name_pok.json() )

pokeball_pok = requests.post(f'{host}/trainers/add_pokeball', headers={'Content-Type':'application/json', 'trainer_token': token}, json={
    "pokemon_id": "12729"
})
print(pokeball_pok.status_code, pokeball_pok.text, pokeball_pok.json() )


