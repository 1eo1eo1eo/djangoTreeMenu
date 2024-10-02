from pyexpat import model
from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    named_url = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="children",
    )
    menu = models.ForeignKey(
        to=Menu,
        related_name="items",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
