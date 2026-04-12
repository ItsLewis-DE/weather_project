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
            data= response.json()
            print(json.dumps(data,indent=4))
        except requests.exceptions.RequestException as e:
            print(f"An error occured: {e}")
            raise

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-04-12 01:23', 'localtime_epoch': 1775956980, 'utc_offset': '-4.0'}, 'current': {'observation_time': '05:23 AM', 'temperature': 11, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 'astro': {'sunrise': '06:22 AM', 'sunset': '07:33 PM', 'moonrise': '03:57 AM', 'moonset': '02:16 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 33}, 'air_quality': {'co': '205.85', 'no2': '19.25', 'o3': '57', 'so2': '4.35', 'pm2_5': '7.25', 'pm10': '7.45', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 14, 'wind_degree': 356, 'wind_dir': 'N', 'pressure': 1030, 'precip': 0, 'humidity': 35, 'cloudcover': 0, 'feelslike': 9, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}