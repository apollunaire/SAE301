from django.db import models


# Create your models here.
class lampe(models.Model):
    on = models.CharField(max_length=10)
    off = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = "lampe"

