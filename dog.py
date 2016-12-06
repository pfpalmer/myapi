from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os import system
import urllib2
import apiai
import pyaudio
import wave
import time
import json
import sys
import os
import subprocess

import subprocess
#text = '"Hello world"'
#subprocess.call('echo '+text+'|festival --tts', shell=True)

#import pyttsx
#engine = pyttsx.init()
#engine.say('Good morning.')
#engine.runAndWait()


#from AppKit import NSSpeechSynthesizer
#speechSynthesizer = NSSpeechSynthesizer.alloc().initWithVoice_("com.apple.speech.synthesis.voice.Bruce")
#speechSynthesizer.startSpeakingString_('Hi! Nice to meet you!')

# length of data to read.
chunk = 1024

CLIENT_ACCESS_TOKEN = 'fef39795986b4878ad99b41e0ba75572'
DEVELOPER_ACCESS_TOKEN = '3e6f4772719145148f4918628dabebf4'

# this worked to get an output.wav file but not from within this file
#curl -k -H "Authorization: Bearer ACCESS_TOKEN" -H "Accept-language: en-US" "https://api.api.ai/v1/tts?v=20150910&text=managed+object" -o output.wav
#curl -k -H "Authorization: Bearer ACCESS_TOKEN" -H "Accept-language: en-US" "https://api.api.ai/v1/tts?v=20150910&text=managed+object" -o output.wav
#curl  -k -H "Authorization: ACCESS_TOKEN" -H "Accept-language: en-US" "https://api.api.ai/v1/tts?v=20150910&text=managed+object" -o output.wav
#req = urllib2.urllib2.Request(url=https://api.api.ai/v1/tts?v=20150910&text


CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2

#CLIENT_ACCESS_TOKEN = 'fef39795986b4878ad99b41e0ba75572'
#DEVELOPER_ACCESS_TOKEN = '3e6f4772719145148f4918628dabebf4'


def ManagedObject(CreateManagedObject):
   print 'this is the test -pfp-'


def main():
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
    #wf = wave.open(sys.argv[1], 'rb')
    wf = wave.open('output.wav','rb')
    p = pyaudio.PyAudio()
    test = "dog"
    system("say Hello world! Paul is the greatest" + test)

# open stream based on the wave object which has been input.
    stream = p.open(format =
                p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)


# read data (based on the chunk size)
    data = wf.readframes(chunk)

# play stream (looping from beginning of file to the end)
#    while data != '':
#        # writing to the stream is what *actually* plays the sound.
#        stream.write(data)
#        data = wf.readframes(chunk)

# cleanup stuff.
    stream.close()    
    p.terminate()


    while True:
        print "> ", 
        user_message = raw_input()
        if user_message == u"exit":
            break
    
        system("say OK you want me to " + user_message)
 
    request = ai.text_request()

    #request.query = "Create managed Object"
    request.query = "new object"
   # request.query = "delete object"

   # response = request.getresponse()
    response = json.loads(request.getresponse().read())
    print json.dumps(response, indent=4, sort_keys=True)
    #response = json.loads(request.getresponse())
    result = response['result']
    action = result.get('action')
    #actionIncomplete = result.get('actionIncomplete', False)

    if action in ['CreateManagedObject']:
        print "we got a create managed object"


    print "---Action is ---:",action
    print "---Action is ---:",action
    print "---Action is ---:",action
    #print response['result']

    exit


if __name__ == '__main__':
    main()



#driver = webdriver.Chrome()
#driver.get("http://www.python.org")
#driver.get("http://skywarp.tb.arbor.net")
#assert "Python" in driver.title
#assert "Arbor Networks APS" in driver.title
#time.sleep(10)
#elem = driver.find_element_by_name("q")
#elem.clear()
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()
