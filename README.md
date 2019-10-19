### Overview and Application Structure
The sunrise application utilises an algorithm that allows 2 way communication to occur between the application and multiple API's, and a web browser and the application. The goal of the application is to get weather information for a particular address. The MVP will return sunrise time for a given address.
The Sunrise application provides a webpage with a user input field where an address can be entered. When an address is entered, a request to the Google maps geocode API is made that returns a Latitude and Longitude for that location. This Latitude and Longitude are then used to call a Sunrise-Sunset API that returns data for that location. The response from this API is parsed by the Sunrise algorithm and builds HTML elements which include times for Sunrise and Sunset.

### Algorithm
The initial route ('/') gets the HTML template that includes a form for user input. The user submits an address into this form that drives the second route. Error handling at this point displays an error if no address was inputted. 

The second route takes the address and sends a get request to the LocationIQ API which returns json data. This data is parsed and the latitude and longitude are stored as independent variables. Error handling at this point returns a HTML warning about incorrect address input.

The latitude and longitude are used to instantiate a class that makes an API call to a Sunrise_Sunset API. This returns json data which is parsed and the sunrise time in UTZ (zulu) is stored as a variable. The latitude and longitude are also used to identify the local timezone at the given address.
The current date (Y,M,D) is stored and concatenated with the local time (H,M,S). This combines to give a local time that is correct for daylight saving.

The returned sunrise time is passed into the returned HTML document as displayed for the user.

### Inputs and Outputs
The input and output of the application will be handled by Flask using HTTP requests to get data, and provide a webpage to display information and allow user data input. It gets HTML and accepts a string for user input. This user input is used to gain a JSON output from the LocationIQ Geocode API which is parsed and becomes the input for the Sunset_Sunrise API. Finally, the output is HTML rendered to display data to the user.

### Structure
The sunrise application will have 3 routes, a GET route which initially return a HTML document which has a form where the user can input an address. This HTML will also encompass a POST route which passes the address input to the third route. The third route is a GET route that uses the address input to get the sunset time for that location. The logic for the routes is encapsulated in classes Lat_Long_Address and Sunrise_Time.  

### Dependencies
The core dependency is Python 3 and it's standard libraries, with the Flask package to make API requests and handle the HTML elements (render_template, flash, redirect) along with flask_wtf and wtforms.
The following packages are also required:
gunicorn 
flask 
pytest
python-dotenv 
requests 
flask-wtf 
timezonefinder 
flake8 
os
json

