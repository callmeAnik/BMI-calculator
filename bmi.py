import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source: 
        r.adjust_for_ambient_noise(source)
        #r.energy_threshold = 450
        print("Listening...")
        r.pause_threshold = 0.9 
        audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")
        
    except Exception as e:
        #print(e)     
        print("Say that again please...")        
        return "None"    
    return query
if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if 'calculate' in query and ('bmi' in query or ('body' in query and 'mass' in query and 'index' in query)):
            try:
                speak('Enter your height in centimeters')
                Height=float(input("Enter your height in centimeters: "))
                speak('Enter your Weight in Kg')
                Weight=float(input("Enter your Weight in Kg: "))
                Height = Height/100
                BMI=Weight/(Height*Height)
                print(f"your Body Mass Index is: {BMI} kg/m^2")
                speak(f"your Body Mass Index is {BMI} Kg per meter square")
                if(BMI>0):
                    if(BMI<=16):
                        print("you are severely underweight")
                        speak("you are severely underweight")
                    elif(BMI<=18.5):
                        print("you are underweight")
                        speak("you are underweight")
                    elif(BMI<=25):
                        print("you are Healthy")
                        speak("you are Healthy")
                    elif(BMI<=30):
                        print("you are overweight")
                        speak("you are overweight")
                    else:
                        print("you are severely overweight")
                        speak("you are severely overweight")
            except Exception as e:
                #print(e)
                print('invalid details')
                speak('invalid details')