from django.contrib import admin
from django.urls import path, include
from cinemas.views import  CinemasViewSet
from rest_framework import permissions
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

app_name = 'Cinemas'

schema_view = get_schema_view(
    openapi.Info(
        title="Cinemas API",
        default_version='v1',
        description="База данных кинотеатров",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="sasha@mail.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.SimpleRouter()
router.register(r'cinema', CinemasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('search_name/', CinemasSearchName.as_view(), name='search_name'),
    # path('search_address/', CinemasSearchAddress.as_view(), name='search_address'),
    path('v1/', include(router.urls), name='cinema_'),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
