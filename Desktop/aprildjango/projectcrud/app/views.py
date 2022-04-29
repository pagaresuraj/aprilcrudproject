from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from app.models import Schoolbranch,ExamModel
from app.forms import Examforms
from app.forms import SchoolbranchForm

# Create your views here.
def home(request):
    return render(request,"app/home.html",{"name":"suraj"} )
def about(request):
    branchs = Schoolbranch.objects.all()
    print(branchs)
    return render(request,"app/branches.html",{'schools':branchs})
#1
def create(request):
    data = {}
    inputdata = SchoolbranchForm(request.POST or None)
    if inputdata.is_valid():
        inputdata.save()

    data['form']=inputdata
    return render(request,"app/input.html",data)
#2
def addform(request):
    data = {}
    inputformdata = Examforms(request.POST or None)

    if inputformdata.is_valid():
        inputformdata.save()
    data['form'] = inputformdata
    return render(request, "app/examform.html", data)



def updateview(request,id):
    data = {} #view-temp transfer as dictionary
    formdata = get_object_or_404(ExamModel,id=id) #for update/ PUT/
    inputformdata = Examforms(request.POST or None, instance = formdata)

    if inputformdata.is_valid():
        inputformdata.save() #store
    data['form'] = inputformdata
    return render(request, "app/examform.html", data)

#delete - >

def deleteview(request,id):

    data = {}
    formdata = get_object_or_404(ExamModel,id=id)

    if request.method == "POST":
        formdata.delete()
        return HttpResponseRedirect("/")
    return render(request,"app/deletedata.html",data )





def schoolview(request):
    school_data = Schoolbranch.objects.all()
    return render (request,"app/schooltemplate.html",{"schools":school_data})

def formview(request):
    form_data = Examform.objests.all()
    return render (request,"app/examform.html",{"Examform":Examform})

