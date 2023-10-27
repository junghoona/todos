from tasks.models import Task
from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    timeframe = models.CharField(max_length=50)

    def get_api_url(self):
        return reverse("api_show_category", kwargs={"id": self.id})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id", "name"]


class Goal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    urgency = models.PositiveSmallIntegerField()
    category = models.ForeignKey(
        Category,
        related_name="goals",
        on_delete=models.PROTECT,
    )

    def get_api_url(self):
        return reverse("api_show_goal", kwargs={"id": self.id})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id", "name"]
