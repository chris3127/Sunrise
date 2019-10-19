#!/usr/bin/env python3

import os
from flask import Flask
from flask import request # work with the current Flask request
from flask import Response
import requests
import json

app = Flask(__name__)

API_KEY_GEOCODE = os.getenv("API_KEY_GEOCODE")

class Lat_Long_Address:
    '''
    This class calls the Google Geocode API to get location data for a specific address.
    '''
    def __init__(self, address):
        '''
        Takes the input from the user and returns a json with the location data.
            :Param address: User input from the application.
            :Type self: Lat_Long_Address
            :Type address: String
        '''
        self.address = address #user input of the address
        
        self.geocode = f'https://us1.locationiq.com/v1/search.php?key={API_KEY_GEOCODE}&q={address}&format=json'
        #Assigning the API endpoint to a variable to call later
        
        self.response = requests.get(self.geocode) #Calling the Google geocode endpoint

    def lat_long(self):
        '''
        Uses the data returned from the API to identify Latitiude and Longitude of the given address.
        '''
        address_data = self.response.json()
        longitude = address_data[0]['lon']
        latitude = address_data[0]['lat']
        return(latitude, longitude)

    def api_status_check(self):
        '''
        Returns the status code of the API call.
        '''
        address_data = self.response.json()
        status = address_data['error']
        return status

    def display_address(self):
        '''
        This returns the address in full.
        '''
        address_data = self.response.json()
        display_address_data = address_data[0]['display_name']
        return display_address_data


class Sunrise_Time:
    '''
    This class calls the Sunrise Sunset API and returns time data based on the latitude and longitude passed.
    '''
    def __init__(self, lat, long):
        '''
        Makes the call to the API and returns with a date object
            Param lat: latitude of address
            Param long: longitude of address
            Type self: Sunrise_Time
            Type lat: int
            Type long: int
            Type return: string
        '''
        self.lat = lat
        self.long = long
        self.sunrise = f'https://api.sunrise-sunset.org/json?lat={lat}&lng={long}'
        self.response = requests.get(self.sunrise)
    
    def sunrise_output(self):
        '''
        This function takes the location sunrise data, parses it and renders it to HTML
        '''
        sunrise_data = self.response.json()
        sunrise_time = sunrise_data['results']['sunrise']
        return sunrise_time

    def api_status_check(self):
        '''
        Checks if the API call was successful.
        '''
        sunrise_data = self.response.json()
        status = sunrise_data['status']
        return status


#FOR TESTING
test_address = "1600 Amphitheatre Parkway, Mountain View, CA"
print(API_KEY_GEOCODE)
address_data = Lat_Long_Address(test_address)
print(address_data.lat_long())
lat_and_long = address_data.lat_long()
lat = lat_and_long[0]
long = lat_and_long[1]
sunrise = Sunrise_Time(lat, long)
print(sunrise.sunrise_output())


# @app.route('/' methods=['GET'])
# def input_form():
#     '''
#     Renders a form on the homepage
#     '''
#     html = ''
    



# @app.route('/' methods=['POST'])

# def render_sunrise_time(address, time):
#     '''
#     Renders the sunrise time to HTML for viewing by user.
#     '''
#     html = f'<h1>Sunrise at {address} is at {time}</h1><br>'
#     return html

