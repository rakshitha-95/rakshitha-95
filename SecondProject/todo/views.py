from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    todos=Todo.objects.all()
    form=TodoForm()

    if request.method == 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/todo')

    context={'todos':todos,'form':form}
    return render(request,'list.html', context)
def updateTask(request,pk):
    todo=Todo.objects.get(id=pk)
    form=TodoForm(instance=todo)
    if request.method== 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
        return redirect('/todo')

    context={'form':form}
    return render(request,'update.html',context)
def deleteTask(request,pk):
    item=Todo.object.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/todo')
    context={'item':item}
    return render(request,'task/delete.html',context)