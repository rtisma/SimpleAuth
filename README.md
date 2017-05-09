# SimpleAuth

This is a stupid simple example of an OAuth2 authorization server for use in testing.

The OAuth2 flow to be concerned with is the Client Credentials Grant. https://tools.ietf.org/html/rfc6749#section-4.4


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
