from django.db import models


class CreatedUpdatedMixin(models.Model):
    """
    CreatedUpdatedMixin
        Used to add created and updated fields to the models
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
