from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from Management.models import WeeklyData,MidData

def getMarks(request):
    if request.user.is_anonymous:
        return render(request,'index.html')
    if request.method == 'POST' and request.POST.get("Enrollment") is not None:
        erNo=request.POST.get("Enrollment")
        weeklyMarks=WeeklyData.objects.all()
        print(weeklyMarks)