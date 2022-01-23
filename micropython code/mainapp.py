import speech_recognition as s_rec
import os

# The speech that is expected to be said some speech in the lists
# is not relevant it's there to minimize the errors
expected_speechSAY_SOMETHING = ["mr. robot say something", "say something", "mr robert say something",
                                "the robot say something", "robert say something", "robot say something",
                                "it's a robot say something", "the rabbit say something"]

expected_speechMOVE_FORWARD = ["mr. robot move forward", "move forward", "mr robert move forward",
                               "the robot move forward", "robert move forward", "robot move forward"]

expected_speechMOVE_BACKWARD = ["mr. robot move backward", "move backward", "mr robert move backward",
                                "the robot move backward", "robert move backward", "robot move backward",
                                "more backwards", "move backwards", "mr. robot moves backward"]

expected_speechROTATE_RIGHT = ["mr. robot rotate right", "rotate right", "mr robert rotate right",
                               "the robot rotate right", "robert rotate right", "robot rotate right",
                               "rotate to the right", "mr. robot rotate to the right"]

expected_speechROTATE_LEFT = ["mr. robot rotate left", "rotate left", "the robot rotate left",
                              "mr robert rotate left", "robot rotate left", "robert rotate left",
                              "the robot rotate left", "rotate to the left", "mr. robot rotate to the left",
                              "the robot rotate to the left"]

expected_speechEXIT = ["mr. robot stop the program", "exit", "close", "exit program", "close program", "stop",
                       "stop program", "shut down", "shut down program", "stop the program"]
                       

# this is the set of codes that the robot going to execute
instructionsSAY_SOMETHONG = open("say_something.py", 'r').read()
instructionsMOVE_FORWARD = open("move_forward.py", 'r').read()
instructionsMOVE_BACKWARD = open("move_backward.py", 'r').read()
instructionsROTATE_RIGHT = open("rotate_right.py", 'r').read()
instructionsROTATE_LEFT = open("rotate_left.py", 'r').read()
ev3_pyfile = 'ev3brick.py'
stop_condition = True

# escape sequences used to color the output
end = "\033[0m"
cyan = "\033[36m"
green = "\033[32m"
red = "\033[31m"

# obtain audio from the microphone
reco = s_rec.Recognizer()


# the usage of this fun is to open the file and write in it the proper script
def instructions_creator(py_file_path, code):
    py_file = open(py_file_path, 'x')
    py_file.write(code)
    print(f"{green}\nthe ev3brick.py file is successfully extracted{end}")
    py_file.close()


def comparator(expected_speech, rec_speech, instructions):
    for speech in expected_speech:
        if rec_speech == speech:
            instructions_creator('ev3brick.py', instructions)


# recognize speech using Google Speech Recognition
while stop_condition:
    with s_rec.Microphone() as source:
        print("Speak!")
        audio = reco.adjust_for_ambient_noise(source)
        audio = reco.listen(source)
        print(f"\n{green}got the audio{end}\n")
    try:
        recognized_speech = reco.recognize_google(audio)
        recognized_speech = recognized_speech.lower()
        print(f"{cyan}Recognized Speech: {recognized_speech}{end}")

    except s_rec.UnknownValueError:
        print(f"**{red}Google Speech Recognition could not understand audio{end}**")
        continue
    except s_rec.RequestError:
        print(f"**{red}Could not request results from Google Speech Recognition service{end}**")

    # loop for comparing the recognized speech and making the decision
    # of what instruction should be extracted for the robot
    try:
        for speech in expected_speechEXIT:
            if recognized_speech == speech:
                print(f"\n**{red}the program has been stopped{end}**")
                stop_condition = False
    except NameError:
        continue
    while True:
        try:
            comparator(expected_speechSAY_SOMETHING, recognized_speech, instructionsSAY_SOMETHONG)
            comparator(expected_speechMOVE_FORWARD, recognized_speech, instructionsMOVE_FORWARD)
            comparator(expected_speechMOVE_BACKWARD, recognized_speech, instructionsMOVE_BACKWARD)
            comparator(expected_speechROTATE_RIGHT, recognized_speech, instructionsROTATE_RIGHT)
            comparator(expected_speechROTATE_LEFT, recognized_speech, instructionsROTATE_LEFT)
            break
        except NameError:
            break
        except FileExistsError:
            os.remove(ev3_pyfile)
            continue
