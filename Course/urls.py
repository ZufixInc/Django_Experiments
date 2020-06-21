from django.contrib import admin
from django.urls import path
from Course.views import *

urlpatterns = [
	path('', view_index),
	path('admin/', admin.site.urls),
]
