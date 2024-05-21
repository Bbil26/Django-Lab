from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('news', news, name='news'),
    path('news/<str:slug>/', news_detail, name='news_detail'),
    path('add/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_cart, name='remove_cart'),
    path('add_count/<int:item_id>', add_count, name='add_count'),
    path('rem_count/<int:item_id>', rem_count, name='rem_count'),
]