import serial



ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
ser.reset_input_buffer()
while True:
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    data = line.split(",")
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])
    print(data[4])
    print(data[5])
    print(data[6])
