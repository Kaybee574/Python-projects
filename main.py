import folium
import phonenumbers
from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder, carrier

# Assuming 'number' is your South African phone number in string format
number = "+27656455536"  # replace with your number

try:
    pepnumber = phonenumbers.parse(number, "ZA")
    location = geocoder.description_for_number(pepnumber, "en")
    print(location)

    service_pro = carrier.name_for_number(pepnumber, "en")
    print(service_pro)

    key = "cf10288cb45c45f2a88faaa024d2805c"  # your OpenCage API Key
    geocoder = OpenCageGeocode(key)
    query = str(location)
    results = geocoder.geocode(query)

    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']

    print(lat, lng)

    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)

    myMap.save("mylocation.html")
except Exception as e:
    print(f"An error occurred: {e}")
