import os
import json
from dotenv import load_dotenv
import sys
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import s3_service
from utils.columns_to_filter import filters
from utils.pokemon_types import pokemon_types

def upload_specific_pokemon_type(pokemon_type):
    try:
        if (pokemon_type not in pokemon_types):
            raise ValueError(f"Invalid Pokemon type: {pokemon_type}. Valid types are: {pokemon_types}")
        all_pokemon_obj = s3_service.get_object('all-pokemon/pokemon.csv')
        all_pokemon_df = pd.read_csv(all_pokemon_obj['Body'])

        for index, pokemon in all_pokemon_df.iterrows():
            pokemon_dict = {}
            for filter in filters:
                if str(pokemon['type1']).lower() == pokemon_type or str(pokemon['type2']).lower() == pokemon_type:
                    if pd.isna(pokemon[filter]):
                        pokemon_dict[filter] = None
                    else:
                        pokemon_dict[filter] = pokemon[filter]
            if pokemon_dict:
                s3_service.upload_object(json.dumps(pokemon_dict), f'{pokemon_type}-pokemons/{pokemon["name"]}.json')

    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    upload_specific_pokemon_type()