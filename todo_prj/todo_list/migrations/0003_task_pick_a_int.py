# Generated by Django 4.1.1 on 2022-10-03 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_list", "0002_remove_task_complete"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="pick_a_int",
            field=models.IntegerField(choices=[(1, 1), (2, 2)], default=1),
            preserve_default=False,
        ),
    ]