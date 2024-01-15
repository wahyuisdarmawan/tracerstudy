from django.db import models
from school.models import School, Vocation

# Create your models here.
class Alumni(models.Model):
    school = models.OneToOneField(School, related_name='alumni', on_delete=models.CASCADE)
    vocation = models.OneToOneField(Vocation, related_name='alumni', on_delete=models.CASCADE)
    nisn = models.IntegerField(blank=True, null=True)
    nik = models.IntegerField(blank=True, null=True)
    nama_alumni = models.CharField(max_length=255, null=True)
    
    male = 'laki-laki'
    female = 'perempuan'
    CHOICES_GENDER = (
        (male, 'laki-laki'),
        (female, 'perempuan'),
    )
    gender = models.CharField(max_length=20, choices=CHOICES_GENDER, null=True)
    tgl_lahir = models.CharField(max_length=50, blank=True, null=True)
    thn_lulus = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ('nama_alumni', 'thn_lulus',)
    
    def __str__(self):
        return self.nisn