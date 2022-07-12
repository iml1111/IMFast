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

For the `python-dotenv` library, you can write an `.env` file in the same path as `settings.py`, or you can directly enter an environment variable.

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

