from oauth2_provider.models import AccessToken
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django import forms
from django.core.exceptions import ObjectDoesNotExist
import json


class TokenForm(forms.Form):
    token = forms.CharField(max_length=255)


def check_token(request):
    '''
    Let's match the spring security endpoint
    :param request: 
    :return: 
    '''

    if request.method == 'POST':
        form = TokenForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']

            try:
                access_token = AccessToken.objects.get(token=token)
            except ObjectDoesNotExist:
                return HttpResponseNotFound(content=json.dumps({'error': 'NOT FOUND!', 'message': 'Go away.'}),
                                            content_type='application/json')

            test_token_response = {
                "exp": 9999999999,
                "user_name": "test@test.test",
                "client_id": "clientId",
                "scope": access_token.scope.split(",")
            }
            print(json.dumps(test_token_response))
            return HttpResponse(content=json.dumps(test_token_response),
                                content_type='application/json')

    return HttpResponseBadRequest(content=json.dumps({'error': 'ERROR!', 'message': 'Go away.'}),
                                  content_type='application/json')
