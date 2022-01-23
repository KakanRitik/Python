#To Run the code We have to install "pip install gTTS"
from gtts import gTTS  #import the google text to speech package
import os # import the operating system module


textFile = open("text.txt","r") #File Handler Variable
textInput1 = "The best way to predict your future is to create it."
textInput2 = textFile.read().replace("\n"," ") #Read the File Handler Variable
language = 'en'


#next we pass the language and the text to the gTTS Engine
output = gTTS(text=textInput1, lang=language, slow=False) # To run textInput2,we have to create .txt,after that we some sentence,so that it will the output.
# output = gTTS(text=textInput2, lang=language, slow=False) #Use with given TExt.txt file.
#Save the output as an mp3 file
output.save("output.mp3")

#Run the output file
os.system("start output.mp3")