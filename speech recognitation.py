import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source and listening to the speech
with sr.Microphone() as source:
    print("Talk")
    # Adjust for ambient noise and record audio
    r.adjust_for_ambient_noise(source)
    audio_text = r.listen(source)
    print("Time over, thanks")

    try:
        # Using Google Speech Recognition to convert audio to text
        print("Text: " + r.recognize_google(audio_text))
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio")
    except sr.RequestError:
        print("Sorry, the service is down")
