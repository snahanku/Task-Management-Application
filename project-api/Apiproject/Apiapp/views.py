from django.shortcuts import render, redirect 
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login , logout , authenticate 
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from Apiapp.forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import  Paginator
from Apiapp.models import UserTask, User
from Apiapp.serializers import Userserializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view
from  rest_framework import filters, generics
from  Apiapp.filters import UserFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter ,OrderingFilter
from django.core.paginator import Paginator

def user_login(request):
    if request.method=="POST":
        username=request.POST.get('username')# fetching user data
        password=request.POST.get('password')# fetching password
        user= authenticate(request, username , password)

        if user is not None:
          login(request , user)# login the data
          return HttpResponse("sucessful")
        else:
            messages.sucess("There was not logged in error, Try Again.....")# fail to get data raise exception
            return redirect('login')
    
    
    return render(request , 'login.html' , {})





def home(request):
      if request.method=="POST":
        username=request.POST.get('username')# fetching the usernamee data
        password=request.POST.get('password')#fetching the  password data
        user_name= authenticate(username)
        user_password=authenticate(password)
        user= authenticate(request , username=username , password=password)
        if user is not None:
          login(request , user)
          return redirect("/api/parse/")
        else:
            messages.success( request , message="There was not logged in error, Try Again.....")# raise excepttion
            return render(request , "login.html")
    
    

      return render(request ,"login.html")




def signup(request):
    if request.method=="POST":
        username= request.POST.get("username")#fetch data
        email=request.POST.get("email")#fetch email data
        password=request.POST.get("password")
        user= User.objects.create_user(
                                   username=username,  #
                                   email=email,        # create data
                                   password=password    #
                                 )
        user.save()    # save data
    return render(request , "signup.html")
def create(request):
    return HttpResponse("create")


def register_page(request):
    form= CreateUserForm()

    if request.method=="POST":
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/api/parse/") 
    context={'form': form}
    return render(request,'register.html',context)















from django_filters.rest_framework import DjangoFilterBackend
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer
    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_fields= ['task_title']
    search_fields=['task_desc']
    ordering_fields=['id']


def create_task(request):
    if request.method=="POST":
        title= request.POST.get("title")
        desc= request.POST.get("body")
        query= User.objects.create(task_title=title , task_desc=desc)
        query.save()

    return render(request , "home.html" ,{"user_list":User.objects.all()})




@api_view(['GET']) # api to  show the data  posted 
def postdata(request):
    data= User.objects.all()
    serializer= Userserializer(data , many=True)
    return Response(serializer.data)

from Apiapp.user_form import UserForm
def update_data(request ,id): ### update the user  data
    if request.method=="POST":#  get the data by post method
        data=User.objects.get(pk=id)#get the data by id 
        fm=UserForm(request.POST, instance=data)#
        if fm.is_valid():#
             fm.save() # change and validate data
             return redirect("/api/parse/")# redirect to the parse page

    else:
         data=User.objects.get(pk=id) # get the data by GET method
         fm=UserForm(instance=data)

    return render(request , "update.html" ,{'form':fm})




def delete_data(request,id):
    data=User.objects.all().filter(id=id).delete()# delete the current data
    return redirect('/api/parse/')#move to the main page
     


#pagination




def page(request):
    page_data=User.objects.all()
    servicedata=User.objects.all()
    paginator=Paginator(page_data,2) 
    page_no=request.GET.get('page')# Show 25 contacts per page.
    finalData=paginator.get_page(page_no)
    st=request.GET.get('search')
    if  st is not None:
        servicedata= User.objects.all().filter(task_title=st)
    data={
        "page_data": finalData,
        "user_data": servicedata
    }
    return render (request , "page.html" , data)
    
  
def services(request):

    servicedata= User.objects.all()
    if request.method=="GET":
            st=request.GET.get('search')
            if  st is not None:
                     servicedata= User.objects.all().filter(task_title=st)
    data={"user_data":  servicedata}
    return render(request , "trial.html",data)




def pagination(request):
    data= User.objects.all()# fetch all user data
    p= Paginator(User.objects.all(), 2)# limit data  per page
    page= request.GET.get('page')#
    venue=p.get_page(page)## set the  data per page
    return render(request , "page.html" , {"page_data": venue})# return the data to the main page


def create(request):
    if request.method=="POST":
        title= request.POST.get("title") # create task  title
        desc= request.POST.get("body")# create  task data
        query= User.objects.create(task_title=title , task_desc=desc)
        query.save()
        return redirect("/api/parse/")# return the created data

    return render(request , "create.html")


from django.db.models import Q
def Filter(request):
    servicedata= User.objects.all()
    if request.method=="GET":
            st=request.GET.get('search')# search the data 
            if  st is not None:
                     servicedata= User.objects.filter(task_title__icontains=st)# filter the searched data
    data={"user_data":  servicedata}
    return render(request , "trial.html",data)



def sort(request):

    servicedata= User.objects.all()
    if request.method=="GET":
            st=request.GET.get('search')
            if  st is not None:
                     servicedata= User.objects.all().filter(task_title=st)
    data={"user_data":  servicedata}
    return render(request , "trial.html",data)