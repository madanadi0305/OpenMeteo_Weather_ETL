import psycopg2
import os
import requests
import pandas as pd
from datetime import date, timedelta
import logging
logging.basicConfig(
    filename='app.log',          # The file to write to
    level=logging.DEBUG,        # Log all messages (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s', # Format: Timestamp - Level - Message
    datefmt='%Y-%m-%d %H:%M:%S'  # Date format
)

latitude = 37.3688
longitude = -122.0363
base_url="https://archive-api.open-meteo.com/v1/"
test_url="https://api.open-meteo.com/v1/forecast?latitude=51.5074&longitude=-0.1278&current_weather=true"
def extract_weather_data(latitude,longitude):
    try:
        latitude_str=str(latitude)
        longitude_str=str(longitude)
        start_date=str(date.today())
        #start_date="2026-01-02"
        end_date=str(date.today()+timedelta(days=0))
        #end_date="2026-01-02"
        place_url=base_url+"era5?latitude="+latitude_str+"&longitude="+longitude_str+"&start_date="+start_date+"&end_date="+end_date+"&hourly=temperature_2m"
        resp=requests.get(place_url)
        logging.info(f"Place URL: {place_url}")
        logging.info(resp.status_code)
        if not resp.status_code==200:
           logging.info("API Unreachable")    
        resp1=resp.json()
        logging.info(f"Weather Response: {resp1}")
        return resp1
    except Exception as e:
        logging.error(f"Problem with Accessing API: {e}")
            
resp2=extract_weather_data(latitude,longitude)
def transform_weather_data(resp1):
    logging.info("===Transforming Pipeline task=====")
    latitude=resp1['latitude']
    longitude=resp1['longitude']
    hourly=resp1['hourly']
    hours=hourly['time']
    logging.info(hours)
    temperatures=hourly['temperature_2m']
    global df1
    #df1=pd.DataFrame(columns=['latitude','longitude','temperatures','hours'])
    
    df=pd.DataFrame(columns=['latitude','longitude','temperatures','hours'])
    logging.info(temperatures)
    rows=[]
    for i in range(24):
        rows.append({
            'latitude':latitude,
            'longitude':longitude,
            'hours':hours[i],
            'temperature':temperatures[i]
        }
            )
    df1=pd.DataFrame(rows)
    

    return df1
     
df=transform_weather_data(resp2)
print("Dataframe:",df.head())
print("shape",df.shape)
def load_weather_data(df):
    cursor=None
    connect=None
    try:
        logging.info("====Load Data into Database Pipeline Task====")
        connect=psycopg2.connect(
        host="localhost",
        database="postgres_etl",
        user="postgres",
        password="####",
        port="5432" # Port is optional, defaults to 5432
        )
        cursor=connect.cursor()
        upsert_query="""insert into meteo_weather_data(latitude,longitude,hours,temperature) values(%s,%s,%s,%s)
                ;
            """
        for _, row in df.iterrows():
            
            
            cursor.execute(upsert_query,(row['latitude'],row['longitude'],row['hours'],row['temperature']))
            connect.commit()
            
        
    except psycopg2.DatabaseError as e:
        logging.error("Error loading into database",exc_info=e)
        
    finally:
        if cursor:
            cursor.close()
            connect.rollback()
        if connect:
            connect.close()

load_weather_data(df)
