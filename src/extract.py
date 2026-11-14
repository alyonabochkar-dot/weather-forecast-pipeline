import requests
import pandas as pd
api = "https://api.open-meteo.com/v1/forecast?latitude=47.90556631741862&longitude=33.4191251317031&hourly=temperature_2m,apparent_temperature,relative_humidity_2m,precipitation_probability,wind_speed_10m,surface_pressure,cloud_cover&timezone=auto"
response = requests.get(api)
data = response.json()
df = pd.DataFrame(data['hourly'])
df['time'] = pd.to_datetime(df['time'])
df['city'] = 'Kryvyi Rig'
nulls = df.isnull().sum()
print(nulls)

