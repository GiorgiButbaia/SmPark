from django.shortcuts import render
from ethjsonrpc import EthJsonRpc #Ethereum JSON RPC Lib
from .models import ParkingLot, PL_User
import cv2


c = EthJsonRpc('127.0.0.1', 8545)

def index(request):
     lines = []
     try:#TODO use getter methods from JSON RPC
          f = open('file.txt','r')
          for line in f:
               lines.append(line)
               break
          f.close()
     except:
          pass
     if len(lines) > 0:
          plLot = ParkingLot.objects.all().get(addr = "0x11aad4f50b2d1173b3dfb00ec14cb199f9374b6a")
          plLot.carId = lines[0]
          plLot.save()
     print "Request received" #That means that the user has connected
     return render(request, 'index/data.json', {'RES': lines,
                                                'ParkingLots': ParkingLot.objects.all(),
                                                'PL_Users': PL_User.objects.all()})
def buyLot(request):
     if request is not None and 'POST' == request.method:
          lotId = request.POST.get("addr")
          numHr = float(request.POST.get("numHr"))
          userName = request.POST.get("userIndex")

          plLot = ParkingLot.objects.all().get(addr = lotIt)
          pl_User = PL_User.objects.all().get(userIndex = userName)
          if pl_User.balance > plLot.price*numHr:
               plLot.state = False
               plLot.hrs = numHr
               pl_User.balance -= plLot.price*numHr;
               pl_User.save()
               plLot.save()
     return render(request, 'index/data.json', {'RES': lines,
                                                'ParkingLots': ParkingLot.objects.all(),
                                                'PL_Users': PL_User.objects.all()})

def freeLot(request):
     if request is not None and 'POST' == request.method:
          lotId = request.POST.get("addr")
          plLot = ParkingLot.objects.all().get(addr = lotId)
          plLot.state = True
          plLot.carId = ""
          plLot.hrs = 0
          plLot.save()
     return render(request, 'index/data.json', {'RES': lines,
                                                'ParkingLots': ParkingLot.objects.all(),
                                                'PL_Users': PL_User.objects.all()})
