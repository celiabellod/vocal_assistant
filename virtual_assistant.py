#Description : This is a virtual assistant program that gets the date, the current time, responds back with a random greeting, and returns information on a person

#pip install pyaudio
#pip install SpeechRecognition
#pip install gTTS
#pip install wikipedia


#Import the libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia


#ignore any warning message
warnings.filterwarnings('ignore')

# Record audio and return it as a string
def recordAudio():

    #record the audio
    r = sr.Recognizer() #creating a recognizer object

    #Open the microphone and start recording
    with sr.Microphone() as source:
        print('Dit quelques choses!')
        audio = r.listen(source)

    #Use Googles speech recognition
    data = ''
    try:
        data = r.recognize_google(audio)
        print('You said :'+data)
    except sr.UnknownValueError: #Check for unknown errors
        print('Google Speech Recognition could not understand the audio, unknow error')
    except sr.RequestError as e: #Check for unknown errors
        print('Request results from Google Speech Recognition service error ' + e)

    return data

#A function to get the virtual assistant response
def assistantResponse(text):
    print(text)

    #convert the text to speech
    myobj = gTTS(text=text, lang='fr-FR', slow=False)

    #save the converted audio to a file
    myobj.save('assistant_response.mp3')

    #Play the converted file
    os.system('start assistant_response.mp3')


#A function for wake words or phrase
def wakeWord(text):
    WAKE_WORDS = ['bonjour ava', 'okay ava', 'salut ava']
    text = text.lower()

    #Check to see if the users command/text contains a wake word/phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    #If the wake word isn't found in the text from the loop and so it returns False
    return False

#A function to get the current date
def getDate():

    now = datetime.datetime.now()
    weekday = calendar.day_name[now.weekday()] #e.g Friday
    dayNum = now.day
    monthName  = calendar.month_name[now.weekday()]
    yearNum = now.year

    return 'Aujourd\'hui nous sommes le'  + dayNum + ' ' + weekday + ' ' + monthName + ' ' + str(yearNum) + '.'


#A function to return a radom greeting response
def greeting(text):
    #Greeting inputs
    GREETING_INPUTS = ['salut', 'bonjour']

    # Greeting response
    GREETING_RESPONSES = ['Bonjour celia', 'Salut celia']

    #If the users input is a greeting, then return a randomlu chosen greeting response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

    #If no greeting was detected then return an empty string
    return ''

#A function to get a persons first and last name from the text
def getPerson(text):
    wordList = text.split() #splitting the text into a list of words

    for i in range(0, len(wordList)):
        if i+3 <= len(wordList) - 1 and wordList[i].lower() == 'qui' and wordList[i+1].lower() == 'est':
            return wordList[i+2] + ' ' + wordList[i+3]




while True:

    text = recordAudio()
    response = ''

    #Check for the word/phrase
    if(wakeWord(text) == True):
        #Check for greetings by the user
        response = response + greeting(text)

        #Check to see if the user said anything having to do with the date
        if('jour' in text):
            get_date = getDate()
            response = response + ' ' + get_date

        if('heure' in text):
            now = datetime.datetime.now()

            response = response + ' ' + 'il est' + str(hour) + ':' + minute + ' '+meridiem+'.'

        #Check to see if the user say 'who is'
        if('qui est' in text):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki


        #Have the assistant response back using audio and the text from response
        assistantResponse(response)