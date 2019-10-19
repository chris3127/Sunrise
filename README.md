### Overview and Application Structure
The sunrise application utilises an algorithm that allows 2 way communication to occur between the application and multiple API's, and a web browser and the application. The goal of the application is to get weather information for a particular address. The MVP will return sunrise time for a given address.
The Sunrise application provides a webpage with a user input field where an address can be entered. When an address is entered, a request to the Google maps geocode API is made that returns a Latitude and Longitude for that location. This Latitude and Longitude are then used to call a Sunrise-Sunset API that returns data for that location. The response from this API is parsed by the Sunrise algorithm and builds HTML elements which include times for Sunrise and Sunset.

### Algorithm


### Inputs and Outputs
The input and output of the application will be handled by Flask using HTTP requests to get data, and provide a webpage to display information and allow user interaction.

### Structure
The sunrise application will have 1 route, 


### Dependencies
The core dependency is Python 3 and it's standard libraries, with the Flask package to make API requests.

