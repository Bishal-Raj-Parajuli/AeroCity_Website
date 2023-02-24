from django.db import models

# Create your models here.
class RoomTypes(models.Model):
    Id = models.BigAutoField(primary_key=True)
    TypeName = models.CharField(max_length=50)
    TypeImage = models.ImageField(upload_to='uploads/')
    TypeDescription = models.TextField(blank=False,max_length=300)

    def __str__(self):
        return self.TypeName

class RoomsDetails(models.Model):
    Id = models.BigAutoField(primary_key=True)
    RoomsNo = models.IntegerField()
    RoomType = models.ForeignKey(RoomTypes, on_delete=models.DO_NOTHING)
    AvailabaleFrom = models.DateField()
    AvailableTo = models.DateField()

    def __str__(self):
        return self.RoomType + '-(' + self.RoomsNo + ')'

class AboutDetails(models.Model):
    Id = models.BigAutoField(primary_key=True)
    PhoneNo = models.CharField(max_length=200)
    Email = models.EmailField()
    Adddress = models.CharField(max_length=100)

    def __str__(self):
        return str(self.Id)

class CustomerDetails(models.Model):
    Id = models.BigAutoField(primary_key=True)
    FullName = models.CharField(max_length=50)
    Address = models.CharField(max_length=20)
    PhoneNo = models.IntegerField()

    def __str__(self):
        return self.FullName

class AboutDescriptions(models.Model):
    Id= models.BigAutoField(primary_key=True)
    Titile = models.CharField(max_length=100)
    Description = models.TextField()

class RoomBookings(models.Model):
    Id = models.BigAutoField(primary_key=True)
    CustomerId = models.ForeignKey(CustomerDetails, on_delete=models.DO_NOTHING)
    BookedForm = models.DateField()
    BookedTo = models.DateField()
    NoOfPax = models.IntegerField()
    RoomType = models.ForeignKey(RoomTypes, on_delete=models.DO_NOTHING)


class HomeSliderImages(models.Model):
    Id = models.BigAutoField(primary_key=True)
    SliderImages = models.ImageField(upload_to='media/uploads/index/')

class AboutHeroImage(models.Model):
    Id = models.BigAutoField(primary_key=True)
    SliderImage = models.ImageField(upload_to='media/uploads/about/')

class RoomHeroImage(models.Model):
    Id = models.BigAutoField(primary_key=True)
    SliderImage = models.ImageField(upload_to='media/uploads/room/')

class ContactHeroImage(models.Model):
    Id = models.BigAutoField(primary_key=True)
    SliderImages = models.ImageField(upload_to='media/uploads/contact/')

class GalleryImages(models.Model):
    Id= models.BigAutoField(primary_key=True)
    SliderImages = models.ImageField(upload_to='media/uploads/gallery/')
    GalleryTitle = models.CharField(max_length=50)

