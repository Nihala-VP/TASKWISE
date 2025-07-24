from django.db import models


from django.contrib.auth.models import User

class Todo(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(null=True)

    PRIORITY_CHOICES=(
        ("low","low"),
        ("medium","medium"),
        ("high","high")
    )

    priority = models.CharField(max_length=20,choices=PRIORITY_CHOICES,default="low")

    STATUS_CHOICES=(
        ("pending","pending"),
        ("in-progress","in-progress"),
        ("completed","completed")
    )

    status = models.CharField(max_length=200,default="pending")

    owner = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    












