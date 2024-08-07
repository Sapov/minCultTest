from django.contrib import admin
from django.urls import path, include
from cinemas.views import CinemasListView, CinemasDetail, CinemasDetailAPIView, CinemasSearchName, CinemasSearchAddress

app_name = 'Cinemas'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('search_name/', CinemasSearchName.as_view(), name='search_name'),
    path('search_address/', CinemasSearchAddress.as_view(), name='search_address'),
    path('list/', CinemasListView.as_view(), name='cinemalist'),
    path('list/<int:pk>/', CinemasDetail.as_view(), name='cinema'),
    path('listdetail/<int:pk>/', CinemasDetailAPIView.as_view(), name='cinema_detail'),

]
