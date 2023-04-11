from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from .views import FacebookLogin, GoogleLogin

# from rest-auth
from rest_auth.views import PasswordResetView, PasswordResetConfirmView
from rest_auth.registration.views import VerifyEmailView

from allauth.account.views import confirm_email
# my cystom verification handler
from .email_confirmation import ConfirmEmailView


urlpatterns = [




    # jwt
    re_path(r'^api-token-auth/', obtain_jwt_token),
    re_path(r'^api-token-refresh/', refresh_jwt_token),

    # accounts
    re_path(r'^accounts/', include('allauth.urls'),
            name='socialaccount_signup'),
    # rest urls
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),



    # email confirmation sent
    re_path(r'^account-confirm-email/$', VerifyEmailView.as_view(),
            name='account_email_verification_sent'),

    # head ache confirmed
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', confirm_email,
            name='account_confirm_email'),



    # reset password
    # re_path(r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),
    # name='password_reset_confirm'),

    path(r'password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path(r'password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),


    # Social auth
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),


]
