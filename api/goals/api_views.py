import json
from .models import Goal, Category
from django.http import JsonResponse
from common.json import ModelEncoder
from django.views.decorators.http import require_http_methods


class CategoryListEncoder(ModelEncoder):
    model = Category
    properties = [
        "name",
        "timeframe",
    ]


class CategoryDetailEncoder(ModelEncoder):
    model = Category
    properties = [
        "name",
        "description",
        "timeframe"
    ]


@require_http_methods(["GET", "POST"])
def api_lst_categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return JsonResponse(
            {"categories": categories},
            encoder=CategoryListEncoder
        )
    else:
        content = json.loads(request.body)

        category = Category.objects.create(**content)
        return JsonResponse(
            category,
            encoder=CategoryListEncoder,
            safe=False
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def api_show_category(request, id):
    if request.method == "GET":
        category = Category.objects.get(id=id)
        return JsonResponse(
            {"category": category},
            encoder=CategoryDetailEncoder,
            safe=False
        )
    elif request.method == "DELETE":
        count, _ = Category.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)

        Category.objects.filter(id=id).update(**content)
        category = Category.objects.get(id=id)
        return JsonResponse(
            category,
            encoder=CategoryDetailEncoder,
            safe=False
        )


class GoalListEncoder(ModelEncoder):
    model = Goal
    properties = ["name"]


class GoalDetailEncoder(ModelEncoder):
    model = Goal
    properties = [
        "name",
        "description",
        "created",
        "deadline",
        "urgency",
        "category",
    ]

    encoders = {
        "category": CategoryListEncoder()
    }


@require_http_methods(["GET", "POST"])
def api_lst_goals(request, category_id):
    if request.method == "GET":
        try:
            goal = Goal.objects.filter(category=category_id)
        except Goal.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid ID: There are no goals in this category"},
                status=400
            )
        return JsonResponse(
            goal,
            encoder=GoalListEncoder,
            safe=False
        )
    else:
        content = json.loads(request.body)
        try:
            category = Category.objects.get(id=category_id)
            content["category"] = category
        except Category.DoesNotExist:
            return JsonResponse(
                {"message": "Invalid ID: Category Does not exist"},
                status=400
            )
        goal = Goal.objects.create(**content)
        return JsonResponse(
            goal,
            encoder=GoalDetailEncoder,
            safe=False
        )


@require_http_methods(["DELETE", "GET", "PUT"])
def api_show_goal(request, id):
    if request.method == "GET":
        goal = Goal.objects.get(id=id)
        return JsonResponse(
            goal,
            encoder=GoalDetailEncoder,
            safe=False
        )
    elif request.method == "DELETE":
        count, _ = Goal.objects.filter(id=id).delete()
        return JsonResponse({"deleted": count > 0})
    else:
        content = json.loads(request.body)

        if "category" in content:
            try:
                category = Category.objects.get(id=content["category"])
                content["category"] = category
            except Category.DoesNotExist:
                return JsonResponse(
                    {"message": "Invalid ID: Category Does not exist"},
                    status=400
                )

        Goal.objects.filter(id=id).update(**content)
        goal = Goal.objects.get(id=id)
        return JsonResponse(
            goal,
            encoder=GoalDetailEncoder,
            safe=False
        )
