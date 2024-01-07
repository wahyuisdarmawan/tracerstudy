from django.db import models

# Create your models here.
class School(models.Model):
    npsn = models.IntegerField(unique=True)
    name = models.CharField(max_length=100, null=True)
    address = models.TextField()
    provinsi = models.CharField(max_length=100, null=True)
    kabupaten = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Vocation(models.Model):
    bidang = models.CharField(max_length=255, null=True)
    program = models.CharField(max_length=255, null=True)
    kompetensi = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.kompetensi