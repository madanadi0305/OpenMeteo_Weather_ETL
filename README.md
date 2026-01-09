# Weather Data ETL Project

## Overview
This project automates the daily extraction of weather data for San Francisco from the Open-Meteo API and loads it into a PostgreSQL database.

## Project Structure

### 1. `postgres_etl_weather.py`
Python script that captures weather data for San Francisco on a daily basis from Open-Meteo and loads the data into a PostgreSQL database.

**Data Source:** Open-Meteo Archive API  
**Target Location:** San Francisco, CA  
**Coordinates:** Latitude 37.371273, Longitude -122.0363

**API Endpoint Example:**
```
https://archive-api.open-meteo.com/v1/era5?latitude=37.371273&longitude=-122.0363&start_date=2025-12-30&end_date=2025-12-30&hourly=temperature_2m
```

### 2. `postgres_weather_etl.bat`
Windows batch file that executes the Python script on a scheduled basis using Windows Task Scheduler.

## Prerequisites

- Python 3.x installed
- PostgreSQL database configured
- Required Python packages (install via `pip install -r requirements.txt`):
  - `psycopg2` or `psycopg2-binary` (PostgreSQL adapter)
  - `requests` (for API calls)
  - Any other dependencies used in the script

## Setup Instructions

### 1. Database Configuration
Ensure your PostgreSQL database is set up with the appropriate:
- Database name
- User credentials
- Connection parameters
- Target table schema

### 2. Environment Configuration
Update the Python script with your database connection details and any required API parameters.

### 3. Windows Task Scheduler Setup

#### Steps to Schedule the ETL Job:

1. **Open Windows Task Scheduler**
   - Press `Win + R`, type `taskschd.msc`, and press Enter

2. **Create a New Task**
   - Click "Create Basic Task" or "Create Task" in the Actions panel
   - Give it a meaningful name (e.g., "Daily Weather ETL")

3. **Set the Trigger**
   - Choose "Daily" as the trigger type
   - Set your desired start time
   - Configure recurrence pattern (every 1 day)

4. **Set the Action**
   - Action type: "Start a program"
   - Program/script: Browse to the location of `postgres_weather_etl.bat`
   - Example: `C:\Users\Amadan\NPV_App_4\postgres_weather_etl.bat`

5. **Configure Additional Settings** (Optional)
   - Set conditions (e.g., only run if computer is on AC power)
   - Configure what to do if the task fails
   - Enable task history for monitoring

6. **Save and Test**
   - Save the scheduled task
   - Right-click the task and select "Run" to test it manually

## Usage

### Manual Execution
To run the ETL process manually:

```bash
# Navigate to the project directory
cd C:\Users\Amadan\NPV_App_4

# Run the batch file
postgres_weather_etl.bat
```

Or run the Python script directly:
```bash
python postgres_etl_weather.py
```

### Automated Execution
Once configured in Windows Task Scheduler, the batch file will automatically execute the Python script at the scheduled time daily.

## Monitoring

- Check Windows Task Scheduler history to verify successful runs
- Review PostgreSQL database logs for data insertion status
- Implement logging in the Python script for detailed execution tracking

## Troubleshooting

### Common Issues:

1. **Script fails to run**
   - Verify Python is in the system PATH
   - Check that all required packages are installed
   - Ensure the batch file has the correct path to the Python script

2. **Database connection errors**
   - Verify PostgreSQL service is running
   - Check database credentials and connection parameters
   - Ensure the database user has appropriate permissions

3. **API request failures**
   - Verify internet connectivity
   - Check if the Open-Meteo API is accessible
   - Review API rate limits and usage quotas

4. **Task Scheduler issues**
   - Ensure the task is enabled
   - Check that the user account has permissions to run scheduled tasks
   - Review the task history for error messages

## Data Source Information

**Open-Meteo API Documentation:** https://open-meteo.com/  
**Archive API:** https://archive-api.open-meteo.com/

## Notes

- This project is independent and not related to other projects in this workspace
- Weather data is collected hourly for the specified San Francisco coordinates
- Ensure adequate disk space for historical weather data storage

## License

[Add your license information here]

## Contact

[Add contact information or maintainer details here]
