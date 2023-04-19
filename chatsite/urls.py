from django.contrib import admin
from django.urls import path

from chat.views import frontpage

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", frontpage)
]
