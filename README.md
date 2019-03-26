# Bonsai Web API
## What is it?
This is a basic Flask app on which to build the different web-based modules for Bonsai.

We foresee four inter-related applications:

* a web application that handles interactions with users (requests for graphs, sessions, login, etc.)
* a REST API that serves both the web application and direct REST requests on one side, and queries the graph DB on the other side,
* a module that receive the whole graph database at server start, converts it into a two dimensional matrix and cache it for ulterior requests,
* and a module that calculates LCA results upon requests from the REST API.

We do not yet have a working DB to receive triplestore queries from. However, we can use a dummy one in the meanwhile.

![alt text](https://github.com/BONSAMURAIS/bonsai_web_api/blob/master/bonsai_web_api/static/pictures/bonsai_web_api_diagram.png)


## Install
Clone the repository

    git clone https://github.com/BONSAMURAIS/bonsai_web_api

Create a virtual environment and activate it

    python3 -m venv venv
    . venv/bin/activate

Or on Windows cmd

    py -3 -m venv venv
    venv\Scripts\activate.bat

## Install bonsai_web_api

    pip install -e .

Or if you are using the master branch, install Flask from source before installing bonsai_web_api

    pip install -e ../..
    pip install -e .

## Run
Linux/MacOS

    export FLASK_APP=bonsai_web_api
    export FLASK_ENV=development
    flask run

Or on Windows cmd

    set FLASK_APP=bonsai_web_api
    set FLASK_ENV=development
    flask run

Open http://127.0.0.1:5000 in a browser.

## Test
    pip install '.[test]'
    pytest -v

## Run with coverage report

    coverage run -m pytest
    coverage report
    coverage html  # open htmlcov/index.html in a browser
