# My degree project from course - Automation Software Testing by Prometheus and GlobalLogic
In this framework I study to test API, UI, Database and it's separated properly.

>How I describe framework and what I tested:
>>chapter of a framework
>>>name of the test - what i learned, working with the test (names of the tests I created and what I tested in API/Database/UI).

## Modules folder
Consists from, folders: "api/clients", "common", "ui".\
Every folder consists from one-few modules in each one I describe classes and their methods to work and use them in tests.


## Tests folder
Consists from, folders: "api", "database", "ui".\
Every folder consists from one-few modules in each one I make tests of some functionality described below.
* api
    + test_api - learned how to send API requests;
    + test_fixture - learned how to use fixtures in tests;
    + test_github_api - made some tests of of GitHub API:
        - commits (commit_list_not_empty, first_commit_author_name, first_commit_author_email), 
        - users (user_exists, user_not_exists);
        - repo (repo_can_be_found, repo_can_be_found_count);
        - emojis (emoji_list_not_empty).
    + test_pokemon_api - learned how to return API response through the fixture 
    (pokemon_first_form_name, pokemon_base_experience, pokemon_id, pokemon_first_type_name);
    + test_restfool_booker - learned how to work with CRUD operations through API, 
    using prepeared objects for testing and add logging into tests and class methods
    (auth, booking_creating, booking_getting, booking_updating, booking_deleting).
* database
    + test_database - learned how to use methods JOIN, SUM, MAX, SELECT, INSERT, DELETE, UPDATE in database testing.
* ui
    + test_first_ui - learned how to work with Selenium webdriver, open page, find element, 
    enter some value into a field, click on element, get text from an element, get page title;
    + test_first_ui_with_page_object - learned how to use POM to previous test 
    (open page, enter login, password, click on Login btn, check error message, check page title);
    + test_uakinoclub_ui - learned how to use POM to more difficult scenarious then previous, 
    training to get elements selectors, getting multiple elements and saving them into a list and work with them, 
    using DRY (don't repeat yourself) practice in tests (through class methods),
    brought the input and output data to constants.
    + test_herokuapp_ui - learned how to check existing of an element, figure out how to drag and drop element, 
    use practices from previous test.
    

## Help to run tests:
* To run all test need to use command:
    + python -m pytest

* To run some type of tests need to use command: 
    + python -m pytest -m <mark name>\
mark names you can select in pytest.ini file, example - python -m pytest -m api.

* To run test in paralel need to use command:
    + python -m pytest -n 4\
(need to be installed "pytest-xdist" module)

* To see test names on console and its status need to use command:
    + python -m pytest -m personal_ui_2 -s -v

* To clean project folder from "__pychache__": pyclean .
    + (need to be installed "pyclean" module)