import cv2
import tkinter as tk
def show_video():
    cap=cv2.VideoCapture(0)
    while True:
       ret,frame=cap.read()
       cv2.imshow('frame',frame)
    cv2.waitKey(1)
# show_video()

def show_window():
    w=['win1','win2','win3']
    n=len(w)
    i=0
    while i<n-1:
        w[i]=tk.Tk()
        w[i].geometry('400x400')
    # w[n].mainloop()
show_window()
