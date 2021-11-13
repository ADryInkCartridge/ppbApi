from django.db import models


from django.db import models
class Images(models.Model):
    filename = models.TextField()
    imagedata = models.TextField()
    password = models.TextField()
    def __str__(self):
        return self.filename
