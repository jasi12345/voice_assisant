import json
import cv2
import speech_recognition as sr
import pyttsx3
import threading
import os
import google.generativeai as genai

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

with open('config.json')as f:
    config=json.load(f)

key=config['api_key']

genai.configure(api_key=key)

model=genai.GenerativeModel("gemini-2.0-flash")

def speak(txt):
    engine.say(txt)
    engine.runAndWait()

def recognize_speech():
    recognizer=sr.Recognizer()

    with sr.Microphone() as source:
        while True:
            print("Listening for a query...")
            recognizer.adjust_for_ambient_noise(source)

            try:
                audio=recognizer.listen(source)
                text=recognizer.recognize_google(audio).lower()
                print(f"User said: {text}")


                if "exit" in text or "stop" in text:
                    speak("Good bye!")
                    os._exit(0)

                
                response=get_ai_response(text)
                speak(response)


            except sr.UnknownValueError:
                speak("Sorry,I don't catch that")

            except sr.RequestError:
                speak("Error connecting to speech recognition service")


def open_continous_video(video_path,frame_delay=100):
    if not os.path.exists(video_path):
        speak("Video not found.Exiting")
        os._exit(0)

    video=cv2.VideoCapture(video_path)

    if not video.isOpened():
        speak("Error opening video file. Exiting")
        os._exit(0)

    while True:
        ret,frame=video.read()

        if not ret:
            video.set(cv2.CAP_PROP_POS_FRAMES,0)
            continue

        cv2.imshow("playing video",frame)


        if cv2.waitKey(frame_delay) & 0xFF ==ord('q'):
            break

    video.release()

    cv2.destroyAllWindows()

def get_ai_response(query):
    response=model.generate_content(query)
    return response.text if response else "I'm sorry, I couldn't process that "

video_path="newth.mp4"

speech_thread=threading.Thread(target=recognize_speech,daemon=True)
speech_thread.start()

open_continous_video(video_path,frame_delay=100)










