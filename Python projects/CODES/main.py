#from keras.models import load_model
import cv2 
import numpy as np
from tkinter import *
from PIL import Image as Img
from PIL import ImageTk
import RPi.GPIO as GPIO
import pigpio
import time
import serial
import os
import threading
from keras.models import load_model
os.system("sudo pigpiod")


# PINOUTS ~~~~~~~~~~~~~~~~~~~
relayPin1 = 21
relayPin2 = 20
irsensor1 = 13
irsensor2 = 6


servo1 = 19
servo2 = 2

# VARIABLES ~~~~~~~~~~~~~~~~~
processflag = 0


# S E T U P ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



model = load_model("keras_model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup (relayPin1, GPIO.OUT)
GPIO.output(relayPin1, GPIO.HIGH)

GPIO.setup (relayPin2, GPIO.OUT)
GPIO.output(relayPin2, GPIO.HIGH)

GPIO.setup(irsensor1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(irsensor2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pwm1 = pigpio.pi()
pwm2 = pigpio.pi()

pwm2.set_mode(servo1, pigpio.OUTPUT)
pwm2.set_mode(servo2, pigpio.OUTPUT)

pwm1.set_PWM_frequency( servo1, 50 )
pwm2.set_PWM_frequency( servo2, 50 )

webCam = cv2.VideoCapture(0)

pwm1.set_servo_pulsewidth( servo1, 570 )
pwm2.set_servo_pulsewidth( servo2, 570 )

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1) #RPi ~~~~~~~~~~
ser.reset_input_buffer()

class BananaApp(Tk):
     def __init__(self, *args, **kwargs):
          Tk.__init__(self, *args, **kwargs)
          
          container = Frame(self)
          container.pack(side="top", fill="both", expand=True)
          container.grid_rowconfigure(0, weight=1)
          container.grid_columnconfigure(0, weight=1)
          
          self.frames = {}
          for F in (SplashScreen, Main):      # FRAME ~~~~~~~~~~
               page_name = F.__name__
               frame = F(parent=container, controller=self)
               self.frames[page_name] = frame
               frame.grid(row=0, column=0, sticky="nsew")


          self.show_frame("Main")

     def show_frame(self, page_name):
          frame = self.frames[page_name]
          frame.tkraise()


class SplashScreen(Frame):
     def __init__(self, parent, controller):
          Frame.__init__(self, parent)
          self.controller = controller


class Main(Frame):
     def __init__(self, parent, controller):
          global camView
          global txtviolet, txtindigo, txtblue, txtcyan, txtgreen, txtyellow, txtorange1, txtorange2, txtred1, txtred2, txtred3
          global txtniroutput, txtcamoutput
          
          Frame.__init__(self, parent)
          self.controller = controller

          def processfunc () :
               global processflag
               processflag = 1

          camView = Label(self, bg = "skyblue")
          camView.place(x = 130, y = 10)

          Label(self, text = "CAMERA DETECTION : ", font = ('', 15)).place(x=130,y=320)
          txtcamoutput = Label(self, text = " ", font = ('', 15))
          txtcamoutput.place(x=130,y=345)

          Label(self, text = "VIOLET : ", font = ('', 15)).place(x=450,y=50)
          Label(self, text = "INDIGO : ", font = ('', 15)).place(x=450,y=80)
          Label(self, text = "BLUE : ", font = ('', 15)).place(x=450,y=110)
          Label(self, text = "CYAN : ", font = ('', 15)).place(x=450,y=140)
          Label(self, text = "GREEN : ", font = ('', 15)).place(x=450,y=170)
          Label(self, text = "YELLOW : ", font = ('', 15)).place(x=450,y=200)
          Label(self, text = "ORANGE : ", font = ('', 15)).place(x=450,y=230)

          txtviolet = Label(self, text = "0", font = ('', 15))
          txtviolet.place(x=600,y=50)

          txtindigo = Label(self, text = "0", font = ('', 15))
          txtindigo.place(x=600,y=80)

          txtblue = Label(self, text = "0", font = ('', 15))
          txtblue.place(x=600,y=110)

          txtcyan = Label(self, text = "0", font = ('', 15))
          txtcyan.place(x=600,y=140)

          
          txtyellow = Label(self, text = "0", font = ('', 15))
          txtyellow.place(x=600,y=200)

          txtorange = Label(self, text = "0", font = ('', 15))
          txtorange.place(x=600,y=230)


          # LABELS

          datac = Canvas(self, bg='white')
          #
          Label(datac, text = "CHLOROPHYLL : ", font = ('', 15), bg='white').place(x=10,y=10)
          Label(datac, text = "G: ", font = ('', 15), bg='white').place(x=10,y=35)
          txtgreen = Label(datac, text = "0", font = ('', 15), bg='white',fg='green')
          txtgreen.place(x=40,y=35)
          #
          Label(datac, text = "CAROTENOIDS : ", font = ('', 15), bg='white').place(x=10,y=60)
          Label(datac, text = "R: ", font = ('', 15), bg='white').place(x=10,y=85)
          Label(datac, text = "O: ", font = ('', 15), bg='white').place(x=100,y=85)
          
          txtred1 = Label(datac, text = "0", font = ('', 15), bg='white',fg='red')
          txtred1.place(x=40,y=85)
          txtorange1 = Label(datac, text = "0", font = ('', 15), bg='white',fg='orange')
          txtorange1.place(x=130,y=85)
          #
          Label(datac, text = "SUGAR INDEX : ", font = ('', 15), bg='white').place(x=10,y=110)
          Label(datac, text = "R: ", font = ('', 15), bg='white').place(x=10,y=135)
          Label(datac, text = "P: ", font = ('', 15), bg='white').place(x=100,y=135)
          Label(datac, text = "B: ", font = ('', 15), bg='white').place(x=190,y=135)

          txtred2 = Label(datac, text = "0", font = ('', 15), bg='white',fg='red')
          txtred2.place(x=40,y=135)
          txtviolet = Label(datac, text = "0", font = ('', 15), bg='white',fg='purple')
          txtviolet.place(x=130,y=135)
          txtblue = Label(datac, text = "0", font = ('', 15), bg='white',fg='blue')
          txtblue.place(x=220,y=135)
          #
          Label(datac, text = "STARCH INDEX : ", font = ('', 15), bg='white').place(x=10,y=160)
          Label(datac, text = "Y: ", font = ('', 15), bg='white').place(x=10,y=185)
          Label(datac, text = "O: ", font = ('', 15), bg='white').place(x=100,y=185)
          Label(datac, text = "R: ", font = ('', 15), bg='white').place(x=190,y=185)

          txtyellow = Label(datac, text = "0", font = ('', 15), bg='white',fg='yellow')
          txtyellow.place(x=40,y=185)
          txtorange2 = Label(datac, text = "0", font = ('', 15), bg='white',fg='orange')
          txtorange2.place(x=130,y=185)
          txtred3 = Label(datac, text = "0", font = ('', 15), bg='white',fg='red')
          txtred3.place(x=220,y=185)
          
          datac.place(x = 450, y = 50, h = 230, w=280)

          Label(self, text = "NIR DETECTION : ", font = ('', 15)).place(x=450,y=320)
          txtniroutput = Label(self, text = "", font = ('', 15))
          txtniroutput.place(x=450,y=345)

          btnprocess = Button(self, text = "PROCESS", font = ("", 20), bg= 'skyblue',
                              command = processfunc)
          btnprocess.place(x = 320, y = 370)
          

def showcam () :

    global camView
    global processflag
    global txtniroutput, txtcamoutput
    global data1, data2, data3, data4, data5, data6, data7, data8


    camx = 100
    camy = 90
    camw = 250
    camh = 490

    
    _, frame = webCam.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rotatecam = cv2.rotate(rgb, cv2.ROTATE_90_CLOCKWISE)
    cv2.rectangle(rotatecam,(camx,camy),(camx+camw,camy+camh),(0,255,0),1)
    
    finalcam = rotatecam[camy+1 : camy + camh, camx+1 : camx + camw]
    finalcam = cv2.resize(finalcam, (200, 300)) 

    img = Img.fromarray(finalcam)
    imgtk = ImageTk.PhotoImage(image=img)
    camView.imgtk = imgtk
    camView.configure(image=imgtk)

    if (processflag == 1) :
         processflag = 0
         image = cv2.resize(finalcam, (224, 224), interpolation=cv2.INTER_AREA)
         image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

         # Normalize the image array
         image = (image / 127.5) - 1

         # Predicts the model
         prediction = model.predict(image)
         index = np.argmax(prediction)
         class_name = class_names[index]
         confidence_score = prediction[0][index]

         # Print prediction and confidence score
         print("Class:", class_name[2:], end="")
         print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
         camout = str(class_name[2:])
         txtcamoutput.config(text = camout)

         
         
         GPIO.output(relayPin1, GPIO.LOW)
         GPIO.output(relayPin2, GPIO.LOW)
         while True:
               print(camout)
               if (str(camout).rstrip() == 'RIPE') :
                    txtniroutput.config(text = " ")
                    time.sleep(8)
                    GPIO.output(relayPin1, GPIO.HIGH)
                    GPIO.output(relayPin2, GPIO.HIGH)
                    processflag = 0
                    break;
                    
               else :
                    if (int(data4) <= 100) :
                         txtniroutput.config(text = "BIOFUEL")
                         if GPIO.input(irsensor1) == GPIO.LOW:
                             GPIO.output(relayPin1, GPIO.HIGH)
                             GPIO.output(relayPin2, GPIO.HIGH)
                             time.sleep(0.5)
                             pwm1.set_servo_pulsewidth( servo1, 1200 )
                             time.sleep(1)
                             pwm1.set_servo_pulsewidth( servo1, 570 )
                             break;

                    else :
                         if (int(data7) >= 101) :
                              if GPIO.input(irsensor2) == GPIO.LOW:
                                   txtniroutput.config(text = "FERTILIZER")
                                   GPIO.output(relayPin1, GPIO.HIGH)
                                   GPIO.output(relayPin2, GPIO.HIGH)
                                   time.sleep(0.5)
                                   pwm2.set_servo_pulsewidth( servo2, 1200 )
                                   time.sleep(1)
                                   pwm2.set_servo_pulsewidth( servo2, 570 )
                                   break;


                         
         

    app.after(5, showcam)

class arduinodata(threading.Thread):
     def __init__(self):
         super(arduinodata, self).__init__()
         self.setDaemon(True)

     def run(self):
          
          global txtviolet, txtindigo, txtblue, txtcyan, txtgreen, txtyellow, txtorange1, txtorange2, txtred1, txtred2, txtred3
          global data1, data2, data3, data4, data5, data6, data7, data8
          while True:
               
               try :
                    line = ser.readline().decode('utf-8').rstrip()
                    #print(line)
                    data = line.split(",")
                    data1 = data[0]
                    data2 = data[1]
                    data3 = data[2]
                    data4 = data[3]
                    data5 = data[4]
                    data6 = data[5]
                    data7 = data[6]
                    data8 = data[7]
                    
                    txtviolet.config(text=str(data[0]))
                    txtindigo.config(text=str(data[1]))
                    txtblue.config(text=str(data[2]))
                    txtcyan.config(text=str(data[3]))
                    txtgreen.config(text=str(data[4]))
                    txtyellow.config(text=str(data[5]))
                    txtorange1.config(text=str(data[6]))
                    txtorange2.config(text=str(data[6]))
                    
                    txtred1.config(text=str(data[7]))
                    txtred2.config(text=str(data[7]))
                    txtred3.config(text=str(data[7]))
               except :
                    pass
             

arduinorcver = arduinodata()
arduinorcver.start()    
    
if __name__ == "__main__":
    app = BananaApp()
    showcam()
    app.title("Banana Maturity Classifier")
    app.minsize(800,480)
    app.mainloop()
