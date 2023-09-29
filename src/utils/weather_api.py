import requests
import os

def fetch_data(location):
        
    try:
        
        WEATHERAPI_API_KEY = os.environ.get("WEATHERAPI_API_KEY", "")
        assert WEATHERAPI_API_KEY, "WEATHERAPI_API_KEY environment variable is missing from .env"

        api_url = f"http://api.weatherapi.com/v1/current.json?key={WEATHERAPI_API_KEY}&q={location}&aqi=no"
        
        response = requests.get(api_url)
        data = response.json()
        
        status = True
        time_data = data['location']['localtime']
        temp_data = data['current']['temp_c']
               
        return status, time_data, temp_data

    except Exception as e:
        
        print(f"Error fetching temperature data: {str(e)}")
        status = False
        
        return status
   
