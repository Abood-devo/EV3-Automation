import pyautogui as gc

# print(gc.position())


def project_selector(project_num=0):
    x_cords = [138, 298, 458, 618, 778]
    while True:
        try:
            gc.click(x=x_cords[project_num], y=132, duration=0.2)
            break
        except IndexError:
            project_num = 0
            continue


def lower_pycharm():
    gc.click(x=1838, y=46, duration=0.2)


def project_starer():
    gc.click(x=233, y=381, duration=0.2)


#lower_pycharm()
#project_selector(0)
#project_starer()





expected_speech_2nd_action = ['mr. robot do action 2', 'the robot do action 2', 'robot do action 2', 'do action 2',
                              'go crazy', 1]
for i in range(len(expected_speech_2nd_action)-1):
    print(expected_speech_2nd_action[i])