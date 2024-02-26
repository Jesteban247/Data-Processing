from datetime import datetime

# Try importing pyowm and catch ImportError if it fails
try:
    from pyowm.owm import OWM
except ImportError:
    import os
    # Install pyowm library using pip
    os.system('pip install pyowm')

    # Try importing pyowm again
    try:
        from pyowm.owm import OWM
    except ImportError:
        print("Failed to install 'pyowm' library. Please install it manually with: pip install pyowm")
        exit()


# Try importing pandas and catch ImportError if it fails
try:
    import pandas as pd
except ImportError:
    import os
    # Install pandas library using pip
    os.system('pip install pandas')

    # Try importing pandas again
    try:
        import pandas as pd
    except ImportError:
        print("Failed to install 'pandas' library. Please install it manually with: pip install pandas")
        exit()



owm = OWM('db5829c814693c6429a0ea9db06f3dce')
mgr = owm.weather_manager()

# Function to retrieve weather data for a city
def get_weather(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather
    return {
        'City': city,
        'Detailed Status': w.detailed_status,
        'Wind Speed': w.wind()['speed'],
        'Wind Direction': w.wind()['deg'],
        'Humidity': w.humidity,
        'Temperature': w.temperature('celsius')['temp'],
        'Max Temperature': w.temperature('celsius')['temp_max'],
        'Min Temperature': w.temperature('celsius')['temp_min'],
        'Rain': w.rain,
        'Heat Index': w.heat_index,
        'Clouds': w.clouds,
        'Time': datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

# List of important cities in the United States
important_cities_us = [
    'New York,US', 'Los Angeles,US', 'Chicago,US', 'Houston,US', 'Phoenix,US',
    'Philadelphia,US', 'San Antonio,US', 'San Diego,US', 'Dallas,US', 'San Jose,US',
    'Austin,US', 'Jacksonville,US', 'San Francisco,US', 'Columbus,US', 'Fort Worth,US',
    'Indianapolis,US', 'Charlotte,US', 'Seattle,US', 'Denver,US', 'Washington,US',
    'Boston,US', 'El Paso,US', 'Nashville,US', 'Detroit,US', 'Oklahoma City,US',
    'Portland,US', 'Las Vegas,US', 'Memphis,US', 'Louisville,US', 'Milwaukee,US'
]

# Retrieve weather data for each city
weather_data = [get_weather(city) for city in important_cities_us]

# Create DataFrame from the weather data
df_weather = pd.DataFrame(weather_data)

# Show the head of the DataFrame
print(df_weather.head())

# Finally, save the DataFrame to a JSON file with the current date in the filename
current_date = datetime.now().strftime("%d-%m-%Y")
file_name = f"{current_date}_data.json"
df_weather.to_json('/workspaces/Data-Processing/Project/API/' + file_name, orient='records')