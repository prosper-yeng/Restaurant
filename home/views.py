from django.shortcuts import render
from .models import BackgroundImages
from menu.models import MenuItems
from about.models import AboutUs, CoreValue, WhyUs
from contact.models import Address, ContactMessage
from booking.models import Booking
from event.models import CustomerEvents,EventBackground
from special.models import Special
from gallery.models import Gallery


# Create your views here.
def index(request):
    contact_msg = None
    booking_msg = None
    background_images = BackgroundImages.objects.all()
    menuObj=MenuItems.objects.all()
    about_us = AboutUs.objects.filter(status=True).first()
    why_us = WhyUs.objects.filter(status=True)
    coreObj = CoreValue.objects.filter(status=True)
    addressObj = Address.objects.filter(status=True).first()
    #Menu
    # menuObj_Dinner=MenuItems.objects.filter(menus__contains='Dinner')
    # menuObj_Starters = MenuItems.objects.filter(menuCategory__menu_category='Starters')
    # MenuObj_Fatol=MenuItems.objects.filter(menuCategory__menu_category='Fatøl')
    menuObj_Dinner = MenuItems.objects.filter(menuSchedule__name='Middag')
    menuObj_Lunsj = MenuItems.objects.filter(menuSchedule__name='Lunsj')
    #drink
    menuObj_drinks = MenuItems.objects.filter(menu_category='Drink')
    #menuObj_mineralvann = MenuItems.objects.filter(drinkType='Minrealvann')
    #Customer events
    customer_event_obj = CustomerEvents.objects.filter(event_category='Customer Event')
    restaurant_event_obj = CustomerEvents.objects.filter(event_category='Restaurant Event')
    event_bg_obj=EventBackground.objects.all()
    # Special events
    specialObj = Special.objects.filter(status=True)

    #Gallery

    gallery_obj=Gallery.objects.filter(status=True)



    contact_msg_exists = ContactMessage.objects.filter(has_message=True).first()
    if contact_msg_exists:
        contact_msg = 'Your email has been sent. If your email contain any enquiry,' \
                    'we will respond you as soon as possible through the email you provided.'
        contact_msg_exists.has_message = False
        contact_msg_exists.save()

    booking_msg_exists = Booking.objects.filter(has_message=True).first()
    if booking_msg_exists:
        booking_msg = 'Your request for reservation has been sent. We will respond to you shortly.'
        booking_msg_exists.has_message = False
        booking_msg_exists.save()

    content = {
        'background_images': background_images,
        'menuObj': menuObj,
        'about_us': about_us,
        'why_us': why_us,
        'coreObj': coreObj,
        'addressObj': addressObj,
        'contact_msg': contact_msg,
        'booking_msg': booking_msg,
        #'menuObj_Middage': menuObj_Middag,
        'menuObj_Lunsj':menuObj_Lunsj,
        'menuObj_Dinner':menuObj_Dinner,
        'menuObj_drinks':menuObj_drinks,
        # 'menuObj_Starters':menuObj_Starters,
        # 'menuObj_Dinner':menuObj_Dinner,
        # 'MenuObj_Fatol':MenuObj_Fatol,
        'customer_event_obj':customer_event_obj,
        'event_bg_obj':event_bg_obj,
        # Special events
        'specialObj': specialObj,
        'gallery_obj': gallery_obj,
        'restaurant_event_obj':restaurant_event_obj,
        #'menuObj_mineralvann':menuObj_mineralvann,
}

    return render(request, 'home/index.html', content)
