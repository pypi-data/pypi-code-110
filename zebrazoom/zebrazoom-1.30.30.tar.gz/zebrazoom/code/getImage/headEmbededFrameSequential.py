from zebrazoom.code.preprocessImage import preprocessImage
import numpy as np
import cv2

def headEmbededFrameSequential(cap, videoPath, frameNumber, hyperparameters):
  
  debug = 0
  
  ret, frame = cap.read()
  
  while not(ret):
    print("WARNING: couldn't read the frameNumber", frameNumber, "for the video", hyperparameters["videoName"])
    frameNumber = frameNumber - 1
    cap.set(1, frameNumber)
    ret, frame = cap.read()
  
  if ("invertBlackWhiteOnImages" in hyperparameters) and hyperparameters["invertBlackWhiteOnImages"]:
    frame = 255 - frame
  
  if ("imagePreProcessMethod" in hyperparameters) and hyperparameters["imagePreProcessMethod"]:
    frame = preprocessImage(frame, hyperparameters)
  
  kernel = np.ones((8,8),np.float32)/25
  thres1  = cv2.filter2D(frame,-1,kernel)
  retval, thres1 = cv2.threshold(thres1, 80, 255, cv2.THRESH_BINARY)
  thres1 = 255 - thres1
  
  frame = 255 - frame
  
  if (debug):
    cv2.imshow('thres1', frame)
    cv2.waitKey(0)
    cv2.imshow('thres1', thres1)
    cv2.waitKey(0)
    
  frame  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  thres1 = cv2.cvtColor(thres1, cv2.COLOR_BGR2GRAY)
  
  return [frame, thres1]
