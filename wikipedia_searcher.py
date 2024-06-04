#used pyttsx3, speechRecognition, pyaudio & wikipedia
#say a name to search for it on wikipedia , say thats it to exit.
import pyttsx3
import speech_recognition as sr
import wikipedia
r=sr.Recognizer()
i=0
while(True):
    try:
        with sr.Microphone() as mic:
            audio=r.listen(mic)
            text=r.recognize_google(audio)
            text.lower()
            print(f"you said : {text}")
            if("that's it" in text):
                print('going to sleep . . .',end='')
                break
            result=wikipedia.summary(text,sentences = 3)
            print(result)
    except Exception as e:
        print(e)
        pass