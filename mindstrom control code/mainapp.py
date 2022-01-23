import speech_recognition as s_rec
import pyautogui as gc

# The speech that is expected to be said some speech in the lists
# is not relevant it's there to minimize the errors

expected_speechDRAW_A_CIRCLE = ['mr. robot draw circle', "mr. robot throw circle", "robot draw circle",
                                "the robot draw circle", "draw a circle", 0]

expected_speech_2nd_action = ['mr. robot do action 2', 'the robot do action 2', 'robot do action 2', 'do action 2',
                              'go crazy', 1]

expected_speech_3rd_action = ['mr. robot do action 3', 'the robot do action 3', 'robot do action 3', 'do action 3',
                              'go to position a', 2]

expected_speech_4th_action = ['mr. robot do action 4', 'the robot do action 4', 'robot do action 4', 'do action 4',
                              'enable crazy mode', 3]

expected_speech_5th_action = ['mr. robot do action 5', 'the robot do action 5', 'robot do action 5', 'do action 5',
                              'runaway', 4]

expected_speechEXIT = ["mr. robot stop the program", "exit", "close", "exit program", "close program", "stop",
                       "stop program", "shut down", "shut down program", "stop the program"]

# escape sequences used to color the output
end = "\033[0m"
cyan = "\033[36m"
green = "\033[32m"
red = "\033[31m"

# obtain audio from the microphone
reco = s_rec.Recognizer()


# the function that will apply all the mouse actions & and the boolean value fo it will help to not
# go into another list of expected_speech list (faster)
def main(expected_speech, speech):
    condition = comparator(expected_speech, speech)
    if condition:
        project_selector(expected_speech[-1])
        project_starer()
        return condition


# this is the recognizer it recognizes speech using Google Speech Recognition API
def recognizer():
    with s_rec.Microphone() as source:
        print("Speak!")
        audio = reco.adjust_for_ambient_noise(source)
        audio = reco.listen(source)
        print(f"\n{green}got the audio{end}\n")
    try:
        recognized_speech_internal = reco.recognize_google(audio)
        recognized_speech_internal = recognized_speech_internal.lower()
        print(f"{cyan}Recognized Speech: {recognized_speech_internal}{end}")
        return recognized_speech_internal
    except s_rec.UnknownValueError:
        print(f"**{red}Google Speech Recognition could not understand audio{end}**")
    except s_rec.RequestError:
        print(f"**{red}Could not request results from Google Speech Recognition service{end}**")


# this fun is for comparing recognized speech with the expected one to make an action based on the result
def comparator(expected_speech, rec_speech):
    for speech in expected_speech:
        if rec_speech == speech:
            return True
    return False


# used to make decision what project to click on (from 0 to 4) default is 0
def project_selector(project_num=0):
    x_cords = [138, 298, 458, 618, 778]
    gc.click(x=x_cords[project_num], y=132, duration=0.2)


# this methode is used to click on the run button to start the mindstorm project
def project_starer():
    gc.click(x=233, y=381, duration=0.2)


# used to stop the ev3 program if it's endless project by clicking on the stop button on the app interface
def project_stop_action():
    gc.click(x=1879, y=933, duration=0.2)


while True:
    recognized_speech = recognizer()
    try:
        if comparator(expected_speechEXIT, recognized_speech):
            print(f"\n**{red}Speech Stopped{end}**")
            break
        main1 = main(expected_speechDRAW_A_CIRCLE, recognized_speech)
        if main1:
            continue
        main2 = main(expected_speech_2nd_action, recognized_speech)
        if main2:
            continue
        main3 = main(expected_speech_3rd_action, recognized_speech)
        if main3:
            continue
        main4 = main(expected_speech_4th_action, recognized_speech)
        if main4:
            continue
        main5 = main(expected_speech_5th_action, recognized_speech)
        if main5:
            continue
    except:
        continue
