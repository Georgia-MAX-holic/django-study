from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from SP.models import HelloWorld
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def hello_world(request):
    if request.method == "POST":
        
        temp= request.POST.get("hello_world_input")
        
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        
        return HttpResponseRedirect(reverse('SP:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, "SP/hello_world.html", context={"hello_world_list": hello_world_list})
    
    
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("SP:hello_world")
    template_name = "SP/create.html"    