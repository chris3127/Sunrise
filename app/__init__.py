#!/usr/bin/env python3

import os
from flask import Flask
from flask import request
from flask import Response
from flask import render_template, flash, redirect
from config import Config
from app.forms import LoginForm
from timezonefinder import TimezoneFinder
import pytz, datetime
import requests
import json

app = Flask(__name__)
app.config.from_object(Config)

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


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Address required'.format(form.address.data))
        return redirect(f'/sunrise?address={form.address.data}')
    return render_template('index.html', title='home', form=form)

@app.route('/sunrise', methods=['GET'])
def conversion():
    '''
    Converts the user input address to Latitude and Longitude coordinates.
    '''
    address = request.args.get('address')
    address_data = Lat_Long_Address(address)
    lat,long = address_data.lat_long()
    sunrise_time = sunrise(lat, long)
    return render_template('sunrise.html', title='sunrise', sunrise_time=sunrise_time)

def sunrise(lat, long):
    '''
    Calls the Sunrise API and returns a time for sunrise
    '''
    tf = TimezoneFinder(in_memory=True)
    longitude = float(long)
    latitude = float(lat)
    lat_long_timezone = tf.timezone_at(lng=longitude, lat=latitude)
    tz = pytz.timezone(lat_long_timezone)
    sunrise = Sunrise_Time(lat, long)
    sunrise_time_zulu = sunrise.sunrise_output()
    print(sunrise_time_zulu)
    today = datetime.date.today().strftime("%Y-%m-%d")
    print(today)
    utc_time = datetime.datetime.strptime(today + " " + sunrise_time_zulu, "%Y-%m-%d %I:%M:%S %p")
    local_time = pytz.utc.localize(utc_time, is_dst=None).astimezone(tz)
    sunrise_time_local = local_time.strftime ("%I:%M:%S %p")
    return sunrise_time_local

