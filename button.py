import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
from auto import *
import inspect

CurDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

window = tk.Tk()
# helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Face_Recogniser")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
# answer = messagebox.askquestion(dialog_title, dialog_text)

window.geometry('1450x750')
window.configure(background='medium sea green')

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

message = tk.Label(window, text="NHẬN DIỆN KHUÔN MẶT" ,bg="Green"  ,fg="white"  ,width=50  ,height=3,font=('times', 30))

message.place(x=200, y=20)