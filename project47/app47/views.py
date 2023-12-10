
from django.shortcuts import render,redirect
from .forms import b2,b3
from .models import a1,a2
# Create your views here.


def FirstPage(request):
    return render(request,'firstpage.html')


def LoginPage(request):
    return render(request,'LoginPageIdea2.html')

'''
def LoginPage(request):
    Login=b1()
    if request.method=='POST':
        Login=b1(request.POST)
        if Login.is_valid():
            # Login.save()
            return redirect('/SecondPage')
            # print(Login.cleaned_data['Email'])
            # print(Login.cleaned_data['Password'])
    else:
        return render(request,'LoginPageIdea2.html',{'forms':Login})

'''

def SecondPage(request):
    data=b2()
    if request.method=='POST':
        data=b2(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/SecondPage')

    return render(request,'Secondpage.html',{'forms':data})


def DataShow(request):
    data=a1.objects.all()
    return render(request,'PatientsDataShow.html',{'res':data})

def Delete(request,id):
    data=a1.objects.get(id=id)
    data.delete()
    return redirect('/Patientsdata')

def Edit(request,id):
    data=a1.objects.get(id=id)
    return render(request,'Edit.html',{'res':data})

def Update(request,id):
    data=a1.objects.get(id=id)
    formdata=b2(request.POST,instance=data)
    if formdata.is_valid():
        formdata.save()
        return redirect('/Patientsdata')


'''This section is for the Nurses to access the patient's data'''

def LoginPageNurse(request):
    return render(request,'LoginPageNurse.html')

'''

def LoginPageNurse(request):
    Login=b1()
    if request.method=='POST':
        Login=b1(request.POST)
        if Login.is_valid():
            # Login.save()
            return redirect('/SecondPageNurse')
            # print(Login.cleaned_data['Email'])
            # print(Login.cleaned_data['Password'])
    else:
        return render(request,'LoginPageNurse.html',{'forms':Login})
'''

def SecondPageNurse(request):
    data=b3()
    if request.method=='POST':
        data=b3(request.POST)
        if data.is_valid():
            data.save()
            return redirect('/SecondPageNurse')

    return render(request,'Secondpagenurse.html',{'forms':data})


def DataShowNurse(request):
    data=a2.objects.all()
    return render(request,'PatientsDataShowNurse.html',{'res':data})

def DeleteNurse(request,id):
    data=a2.objects.get(id=id)
    data.delete()
    return redirect('/Patientsdatanurse')

def EditNurse(request,id):
    data=a2.objects.get(id=id)
    return render(request,'EditNurse.html',{'res':data})

def UpdateNurse(request,id):
    data=a2.objects.get(id=id)
    formdata=b3(request.POST,instance=data)
    if formdata.is_valid():
        formdata.save()
        return redirect("/Patientsdatanurse")