import requests
import streamlit as st

st.title("Pokédex")
st.markdown("#### Enter the name of the Pokemon")
pokemon_name = st.text_input(" ")

if pokemon_name:
  url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
  response = requests.get(url)

  if response.status_code == 200:
    pokemon_info = response.json()
    p_name = pokemon_info["name"].capitalize()
    p_id = pokemon_info["id"]

    st.subheader(f"{p_name} (#{p_id})")

    type_colors = {
        "Normal": "#A8A878",
        "Fire": "#F08030",
        "Water": "#6890F0",
        "Electric": "#F8D030",
        "Grass": "#78C850",
        "Ice": "#98D8D8",
        "Fighting": "#C03028",
        "Poison": "#A040A0",
        "Ground": "#E0C068",
        "Flying": "#A890F0",
        "Psychic": "#F85888",
        "Bug": "#A8B820",
        "Rock": "#B8A038",
        "Ghost": "#705898",
        "Dragon": "#7038F8",
        "Dark": "#705848",
        "Steel": "#B8B8D0",
        "Fairy": "#EE99AC",
    }

    # Put the image and basic metrics side-by-side using columns
    col1, col2 = st.columns(2)

    with col1:
      st.image(
          pokemon_info["sprites"]["other"]["official-artwork"][
              "front_default"
          ],
          width=300
      )

    with col2:
      st.markdown("### Quick Info")
      # Display types nicely
      st.markdown(f"**Height:** {pokemon_info['height'] * 0.1:.1f} m")
      st.markdown(f"**Weight:** {pokemon_info['weight'] * 0.1:.1f} kg")

    st.markdown("---")
    with st.popover("Settings"):
        st.markdown("### Select the info you want to view related to the pokemon: ")
        selected_choice = st.multiselect(
            " ", ["STATS", "ABILITIES", "MOVES","TYPES"], default=["STATS"]
        )

    if "STATS" in selected_choice:
      st.markdown("### **Pokemon Stats**")
      # Optional: You can put stats in columns or use metric cards here too!
      for i in pokemon_info["stats"]:
        st.markdown(f"> **{i['stat']['name'].upper()}:** {i['base_stat']}")
        


    if "MOVES" in selected_choice:
      st.markdown("### **Pokemon Moves**")
      for i in pokemon_info["moves"][:10]:
        st.markdown(f"> {i['move']['name'].capitalize()}")

    if "ABILITIES" in selected_choice:
      st.markdown("### **Pokemon Abilities**")
      for i in pokemon_info["abilities"]:
        st.markdown(f"> *{i["ability"]["name"].capitalize()}*")

    if "TYPES" in selected_choice:
      st.markdown("### **Pokemon Type**")
      for item in pokemon_info["types"]:
        t_name = item["type"]["name"].capitalize()
        #Fall back to gray if type isn't found
        bg_color = type_colors.get(t_name, "#777777")

        #Render custom html badge
        st.markdown(
            f'<span style="background-color: {bg_color}; color: white; padding:'
            f' 5px 14px; border-radius: 15px; font-weight: bold; font-size:'
            f' 14px; display: inline-block; margin-bottom: 5px;">{t_name}</span>',
            unsafe_allow_html=True,
        )#Used to add a custom layout for every type

  else:
    st.error("Pokémon not found! Check the spelling and try again.")