from django.contrib import admin
from app import models

# Register your models here.
admin.site.register([
    models.RoomTypes, 
    models.RoomsDetails,
    models.AboutDetails,
    models.CustomerDetails,
    models.AboutDescriptions,
    models.RoomBookings,
    models.HomeSliderImages, 
    models.ContactHeroImage,
    models.RoomHeroImage,
    models.AboutHeroImage,
    models.GalleryImages
    ])
