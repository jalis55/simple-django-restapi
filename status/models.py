from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status(models.Model):
    text=models.CharField(max_length=200,blank=True,null=True)
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    created_at=models.DateField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Status"
