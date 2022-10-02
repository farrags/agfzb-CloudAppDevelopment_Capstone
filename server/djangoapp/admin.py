from django.contrib import admin
# from .models import related models
from .models import CarMake , CarModel

# Register your models here.

class CarModelInline (admin.StackedInline):
    model = CarModel
    extra = 0

class CarModelAdmin(admin.ModelAdmin):
    inlines = [
        CarModelInline,
    ]

admin.site.register(CarMake, CarModelAdmin)
admin.site.register(CarModel)


# CarMakeAdmin class with CarModelInline

# Register models here
