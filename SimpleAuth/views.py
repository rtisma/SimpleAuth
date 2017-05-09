from oauth2_provider.models import AccessToken
from django.http import HttpResponse, HttpResponseBadRequest
from django import forms


class TokenForm(forms.Form):
    token = forms.CharField(max_length=255)


def check_token(request):
    if request.method == 'POST':
        form = TokenForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            accessToken = AccessToken.objects.get(token=token)
            return HttpResponse(accessToken.scope)

    return HttpResponseBadRequest('Go away.')
