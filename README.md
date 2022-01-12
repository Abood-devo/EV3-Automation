- EV3 autmation project. 
- reach me on twitter: adfd_2

## About 
>The idea behind this project is to make the lego ev3 robot do actions using voice 
>e,g moving forward or even more complex things like measuring a distance between two 
>points this is the initial project (first version) feel free help me to make it better🤞🤞

## Requirements 
> - Speech recognition package

you can install it by running this command
`pip install speechrecognition`

> - PyAudio

Unfortunately the pyaudio package can't be installed using pip IDK why
but you can install it manually by first downloading the `whl` file 
and then running `pip install "whl file name"` for more details visit this [site](https://stackoverflow.com/a/55630212)

## Exiecution steps
>- Exiecute (mainapp.py)
>- Recording audio will start, it keeps recording until you stop talking.
>- Then the audio file will be sent to Google servers to analyze the speech and return text.  
>- Comparing the text with the predefined list of an expected speech.
>- Extracting the ev3brick.py file that contains the instructions for the robot.
>- You can send the file to the brick using bluetooth and run it.

## Sample output
> ![sample output](https://github.com/Abood-devo/EV3-Automation/blob/main/images/sample%20output.png)

**The ev3brick file that the robot should operate after saying 'mr. robot move forward'**

![ev3brick file](https://github.com/Abood-devo/Abood-devo/blob/main/images/output%20file.png)
