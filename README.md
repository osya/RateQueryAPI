# Rate Query API

## Introduction

[![Build Status](https://travis-ci.org/osya/RateQueryAPI.svg?branch=master)](https://travis-ci.org/osya/RateQueryAPI/) [![Coverage Status](https://coveralls.io/repos/github/osya/RateQueryAPI/badge.svg?branch=master)](https://coveralls.io/github/osya/RateQueryAPI?branch=master)

This app implements a Flask-based HTTP API for working with Telnet. Telnet commands hardcoded in the view methods
(in the get_vendors_for_destination() and in the get_vendor_rate())

Used technologies:

- Testing:
  - Telnet were injected via Flask-Injector and mocked via pytest-mock
  - Flask-WebTest also used
- Travis CI

## Installation

First, set your app's secret key as an environment variable. For example, example add the following to ``.bashrc`` or ``.bash_profile``.

```bash
    export RATE_QUERY_API_SECRET='something-really-secret'
```

In your production environment, make sure the `RATE_QUERY_API_ENV` environment variable is set to `"prod"`.

Then run the following commands to bootstrap your environment.

```shell
    git clone http://valeriy@stash.denovolab.com/scm/rqa/alpha
    cd alpha
    pip install -r requirements/dev.txt
    python manage.py server
```

## Usage

You can execute the following curls and get result:

```shell
curl http://149.56.132.178:5000/api/v1/GetVendorsForDestination/US%20Virgin%20Islands%20Proper
curl http://149.56.132.178:5000/api/v1/GetVendorRate/US%20Virgin%20Islands%20Proper
```

### Shell

To open the interactive shell, run `python manage.py shell`

By default, you will have access to `app` model.

## Tests

To run all tests, run

```shell
    python manage.py test
```
