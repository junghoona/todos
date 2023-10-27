from django.db import models
from django.urls import reverse


class Status(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("id",)


class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True)
    status = models.ForeignKey(
        Status,
        related_name="tasks",
        on_delete=models.PROTECT,
    )

    @classmethod
    def create(cls, **kwargs):
        kwargs["status"] = Status.objects.create(name="TO-DO")
        task = cls(**kwargs)
        task.save()
        return task

    def proceed(self):
        status = Status.objects.create(name="IN PROGRESS")
        self.status = status
        self.save()

    def complete(self):
        status = Status.objects.create(name="COMPLETED")
        self.status = status
        self.save()

    def get_api_url(self):
        return reverse("api_show_task", kwargs={"id": self.id})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("name",)
