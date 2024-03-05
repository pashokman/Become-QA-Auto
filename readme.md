# My degree project from course - Automation Software Testing by Prometheus and GlobalLogic
In this framework I study to test API, UI, Database and it's separated properly in different folders.\

How I describe framework and what I tested:
* ```<chapters name>``` of a framework
    + ```<tests name>``` - what I learned, working with the test (names of the tests I created and what I tested in API/Database/UI).

## Modules folder
Consists from folders: ```api/clients```, ```common```, ```ui```.\
Every folder consists from one-few modules in each one I describe classes and their methods to work with and use them in tests.


## Tests folder
### Tests are arranged in order of increasing complexity.
Consists from, folders: ```api```, ```database```, ```ui```.\
Every folder consists from one-few modules in each one I make tests of some functionality described below.
* ```api```
    + ```test_api``` - learned how to send API requests;
    + ```test_fixture``` - learned how to use fixtures in tests;
    + ```test_github_api``` - made some tests of GitHub API:
        - ```commits``` (commit_list_not_empty, first_commit_author_name, first_commit_author_email), 
        - ```users``` (user_exists, user_not_exists);
        - ```repo``` (repo_can_be_found, repo_can_be_found_count);
        - ```emojis``` (emoji_list_not_empty).
    + ```test_pokemon_api``` - learned how to return API response through the fixture 
    (pokemon_first_form_name, pokemon_base_experience, pokemon_id, pokemon_first_type_name);
    + ```test_restfool_booker``` - learned how to work with CRUD operations through API, 
        - using prepeared objects for testing and add logging into tests and class methods
        (auth, booking_creating, booking_getting, booking_updating, booking_deleting);
        - add additional conditions to page methods (return status code if it does not match to input status code);
        - import test data from another file;
        - solved the problem vs copying (use deepcopy), to change only copied dictionary, not original one;
        - made test of creating booking without body parameters;
        - assigned asserts error messages into variable;
        - used try/except blocks in tests.
* ```database```
    + ```test_database``` - learned how to use methods JOIN, SUM, MAX, SELECT, INSERT, DELETE, UPDATE in database testing.
* ```ui/page_objects```
    + ```study1``` - folder with first steps in auto testing:
        - ```test_first_ui``` - learned how to work with Selenium webdriver, open page, find element, enter some value into a field, click on element, get text from an element, get page title;
        - ```test_first_ui_with_page_object``` - learned how to use POM to previous test (open page, enter login, password, click on Login btn, check error message, check page title);
        - ```test_uakinoclub_ui``` - learned how to use POM to more difficult scenarious then previous, learned how to get elements selectors, getting multiple elements and saving them into a list and work with them, using DRY (don't repeat yourself) practice in tests (through class methods), assign the input and output data to constants.
        - ```test_herokuapp_ui``` - learned how to check existing of an element, figure out how to drag and drop element, and use practices from previous tests.
    + ```study2``` - forlder with more difficult automation scenario then all previous. It described delow.  
    Here I learned how to:
        - handle with waiters,
        - switch iframes,
        - switch windows (browser tabs),
        - add external answer to asserts,
        - training how to uses external module functions (AdditionalFunctions.select_item_from_list),
        - add Allure severity to tests,
        - add screenshots on failure in Allure report.
* ```run tests in Jenkins```
    + added "allure_report_jenkins_git_hub" to project root folder (one test is broken in purpose)
    + solve the problem when some UI tests fail in Jenkins, but succeed on local machine:
        - used GitHub project URL to get framework from it;
        - created virtual environment;
        - use virtual environment;
        - install all needed modules;
        - connected Allure reporting in Jenkins.

    
    ### UI TASK - test_estimate_calc.py (most difficult task in project)
    1. Open https://cloud.google.com/.
    2. By clicking the search button on the portal at the top of the page, enter in the search field ```Google Cloud Platform Pricing Calculator```.
    3. Start the search by clicking the Search button.
    4. In the search results, click ```Google Cloud Platform Pricing Calculator``` and go to the calculators page.
    5. Activate the ```COMPUTE ENGINE``` section at the top of the page.
    6. Fill in the form with the following data:  
        - Number of instances: ```4```.  
        - What are these instances for ?: ```leave blank```.  
        - Operating System / Software: ```Free: Debian, CentOS, CoreOS, Ubuntu, or other User Provided OS```.  
        - VM Class: ```Regular```.  
        - Series: ```N1```.  
        - Machine type: ```n1-standard-8 (vCPUs: 8, RAM: 30 GB)```.  
        - Select Add GPUs.  
            a. Number of GPUs: ```1```.  
            b. GPU type: ```NVIDIA Tesla V100```.  
        - Local SSD: ```2x375 Gb```.  
        - Datacenter location: ```Frankfurt (europe-west3)```.  
        - Commited usage: ```1 Year```.  
    7. Click on ```Add to Estimate``` button.
    8. Select ```EMAIL ESTIMATE``` icon in Estimate block.
    9. In a new tab, open https://10minutemail.com or a similar service for generating temporary emails.
    10. Copy the mailing address generated in ```10minutemail``` service.
    11. Return to the calculator, in the ```Email field``` enter the address from the previous point.
    12. Press ```SEND EMAIL``` button.
    13. Wait for the letter with the cost calculation and check that the Total Estimated Monthly Cost in the letter matches what is displayed in the calculator (wait for the email, open letter, check the sum in the letter with the sum on Estimate block).
    14. Add assertions after filling the form and making estimate.
    

## Help to run tests (all command runs in VS Code Bash terminal):
* To run all test need to use command: 
```
python -m pytest
```

* To run some type of tests need to use command (mark names you can select in pytest.ini file, example - ```python -m pytest -m api```, to use few markers ```api or api2```):
```
python -m pytest -m mark_name
```

* To run test in paralel need to use command (need to be installed ```pytest-xdist``` module - ```pip install pytest-xdist```):
```
python -m pytest -n 4
```

* To see test names on console and its status need to use command:
```
python -m pytest -m personal_ui_2 -s -v
```

* To clean project folder from ```__pychache__``` and similar temp folders (need to be installed ```pyclean``` module - ```pip inslall pyclean```): 
```
pyclean .
```

* To run tests and make a report  (need to be installed ```pytest-html``` module - ```pip install pytest-html```):
```
python -m pytest -m google_calc --html=report.html --self-contained-html
```

* To get extra test summary for all tests (passed/failed):
```
python -m pytest -m google_calc -rA
```

* To run only tests that have a keyword in test name (message), to run test with different words use or operator (message or task)? to run all test except with keyword (not message):
```
python -m pytest -m google_calc -k message
```

* To make ```JUnitXML report``` (should be installed this module - ```pip install junit-xml```):
```
python -m pytest -m pokemon_api --junit-xml=report2.xml
```

* To make Allure report first command shoud run in terminal (VS Code), second one in ```cmd``` from project root folder:
```
python -m pytest -m pokemon_api --alluredir="./reports"
```
```
allure serve "./reports"
```

* To run tests in all browsers should uncomment ```browser_type``` fixture with params and comment fixture without params in ```conftest.py``` file:
```
python -m pytest -m google_calc
```

* To run tests only in one of 3 browsers, should uncomment ```browser_type``` fixture without params and comment fixture with params in ```conftest.py``` file:
```
python -m pytest -m google_calc --browser-type edge --alluredir="./reports"
```