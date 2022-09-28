from django.shortcuts import render, redirect

from todo_prj.todo_list.forms import TodoForm
from todo_prj.todo_list.models import Task


# Create your views here.


def todo_page(request):
    tasks = Task.objects.all()                           # Task is the Model/Table name
    form = TodoForm()                                    # Here we call TodoForm so we can pass it to context
    context = {"tasks": tasks, "form": form}             # This will be used in html template

    # This is Create from CRUD
    if request.method == "POST":                         # This is syntax to save data in DB when something is added
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("todo_page")                     # This will redirect us to the home page again
    return render(request, "html_todo.html", context)


def update_task(request, pk):                            # This will trow the primary key for the task we want to update
    task = Task.objects.get(id=pk)                       # This is syntax to take a specific object from our Model/Table by id/pk
    form = TodoForm(instance=task)                       # form will be a instance of the obj we took by its id/pk in Model/Table
    context = {"form": form}

    # This is Update from CRUD
    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)     # We need to pass the instance otherwise it will create a new obj in the DB
        if form.is_valid():
            form.save()
        return redirect("todo_page")
    return render(request, "html_update.html", context)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)
    form = TodoForm(instance=item)
    context = {"item": item}

    #This is Delete from CRUD
    if request.method == "POST":
        item.delete()
        return redirect("todo_page")
    return render(request, "html_delete.html", context)
