import json
from .models import Task
from django.http import JsonResponse
from common.json import ModelEncoder
from django.views.decorators.http import require_http_methods


class TaskListEncoder(ModelEncoder):
    model = Task
    properties = [
        "name",
        "due_date",
        "status"
    ]

    def get_extra_data(self, o):
        return {"status": o.status.name}


class TaskDetailEncoder(ModelEncoder):
    model = Task
    properties = [
        "name",
        "description",
        "created",
        "due_date",
        "status"
    ]

    def get_extra_data(self, o):
        return {"status": o.status.name}


@require_http_methods(["GET", "POST"])
def api_lst_tasks(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        return JsonResponse(
            {"tasks": tasks},
            encoder=TaskListEncoder
        )
    else:
        content = json.loads(request.body)
        task = Task.create(**content)
        return JsonResponse(
            task,
            encoder=TaskDetailEncoder,
            safe=False
        )


@require_http_methods(["DELETE", "GET"])
def api_show_task(request, id):
    if request.method == "GET":
        task = Task.objects.get(id=id)
        return JsonResponse(
            task,
            encoder=TaskDetailEncoder,
            safe=False,
        )
    elif request.method == "DELETE":
        count, _ = Task.objects.filter(id=id).delete()
        return JsonResponse(
            {"deleted": count > 0}
        )


@require_http_methods(["PUT"])
def api_proceed_task(request, id):
    task = Task.objects.get(id=id)
    task.proceed()
    return JsonResponse(
        task,
        encoder=TaskDetailEncoder,
        safe=False
    )


@require_http_methods(["PUT"])
def api_complete_task(request, id):
    task = Task.objects.get(id=id)
    task.complete()
    return JsonResponse(
        task,
        encoder=TaskDetailEncoder,
        safe=False
    )
