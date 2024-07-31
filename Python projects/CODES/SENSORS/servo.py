#pip3 install pigpio
#sudo systemctl enable pigpiod
#sudo systemctl start pigpiod
import RPi.GPIO as GPIO
import pigpio
import time
import os
os.system("sudo pigpiod")
print ("START PROGRAM")

#servo = 19
servo = 2

# more info at http://abyz.me.uk/rpi/pigpio/python.html#set_servo_pulsewidth

pwm = pigpio.pi()
pwm.set_mode(servo, pigpio.OUTPUT)

pwm.set_PWM_frequency( servo, 50 )

print( "0 deg" )
pwm.set_servo_pulsewidth( servo, 570 ) ;
time.sleep( 3 )

print( "90 deg" )
pwm.set_servo_pulsewidth( servo, 1500 ) ;
time.sleep( 3 )

print( "0 deg" )
pwm.set_servo_pulsewidth( servo, 570 ) ;
time.sleep( 3 )

#print( "180 deg" )
#pwm.set_servo_pulsewidth( servo, 2500 ) ;
#time.sleep( 3 )

# turning off servo
pwm.set_PWM_dutycycle( servo, 0 )
pwm.set_PWM_frequency( servo, 0 )
