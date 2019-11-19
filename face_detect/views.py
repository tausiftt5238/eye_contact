from django.shortcuts import render
from django.http import HttpResponse
import serial 
import time 

# Create your views here.
def index(request):
    machine = request.session.get('machine')
    # if not machine:
    #     machine = serial.Serial('/dev/ttyUSB0', 115200, timeout=10)
    request.session['machine'] = machine
    return render(request, 'clm_video.html')

def move_machine(request):
    machine = request.session.get('machine')
    
    x = request.GET.get('x', '')
    y = request.GET.get('y', '')

    # machine.write('G0 X0 Y0\n'.encode())
    print('moved by x: ' + x + ', y: ' + y)
    return HttpResponse('moved by x: ' + x + ', y: ' + y)

    #For testing