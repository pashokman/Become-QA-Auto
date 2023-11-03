To run all test need to use command: 
python -m pytest

To run some type of tests need to use command: 
python -m pytest -m <mark name>
mark name tou can select in pytest.ini file, example - python -m pytest -m api.

To run test in paralel need to use command:
python -m pytest -n 4
(need to be installed "pytest-xdist" module)

To see test names on console and its status need to use command:
python -m pytest -m personal_ui_2 -s -v

To clean project folder from "__pychache__": pyclean .
(need to be installed "pyclean" module)