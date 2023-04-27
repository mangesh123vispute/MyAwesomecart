
from django.urls import path
from . import views

urlpatterns = [
path("",views.index,name='shopHome'),
path("about/",views.about,name='Aboutus'),
path("contact/",views.contact,name='Contactus'),
path("tracker",views.tracker,name='TrakingStatus'),
path("search/",views.search,name='Search'),
path("productView/",views.productView,name='productView'),
path("checkout/",views.checkout,name='Checkout'),
]
