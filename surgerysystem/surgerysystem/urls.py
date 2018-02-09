from django.contrib import admin
from django.urls import include, path, re_path
from surgerysystem.views import position, checkin, delete, doctors, help_view, login

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('position/(\d{3})/$', position),
    re_path('checkin/(\d{3})/$', checkin),
    re_path('checkin/(\d{3})/(\d{2})/$', checkin),
    re_path('delete/(\d{3})/$', delete),
    path('doctors/', doctors),
    path('help/', help_view),
    re_path('login/(\d{2})/$', login)
]
