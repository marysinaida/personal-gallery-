from django.test import TestCase
from .models import Image,Location,Category


# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        pass
        
        # Creating a new category
        self.new_category = Category(name='travel')
        self.new_category.save()
        
        
        # Creating a new location
        self.new_location = Location(name='nairobi')
        self.new_location.save()
        
        # Creating new Image
        self.new_image = Image(title='Image1',
        description='This is my first image to upload')
        self.new_image.save()
    
    
    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()


class LocationTestClass(TestCase):
    """
    A test that checks for the behaviour of the image class
    """
    def setUp(self):
        pass

class CategoryTestClass(TestCase):
    """
    A test  that checks the functionality of the image class
    """
    def setUp(self):
        pass
        
