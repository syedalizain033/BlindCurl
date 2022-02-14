from django.http import HttpResponse
from django.shortcuts import render
from .forms import FormClass

def home(request):
    form = FormClass(request.POST)
    if request.method=="POST" and form.is_valid() :
        
        url=form.cleaned_data['urlCommand']
        url=str(url)
        checklist=["$", '&','wget']
        checkUrl=check=any(checklist in url for checklist in checklist)
        if checkUrl:
            form = FormClass()
            return render(request, "app/home.html", {'error': "Character not allowed", 'form':form})
        else:
            import os
            com=("curl -I "+url+" 2>&1 | awk '/HTTP\// {print $2}'")
            #com= "ls"
            stream = os.popen(com)
            output = stream.read()
            return render(request, "app/home.html", {'form': form, 'code': output})
        
        
    else:
        form = FormClass()
        return render(request, "app/home.html", {'form': form})

def about(request):
    return HttpResponse("NO ABOUT")

def contact(request):
    return HttpResponse("NO RESPONSE")
