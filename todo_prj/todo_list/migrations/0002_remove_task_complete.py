# Generated by Django 4.1.1 on 2022-09-29 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todo_list", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="task",
            name="complete",
        ),
    ]