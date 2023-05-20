from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView,ListView,DetailView,UpdateView
from vehicleweb.forms import *
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

def signin_required(fn):
    def wrapper(request,*args,**kw):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kw)
    return wrapper

def signin_required(fn):
    def wrapper(request,*args,**kw):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kw)
    return wrapper

decs=[signin_required,never_cache]


class SuperAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.userprofile.role == 'superadmin'

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.userprofile.role == 'admin' or self.request.user.userprofile.role == 'superadmin'


class RegistrationView(CreateView):
    template_name="register.html"
    form_class=UserRegistrationForm
    model=User
    success_url=reverse_lazy("login")

class LoginView(FormView):
    template_name="login.html"
    form_class=LoginForm

    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                return redirect("login")

@method_decorator(decs,name="dispatch")
class IndexView(TemplateView):
    template_name="index.html"

@method_decorator(decs,name="dispatch")
class VehicleCreateView(CreateView,SuperAdminRequiredMixin):
    template_name = 'add_vehicle.html'
    form_class = VehicleForm
    success_url = reverse_lazy('list_vehicle')
    
    def form_valid(self, form):
        form.instance.save()
        return super().form_valid(form)

@method_decorator(decs,name="dispatch")
class VehicleListView(ListView,LoginRequiredMixin):
    template_name = 'list_vehicle.html'
    model = Vehicle
    context_object_name = 'data'

@method_decorator(decs,name="dispatch")
class UpdateVehicle(UpdateView,AdminRequiredMixin):
    model = Vehicle
    form_class = VehicleForm
    template_name = 'update_vehicle.html'
    success_url = reverse_lazy('list_vehicle')

        

def vehicle_delete(request,pk):
    if request.method=="GET":
        id=pk
        Vehicle.objects.get(vehicle_id=id).delete()
        return redirect("list_vehicle") 
    

def sign_out_view(request,*args,**kw):
    logout(request)
    return redirect("login")
    








