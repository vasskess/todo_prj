from django.urls import path

from todo_prj.todo_list.views import todo_page, update_task, delete_task

urlpatterns = (
    path("", todo_page, name="todo_page"),                            # name the url pathern so we can call it by it
    path("update_task/<str:pk>/", update_task, name="update_task"),   # dynamic url + dynamic url by naming it
    path("delete_task/<str:pk>/", delete_task, name="delete_task"),   # <str:pk> its pk couse we name it pk in the view
)