#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3

if __name__ == "__main__":
    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want the robo to speak: ")
        if x.lower() in ["bye", "bii"]:
            engine.say("Thank you, see you later")
            engine.runAndWait()
            break
        engine.say(x)
        engine.runAndWait()


# In[ ]:




