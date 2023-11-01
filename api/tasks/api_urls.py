from django.urls import path
from .api_views import (
    api_lst_tasks,
    api_show_task,
    api_proceed_task,
    api_complete_task
)


urlpatterns = [
    path(
        "tasks/",
        api_lst_tasks,
        name="api_lst_tasks",
    ),
    path(
        "tasks/<int:id>/",
        api_show_task,
        name="api_show_task",
    ),
    path(
        "tasks/<int:id>/proceed/",
        api_proceed_task,
        name="api_proceed_task",
    ),
    path(
        "tasks/<int:id>/complete/",
        api_complete_task,
        name="api_complete_task",
    )
]
