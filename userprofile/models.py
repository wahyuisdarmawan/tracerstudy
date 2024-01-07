from django.db import models
from django.contrib.auth.models import User
from school.models import School, Vocation

# Create your models here.
class Userprofile(models.Model):
    admin = 'admin'
    staff = 'staff'
    alumni = 'alumni'

    CHOICES_ROLE = (
        (admin, 'admin'),
        (staff, 'staff'),
        (alumni, 'alumni'),
    )

    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=CHOICES_ROLE, default=admin, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('user',)

    def __str__(self):
        return self.role

class Alumnibio(models.Model):
    user = models.OneToOneField(User, related_name='alumnibio', on_delete=models.CASCADE)
    school = models.OneToOneField(School, related_name='alumnibio', on_delete=models.CASCADE)
    vocation = models.OneToOneField(Vocation, related_name='alumnibio', on_delete=models.CASCADE)
    nisn = models.IntegerField(unique=True)
    nik = models.IntegerField(unique=True, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    tgl_lahir = models.DateField(blank=True, null=True)
    tingkat_pendidikan = models.CharField(max_length=100, null=True)
    thn_lulus = models.CharField(max_length=100, null=True)

    class Meta:
        ordering = ('thn_lulus',)
    
    def __str__(self):
        return self.nisn
