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

# serial read code courtesy of mrExplore on the Arduino Forum, edited to program needs and expanded
def readserial(baudrate, timestamp=False):
    try:
        ser1 = Serial('COM1', baudrate, timeout=0.1)
    except:
        ser1 = None
    
    try:
        ser2 = Serial('COM2', baudrate, timeout=0.1)
    except:
        ser2 = None

    try:
        ser3 = Serial('COM3', baudrate, timeout=0.1)
    except:
        ser3 = None

    try:
        ser4 = Serial('COM4', baudrate, timeout=0.1)
    except:
        ser4 = None

    while True:

        if ser1 != None: 
            data1 = ser1.readline().decode().strip() 
        else: 
            data1 = None
        if ser2 != None: 
            data2 = ser2.readline().decode().strip()
        else:
            data2 = None
        if ser3 != None: 
            data3 = ser3.readline().decode().strip()
        else:
            data3 = None
        if ser4 != None: 
            data4 = ser4.readline().decode().strip()
        else:
            data4 = None

        if data1 or data2 or data3 or data4 and timestamp:
            timestamp = time.strftime('%H:%M:%S')
            return f'{timestamp} > {data1}', f'{timestamp} > {data2}', f'{timestamp} > {data3}', f'{timestamp} > {data4}'
        elif data1 or data2 or data3 or data4:
            return str(data1), str(data2), str(data3), str(data4)
        else:
            return "COM1 OFFLINE", "COM2 OFFLINE", "COM3 OFFLINE", "COM4 OFFLINE"



while 1:
    ui.background(0,0,0) # set background:  red, green, blue
    ui.textSize(height/100)
    ui.text(f"OpenGCS Terminal >> {ver}", height-(height-(height/100)), height-(height-(height/60)))
    data1, data2, data3, data4 = readserial(250000)
    ui.text(str(data1), height-(height-(height/100)), (height-(height-(height/60))+height/100+10))
    ui.text(str(data2), height-(height-(height/100)), (height-(height-(height/60))+height/100+20))
    ui.text(str(data3), height-(height-(height/100)), (height-(height-(height/60))+height/100+30))
    ui.text(str(data4), height-(height-(height/100)), (height-(height-(height/60))+height/100+40))
    process_count+=1
    ui.redraw() # refresh the window