import speech_recognition as speechrec

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
                       

# escape sequences used to color the output
end = "\033[0m"
cyan = "\033[36m"
green = "\033[32m"
red = "\033[31m"

# obtain audio from the microphone
reco = speechrec.Recognizer()


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
with speechrec.Microphone() as source:
    print("Speak!")
    audio = reco.adjust_for_ambient_noise(source)
    audio = reco.listen(source)
    print(f"\n{green}got the audio{end}\n")
try:
    recognized_speech = reco.recognize_google(audio)
    recognized_speech = recognized_speech.lower()
    print(f"{cyan}Recognized Speech: {recognized_speech}{end}")

except speechrec.UnknownValueError:
    print(f"**{red}Google Speech Recognition could not understand audio{end}**")
except speechrec.RequestError as e:
    print(f"**{red}Could not request results from Google Speech Recognition service{end}**")
