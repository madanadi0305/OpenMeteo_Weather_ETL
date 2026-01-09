1. postgres_etl_weather.py
   This file captures weather data for San Francisco city on a daily basis from open meteo and loads the data into Postgres Database
2.postgres_weather_etl.bat
   This batch file runs the python scripts everyday based on a trigger time set using Windows Scheduler


How to run this file
1. From Windows Scheduler add the location of the batch file as the source and assign it a time to run daily
2. The batch file will run the python file and extract data from open-meteo website.
   URL: https://archive-api.open-meteo.com/v1/era5?latitude=37.371273&longitude=-122.0363&start_date=2025-12-30&end_date=2025-12-30&hourly=temperature_2m

