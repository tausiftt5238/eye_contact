from django.shortcuts import render
from django.http import HttpResponse
import serial 
import time 

# Create your views here.
def index(request):
    global machine 
    global prev_x
    global prev_y
    global count 
    prev_x = 0
    prev_y = 0
    machine = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
    count = 0

    return render(request, 'clm_video.html')

def move_machine(request):
    global machine 
    global count 
    x = request.GET.get('x', '')
    y = request.GET.get('y', '')

    if count == 0:
        # machine = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
        
        global prev_x
        global prev_y 

    # x = float(x) - 200
    # y = float(y) - 140

        # x = -(-float(x) + 380)/2
        # y = -(-float(y) + 315)/2
    
        x = float(x)/2 - 270/2 - 60
        y = float(y)/2 - 200/2 - 60# Because X,Y provided by the camera is double of what the xy plotter uses [probably 0.5mm]

        print(str(x) + " " + str(y))
    
        machine.write(('G91\n').encode())
        machine.write(('G21\n').encode())
        machine.write(('G0 X'+str(x)+' Y' + str(y) + '\n').encode())
    count = (count + 1) % 10
    # machine.write(('G0 X'+str(x)+' Y' + str(y) + '\n').encode())
    return HttpResponse('moved by x: ' + str(x) + ', y: ' + str(y))
#again
