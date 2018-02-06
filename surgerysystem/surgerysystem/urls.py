from django.contrib import admin
from django.urls import include, path, re_path
from surgerysystem.views import hello, current_datetime, hours_ahead

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('time/', current_datetime),
    path('another-time-page/', current_datetime),
    re_path('time/plus/(\d{1,2})/$', hours_ahead),
]
