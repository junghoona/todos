from django.urls import path
from .api_views import (
    api_lst_categories,
    api_show_category,
    api_lst_goals,
    api_show_goal
)


urlpatterns = [
    path(
        "categories/",
        api_lst_categories,
        name="api_lst_categories",
    ),
    path(
        "categories/<int:id>/",
        api_show_category,
        name="api_show_category",
    ),
    path(
        "categories/<int:category_id>/goals/",
        api_lst_goals,
        name="api_lst_goals",
    ),
    path(
        "goals/<int:id>/",
        api_show_goal,
        name="api_show_goal"
    )
]
