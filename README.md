# SimpleAuth

[![](https://images.microbadger.com/badges/image/dandric/simpleauth.svg)](https://microbadger.com/images/dandric/simpleauth "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/dandric/simpleauth.svg)](https://microbadger.com/images/dandric/simpleauth "Get your own version badge on microbadger.com")


This is a stupid simple example of an OAuth2 authorization server for use in testing. You can fire this server up, and it will have a test token already present with a super long TTL. You can use the client credentials to create your own tokens with your own scopes if required for your own testing as well. 

The primary OAuth2 flow I was concerned with is the Client Credentials Grant. https://tools.ietf.org/html/rfc6749#section-4.4
Though there is no reason you cannot register different applications using the different flows all supported by the django-oauth-tooklit. 

The server is build with [Django](https://www.djangoproject.com) and uses the [django-oauth-toolkit](http://django-oauth-toolkit.readthedocs.io/en/latest/index.html)

For documentation on registering applications, please see: http://django-oauth-toolkit.readthedocs.io/en/latest/tutorial/tutorial_01.html#create-an-oauth2-client-application

# Running
This simple server is available as a docker container

```bash
docker pull dandric/simpleauth
docker run -p 8000:8000 dandric/simpleauth

```

# Django Admin

```
username: test
password: test_123_password
```

# Client Credentials
```
application name: test
client_id: clientId
client_secret: clientSecret
```


# Tokens
When running the app, it will already have a valid token `testToken` with a TTL of several years. The scopes assigned to this token will be `upload` and `download`

## Creation

### Request
To generate a new token with all available scopes:

```bash
curl --request POST \
  --url http://localhost:8000/o/token/ \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data 'grant_type=client_credentials&client_id=clientId&client_secret=clientSecret'
```

### Response

```json
{
	"access_token": "Cukj8hbZr9trVEOhwHbak4S3NwTIWN",
	"scope": "test.download test.upload",
	"expires_in": 36000,
	"token_type": "Bearer"
}
```

## Introspection
The spec for token introspection still has no adoption from frameworks, so I've included a really simple `check_token` endpoint that returns the scopes for a valid token. 

### Request

```bash
curl --request POST \
  --url http://localhost:8000/check_token/ \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data token=testToken
```

### Response 

```text
download,upload
```
