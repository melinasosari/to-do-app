from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=254)
    discription = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    class Meta:
       ordering = ['is_done']
    
    