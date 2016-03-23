# edx-api-client

Python interface for edX REST APIs

## Installation

To get the latest stable release from PyPi

```bash
pip install edx-api-client (not yet deployed on pypi)
```

To get the latest commit from GitHub

```bash
pip install -e git+git://github.com/mitodl/edx-api-client.git#egg=edx-api-client
```


## Tests

If you're going to run integration tests, you'll need to specify the
`ACCESS_TOKEN` environment variable to a valid access token.

You can create an access token (and the associated oauth app, and
grant) through the edX admin.

If you're going to run the integration tests against localhost, you'll
additionally need to turn off TLS validation with the environment
variable `OAUTHLIB_INSECURE_TRANSPORT=1`. This will skip the HTTPS
validation which is required by the OAuth spec.

## Release Notes

