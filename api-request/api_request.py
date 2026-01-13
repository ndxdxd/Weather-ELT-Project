import requests
api_key = "fab0e898f98dc0eae360ad742213406e"
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=New York"

def fetch_data():
    print(("fetching weather data from weatherstack API..."))
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API Response Received Successfully")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        raise


def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'},
             'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-10-27 04:13', 'localtime_epoch': 1761538380, 'utc_offset': '-4.0'},
               'current': {'observation_time': '08:13 AM', 'temperature': 5, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0008_clear_sky_night.png'], 'weather_descriptions': ['Clear '], 
                           'astro': {'sunrise': '07:21 AM', 'sunset': '05:58 PM', 'moonrise': '01:13 PM', 'moonset': '10:00 PM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 25},
                            'air_quality': {'co': '288.85', 'no2': '34.95', 'o3': '18', 'so2': '6.45', 'pm2_5': '9.75', 'pm10': '9.75', 'us-epa-index': '1', 'gb-defra-index': '1'},
                              'wind_speed': 13, 'wind_degree': 25, 'wind_dir': 'NNE', 'pressure': 1029, 'precip': 0, 'humidity': 70, 'cloudcover': 25, 'feelslike': 2, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}

