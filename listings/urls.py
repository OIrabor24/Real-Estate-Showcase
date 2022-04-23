from django.urls import path 

from . import views

#/listings
urlpatterns = [ 
    path('', views.index, name='listings'), #/listings
    path('<int:listing_id>', views.listing, name='listing'), #/listing/<int:pk>
    path('search/', views.search, name='search'),
] 