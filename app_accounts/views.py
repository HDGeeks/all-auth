# all-auth social login
from allauth.socialaccount.providers.facebook.views import \
    FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.shortcuts import render
from rest_auth.registration.views import SocialLoginSerializer, SocialLoginView


# Create your views here.



class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    serializer_class = SocialLoginSerializer

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


fb_login = FacebookLogin.as_view()


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
