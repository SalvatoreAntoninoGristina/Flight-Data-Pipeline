import os
from dotenv import load_dotenv
import requests
import pandas as pd

load_dotenv()
api_key = os.getenv("AVIATIONSTACK_API_KEY")

url = f"https://api.aviationstack.com/v1/flights?access_key={api_key}"

response = requests.get(url)
data = response.json()
df = pd.json_normalize(data['data'])
# print(df.shape)         # (righe, colonne)
# print("___________________")
# print(df.columns)       # nomi delle colonne
# print("___________________")
# print(df.dtypes)        # tipi di dato per ogni colonna
# print("___________________")
# print(df.isnull().sum())    # quanti NaN per colonna
# print("___________________")
#print(df.info())            # visione sintetica
#print(df['flight_status'].value_counts())
#print(df)