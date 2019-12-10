from django.shortcuts import render
from django.http import HttpResponse
import serial 
import time 

# Create your views here.
def index(request):
    global machine 
    global prev_x
    global prev_y 
    prev_x = 0
    prev_y = 0
    # machine = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
    
    return render(request, 'clm_video.html')

def move_machine(request):
    global machine 

    machine = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)


    x = request.GET.get('x', '')
    y = request.GET.get('y', '')

    global prev_x
    global prev_y 

    print(x + " " + y)

    # x is 200, y is 140 if the face is in middle of it 

    x = float(x) - 200
    y = float(y) - 140
    
    print(str(x) + " " + str(y))

    alpha = 0.5

    prev_x = alpha * prev_x + (1 - alpha) * x 
    prev_y = alpha * prev_y + (1 - alpha) * y

    # if prev_x > x + 5 or prev_x < x - 5:
    #     prev_x = x
    # if prev_y > y + 5 or prev_y < y - 5:
    #     prev_y = y
    machine.write(('G0 X'+str(prev_x)+' Y' + str(prev_y) + '\n').encode())
    # print('moved by x: ' + str(x) + ', y: ' + str(y))
    return HttpResponse('moved by x: ' + str(x) + ', y: ' + str(y))
#again