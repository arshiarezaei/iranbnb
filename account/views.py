from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .form import LoginForm,UserRegistrationForm,RentOutAHomeForm
from django.contrib.auth.decorators import login_required
from .models import RentOutAHome
from rest_framework.views import APIView
from .serializer import UserSerializer,RentOutAHomeSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('authenticated successfully ')
                else:
                    return HttpResponse('disable account')
            else:
                return HttpResponse('invalid login')
    else:
        form=LoginForm()
        return render(request,'account/login.html',{'form':form})


@login_required
def dashboard(request):
    return render(request,'registration/dashboard.html',{'section':'dashboard'})


def register(request):
    if request.method == 'POST':
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user=user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request,'account/register_done.html',{'newuser':new_user})
    else:
        user_form=UserRegistrationForm()
        return render(request,'account/register.html',{'user_form':user_form})


@login_required
def rent_out_a_home(request):
    # TODO : store valid data into account

    if request.method == 'POST':
        form = RentOutAHomeForm(request.POST)
        home = RentOutAHome(surface_area=request.POST['surface_area'], number_of_rooms=request.POST['number_of_rooms'],
                            address=request.POST['address'], start_date=request.POST['start_date'],
                            finale_date=request.POST['finale_date'],
                            identity_docs=request.POST['identity_docs'], photo=request.POST['photo']
                            , cost_per_day=request.POST['cost_per_day'],
                            owner=request.user)
        home.save()
        return HttpResponse ('valid')

    else:

        rent_out_a_homee = RentOutAHomeForm()
        return render(request,'account/rent_out_a_home.html',{'rent_out_a_home_form':rent_out_a_homee})


@login_required
def rent_a_home(request):
    return render(request,'account/rent_a_home.html')


class UserModelApi(APIView):

    def get(self,request):
        users = User.objects.all().values('username','first_name','email','password')
        user_list = list(users)
        return Response({"users":user_list})

    def post(self,request):
        user = request.data.get('newUser')
        serializer = UserSerializer(data=user,many=True)
        if serializer.is_valid(raise_exception=True):
            save = serializer.save()
        return Response(serializer.errors)


class RentOutAHomeApi(APIView):
    @method_decorator(login_required)
    def get(self,request):
        homes=RentOutAHome.objects.all().values()
        homes_list = list(homes)
        return Response({"homes":homes_list})

    @method_decorator(login_required)
    def post(self,request):
        home = request.data.get('newHome')
        serializer = RentOutAHomeSerializer(data=home,many=False)
        if serializer.is_valid(raise_exception=True):
            save = serializer.save()
        return Response(serializer.errors)