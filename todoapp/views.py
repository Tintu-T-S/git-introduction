from django.shortcuts import render, redirect

from todoapp.form import playersForm
from todoapp.models import players
# from django.forms import playersForm
# Create your views here.
def add(request):
    bat = players.objects.all()
    if request.method =="POST":
        name = request.POST.get('name','')
        nationality = request.POST.get('nationality', '')
        state = request.POST.get('state', '')
        match = request.POST.get('match', '')
        run = request.POST.get('run', '')
        average = request.POST.get('average', '')
        wicket = request.POST.get('wicket', '')
        date = request.POST.get('date','')
        # image = request.POST.get('image', '')
        innings = players(name=name,nationality=nationality,state=state,matches=match,runs=run,average=average,wickets=wicket,date=date)
        innings.save()
    return render(request,"home.html",{'top':bat})


def update(request,id):
    task = players.objects.get(id=id)
    form = playersForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save();
        return redirect('/')
    return render(request,"edit.html",{'form':form, 'task':task})

def delete(request,playerid):
    lbw = players.objects.get(id=playerid)
    if request.method == "POST":

        lbw.delete()
        return redirect('/')
    return render(request,"delete.html")


