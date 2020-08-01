from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import WeeklyData,MidData
import json

# Create your views here.
def Index(request):
    if request.user.is_anonymous:
        return render(request,'index.html')
    return render(request,'dashBoard.html')

def Home(request):
    if request.method == 'POST':
        username=request.POST.get('userName')
        password=request.POST.get('userPassword')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'index.html')
    return render(request,'index.html')
    
def userLogOut(request):
    logout(request)
    return redirect('/')

def addMarks(request):
    if request.user.is_anonymous:
        return render(request,'index.html')
    
    erList=[]
    
    for i in range(170303108051,170303108061):
        erList.append(i)

    List={
        'ErList': erList,
    }
    if request.method == 'POST' and request.POST.get('weeklySubmit') is not None:
        erNo=request.POST.get('weeklyErNo')
        AP=request.POST.get('weeklyAP')
        PDC=request.POST.get('weeklyPDC')
        SE=request.POST.get('weeklySE')
        WDD=request.POST.get('weeklyWDD')
        if WDD == '':
            WDD = None
        elif AP == '':
            AP = None
        data=WeeklyData(ErNo=erNo,advancePython=AP,PDC=PDC,SE=SE,WDD=WDD)
        data.save()
        
        return render(request,'addMarks.html',List)    

    if request.method == 'POST' and request.POST.get('midSubmit') is not None:
        erNo=request.POST.get('midErNo')
        AP=request.POST.get('midAP')
        PDC=request.POST.get('midPDC')
        SE=request.POST.get('midSE')
        WDD=request.POST.get('midWDD')
        if WDD == '':
            WDD = None
        elif AP == '':
            AP = None

        data=MidData(ErNo=erNo,advancePython=AP,PDC=PDC,SE=SE,WDD=WDD)
        data.save()

        return render(request,'addMarks.html',List)


    return render(request,'addMarks.html',List)

def viewMarks(request):
    if request.user.is_anonymous:
        return render(request,'index.html')

    weekly=WeeklyData.objects.all()

    mid=MidData.objects.all()

    List={
        'weekly': weekly,
        'mid':mid
    }

    return render(request,'viewMarks.html',List)



def updateMarks(request):
    if request.user.is_anonymous:
        return render(request,'index.html')
    
    erList=[]
    
    for i in range(170303108051,170303108061):
        erList.append(i)

    List={
        'ErList': erList
    }
    return render(request,'updateMarks.html',List)


def getMarks(request):
    if request.user.is_anonymous:
        return render(request,'index.html')

    if request.method == 'POST' and request.POST.get("Enrollment") is not None:
        mdM=MidData.objects.filter()
        erNo=request.POST.get("Enrollment")
        wkM=WeeklyData.objects.filter(ErNo__exact=str(erNo))
        wkMCount=WeeklyData.objects.filter(ErNo__exact=str(erNo)).count()
        # print(wkMCount)
        if wkMCount>0:
            ap=wkM[0].advancePython
            pdc=wkM[0].PDC
            se=wkM[0].SE
            wdd=wkM[0].WDD
            wL={'Wap':ap,'Wpdc':pdc,'Wse':se,'Wwdd':wdd}
            wL['Status']='ok'
            weeklyList=json.dumps(wL)
            print(weeklyList)
        else:
            weeklyList={}
        
        return HttpResponse(weeklyList)
    return HttpResponse('')
