"""JangWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from JangWeb import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/',views.homePage),
    path('Home/',views.Home,name="Home"),
    path('About-us/',views.About,name="About-us"),
    path('Services/',views.Services,name="Services"),
    path('contact-us/',views.contactUs,name="contact-us"),
    path('userform/',views.userform,name="userform"),
    path('calculator/',views.calculator),
    path('Marksheet/',views.Marksheet),
    path('NewsPage/<slug>',views.NewsPage),



]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
