from unicodedata import category
from django.db import models




# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length = 80)

    def save_location(self):
      self.save()

    def delete_location(self):
      self.delete()

    @classmethod
    def update_location(cls, id, name):
      cls.objects.filter(id=id).update(name=name)

    @classmethod
    def delete_location(cls):
      cls.objects.all()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length = 80)

    def save_category(self):
      self.save()

    def delete_category(self):
      self.delete()

    @classmethod
    def update_category(cls, id, name):
      cls.objects.filter(id=id).update(name=name)

    def __str__(self):
        return self.name

class Image(models.Model):
  name = models.CharField(max_length=80)
  description = models.CharField(max_length=100)
  location = models.ForeignKey(Location, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.name
