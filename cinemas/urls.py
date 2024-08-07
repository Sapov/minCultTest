from django.contrib import admin
from django.urls import path, include
from cinemas.views import CinemasListView, CinemasDetail, CinemasDetailAPIView, CinemasSearchName

app_name = 'Cinemas'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('search/', CinemasSearchName.as_view(), name='search'),
    path('list/', CinemasListView.as_view(), name='cinemalist'),
    path('list/<int:pk>/', CinemasDetail.as_view(), name='cinema'),
    path('listdetail/<int:pk>/', CinemasDetailAPIView.as_view(), name='cinema_detail'),

]
