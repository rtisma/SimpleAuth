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

## Request
To generate a new token with all available scopes:

```bash
curl --request POST \
  --url http://localhost:8000/o/token/ \
  --header 'content-type: application/x-www-form-urlencoded' \
  --data 'grant_type=client_credentials&client_id=clientId&client_secret=clientSecret'
```

## Response

```json
{
	"access_token": "Cukj8hbZr9trVEOhwHbak4S3NwTIWN",
	"scope": "test.download test.upload",
	"expires_in": 36000,
	"token_type": "Bearer"
}
```
