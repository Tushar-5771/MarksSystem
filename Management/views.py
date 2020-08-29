from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import WeeklyData,MidData
import json
from django.contrib import messages

# Create your views here.
def Index(request):
    if request.user.is_anonymous:
        weekly=WeeklyData.objects.all()

        mid=MidData.objects.all()

        List={
            'weekly': weekly,
            'mid':mid
        }
        
        return render(request,'HomePage.html',List)
    
    erList=[]
    
    for i in range(170303108051,170303108061):
        erList.append(i)

    List={
        'ErList': erList
    }
    
    return render(request,'addMarks.html',List)

def Home(request):
    if request.method == 'POST':
        username=request.POST.get('userName')
        password=request.POST.get('userPassword')

        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            # messages.warning(request,"Either Username or Password is worng..")
           
            return render(request,'index.html',{'flag':1})
            
    return render(request,'index.html',{'flag':0})
    
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
       
        # messages.success(request,'Data is Inserted Successfully....')
        List['flage']=1
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
        # messages.success(request,'Data is Inserted Successfully....')
        List['Mflage']=1
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

    if request.method == 'POST' and request.POST.get('weeklySubmit') is not None:
        erNo=request.POST.get('weeklyEr')
        AP=request.POST.get('weeklyAP')
        PDC=request.POST.get('weeklyPDC')
        SE=request.POST.get('weeklySE')
        WDD=request.POST.get('weeklyWDD')
        if WDD == '':
            WDD = None
        elif AP == '':
            AP = None
        WeeklyData.objects.filter(ErNo__exact=str(erNo)).update(advancePython=AP,PDC=PDC,SE=SE,WDD=WDD)
        
        messages.success(request,'Data is Updated Successfully....')
        List['flage']=1
        return render(request,'updateMarks.html',List)    

    if request.method == 'POST' and request.POST.get('midSubmit') is not None:
        erNo=request.POST.get('MidEr')
        AP=request.POST.get('midAP')
        PDC=request.POST.get('midPDC')
        SE=request.POST.get('midSE')
        WDD=request.POST.get('midWDD')
        if WDD == '':
            WDD = None
        elif AP == '':
            AP = None
        
        MidData.objects.filter(ErNo__exact=str(erNo)).update(advancePython=AP,PDC=PDC,SE=SE,WDD=WDD)

        messages.success(request,'Data is Updated Successfully....')
        List['Mflage']=1
        return render(request,'updateMarks.html',List)

    return render(request,'updateMarks.html',List)


def getMarks(request):
    if request.user.is_anonymous:
        return render(request,'index.html')

    #for update marks
    if request.method == 'POST' and request.POST.get("Enrollment") is not None:
        
        erNo=request.POST.get("Enrollment")
        #weekly Marks
        wkM=WeeklyData.objects.filter(ErNo__exact=str(erNo))
        wkMCount=WeeklyData.objects.filter(ErNo__exact=str(erNo)).count()
        # Mid Marks
        mdM=MidData.objects.filter(ErNo__exact=str(erNo))
        MdCount=MidData.objects.filter(ErNo__exact=str(erNo)).count()
        wL={}
        if wkMCount>0:
            ap=wkM[0].advancePython
            pdc=wkM[0].PDC
            se=wkM[0].SE
            wdd=wkM[0].WDD
            wL={'Wap':ap,'Wpdc':pdc,'Wse':se,'Wwdd':wdd}
            wL['Status']='ok'
        else:
            wL['Status']=''

        mL={}
        if MdCount>0:
            ap=mdM[0].advancePython
            pdc=mdM[0].PDC
            se=mdM[0].SE
            wdd=mdM[0].WDD
            mL={'Map':ap,'Mpdc':pdc,'Mse':se,'Mwdd':wdd}
            mL['Status']='ok'
        else:
            
            mL['Status']=''

        Data={"weekly":wL,"mid":mL}
        DataDict=json.dumps(Data)

        return HttpResponse(DataDict)

    #for existing record in weeklly
    if request.method == 'POST' and request.POST.get("addWeeklyEnrollment") is not None:
        erNo=request.POST.get("addWeeklyEnrollment")
        #weekly Marks
        wkM=WeeklyData.objects.filter(ErNo__exact=str(erNo))
        wkMCount=WeeklyData.objects.filter(ErNo__exact=str(erNo)).count()
        wL={}
        if wkMCount>0:
            # ap=wkM[0].advancePython
            # pdc=wkM[0].PDC
            # se=wkM[0].SE
            # wdd=wkM[0].WDD
            # wL={'Wap':ap,'Wpdc':pdc,'Wse':se,'Wwdd':wdd}
            wL['Status']='ok'
        else:
            wL['Status']=''
        # messages.info(request,"Data is Already Enterd..")
        return HttpResponse(json.dumps(wL))

    #for existing record in mid 
    if request.method == 'POST' and request.POST.get("addmidErNo") is not None:
        erNo=request.POST.get("addmidErNo")
        # Mid Marks
        print(erNo)
        mdM=MidData.objects.filter(ErNo__exact=str(erNo))
        MdCount=MidData.objects.filter(ErNo__exact=str(erNo)).count()

        mL={}
        if MdCount>0:
            # ap=mdM[0].advancePython
            # pdc=mdM[0].PDC
            # se=mdM[0].SE
            # wdd=mdM[0].WDD
            # mL={'Map':ap,'Mpdc':pdc,'Mse':se,'Mwdd':wdd}
            mL['Status']='ok'
        else:
            mL['Status']=''

        return HttpResponse(json.dumps(mL))
        
    return HttpResponse('')
