# Fire Alerts
Using jetson inference to recognize fire.

## Run
Download the folder on a nano with `jetson-inference` and a webcam installed. Run `finalproject.py` with `python3`.

## Algorithm
First it opens the camera feed, then it asks the model, which is a retrained imagenet, if the object on the camera feed is fire. If its fire with a >90% confidence, then it prints "FIRE" out on the console

## Purpose
Helps people detect if there is a fire in their household

## [Video](https://youtu.be/lfhovuwyxOk)
