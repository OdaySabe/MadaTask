from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import employee,coustomer,service

def loginpage(request):
    if request.method=='POST':
       username=request.POST.get("username")
       password=request.POST.get("password")
       try:
        employee.objects.get(username=username,password=password)
        request.session["login"]=True
        return redirect('/homepage')
       except employee.DoesNotExist:
        return render(request,'pages/loginpage.html',{'message':"User not exist"})
    else:
     request.session["login"]=False
     return render(request,'pages/loginpage.html',{'message':"Enter user"})
def logout(request):
    request.session["login"]=False
    return render(request,'pages/loginpage.html',{'message':"Enter user","login": request.session["login"]})
def homepage(request):
    if request.POST.get('delete')!=None:
        cm = coustomer.objects.get(id=request.POST.get('delete'))
        cm.delete()
        return redirect('/homepage')
    searchname=request.GET.get("searchname")
    searchnumber=request.GET.get("searchnumber")
    if searchname!=None or searchnumber!=None:
        allCoustomers=coustomer.objects.all().filter(name__contains=searchname).filter(phonenumber__contains=searchnumber)
    else:
        allCoustomers=coustomer.objects.all()
    coustomersDetails=[]
    for cm in allCoustomers:
        coustomerServices=cm.services.all()
        coustomersDetails.append({"cm":cm,"coustomerServices":coustomerServices})   
    return render(request,'pages/homepage.html',{"login": request.session["login"],"coustomersDetails":coustomersDetails})
def addcoustomer(request):
    if request.method=="POST":
      addService=service.objects.get(name=request.POST.get('services'))
      newCoustomer=coustomer(name=request.POST.get('name'),age=request.POST.get('age'),phonenumber=request.POST.get('phonenumber'),
      city=request.POST.get('city'),registerdate=request.POST.get('registerdate'))
      newCoustomer.save()
      newCoustomer.services.add(addService)
      return redirect('/homepage')
    return render(request,'pages/addcoustomer.html',{"login": request.session["login"],"srs":service.objects.all()})

def editcoustomer(request):
    if request.POST.get('edit')!=None:
     cm = coustomer.objects.get(id=request.POST.get('edit'))
     return render(request,'pages/editcoustomer.html',{"login": request.session["login"],"coustomer":cm})
    elif request.method=='POST' and request.POST.get('edit')==None :
     cm = coustomer.objects.get(id=request.POST.get('thisCoustomer'))
     cm.name=request.POST.get('name')
     cm.age=request.POST.get('age')
     cm.phonenumber=request.POST.get('phonenumber')
     cm.city=request.POST.get('city')
     cm.registerdate=request.POST.get('registerdate')
     cm.save()
    
     return redirect('/homepage')
    else:
     return HttpResponse("Not Valid")
       
def editservices(request):
    if(request.method=="GET"):
        return HttpResponse("Not Valid")
    elif request.POST.get('addingService')!=None:
        Coustomer=coustomer.objects.get(id=request.POST.get('editservice'))
        Coustomer.services.add(service.objects.get(id=request.POST.get('addingService')))
        CoustomerServices=Coustomer.services.all()
        array=[]
        for s in CoustomerServices:
           array.append(s.id)
        OtherServices=service.objects.all().exclude(id__in=array)
        return render(request,'pages/editservices.html',{"login": request.session["login"],'Coustomer':Coustomer,
        'CoustomerServices':CoustomerServices,'OtherServices':OtherServices})

    elif request.POST.get('deletingservice')!=None:
        Coustomer=coustomer.objects.get(id=request.POST.get('editservice'))
        Coustomer.services.remove(service.objects.get(id=request.POST.get('deletingservice')))
        CoustomerServices=Coustomer.services.all()
        array=[]
        for s in CoustomerServices:
         array.append(s.id)
        OtherServices=service.objects.all().exclude(id__in=array) 
        return render(request,'pages/editservices.html',{"login": request.session["login"],'Coustomer':Coustomer,
             'CoustomerServices':CoustomerServices,'OtherServices':OtherServices})
    else:
             Coustomer=coustomer.objects.get(id=request.POST.get('editservice'))
             CoustomerServices=Coustomer.services.all()
             array=[]
             for s in CoustomerServices:
              array.append(s.id)
             OtherServices=service.objects.all().exclude(id__in=array) 
             return render(request,'pages/editservices.html',{"login": request.session["login"],'Coustomer':Coustomer,
             'CoustomerServices':CoustomerServices,'OtherServices':OtherServices})
def listallservices(request):
    List={}
    for Service in service.objects.all():
        List[""+Service.name]=[]
        for Coustomer in coustomer.objects.all():
                try: 
                   sr=Coustomer.services.all().get(id=Service.id)
                   List[""+Service.name].append(Coustomer)
                except:
                    continue
    
    return render(request,'pages/listallservices.html',{"login": request.session["login"],"List":List})
    

#####################
 


# Create your views here.
