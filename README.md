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
4. Ensure DuckAll.png is in the same folder, or change the path in duck_hun_main.py
5. Run duck_hunt_main.py

## Relevent Functions
When running through the terminal, some arguments can be passed to setup the game. Please refer to table below for commands.
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
[1] OpenCV. "Introduction to SIFT (Scale-Invariant Feature Transform)". docs.opencv.org. https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html (Accessed April 4, 2022).

[2] OpenCV. "Feature Matching". docs.opencv.org. https://docs.opencv.org/3.4/dc/dc3/tutorial_py_matcher.html(Accessed April 4, 2022).

[3] sr1rsimon. "How to get key points or pixel coordinates of an image from descriptor produced by SIFT algorithm". stackoverflow.com. https://stackoverflow.com/questions/57859836/how-to-get-key-points-or-pixel-coordinates-of-an-image-from-descriptor-produced. (Accessed April 4, 2022).

[4] D. G. Lowe, "Distinctive Image Features from Scale-Invariant Keypoints," International Journal of Computer Vision, vol. 60, (2), pp. 91-110, 2004.

[5] P. Jajodia, “Removing outliers using standard deviation in Python,” KDnuggets. https://www.kdnuggets.com/2017/02/removing-outliers-standard-deviation-python.html. (Accessed April 4, 2022).

[6] OpenCV. "cv::BFMatcher Class Reference". docs.opencv.org. https://docs.opencv.org/3.4/d3/da1/classcv_1_1BFMatcher.html#ac6418c6f87e0e12a88979ea57980c020 (Accessed April 5, 2022).
