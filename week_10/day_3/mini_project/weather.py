from pyowm import OWM
import requests
import json
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pytz
from datetime import datetime, timedelta

r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Tel Aviv,IL&appid=8e23071b08ad49de8690cb6ef17e5651")
weather=r.json()
print("*****TEL AVIV*****")
print("The weather in {} is {}.".format("Tel Aviv",weather["weather"][0]["main"]))
print("The temperature is {}. It feels like {}.".format(weather["main"]["temp"],weather["main"]["feels_like"]))
print("The minimum temperature is {} and the maximum temperature is {}.".format(weather["main"]["temp_min"],weather["main"]["temp_max"]))
print("The time of sunrise is {}, and the time of sunset is {}.".format(weather["sys"]["sunrise"],weather["sys"]["sunset"]))
print("The wind speed is {}. The wind deg is {}.\n\n".format(weather["wind"]["speed"],weather["wind"]["deg"]))

##own=pyom.OWM("8e23071b08ad49de8690cb6ef17e5651")
##mgr=own.weather_manager()
##observation=mgr.weather_at_place("Tel Aviv,IL")
##weather=observation.weather
##print(weather)


with open("city.json","r",encoding='utf-8') as f:
    cities=json.load(f)

user_weather_choice=input("Which city's weather would you like to look up? ")
city_id=""
for i in range(len(cities)):
    if user_weather_choice==cities[i]["name"]:
        city_id=cities[i]["id"]
        break
if city_id=="":
    print("Sorry, that city was not found.")
    sys.exit()

        
appid="8e23071b08ad49de8690cb6ef17e5651"
endpoint="http://api.openweathermap.org/data/2.5/weather?"
params={
    "id":city_id,
    "appid":appid
    }

req=requests.get(endpoint,params=params)
weather_report=req.json()

print("*****{}*****".format(user_weather_choice))
print("The weather in {} is {}.".format(user_weather_choice,weather_report["weather"][0]["main"]))
print("The temperature is {}. It feels like {}.".format(weather_report["main"]["temp"],weather_report["main"]["feels_like"]))
print("The minimum temperature is {} and the maximum temperature is {}.".format(weather_report["main"]["temp_min"],weather_report["main"]["temp_max"]))
print("The time of sunrise is {}, and the time of sunset is {}.".format(weather_report["sys"]["sunrise"],weather_report["sys"]["sunset"]))
print("The wind speed is {}. The wind deg is {}.\n\n".format(weather_report["wind"]["speed"],weather_report["wind"]["deg"]))



user_forecast_choice=input("Which city's forecast would you like to look up? ")
city_forecast_id=""
for i in range(len(cities)):
    if user_forecast_choice==cities[i]["name"]:
        city_forecast_id=cities[i]["id"]
        break
if city_forecast_id=="":
    print("Sorry, that city was not found.")
    sys.exit()

        
appid="8e23071b08ad49de8690cb6ef17e5651"
endpoint="http://api.openweathermap.org/data/2.5/forecast?"
params={
    "id":city_id,
    "appid":appid
    }

request=requests.get(endpoint,params=params)
forecast=request.json()
humidity=[]
for p in range(len(forecast)):
    humidity.append(forecast["list"][p]["main"]["humidity"])
    print("   ****DAY {} FORECAST****".format(p+1))
    print("The weather in {} will be {}.".format(user_forecast_choice,forecast["list"][p]["weather"][0]["main"]))
    print("The temperature will be {}. It will feel like {}.".format(forecast["list"][p]["main"]["temp"],forecast["list"][p]["main"]["feels_like"]))
    print("The minimum temperature will be {} and the maximum temperature will be {}.".format(forecast["list"][p]["main"]["temp_min"],forecast["list"][p]["main"]["temp_max"]))
    print("\n")

##pol = OWM('8e23071b08ad49de8690cb6ef17e5651')
##
### Get latest CO Index on geocoordinates
##pollution=pol.coindex_around_coords(300,1060)
##print(pollution)

tomorrow = datetime.now() + timedelta(days=1)
tomorrow_f = tomorrow.strftime('%d/%m/%Y')

tomorrow1 = datetime.now() + timedelta(days=2)
tomorrow1_f = tomorrow1.strftime('%d/%m/%Y')

tomorrow2 = datetime.now() + timedelta(days=3)
tomorrow2_f = tomorrow2.strftime('%d/%m/%Y')

tomorrow3 = datetime.now() + timedelta(days=4)
tomorrow3_f = tomorrow3.strftime('%d/%m/%Y')

tomorrow4 = datetime.now() + timedelta(days=5)
tomorrow4_f = tomorrow4.strftime('%d/%m/%Y')

labels=[10,20,30,40,50,60,70,80,90,100]

plt.rcdefaults()
fig, ax = plt.subplots()




# Example data
days = (tomorrow_f, tomorrow1_f,tomorrow2_f,tomorrow3_f,tomorrow4_f)
y_pos = np.arange(len(days))

error = np.random.rand(len(days))

ax.barh(y_pos, humidity, xerr=error, align='center')

ax.set_yticks(y_pos)
ax.set_yticklabels(days)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xticks(labels)
ax.set_xticklabels(labels)
ax.set_xlabel('Humidity (%)')
ax.set_title('Humidity Forecast: {}'.format(user_forecast_choice))

rects = ax.patches

# For each bar: Place a label
for rect in rects:
    # Get X and Y placement of label from rect.
    x_value = rect.get_width()
    y_value = rect.get_y() + rect.get_height() / 2

    # Number of points between bar and label. Change to your liking.
    space = 5
    # Vertical alignment for positive values
    ha = 'left'

    # If value of bar is negative: Place label left of bar
    if x_value < 0:
        # Invert space to place label to the left
        space *= -1
        # Horizontally align label at right
        ha = 'right'

    # Use X value as label and format number with one decimal place
    label = "{}".format(x_value)

    # Create annotation
    plt.annotate(
        label,                      # Use `label` as label
        (x_value, y_value),         # Place label at end of the bar
        xytext=(space, 0),          # Horizontally shift label by `space`
        textcoords="offset points", # Interpret `xytext` as offset in points
        va='center',                # Vertically center label
        ha=ha)                      # Horizontally align label differently for
                                    # positive and negative values.
plt.show()
