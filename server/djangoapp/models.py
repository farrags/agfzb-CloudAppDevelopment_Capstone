from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    car_name = models.CharField(max_length=25, help_text='Enter car make')
    car_description = models.TextField()
    
    def __str__(self):
        return self.type

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    dealer_id = models.CharField(null=False, max_length=40,) 
    SUV = "SUV"
    Sedan = "Sedan"
    Wagon = "Wagon"  
    TYPE_CHOICES = [(SUV, 'SUV'),(Sedan, 'Sedan'),(Wagon, 'Wagon'),]
    Type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES,
    )
    Year = models.DateField
    def __str__(self):
        return self.type

# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
