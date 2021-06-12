import speech_recognition as sr

def take_command():    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        print("Hiii1")
        audio=r.listen(source)
        print("Hiii2")
    try:
        command=sr.Recognizer().recognize_google(audio,language='en_in')
        print(f"User said : {command}\n")

    except Exception as e:
        print("Say that again please...")
        return ""
    return command

print(take_command())