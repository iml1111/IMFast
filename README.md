![imfast](https://user-images.githubusercontent.com/29897277/178490130-561c60cd-5e77-47c8-a5a4-239c908a1b13.png)
# IMFast
**Boilerplate for Large Scale FastAPI Web Backend Structure (Edited 2022-07-12)**

This is boilerplate, assuming you are building a large-scale application server using `FastAPI`.

I look forward to your feedback.

If you use Mongodb with `Motor`, I recommend this.

- [IMFast-Motor](https://github.com/iml1111/IMFast-Motor)

## Dependency

- python 3.9+
- FastAPI >= 0.78
- uvicorn >= 0.18.2

In IMFast, the following libraries are additionally installed for convenient development.

```
- python-dotenv
- orjson
- pytest
- jinja2
- loguru
- python-jose[cryptography]
- passlib[bcrypt]
- requests
- httpx
- trio
```

## Environment variables

To run the application, you need to set the following environment variables.

For the `python-dotenv` library, you can write an `dev.env` file in the same path as `settings.py`, or you can directly enter an environment variable.

```
- APP_NAME
- {APP_NAME}_SECRET_KET
- {APP_NAME}_SLOW_API_TIME
...
```

But, since default values are defined for all environment variables, it can be executed immediately.

## Get Started

```shell
$ git clone https://github.com/iml1111/IMFast
$ cd IMFast/

# virtualenv (if necessary)
$ python3 -m venv venv
$ source ./venv/bin/activate

# Install dependency
$ cd IMFlask/
$ pip install -r requirements.txt

# App test
$ ./imfast test
test/test_basics.py::test_app_exists PASSED                                        [  9%]
test/test_basics.py::test_index_page[asyncio] PASSED                               [ 18%]
test/test_basics.py::test_index_page[trio] PASSED                                  [ 27%]
test/test_basics.py::test_404_page[asyncio] PASSED                                 [ 36%]
test/test_basics.py::test_404_page[trio] PASSED                                    [ 45%]
test/test_sample.py::test_get_champion[asyncio] PASSED                             [ 54%]
test/test_sample.py::test_get_champion[trio] PASSED                                [ 63%]
test/test_sample.py::test_create_champion[asyncio] PASSED                          [ 72%]
test/test_sample.py::test_create_champion[trio] PASSED                             [ 81%]
test/test_sample.py::test_bad_request_api[asyncio] PASSED                          [ 90%]
test/test_sample.py::test_bad_request_api[trio] PASSED                             [100%]

11 passed in 0.24s.

$ App start
$ ./imfast run
INFO:     Will watch for changes in these directories:
INFO:     Uvicorn running on http://127.0.0.1:5000 (Press CTRL+C to quit)
INFO:     Started reloader process [4053] using StatReload
INFO:     Started server process [4093]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Commands

You can try various commands in the form of `imfast <command>`. The command codes are written in `main.py`.

```shell
$ ./imfast --help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

  Command Groups

Options:
  --help  Show this message and exit.

Commands:
  init-db   Sample command
  prod-run  Please use 'imfast prod-run'.
  routes    Print all routes
  run       Please use 'imfast run'.
  test      Run tests
  
$ ./imfast routes
# Routes
Path ======================= Methods ======= Name ==============
/                           {'GET'}          index
/api/auth/me                {'GET'}          me
/api/auth/refresh           {'POST'}         refresh
/api/auth/signin            {'POST'}         login
/api/v1/champion            {'GET'}          get_champion
/api/v1/champion            {'POST'}         create_champion
/api/v1/sample/bad_request  {'PUT'}          bad_request_api
/api/v1/sample/error        {'POST'}         error
/api/v1/sample/slow         {'GET'}          slow
/docs                       {'HEAD', 'GET'}  swagger_ui_html
/docs/oauth2-redirect       {'HEAD', 'GET'}  swagger_ui_redirect
/openapi.json               {'HEAD', 'GET'}  openapi
/redoc                      {'HEAD', 'GET'}  redoc_html
```

`IMFast/imfast` is simple shell script, Help your fastapi development. 

If you want to check the script detail, click [here.](https://github.com/iml1111/IMFast/blob/main/IMFast/imfast)



# Concepts

### Application Factory

Applications should operate differently at development, testing, and production levels.

### Dependency Separation

All Controllers and Modules must be independently executable except for API endpoint functions.

### Extremely scalable

All structures are just files and folders based on modules and packages that are basically supported by Python. There are no restrictions, and you should be able to expand and change it as much as you want.



## Structure

```
IMFast
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   ├── template.py
│   │   └── v1
│   │       ├── __init__.py
│   │       └── sample.py
│   ├── asset
│   │   └── index.html
│   ├── decorator.py
│   ├── depends
│   │   ├── __init__.py
│   │   └── jwt.py
│   ├── error_handler.py
│   ├── exception.py
│   ├── middleware
│   │   ├── __init__.py
│   │   └── hello.py
│   ├── request.py
│   ├── response.py
│   └── route
│       ├── __init__.py
│       └── gzip.py
│
├── controller
│   ├── __init__.py
│   ├── jwt.py
│   └── password.py
│
├── model
│   ├── __init__.py
│   └── appmodel
│       ├── __init__.py
│       └── champion.py
│
├── test
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_basics.py
│   └── test_sample.py
│
├── main.py
├── settings.py
├── imfast
├── requirements.txt
├── dev.env
└── prod.env
```

## main.py

main module of IMFast. It manages the objects created by the application factory.

It calls the appropriate settings from `settings.py`, creates an Application object, and executes the given command.

## app

Here, code related to FastAPI is written. Required resources are placed in the appropriate space according to the rules adhered to by FastAPI.

- **app/api**: set of API Routers
- **app/assets**: set of static templates
- **app/decorator**: It is a set that manages API level middleware as a decorator.
- **app/depends**: set of FastAPI Denpendencies
- **app/error_handler**: set of Exception and Status code Handler
- **app/exception**: set of custom Exceptions
- **app/middleware**: set of FastAPI custom Middlewares
- **app/route**: set of custom FastAPI APIRoute
- **app/request**: set of custom FastAPI Request
- **app/response**: set of API Response and Response Model Factory

## controller

This means an independent module that does not depend on FastAPI.

## model 

It manages various types of data models used in applications including DTO and ORM.

- **model/appmodel**: A set of `Pydantic` models to control FastAPI body data

## test

It is a test module package written based on `pytest`.
