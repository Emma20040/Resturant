from django.db import models

# model for item type  e.g breakfast or launch
class ItemType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

# class for food item
class Food(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=20, blank= False, null= False)
    image = models.ImageField(upload_to='uploads/food')
    category = models.ForeignKey(ItemType, on_delete=models.SET_NULL, null=True )

    def __str__(self):
        return self.name
