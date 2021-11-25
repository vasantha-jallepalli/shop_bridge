from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('item/add/v1', csrf_exempt(views.add_item), name='add_item'),
    path('item/<int:item_id>/update/v1', csrf_exempt(views.update_item), name='update_item'),
    path('item/<int:item_id>/delete/v1', csrf_exempt(views.delete_item), name='delete_item'),
    path('items/v1', csrf_exempt(views.get_items), name='get_items'),
]
