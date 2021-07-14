from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib import messages
from django import forms
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import SignUpForm, Loginform

from .models import projects_list, collections_list, materials_list
from .mixins import AlreadyAuthenticated

# # Create your views here.
# def loginpage(request):
#     # logout(request)
#     form = signinform()
#     form2 = loginform()
#     context = {'form':form,'form2':form2}
#     return render(request,'login.html',context)


# def signup(request):
#     if request.method == 'POST':
#         form = signinform(request.POST)
#         if form.is_valid():
#             print("valid")
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request,user)
#             return render(request,'projects.html')
#         else:
#             print("invalid")
#     form = signinform()
#     context = {'form':form}
#     return render(request,'login.html',context)

# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import AuthenticationForm
# def signin(request):
#     if request.method == 'POST':
#         formi = AuthenticationForm(data=request.POST)
#         if formi.is_valid():
#             user = formi.get_user()
#             login(request, user)
#             return redirect('/menu/')
#     form = signinform()
#     form2 = loginform()
#     context = {'form':form,'form2':form2}
#     return render(request,'login.html',context)

# def home(request):
#     logout(request)
#     form = signinform()
#     form2 = loginform()
#     context = {'form':form,'form2':form2}
#     return render(request,'login.html',context)


class LoginView(AlreadyAuthenticated, LoginView):
    """
    Login view
    """
    form_class = Loginform
    template_name = 'login.html'
    redirect_authenticated_user = True


class SignUpView(AlreadyAuthenticated, FormView):
    """Customer SignUp View"""
    form_class = SignUpForm
    template_name = 'signup.html'
    success_url = 'login:signup'

    def form_valid(self, form):
        self.object = form.save()
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=email, password=password)
        if user and user.is_active:
            login(self.request, user)
            if self.request.GET.get('next'):
                return redirect(self.request.GET.get('next'))
            else:
                self.success_url = reverse_lazy('login:menu')
        return super(self.__class__, self).form_valid(form)


@login_required
def menu(request):
    return render(request,'menu.html',{"pro_list" : projects_list, "col_list" : collections_list,"mat_list" : materials_list})

@login_required
def projects(request):
    return render(request,'projects.html',{"data" : projects_list,})

@login_required
def materials(request):
    return render(request,'materials.html',{"data" : materials_list,})

@login_required
def collections(request):
    return render(request,'collections.html',{"data" : collections_list,})


@login_required
def project_detail(request):
    pro_req = []
    if request.method == 'GET':
        lis = list(request.GET.keys())
        for pro in projects_list:
            if str(pro.pk) in lis:
                pro_req.append(pro)
    if len(pro_req)==0:
        pro_req = projects_list[:3]
    return render(request,'projects_detail.html',{"data" : pro_req,})


@login_required
def collection_detail(request):
    col_req = []
    if request.method == 'GET':
        lis = list(request.GET.keys())
        for col in collections_list:
            if str(col.pk) in lis:
                col_req.append(col)
    if len(col_req)==0:
        col_req = collections_list[:3]
    return render(request,'collections_detail.html',{"data" : col_req,})



@login_required
def material_detail(request):
    mat_req = []
    if request.method == 'GET' or pk==0:
        lis = list(request.GET.keys())
        for mat in materials_list:
            if str(mat.pk) in lis:
                mat_req.append(mat)
    if len(mat_req)==0:
        mat_req = materials_list[:3]
    return render(request,'material_detail.html',{"data" : mat_req,})


@login_required
def material_details(request,pk=0):
        mat_req = []
        if pk!=0:
            for mat in materials_list:
                if str(mat.pk) == str(pk):
                    mat_req.append(mat)
        if len(mat_req)==0:
            mat_req = materials_list[:3]
        return render(request,'material_detail.html',{"data" : mat_req,})


@login_required
def collection_details(request,pk):
    col_req = []
    if pk!=0:
        for col in collections_list:
            if str(col.pk) == str(pk):
                col_req.append(col)
    if len(col_req)==0:
        col_req = collections_list[:3]
    return render(request,'collections_detail.html',{"data" : col_req,})


@login_required
def project_details(request,pk):
    pro_req = []
    if pk!=0:
        for pro in projects_list:
            if str(pro.pk) == str(pk):
                pro_req.append(pro)
    if len(pro_req)==0:
        pro_req = projects_list[:3]
    return render(request,'projects_detail.html',{"data" : pro_req,})

@login_required
def details(request):
    mat, col, pro, mat_req, col_req, pro_req = [], [], [], [], [], []
    if request.method == 'GET' or pk==0:
        lis = list(request.GET.keys())
        print(lis)
        for li in lis:
            if "mat" in li:
                mat.append(int(li.replace('mat',"")))
            elif "col" in li:
                col.append(int(li.replace('col',"")))
            elif "pro" in li:
                pro.append(int(li.replace('pro',"")))
        print(mat,col,pro)

    if len(mat)>0:
        for material in materials_list:
            if int(material.pk) in mat:
                mat_req.append(material)
    if len(col)>0:
        for collection in collections_list:
            if int(collection.pk) in col:
                col_req.append(collection)
    if len(pro)>0:
        for project in projects_list:
            if int(project.pk) in pro:
                pro_req.append(project)
                
    if len(mat_req)==0 and len(col_req) == 0 and len(pro_req)==0:
        mat_req = materials_list[:1]
        col_req = collections_list[:1]
        pro_req = projects_list[:1]

    context = {'mat_list': mat_req, 'col_list' : col_req, 'pro_list' : pro_req, 'projects_list': projects_list, 'collections_list': collections_list}
    return render(request, 'details.html', context)
