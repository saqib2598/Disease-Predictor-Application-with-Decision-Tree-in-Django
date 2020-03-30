from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.index, name='dp_app-index'),
    path('acutecholecystitis/',views.acutecholecystitis,name='dp_app-acute'),
    path('bronchitis/',views.bronchitis,name='dp_app-bronchitis'),
    path('diabetes/',views.diabetes,name='dp_app-diabetes'),
    path('hepatitisC/',views.hepatitisC,name='dp_app-hepatitisC'),
]