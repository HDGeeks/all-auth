from django.contrib import admin
from django.urls import path, include , re_path
from rest_framework import permissions

# simple jwt token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

# api documentation
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


# from rest-auth
from rest_auth.registration.views import SocialLoginView ,SocialLoginSerializer
from rest_auth.views import PasswordResetView, PasswordResetConfirmView
from rest_auth.registration.views import VerifyEmailView, RegisterView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


# all-auth social login
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.account.views import confirm_email


# my cystom verification handler
from .email_confirmation import ConfirmEmailView 


# Create your views here.
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer
    #callback_url = 'CALLBACK_URL_YOU_SET_ON_GOOGLE'

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
google_login = GoogleLogin.as_view()

   

  
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
    #path('home',home ,name='home'),
    path('admin/', admin.site.urls),

    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

   

    # email confirmation sent
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(),
    name='account_email_verification_sent'),
    
    # head ache confirmed
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', confirm_email ,
    name='account_confirm_email'),

    #re_path(r'^verify-email/$', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    #re_path(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$', ConfirmEmailView.as_view(), name='account_confirm_email'),

     # reset password
    re_path(r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),
     name='password_reset_confirm'),

    # Social auth
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),


    # simple jwt token system
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    

    # API documentation urls
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    

]
