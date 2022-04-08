from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from SP_app.forms import AccountUpdateForm
from SP_app.models import HelloWorld
from django.views.generic import CreateView , DetailView , UpdateView , DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def hello_world(request):
    if request.method == "POST":
        
        temp= request.POST.get("hello_world_input")
        
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        
        return HttpResponseRedirect(reverse('SP_app:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, "SP_app/hello_world.html", context={"hello_world_list": hello_world_list})
    
    
class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("SP_app:hello_world")
    template_name = "SP_app/create.html"    
    
class AccountDetailView(DetailView):
    model= User
    context_object_name= "target_user"
    template_name = "SP_app/detail.html"
    
    
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = "target_user"
    form_class = AccountUpdateForm
    success_url = reverse_lazy("SP_app:hello_world")
    template_name = "SP_app/update.html"
    

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = "target_user"
    success_url = reverse_lazy("SP_app:login")
    template_name = "SP_app/delete.html"