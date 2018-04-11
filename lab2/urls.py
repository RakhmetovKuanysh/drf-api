from django.contrib import admin
from django.urls import path, include, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todos/', include("todo.urls")),
    path('api/contacts/', include("contacts.urls")),
    re_path(r'^api-auth/', include('rest_framework.urls'))
]
