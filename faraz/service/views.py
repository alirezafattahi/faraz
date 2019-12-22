from django.shortcuts import render  ,get_object_or_404
from .forms import proform , msgform
from .models import contract , person
from django.utils import timezone

# Create your views here.


def pro(request):
    if request.method == 'POST':
        form = proform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = proform
    return render(request , 'pro_edit.html', {'form' : form})

def msg(request , s , r):
    if request.method == 'POST':
        form = msgform(request.POST)
        if form.is_valid():
            ms = form.save(commit=False)
            if s[0] == 'T' : ms.is_replay=True
            if s[1] == 'T' : ms.is_ticket=True
            ms.reciver = r
            ms.sender = request.user
            ms.datetime = timezone.now()
            ms.save()
    else:
        form = msgform
    return render(request, 'msg.html' , {'form' : form})




def contract_list(request):
    output = contract.objects.all()
    data = {
        'contract_list' : output
    }
    return render(request , 'contract_list.html' , data)

def contract_details(request , id):
    c = get_object_or_404 (contract , id=id)
    p = get_object_or_404 (person , id=id)
    data = {
        'contract' : c,
        'person' : p
    }
    return render(request , 'contract_details.html' , data)
    
def index(request):
    return render(request , 'index.html' )


def person_list(request):
    output = person.objects.all()
    data = {
        'person' : output
    }
    return render (request , 'person_list.html' , data)

def profile(request , id):
    output = get_object_or_404(person , id=id)
    data = {
        'profile_details' : output
    }
    return render(request , 'profile.html' , data)
    