import requests
pokemon_name = input("Enter the name of the pokemon: ")

url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
poke_info = requests.get(url)

if poke_info.status_code == 200:
    poke_data = poke_info.json()
    print("Name:",poke_data["name"].title())
    print("Height: ",poke_data["height"])
    print("Weight: ",poke_data["weight"])
    print("Base experience: ",poke_data["base_experience"])
    print("Stats: ", poke_data["stats"])
    print("---- STATS ----")
    for i in poke_data["stats"]:
        print(f"{i["stat"]["name"].upper()}: {i["base_stat"]}")
    print("-----TYPE-----")
    for item in poke_data["types"]:
        print(f"<*> {item["type"]["name"].title()}")

    print("----- MOVES -----")
    for i in poke_data["moves"][:10]:
        print(f"** {i["move"]["name"]}")

    print(f"Abilities: ",poke_data["abilities"] )

else:
    print("Error using while retirieving the data.")