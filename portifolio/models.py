from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    

class location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length =30)
    description = models.TextField()
    category = models.ForeignKey(category)
    location = models.ForeignKey(location)
    pub_date = models.DateTimeField(auto_now_add=True)




        



     


