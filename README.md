# ShortenUrl
This project is a Django-based URL shortener system that allows users to shorten URLs, set expiration times, and track usage analytics.

##Features

1. Core Functionality:
   - Create a shortened URL for any given long URL.
   - Each shortened URL is unique and idempotent.

2. Expiry:
   - Users can specify an expiration time (in hours).
   - Default expiration time is 24 hours if not specified.
   - Expired URLs no longer redirect to the original URL.

3. Analytics:
   - Tracks the number of times each shortened URL is accessed.
   - Logs the timestamp and IP address of each access.

4. Storage:
   - Uses SQLite to store:
     - Original URL
     - Shortened URL
     - Creation and expiration timestamps
     - Access logs (timestamp and IP address).

5. API Endpoints:
   - `POST /shorten/`: Create a shortened URL.
   - `GET /<short_url>/`: Redirect to the original URL if not expired.
   - `GET /analytics/<short_url>/`: Retrieve analytics data for a specific shortened URL.

##Installation

1. create a virtual environment using the below command:
	-> py -m venv env
	
2. Activate the environment:
	-> go to Scripts folder with this command: cd env/Scripts
	-> To activate the env type: activate.bat

3. After activating the env, go to the project directory where requirements.txt present and install all the necessary package using below command.
	-> pip install -r requirements.txt

4. Go to inside project directory where manage.py file is present and run the below command to create database and required table:
	-> py manage.py makemigrations  
	-> py mange.py migrate
	
5. Now activate the server with the below command:
	-> py manage.py runserver

6. To test run the request.py file or go to browser and hit this url <http://127.0.0.1:8000/shorten/> with the below data:
	{
    "original_url": "<url>",
    "expiry_hours": 24
}
