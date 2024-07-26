import speech_recognition as sr
import pyaudio

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Silence please!")
    print("Speak now:")
    audio=r.listen(source)
    try:
        speech_text=r.recognize_google(audio, language='ta')
        print(speech_text)
    except sr.UnknownValueError:
        print("Couldn't Understand!")
    except sr.RequestError:
        print("Couldn't request result from Google")

