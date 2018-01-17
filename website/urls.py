from django.contrib import admin
from django.urls import path,include

urlpatterns = [
	path(r'vuelos/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path(r'api/', include('polls.api.urls'))
]
