from django.shortcuts import render
from app import models;



# Create your views here.
def Home(request):
    roomTypes = models.RoomTypes.objects.all()
    homeImageSlider = models.HomeSliderImages.objects.all()
    aboutDescription = models.AboutDescriptions.objects.all()
    gallery = models.GalleryImages.objects.all()
    contact = models.AboutDetails.objects.last()

    context = {
        'room': roomTypes,
        'imageSlider': homeImageSlider,
        'aboutDescription': aboutDescription,
        'gallery': gallery,
        'contact': contact
    }
    return render(request, 'app/index.html', context=context)


def Rooms(request):
    roomTypes = models.RoomTypes.objects.all()
    gallery = models.GalleryImages.objects.all()
    contact = models.AboutDetails.objects.last()
    roomsHeroImage = models.RoomHeroImage.objects.last()

    context = {
        'room': roomTypes,
        'gallery': gallery,
        'contact': contact,
        'roomHeroImage': roomsHeroImage
    }
    return render(request, 'app/Rooms.html',  context=context)

def AboutUs(request):
    aboutHeroImage = models.AboutHeroImage.objects.last()
    aboutDescription = models.AboutDescriptions.objects.all()
    contact = models.AboutDetails.objects.last()
    

    context = {
        'aboutHeroImage': aboutHeroImage,
        'aboutDescription': aboutDescription,
        'contact': contact
    }
    return render(request, 'app/AboutUs.html', context=context)


def Contact(request):
    contact = models.AboutDetails.objects.last()
    contactHeroImage = models.AboutHeroImage.objects.last()
    context = {
        'contact': contact,
        'contactHeroImage': contactHeroImage
    }
    return render(request, 'app/contact.html', context=context)