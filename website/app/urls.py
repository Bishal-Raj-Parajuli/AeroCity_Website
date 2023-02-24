from django.urls import path
from app import views as appView

urlpatterns = [
    path('', appView.Home, name='home' ),
    path('rooms', appView.Rooms, name='rooms' ),
    path('aboutus', appView.AboutUs, name='about_us' ),
    path('contact', appView.Contact, name='contact' )
]