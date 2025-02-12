import requests
import json
import streamlit as st

st.title("Weather App 🌤️")

api_key = st.secrets["API_KEY"]
city = st.text_input("Enter city name : ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}"

weather_images = {
    "Clouds": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHQ0Y2c2NGJvY3NlM2trMmFibXppZTA4cXVmaDV5d2dxdGIzbXdqZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VDGOdvmp1bpc3PcCry/giphy.gif",
    "Thunderstorm": "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGlhbmUxYTBtb2IzenV3cmQwbTJrNjgwNXVhYXVod29pcmJwencwZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qRY3cPYRkyQh2/giphy.gif",
    "Drizzle":  "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExenRuY2YxMWp5djUwdzV4NzN3czV0MDkzaDJrbmVyZjBqb3J6eHcybyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l1BgQOc1Jj7L86BA4/giphy.gif",
    "Rain": "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM2lhMXYwc25jM2FwdTN6OWE1ZXNhdWt2bjhkeHp6OHFhcnRlcXJhNCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/U8wCBLhkjNknS/giphy.gif",
    "Snow": "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXdpN3ZsM2Rtdzc4dTdzMDVudjdsN2ZlODZhbjk1a2FyaXA0NmRlcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Qx9PT3PqjXgJj6uFs2/giphy.gif",
    "Clear": "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExMDB6eXE5N24xdjRzZmF5czc2d3M1bG9qbWVrc2o2YjRvbm9yZ2F6aSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fS4cWezsJoXPYzLR45/giphy.gif",
    "Atmosphere": "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdTV1NXhtczVleGdmcjFmbnNuYXJjZ2E1OTVtc3ZvaWQxZ3RmOW52aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xkvwnCSj7B2hApwISX/giphy.gif"
}
try :
    response = requests.get(url)
    data = response.json()
    #prettify_data = json.dumps(data, indent=4)
    if data['cod'] == 200 :
        weather = data['weather'][0]['main']
        icon_id = data["weather"][0]["icon"]
        icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
        description = data['weather'][0]['description']
        lat = data ['coord']["lat"]
        lon = data ['coord']["lon"]
        country_code = data['sys']['country']
        bg_image = weather_images.get(weather)
        st.markdown("<div style='text-align: center;'><h2>Weather in " + city.title() + "</h2></div>", unsafe_allow_html=True)
        st.image(bg_image,use_container_width=True)
        st.write(f"Weather in {city} : ",weather)
        st.image(icon_url)
        st.write(f"Description :",description)
        st.write("Lattitude : ",lat)
        st.write("Longitude : ",lon)
        st.write("Contry code : ",country_code)

except Exception as e:
       st.write("Invalid Input or Data Not found")





