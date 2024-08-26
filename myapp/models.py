from django.db import models
from django.utils import timezone

class DummyData(models.Model):
    column1 = models.CharField(max_length=100)
    column2 = models.CharField(max_length=100)
    column3 = models.CharField(max_length=100)
    column4 = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.column1