# Basketball Shot Prediction using OpenCV

## Overview

This project is a computer vision-based application designed to analyze a basketball shot from video footage and predict the trajectory of the ball.

The system uses OpenCV for video processing, object detection, and trajectory tracking. The detected ball positions are used to model the trajectory and determine whether the shot is likely to result in a basket.

## Features

* Basketball detection from video footage
* Real-time/Frame-by-frame video processing
* Color-based object detection
* Contour-based ball localization
* Basketball trajectory tracking
* Polynomial regression for trajectory prediction
* Prediction of whether the shot results in a basket

## Technologies Used

* Python
* OpenCV
* NumPy
* Polynomial Regression
* Computer Vision

## Working Principle

The system processes a basketball video frame by frame.

### 1. Video Input

A video containing a basketball shot is provided as the input to the system.

### 2. Ball Detection

OpenCV-based image processing is used to identify the basketball in each frame.

Color-based detection is applied to isolate the ball from the surrounding environment, followed by contour detection to identify its position.

### 3. Trajectory Tracking

The detected position of the basketball is recorded across successive frames.

These coordinates are used to track the movement of the ball throughout the shot.

### 4. Trajectory Prediction

The collected ball coordinates are used with polynomial regression to approximate the trajectory of the basketball.

The resulting trajectory can then be used to estimate the path of the ball and determine whether it is likely to enter the basket.

## Project Workflow

```text
Video Input
     ↓
Frame Extraction
     ↓
Color-Based Ball Detection
     ↓
Contour Detection
     ↓
Ball Position Tracking
     ↓
Trajectory Data
     ↓
Polynomial Regression
     ↓
Trajectory Prediction
     ↓
Shot Result Prediction
```

## Example Output

The system tracks the basketball throughout the shot and generates a predicted trajectory based on the detected ball coordinates.

The output can be visualized by overlaying the detected trajectory and predicted path on the video frames.

## What I Learned

Through this project, I gained practical experience in:

* Python programming
* OpenCV and computer vision
* Video and image processing
* Object detection using color and contours
* Coordinate tracking
* Data fitting using polynomial regression
* Converting visual data into useful predictions

## Future Improvements

Possible improvements include:

* Using deep-learning-based object detection for more robust basketball detection
* Improving trajectory prediction under different lighting conditions
* Supporting multiple camera angles
* Estimating shot accuracy over a larger dataset
* Adding automatic detection of the hoop
* Developing a real-time camera-based version

## Author

**Jayesh Kumar**
B.Tech – Electronics and Communication Engineering
SRM University-AP
