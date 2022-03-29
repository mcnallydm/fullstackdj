from django.db import models

# Create your models here.

class Speaker(models.Model):
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=40)
    description = models.CharField(max_length=200)
    avatar = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id}:{self.name}:{self.lastname}"


class Schedule(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True)
    speaker = models.ForeignKey(
        Speaker, blank=True, on_delete=models.SET_NULL, null=True, related_name="speaker_name")
    time = models.CharField(max_length=5)
    bgcolor = models.CharField(max_length=8, blank=True)

    def __str__(self):
        return f"{self.title}:{self.description}:{self.speaker}:{self.time}:{self.bgcolor}"
