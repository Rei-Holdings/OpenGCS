from processing_py import *
import processing_py as procpy
from serial import *
import time
import tkinter as tk

root = tk.Tk()
height = root.winfo_screenheight()
width = root.winfo_screenwidth()

ver = "v0.0.1 Nightly"

ui = App(width, height)
process_count = 0

# serial read code courtesy of mrExplore on the Arduino Forum!
def readserial(comport, baudrate, timestamp=False):

    ser = Serial(comport, baudrate, timeout=0.1)

    while True:

        data = ser.readline().decode().strip()

        if data and timestamp:
            timestamp = time.strftime('%H:%M:%S')
            return f'{timestamp} > {data}'
        elif data:
            return str(data)
        else:
            return "NULL"


while 1:
    ui.background(0,0,0) # set background:  red, green, blue
    ui.textSize(height/100)
    ui.text(f"OpenGCS Terminal >> {ver}", height-(height-(height/100)), height-(height-(height/60)))
    data = readserial(3, 115200)
    ui.text(str(process_count), height-(height-(height/100))+5, (height-(height-(height/60))+height/100+10))
    process_count+=1
    ui.redraw() # refresh the window