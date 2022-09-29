from django.contrib import admin

from todo_prj.todo_list.models import Task


# Register your models here.


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created",
    )  # This will display all the attributes in
       # the admin panel that are in the brackets
