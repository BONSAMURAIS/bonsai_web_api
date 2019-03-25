# Bonsai Web API

## What is it?
This is a basic Flask app on which to build the different web-based modules for Bonsai.

We foresee three modules:
* a module that handles user interactions (requests for graphs, login, etc.)
* a module that calculates LCA results
* a module that converts DB extractions into matrices usable by the LCA calculation module

An additional fourth module could handle users' submission of data to integrate the DB.

We do not yet have a working DB to receive triplestore queries from. However, we can use a dummy one in the meanwhile.

# Install
Clone the repository

    git clone https://github.com/BONSAMURAIS/web-api
    

Create a virtual environment and activate it

    python3 -m venv venv
    . venv/bin/activate

Or on Windows cmd

    py -3 -m venv venv
    venv\Scripts\activate.bat

Install bonsai_web_api

    pip install -e .

Or if you are using the master branch, install Flask from source before
installing bonsai_web_api

    pip install -e ../..
    pip install -e .


# Run

Linux/MacOS

    export FLASK_APP=bonsai_web_api
    export FLASK_ENV=development
    flask run

Or on Windows cmd::

    set FLASK_APP=flaskr
    set FLASK_ENV=development
    flask run

Open http://127.0.0.1:5000 in a browser.


# Test

    pip install '.[test]'
    pytest

Run with coverage report

    coverage run -m pytest
    coverage report
    coverage html  # open htmlcov/index.html in a browser
