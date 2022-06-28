from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static

# api documentation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    # API schema for our accounts

    openapi.Info(
        title="Accounts API",
        default_version='v1',
        description="user accounts API description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="dannyhd88@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # rest
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('root/', include('app_accounts.urls')),

    # API documentation urls
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
