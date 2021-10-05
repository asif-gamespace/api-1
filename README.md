# gamespace_API_Testing

This project is a starting point for `gamespaceinc` API testing.

## Installation

##### Use the package manager pip to install project dependency

    $ cd to the directory where requirements.txt is located
    $ run: pip3 install -r requirements.txt

## Run Project

    $ cd to the "Test" directory
    $ run: python3 testconf/runtest.py

## Run single file with test report
    
    $ pytest -s --alluredir=report_allure/ --html=report_html/report.html --self-contained-html  'path of the testcase'
