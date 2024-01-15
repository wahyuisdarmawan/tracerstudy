from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userprofile(models.Model):
    admin = 'admin'
    staff = 'staff'

    CHOICES_ROLE = (
        (admin, 'admin'),
        (staff, 'staff'),
    )

    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=CHOICES_ROLE, default=admin, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('user',)

    def __str__(self):
        return self.role