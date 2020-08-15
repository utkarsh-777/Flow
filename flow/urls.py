"""flow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #auth
    path('', views.home,name='home'),
    path('signup/', views.signupuser,name='signupuser'),
    path('login/', views.loginuser,name='loginuser'),
    path('logout/', views.logoutuser,name='logoutuser'),
    #post
    path('post/', views.post,name='post'),
    path('<int:post_pk>/', views.expandpost,name='expandpost'),
    #own
    path('profile/', views.userprofile,name='userprofile'),
    path('save/', views.savepost,name='savedpost'),
    path('post/<int:post_pk>',views.viewpost,name='viewpost'),
    path('post/<int:post_pk>/unpost',views.unpost,name='unpost'),
    path('post/<int:post_pk>/makepost',views.makepost,name='makepost'),
    path('post/<int:post_pk>/deletepost',views.deletepost,name='deletepost'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)