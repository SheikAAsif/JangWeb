from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import jForm
from services.models import services
from News.models import News
from django.core.paginator import Paginator
from contactEnquiry.models import contactEnquiry




def homePage(request):
    return HttpResponse("welcome to my site")
#--------------------------------------------
#  keyword for over all search    __icontains
def Home(request):
    NewsData=News.objects.all()
    servicesData=services.objects.all()
            
    if request.method=='GET':
        search=request.GET.get('search')
        if search!=None:
            servicesData=services.objects.filter(servicew_title__icontains=search)
            
    data={
        'servicesData':servicesData,
        'NewsData':NewsData
    }

    return render(request,"index.html",data)


def NewsPage(request,slug):
    #NewsData=News.objects.all()
    NewsDataSlug=News.objects.get(news_slug=slug)

    data={
        'NewsDataSlug':NewsDataSlug
        
        
    }
    return render(request,"NewsPage.html",data)



def About(request):
    if request.method=="GET":
        output=request.GET.get('output')

    return render(request,"About-us.html",{'output':output})

def contactUs(request):
    servicesData=services.objects.all()
    pagi=Paginator(servicesData,1)
    page_num=request.GET.get('page')
    final_data=pagi.get_page(page_num)
    last_page=final_data.paginator.num_pages
    
    data={
        'servicesData':final_data,
        'last_page':last_page,
        'total_page_list':[L+1 for L in range(last_page)],
        #'previous_page_num':[p-1 for p in range(last_page)]
    }



    return render(request,"contact-us.html",data)


def Services(request):
    return render(request,"Services.html")

def userform(request):
    if request.method == "POST":
        name=request.POST.get('name')
        lastname=request.POST.get('lastname')
        address=request.POST.get('address')
        address2=request.POST.get('address2')
        city=request.POST.get('city')
        cn=contactEnquiry(user_name=name,user_last_name=lastname,user_address=address,user_old_address=address2,user_city=city)
        cn.save()
    return render(request,"userform.html")


#def userform(request):
    fn=jForm()
    total=0
    data={'form':fn}

    try:

        if request.method == "POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            n3=int(request.POST.get('num3'))
            total=n1+n2+n3
            data={
                'form':fn,
                'total':total
            }

    except:
        pass
    return render(request,"userform.html",data)

def userEnquiry(request):

    return render(request,"userform.html")


    
def calculator(request):
    c=""
    d={}
    

    if request.method=="POST":
        n1=eval(request.POST.get('num1'))
        n2=eval(request.POST.get('num2'))
        opr=request.POST.get('opr')
        if opr=="+":
            c=n1+n2
        elif opr=="-":
            c=n1-n2
        elif opr=="*":
            c=n1*n2
        elif opr=="/":
            c=n1/n2
        else:
            c="invalid opr"
        d={
            'n1':n1,
            'n2':n2,
            'opr':opr,
            'c':c

            
        }
    
        
    return render(request,"calculator.html",d)

def Marksheet(request):
    
    t=""
    per=""
    gd=''
    data={}

    if request.method=="POST":
        if request.POST.get('num1')=="":
            return render(request,"Marksheet.html",{'error':True})
        
        n1=int(request.POST.get('num1'))
        n2=int(request.POST.get('num2'))
        n3=int(request.POST.get('num3'))
        n4=int(request.POST.get('num4'))
        n5=int(request.POST.get('num5'))
        t=n1+n2+n3+n4+n5
        per=t*100/500
        if per>=85:
            gd="A1"
        elif per>=65:
            gd="A"
        elif per>=55:
            gd="B"
        elif per>=35:
            gd="C"
        else:
            gd="Fail"
        data={
            'n1':n1,
            'n2':n2,
            'n3':n3,
            'n4':n4,
            'n5':n5,
            't':t,
            'per':per,
            'gd':gd

        }
        
    return render(request,"Marksheet.html",data)

#def userform(request):
    #finalvalue=0
    #data={}
    #try:
        #if request.method=="POST":
            #n1=int(request.POST.get('num1'))
            #n2=int(request.POST.get('num2'))
            #finalvalue=n1+n2
            #print(n1,n2)
            #data={
             #   'n1':n1,
             #   'n2':n2,
             #   'output':finalvalue
            #}
            #url="/About-us/?output={}".format(finalvalue)
            #return HttpResponseRedirect(url)
        
    #except:
        #pass

    #return render(request,"userform.html",data)
    #return render(request,"userform.html",{'output':finalvalue})
