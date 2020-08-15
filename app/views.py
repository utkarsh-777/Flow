from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import Postform
from .models import PostModel
from django.utils import timezone

def home(request):
    posts = PostModel.objects.filter(DatePosted__isnull=False).order_by('-DatePosted')
    return render(request,'home.html',{'posts':posts})

def signupuser(request):
    if request.method == 'GET':
        return render(request,'signupuser.html',{'form':UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request,'signupuser.html',{'form':UserCreationForm,'error':'Username taken!'})
        else:
            return render(request,'signupuser.html',{'form':UserCreationForm,'error':'Passwords does not match!'})

def loginuser(request):
    if request.method == 'GET':
        return render(request,'loginuser.html',{'form':AuthenticationForm})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'loginuser.html',{'form':AuthenticationForm,'error':'Username and Password does not match!'})

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return render(request,'logoutuser.html')

@login_required
def post(request):
    if request.method == 'GET':
        return render(request,'post.html',{'form':Postform})
    else:
        post = Postform(request.POST,request.FILES)
        newpost = post.save(commit=False)
        newpost.user = request.user
        newpost.DatePosted = timezone.now()
        newpost.save()
        return redirect('home')

@login_required
def userprofile(request):
    userposts = PostModel.objects.filter(user = request.user).order_by('-DatePosted')
    return render(request,'userprofile.html',{'posts':userposts})

@login_required
def savepost(request):
    if request.method == 'GET':
        return render(request,'savepost.html',{'form':Postform})
    else:
        post = Postform(request.POST,request.FILES)
        newpost = post.save(commit=False)
        newpost.user = request.user
        newpost.save()
        return redirect('userprofile')

@login_required
def viewpost(request,post_pk):
    post = get_object_or_404(PostModel,pk=post_pk,user=request.user)
    form = Postform(instance=post)
    if request.method == 'GET':
        return render(request,'viewpost.html',{'form':form,'id':post.id,'date':post.DatePosted})
    else:
        form = Postform(request.POST,request.FILES,instance=post)
        form.save()
        return redirect('userprofile')

@login_required
def unpost(request,post_pk):
    post = get_object_or_404(PostModel,pk=post_pk,user=request.user)
    if request.method == 'POST':
        post.DatePosted = None
        post.save()
        return redirect('userprofile')

@login_required
def makepost(request,post_pk):
    post = get_object_or_404(PostModel,pk=post_pk,user=request.user)
    if request.method == 'POST':
        post.DatePosted = timezone.now()
        post.save()
        return redirect('home')

@login_required
def deletepost(request,post_pk):
    post = get_object_or_404(PostModel,pk=post_pk,user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('userprofile')

@login_required
def expandpost(request,post_pk):
    thepost = get_object_or_404(PostModel,pk=post_pk)
    if request.method == 'GET':
        return render(request,'expandpost.html',{'post':thepost})