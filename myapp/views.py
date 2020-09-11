from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
# Create your views here.
def create_topic(request):
    if request.method=="POST":
        topic=request.POST.get("topic")
        t=Topic.objects.get_or_create(topic_name=topic)
        if t[1]==True:
            t[0].save()
            return HttpResponse("<h2>Topic Added Successfully</h2>")
        else:
            return HttpResponse("<h2>Topic Is Already Exist In Table</h2>")
    return render(request,"create_topic.html")

def create_webpage(request):
    if request.method=="POST":
        topic=request.POST.get('topic')
        name=request.POST.get('name')
        url=request.POST.get("url")
        t=Topic.objects.get_or_create(topic_name=topic)[0]
        w=Webpage.objects.get_or_create(topic=t,name=name,url=url)[0]
        w.save()
        return HttpResponse("<h2>Webpage Added Successfully</h2>")
    topics=Topic.objects.all()
    return render(request,"create_webpage.html",context={'topics':topics})
def display_topics(request):
    topics=Topic.objects.all()
    return render(request,"display_topic.html",context={'topics':topics})
def display_webpages(request):
    webpages=Webpage.objects.all()
    return render(request,"display_webpage.html",context={'webpages':webpages})
def display_topic(request,id):
    topics=Topic.objects.filter(id=id)
    return render(request,"display_topic.html",context={'topics':topics})
def display_webpage(request,wid):
    webpages=Webpage.objects.filter(id=wid)
    return render(request,"display_webpage.html",context={'webpages':webpages})
def create_access(request):
    if request.method=="POST":
        webpage=request.POST.get("webpage")
        datetime=request.POST.get("datetime")
        w=Webpage.objects.get_or_create(name=webpage)[0]
        d=AccessDetails.objects.get_or_create(webpage=w,datetime=datetime)[0]
        d.save()
        return HttpResponse("<h1>DateTime Added Successfully</h1>")
    webpages=Webpage.objects.all()
    return render(request,"create_access.html",context={'webpages':webpages})
def display_access1(request):
    accessdetails=AccessDetails.objects.all()
    return render(request,"display_access.html",context={'accessdetails':accessdetails})
def display_access(request,aid):
    accessdetails=AccessDetails.objects.filter(id=aid)
    return render(request,"display_access.html",context={'accessdetails':accessdetails})
def search(request,wid):
    if request.GET.get('search'):
        id=request.GET['search']
        webpages=Webpage.objects.all()
        webpages=Webpage.objects.filter(id=wid)
        return render(request,'display_webpage.html',context={'webpages':webpages})
    webpages=Webpage.objects.all()
    return render(request,'search.html')
