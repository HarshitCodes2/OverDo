from django.db import models

# Create your models here.

class Todos(models.Model):
    title = models.CharField(max_length=500, null=False, blank=False)
    description = models.TextField()
    isCompleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-createdAt']
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

