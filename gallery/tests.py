from django.test import TestCase
from .models import Location, Category, Image


# Create your tests here.

class LocationTest(TestCase):
  def setUp(self):
    self.malindi = Location(name = 'Malindi')
    self.timbuktu = Location(name = 'Timbuktu')

  def tearDown(self):
    Location.objects.all().delete()

    #test if locations add to db
  def test_save_location(self):
      self.malindi.save_location()
      self.timbuktu.save_location()
      locations = Location.objects.all()
      self.assertEqual(len(locations),2)

    #test if location is deleted
  def test_delete_location(self):
      self.malindi.save_location()
      locations1= Location.objects.all()
      self.assertEqual(len(locations1),1)
      self.malindi.delete_location()
      locations2= Location.objects.all()
      self.assertEqual(len(locations2),1)


#Test Category
class CategoryTest(TestCase):
  def setuP(self):
    self.tech = Category(name = 'tech')
    self.art = Category(name = 'art')

  def tearDown(self):
    Category.objects.all().delete()

    #test if category adds to db
  def test_save_category_method(self):
    self.tech.save_category()
    self.art.save_category()
    categories = Category.objects.all()
    self.assertTrue(len(categories) == 2)

      #test if category is deleted    
  def test_delete_category(self):
    self.tech.save_category()
    self.art.save_category()
    categories1 = Category.objects.all()
    self.assertEqual(len(categories1),2)
    self.tech.delete_category()
    categories2 = Category.objects.all()
    self.assertEqual(len(categories2),1)
      
      #test if category name is updated
  def test_update_category(self):
        self.tech.save_category()
        self.tech.update_category(self.tech.id,'technology')
        update = Category.objects.get(name = "technology")
        self.assertEqual(update.name, 'technology')