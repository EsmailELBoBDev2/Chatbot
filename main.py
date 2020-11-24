import webbrowser
import time 
import vlc ## pip3.8 install python-vlc
import random
import adventure
import subprocess
import requests
import json 

print("Hello My name is --- I'm a still new personal assistant bot so i'm still limited, however i'm able to do stuff like search `search about 'something'` and search in wiki about stuff `search in wiki about 'something'` and make appointments `Make an appointment`\n")

def process():
    usrCMD = input("How i may help you today? — Type 'exit' to leave: \n> ")

    if usrCMD.lower() == 'exit':
        exit()
    elif "search" in usrCMD.lower():
        search()
    elif "timer" in usrCMD.lower():
        timer()    
    elif "joke" in usrCMD.lower():
        joke()
    elif "fun fact" in usrCMD.lower() or "fun facts" in usrCMD.lower():
        fact()
    elif "game" in usrCMD.lower():
        game()
    elif "weather" in usrCMD.lower():
        weather()
    else:
        print("Something went wrong, check typo!")
        exit()


## NEEDS webbrowser lib
def search():
    print("\n")
    query = input("What do you want to search about: ")
    webbrowser.get('chromium').open('https://duckduckgo.com/?q=' + query)
    print("Opened the browser and searching about " + query)
    print("\n\n")

## NEEDS time, vlc lib
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
# https://stackoverflow.com/a/25899180
def timer():
    print("\n")
    def countdown(t): 
        while t: 
            mins, secs = divmod(t, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs) 
            print(timer, end="\r") 
            time.sleep(1) 
            t -= 1
        p = vlc.MediaPlayer("/home/esmailelbob/Desktop/smartbot/src/timer.mp3")
        p.play()
        print('Times up!!') 
    # input time in seconds 
    t = input("Enter the time in seconds: ") 
    # function call 
    countdown(int(t)) 
    print("\n\n")

## NEEDS random lib
def joke():
    print("\n")
    jokes_list = ["What’s the best thing about Switzerland?\nI don’t know, but the flag is a big plus", "I invented a new word!\nPlagiarism", "Did you hear about the mathematician who’s afraid of negative numbers?\nHe’ll stop at nothing to avoid them", "Why do we tell actors to “break a leg?”\nBecause every play has a cast."] ## https://www.rd.com/list/short-jokes/
    n = random.randint(1, len(jokes_list))
    print(jokes_list[n])
    print("\n\n")

## NEEDS random lib
def fact():
    print("\n")
    fact_list = ["Banging your head against a wall for one hour burns 150 calories.", "In Switzerland it is illegal to own just one guinea pig.", "Pteronophobia is the fear of being tickled by feathers.", "Snakes can help predict earthquakes."] ## https://www.thefactsite.com/top-100-random-funny-facts/
    n = random.randint(1, len(fact_list))
    print(fact_list[n])
    print("\n\n")

## NEEDS adventure, subprocess lib
def game():
    print("\n")
    print("This game by: https://pypi.org/project/adventure/, If you want to leave simply close the terminal window or press `CTRL + C` Button. Press Enter to continue!")
    input()
    subprocess.Popen( ["xfce4-terminal", "-e", "python3.8 -m adventure" ])
    print("\n\n")

## NEEDS requests, json lib
## https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
def weather():
    print("\n")
    api_key = "69b5c90fdc873b3a73b25f5e3f16f1a3"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = input("Enter city name : ") 
    
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    # print(complete_url)

    response = requests.get(complete_url) 
    
    x = response.json() 
    
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        current_pressure = y["pressure"] 
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 
        print(" Temperature (in Celsius unit) = ~" +
        ## https://www.rapidtables.com/convert/temperature/kelvin-to-celsius.html
                        str(int(current_temperature - 273.15)) + 
            "\n atmospheric pressure (in hPa unit) = ~" +
                        str(current_pressure) +
            "\n humidity (in percentage) = ~" +
                        str(current_humidiy) +
            "\n description = " +
                        str(weather_description)) 
    else: 
        print(" City Not Found ") 
    print("\n\n")

while True:
    process()

    
