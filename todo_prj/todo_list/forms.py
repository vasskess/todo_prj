from django import forms
from django.forms import ModelForm

from todo_prj.todo_list.models import Task


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task                                                         # ____________
        fields = ["title", ]      # This will create a "empty field" --> Title:|          |  It only works with editable attribute
                                                                              # ````````````
