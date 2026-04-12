import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()

#Load variable 
url_base = os.getenv("URL_BASE")
api_key = os.getenv("API_KEY")

#Check url_base and api_key if it exist
def fetch_weather_data():
        print("Fetching wather data from API...")
        if not url_base:
            raise ValueError("MISSING URL_BASE")
        if not api_key:
            raise ValueError("MISSING API_KEY")

        params = {"access_key":api_key,"query":"New York"}
        try:
            response = requests.get(url_base,params = params,timeout=30)
            response.raise_for_status()
            print("API reponse received succesfully.")
            return request.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occured: {e}")
            raise

fetch_weather_data()