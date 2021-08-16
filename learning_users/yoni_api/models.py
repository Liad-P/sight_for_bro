from django.db import models

# Create your models here.
class yoni_class(models.Model):
    nickname = models.CharField(max_length=200)
    brother = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brother} - {self.nickname}"
