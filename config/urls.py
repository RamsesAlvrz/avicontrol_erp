# urls.py (Principal del proyecto)
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('granjas/', include(('granjas.urls', 'granjas'), namespace='granjas')),
    
    # Redirige la raíz ('') hacia '/granjas/granjas/'
    path('', RedirectView.as_view(pattern_name='granjas:granja_list', permanent=False)),
]