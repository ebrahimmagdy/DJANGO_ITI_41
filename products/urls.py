# list all proudcts app routes 
from django.urls import path
from django.conf.urls import url 
from .views import home, item

urlpatterns = [
    path('home', home.index),
    # items management urls
    path('item', item.index, name='item_list'),
    url(r'^item/(?P<item_id>\d+)/$', item.read, name='item_read'),
    path('item/add', item.create, name='item_add'),
    # path('item/save', item.save, name='item_save')
    url(r'^item/(?P<item_id>\d+)/delete$', item.delete, name='item_delete'),
    url(r'^item/category/(?P<category_id>\d+)$', item.category, name='item_category'),

    # end of items urls
]