import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
import pyttsx3
import time
import beepy
from gtts import gTTS
from selenium import webdriver



url ='https://www.drsikora.com/appointments.html'

def scrape(url):
    data = requests.get(url)

    #try:
        #print(data.text)
    #except:
        #print("Not found")

    soup = BeautifulSoup(data.text, 'html5lib')

    name = soup.find("div", {"id": "formdiv"})

    form = name.form

    listOfElements = []
    for p in form.find_all("p"):
        if ':' in p.text:
            text = p.text.split(':')
            listOfElements.append(text[0])

    return listOfElements

def SpeechRecognizer():
    import speech_recognition as sr
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as src:
            r.adjust_for_ambient_noise(src)
            audio = r.listen(src)
            text = r.recognize_google(audio)
    return text

information = scrape(url)
#print(information)

listOfInput = []

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
def SpeakText(command):

    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        listOfInput.append(query)
        print(f"User said: {query}\n")
        return query

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    #return query
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="/Users/parvbhardwaj/Desktop/chromedriver")
driver.get("https://www.drsikora.com/appointments.html")
time.sleep(1)
SpeakText("Are you a new patient?")
takeCommand()
if(listOfInput[0] == "yes"):
    button = driver.find_element_by_id("1_type_0")
    button.click()
    time.sleep(1)

else:
    button = driver.find_element_by_id("1_type_1")
    button.click()
    time.sleep(1)

for item in information:
    print(item)
    SpeakText(item)
    takeCommand()
print(scrape(url))
stringEmail = listOfInput[2]
stringEmail = stringEmail.replace("at" , "@")
stringEmail = stringEmail.replace(" " , "")
listOfInput[2] = stringEmail.lower()
#print(stringEmail)
print(listOfInput)


time.sleep(1)

time.sleep(1)
driver.find_element_by_name("2_fullname").send_keys(listOfInput[1])
time.sleep(1)
driver.find_element_by_name("3_email").send_keys(listOfInput[2])
time.sleep(1)
driver.find_element_by_name("4_phone").send_keys(listOfInput[3])
time.sleep(1)
driver.find_element_by_name("5_nature").send_keys(listOfInput[4])
time.sleep(1)
driver.find_element_by_name("6_days").send_keys(listOfInput[5])
time.sleep(1)
driver.find_element_by_name("7_times").send_keys(listOfInput[6])

time.sleep(1)
submitButton = driver.find_element_by_id("imagefield3")
submitButton.click()
time.sleep(10)
"""
How to configure this python file on your machine for testing:
    1.Install the required pacakges(written on the top of this file)
    2.The webdriver version should be in the same folder as the file to prevent any
    crashes. The webdriver version should also be the same version used by Chrome
INFO about the video recored:
The printed commands like listening, recognizing and some data printed is
for testing purposes only and it will be removed in the file version of this software

NOTE; As of march 20 4:52AM this software executes successfully without any errors
if for some reason the code breaks while you're testing it. Please reach out to
us at: axk1312@case.edu, pxb410@case.edu, gbk29@case.edu or sxc1514@case.edu
"""

