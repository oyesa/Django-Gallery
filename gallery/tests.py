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
    
  