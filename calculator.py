from flask import Flask, render_template, request
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_distance():
    address1 = request.form['address1']
    address2 = request.form['address2']

    geolocator = Nominatim(user_agent='my-app')
    lat1, lon1, lat2, lon2 = None, None, None, None
    error_messages = []

    if address1:
        location1 = geolocator.geocode(address1)
        if location1:
            lat1 = location1.latitude
            lon1 = location1.longitude
        else:
            error_messages.append('Invalid Address 1')

    if address2:
        location2 = geolocator.geocode(address2)
        if location2:
            lat2 = location2.latitude
            lon2 = location2.longitude
        else:
            error_messages.append('Invalid Address 2')

    return render_template('index.html', address1=address1, address2=address2, lat1=lat1, lon1=lon1, lat2=lat2, lon2=lon2, error_messages=error_messages)

if __name__ == '__main__':
    app.run(debug=True)
