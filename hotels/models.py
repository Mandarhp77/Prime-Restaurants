from django.db import models

class Hotels(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    items = models.CharField(max_length=50)
    lat_long = models.CharField(max_length=50)
    full_details = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'hotels'
        verbose_name_plural = "Hotels"


