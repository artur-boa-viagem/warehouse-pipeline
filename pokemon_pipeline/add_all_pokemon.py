import os
import json
import tempfile
import kagglehub
import boto3
from dotenv import load_dotenv
import sys
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import s3_service

# Load environment variables
load_dotenv()

def upload_all_pokemon():
    """Download Pokemon dataset from Kaggle and upload to S3"""
    temp_dir = tempfile.mkdtemp()
    print(f"Created temporary directory: {temp_dir}")
    
    try:
        dataset_path = kagglehub.dataset_download('rounakbanik/pokemon')
        print(f"dataset_path: {dataset_path}")
        
        pokemon_csv_path = os.path.join(dataset_path, "pokemon.csv")

        temp_csv_path = os.path.join(temp_dir, "pokemon.csv")
        
        pokemon_csv = pd.read_csv(pokemon_csv_path)
        pokemon_csv.to_csv(temp_csv_path, index=False)
        
        try:
            with open(temp_csv_path, 'rb') as file:
                s3_service.upload_object(file, 'all-pokemon/pokemon.csv')
            print("Direct upload successful!")
        except Exception as e:
            print(f"Direct upload failed: {e}")
        
    except Exception as e:
        print(f"Error: {e}")
        raise
    finally:
        print("Cleaning up temporary files...")

if __name__ == "__main__":
    upload_all_pokemon()