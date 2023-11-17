#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import json
import pyttsx3
city=input("Enter the city")
url=f"http://api.weatherapi.com/v1/current.json?key=3680764057ad489bb90135932231711&q={city}&aqi=no"
data=requests.get(url)

wdic=json.loads(data.text)
print(wdic)

temperature=wdic["current"]["temp_c"]
condit=wdic["current"]["condition"]["text"]
engine=pyttsx3.init()
engine.say(f"The temperature in {city} is {temperature} degree celsius")
engine.runAndWait()
engine.say(f"The condition in {city} is {condit}")
engine.runAndWait()


# In[ ]:




