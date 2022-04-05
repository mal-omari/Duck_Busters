# Duck Busters

The duck buster project is part of ECE 471 Duck Hunt Challenge.

The goal of the challenge is to detect and report the location of the ducks in a custom version of Duck Hunt.
Once a duck is found its coordinate location of screen is determined and the duck is shot.

The Duck Buster solution utilizes standard OpenCV libraries plus additional outlier detection. The project is created using python 3.

## Required Files

All files can be found within this repository

1. duck_hunt_main.py
2. solution.py
3. requirements.txt
4. DuckAll.png

## Steps To Run
1. Install Python 3 (Skip if already done)
2. Create Virtual enviroment
3. Install requirements.txt
4. Run duck_hunt_main.py

## Relevent Functions
When running through the terminal, some arguments can be passed to setup the game. Please refer to table below for arguments.
|Command|Name|Description|
|--|--|--|
|-m|Move Type|Setting the type of coordinate. Absolute, Relative, or Manual (Default = Relative)|
|-a|Move Amount|When using relative coordinate, set the delta move amount (Default = 1)|
|-l|Level|Manually set which level to start. (Default = 0)|
|-q|Quiet|No visual output or debugging messages|
|-r|Randomize|Randomize the levels when level = 0|
|-w|Window Size|Override game window size. (Default = 1024x768)|
|-d|Duration|Override level duration|
|-s|Seed|Override randowm seed for reproducability|

## Sources
