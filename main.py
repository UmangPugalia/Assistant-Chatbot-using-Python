    import pyttsx3
    import speech_recognition as sr
    import datetime
    import wikipedia
    import webbrowser
    import os

    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')


    engine.setProperty('voice',voices[0].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()



    def wishMe():  
        hour=int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon")

        else:
            speak("Good Evening!")

        speak("I am Siri. Please tell me how may I help you")

    def takeCommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.energy_threshold = 300
            r.dynamic_energy_threshold = True
            r.pause_threshold = 2.5  
            r.adjust_for_ambient_noise(source, duration=1)  
            audio=r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")

        except Exception as e:
            #print(e)
            print("say that again please...")
            return "None"
        return query


    if __name__=="__main__":
        wishMe()
        while True:
            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results=wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif 'open google' in query:
                webbrowser.open("google.com")
            
            elif 'open spotify' in query:
                webbrowser.open("spotify.com")

            elif 'play bin tere' in query:
                music_dir = 'D:\\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[0]))
            
            elif 'play tere hawale' in query:
                music_dir = 'D:\\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[2]))

            elif 'play vartaman' in query:
                music_dir = 'D:\\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[3]))

            elif 'play ishq hai' in query:
                music_dir = 'D:\\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir,songs[1]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")   
                print(strTime) 
                speak(f"Sir, the time is {strTime}")

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")   
                print(strTime) 
                speak(f"Sir, the time is {strTime}")

            elif 'open code'in query:
                codePath="D:\\umang\\virtual studio code\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)