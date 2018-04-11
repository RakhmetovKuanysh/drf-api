from django.urls import path, re_path
from . import views

urlpatterns = [
    path('contacts/', views.contacts_list),
    re_path(r'^contacts/(?P<contact_id>[0-9]+)/$', views.contact_detail),
]