#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
import cv2
import time
import numpy as np

capture_duration = 4
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    # Record Audio
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        # Speech recognition using Google Speech Recognition
        try:

            print("You said: " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    # The duration in seconds of the video captured

    start_time = time.time()
    cap = cv2.VideoCapture(0)

    while(int(time.time() - start_time) < capture_duration):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here

        # Display the resulting frame
        cv2.putText(frame,r.recognize_google(audio) , (22, 34), font, 1, (200, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()