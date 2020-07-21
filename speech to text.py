
import speech_recognition as sr 
import os

mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"

sample_rate = 48000 
chunk_size = 1024 #2048

r = sr.Recognizer() 
mic_list = sr.Microphone.list_microphone_names() 
for i, microphone_name in enumerate(mic_list): 
	if microphone_name == mic_name: 
		device_id = i 
device_id = 1
count=0
while True:
 with sr.Microphone(device_index = device_id, sample_rate = sample_rate,chunk_size = chunk_size) as source: 
        r.adjust_for_ambient_noise(source) 
        print ("Say Something")
        audio = r.listen(source) 
                
        try: 
                text = r.recognize_google(audio) 
                print ("you said: " + text )
                count =1
                break

        except sr.UnknownValueError: 
                print("Speech Recognition could not understand audio") 

        except sr.RequestError as e: 
                print("Could not request results from Googlespeech Recognition service; {0}".format(e))
        if count==1:
                print('hfjhjh')
                
                
                break
 if count==1:
         print('gggg')
         count=0
         break
