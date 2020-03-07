import tkinter
from urllib.request import urlopen
import json

def print_author():
    info = '''
    Author:     Jakub Jonczyk
    Created at: 8.09.2019
    '''
    print(info)

def load_location(location):
    try:
        with urlopen("https://www.metaweather.com/api/location/search/?query={}".format(location)) as file:
            text = file.read().decode("utf-8")
            object = json.loads(text)
            woeid = object[0]['woeid']
            return woeid
    except:
        print("I cannot find this location, sorry...")

def set_temperature():
    woeid = load_location(pole1.get())
    date = pole0.get()
    with urlopen("https://www.metaweather.com/api/location/{}/{}".format(woeid, date)) as file:
        napis = file.read().decode("utf-8")
        obiekt = json.loads(napis)
        temp = obiekt[0]["the_temp"]
        pole2.configure(text = temp)

def set_air_pressure():
    woeid = load_location(pole1.get())
    date = pole0.get()
    with urlopen("https://www.metaweather.com/api/location/{}/{}".format(woeid, date)) as file:
        napis = file.read().decode("utf-8")
        obiekt = json.loads(napis)#["consolidated_weather"]
        airp = obiekt[0]["air_pressure"]
        pole3.configure(text=airp)

def set_weather_conditions():
    woeid = load_location(pole1.get())
    date = pole0.get()
    with urlopen("https://www.metaweather.com/api/location/{}/{}".format(woeid, date)) as file:
        napis = file.read().decode("utf-8")
        obiekt = json.loads(napis)#["consolidated_weather"]
        weather = obiekt[0]['weather_state_name']
        #return weather
        pole4.configure(text=weather)

print_author()
root = tkinter.Tk()

pole0 = tkinter.Entry(master=root)
pole0.grid(row=0, column=1)
pole1 = tkinter.Entry(master=root)
pole1.grid(row=1, column=1)
pole2 = tkinter.Label(master=root, text="Set date and location to continue...")
pole2.grid(row=2, column=1)
pole3 = tkinter.Label(master=root, text="Set date and location to continue...")
pole3.grid(row=3, column=1)
pole4 = tkinter.Label(master=root, text="Set date and location to continue...")
pole4.grid(row=4, column=1)

napis0 = tkinter.Label(master=root, text="Date [yyyy/mm/dd]: ")
napis0.grid(row=0, column=0)
napis1 = tkinter.Label(master=root, text="Location: ")
napis1.grid(row=1, column=0)
napis2 = tkinter.Button(master=root, text="Check temperature [st. C]", command=set_temperature)
napis2.grid(row=2, column=0)
napis3 = tkinter.Button(master=root, text="Check air pressure [hPa]", command=set_air_pressure)
napis3.grid(row=3, column=0)
napis4 = tkinter.Button(master=root, text="Check weather conditions", command=set_weather_conditions)
napis4.grid(row=4, column=0)

root.mainloop()