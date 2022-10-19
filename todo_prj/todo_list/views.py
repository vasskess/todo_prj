from django.shortcuts import render, redirect

from todo_prj.todo_list.forms import TodoForm
from todo_prj.todo_list.models import Task


# Create your views here.


def todo_page(request):
    tasks = Task.objects.all()                           # Task is the Model/Table name
    form = TodoForm()                                    # Here we call TodoForm, so we can pass it to context

    # This is Create from CRUD
    if request.method == "POST":                         # This is syntax to save data in DB when something is added
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("todo_page")                     # This will redirect us to the home page again
    context = {"tasks": tasks, "form": form}             # This will be used in html template
    return render(request, "html_todo.html", context)


def view_task(request, pk):
    task = Task.objects.get(id=pk)
    context = {}

    # This is Read from CRUD
    if request.method == "POST":
        return redirect("todo_page")
    context["task"] = task
    return render(request, "html_view.html", context)


def update_task(request, pk):                  # This will trow the primary key for the task we want to update
    task = Task.objects.get(id=pk)             # This is syntax to take a specific object from our Model/Table by id/pk
    form = TodoForm(instance=task)             # form will be an instance of the obj we took by its id/pk in Model/Table
    context = {}

    # This is Update from CRUD
    if request.method == "POST":
        form = TodoForm(request.POST, instance=task)         # We need to pass the instance otherwise
        if form.is_valid():                                  # it will create a new obj in the DB
            form.save()
        return redirect("todo_page")
    context["form"] = form
    return render(request, "html_update.html", context)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)
    context = {"item": item}

    # This is Delete from CRUD
    if request.method == "POST":
        item.delete()
        return redirect("todo_page")
    return render(request, "html_delete.html", context)
