from django.http import HttpResponse 
from .forms import Ajoutcode
from django.shortcuts import render,HttpResponseRedirect
from .models import Syndrome
from .models import Modulo
from .utils.niederetter import func_goppa
from .utils.niederetter import perm_alea
from .utils.niederetter import mat_inv
from .utils.niederetter import mat_par
from .utils.niederetter import niederetteK
from .utils.niederetter import encod_mess

# Create your views here. 
def ajout_code(request): 
    if request.method == 'POST':
       
        fm=Ajoutcode(request.POST)
        if fm.is_valid():
            ce=fm.cleaned_data['code_envoyé']
            cr=fm.cleaned_data['code_reçu']
            reg= Syndrome(code_envoyé= ce,code_reçu=cr)
            reg.save()
            fm=Ajoutcode()

    else: 
        fm=Ajoutcode()
    synd=Syndrome.objects.all()

    return render(request, 'polls/ajout.html',{'form':fm ,'syn':synd})

def delete(request,id):
    if request.method == 'POST':
        pi = Syndrome.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


def niederetter(request):
    if request.method == 'POST':
        modulo=request.POST.get('modulo')
        fg=func_goppa(modulo)
        mp=perm_alea(modulo)
        mi=mat_inv(modulo)
        mp=mat_par(modulo)
        k=niederetteK(modulo)
        return render(request, 'polls/niederetter.html',{ 'fgoppa': fg , "perm_alea" : mp, "mat_inv": mi ,"mat_par":mp , "k":k})
    return render(request, 'polls/niederetter.html')

def codage(request): 
    if request.method == 'POST':
        modulo=request.POST.get('modulo')
        message=request.POST.get('message')
        me=encod_mess(message,modulo)
        return render(request, 'polls/codage.html',{'m': me})

    return render(request, 'polls/codage.html')

