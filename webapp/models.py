from django.db import models

# Create your models here.


class Greetings(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    url = models.URLField(max_length=500)
    class Meta:
        db_table = 'greetings'

    def __str__(self):
        return self.title
