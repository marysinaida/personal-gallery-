from django.db import models
import datetime as dt

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()
    
    def delete_category(self):
        self.delete()

    def update_category(self):
        self.update()

class Location(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.update_location()

    @classmethod
    def get_location(cls):
        location = cls.objects.all()
        return location

class Image(models.Model):
    title = models.CharField(max_length =30)
    description = models.TextField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)
    pub_date = models.DateTimeField(auto_now_add=True)
    category_image = models.ImageField(upload_to = 'photos/')

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self):
        self.update_image()
    
    @classmethod
    def search_by_category(cls,search_term):
        portifolio = cls.objects.filter(category__name__icontains=search_term)
        return portifolio

    @classmethod
    def get_image_by_id(cls,id):
        img_id = cls.object.get(pk=id)
        return img_id
    




        



     


