from django.shortcuts import render, redirect
from .forms import CreateRecordForm, UpdateRecordForm

from .models import Blog
from django.contrib import messages

def home(request):

    return render(request, 'testapp4/dashboard.html')
def dashboard(request):

    my_records = Blog.objects.all()

    context = {'records': my_records}

    return render(request, 'testapp4/dashboard.html', context=context)

def create(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Made Blog")

            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'testapp4/create.html', context=context)

def update(request, pk):

    record = Blog.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Updated Blog")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'testapp4/update.html', context=context)

def singular(request, pk):

    all_records = Blog.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'testapp4/view.html', context=context)

def delete(request, pk):

    record = Blog.objects.get(id=pk)

    record.delete()

    messages.success(request, "Deleted Blog")

    return redirect("dashboard")


