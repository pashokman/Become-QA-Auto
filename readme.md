# My degree project from course - Automation Software Testing by Prometheus and GlobalLogic
In this framework I study to test API, UI, Database and it's separated properly.

"modules" folder consists from, folders: "api/clients", "common", "ui". \
Every folder consists from one-few modules in wich one I describe classes and their methods to work with API/Database/UI in tests.


### Help to run tests:
>To run all test need to use command:
>>python -m pytest

>To run some type of tests need to use command: 
>>python -m pytest -m <mark name>\
mark names you can select in pytest.ini file, example - python -m pytest -m api.

>To run test in paralel need to use command:
>>python -m pytest -n 4\
(need to be installed "pytest-xdist" module)

>To see test names on console and its status need to use command:
>>python -m pytest -m personal_ui_2 -s -v

>To clean project folder from "__pychache__": pyclean .
>>(need to be installed "pyclean" module)