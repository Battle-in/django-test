from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    #photo = models.ImageField(upload_to="photo/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + ' ' + self.title

    def to_json(self):
        return {
            #'id': self.indexes,
            'title': self.title,
            'content': self.content,
            'time_create': self.time_create.__str__(),
            'time_update': self.time_update.__str__(),
        }