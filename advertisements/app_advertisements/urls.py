from django.urls import path
from .views import index, top_sellers

urlpatterns = [
    path('',index, name='base_page'),
    path('top-sellers', top_sellers, name='top-sellers')
    ]