# My degree project from course - Automation Software Testing by Prometheus and GlobalLogic
In this framework I study to test API, UI, Database and it's separated properly in different folders.

How I describe framework and what I tested:
>chapter of a framework
>><name of the test> - what i learned, working with the test (names of the tests I created and what I tested in API/Database/UI).

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
* ui/page_objects
    + study1 - folder with first steps in auto testing.
        - test_first_ui - learned how to work with Selenium webdriver, open page, find element, 
        enter some value into a field, click on element, get text from an element, get page title;
        - test_first_ui_with_page_object - learned how to use POM to previous test 
        (open page, enter login, password, click on Login btn, check error message, check page title);
        - test_uakinoclub_ui - learned how to use POM to more difficult scenarious then previous, 
        training to get elements selectors, getting multiple elements and saving them into a list and work with them, 
        using DRY (don't repeat yourself) practice in tests (through class methods),
        brought the input and output data to constants.
        - test_herokuapp_ui - learned how to check existing of an element, figure out how to drag and drop element, 
        use practices from previous tests.
    + study2 - forlder with more difficult automation scenario then all previous. It described delow. 
    Here I learned how to:
        - handle with waiters,
        - switch iframes,
        - switch windows(browser tabs),
        - add external answer to asserts,
        - training to uses external module function (AdditionalFunctions.select_item_from_list).
    
    ### UI TASK - test_estimate_calc.py
    1. Open https://cloud.google.com/.
    2. By clicking the search button on the portal at the top of the page, enter in the search field "Google Cloud Platform Pricing Calculator".
    3. Start the search by clicking the search button.
    4. In the search results, click "Google Cloud Platform Pricing Calculator" and go to the calculator page.
    5. Activate the COMPUTE ENGINE section at the top of the page.
    6. Fill in the form with the following data:
        a. Number of instances: 4.\
        b. What are these instances for ?: leave blank.\
        c. Operating System / Software: Free: Debian, CentOS, CoreOS, Ubuntu, or other User Provided OS.\
        d. VM Class: Regular.\
        e. Series: N1.\
        f. Machine type: n1-standard-8 (vCPUs: 8, RAM: 30 GB).\
        g. Select Add GPUs.\
            1. Number of GPUs: 1.\
            2. GPU type: NVIDIA Tesla V100.\
        h. Local SSD: 2x375 Gb.\
        i. Datacenter location: Frankfurt (europe-west3).\
        j. Commited usage: 1 Year.\
    7. Click Add to Estimate.
    8. Select EMAIL ESTIMATE.
    9. In a new tab, open https://10minutemail.com or a similar service for generating temporary emails.
    10. Copy the mailing address generated in 10minutemail.
    11. Return to the calculator, in the Email field enter the address from the previous paragraph.
    12. Press SEND EMAIL.
    13. Wait for the letter with the cost calculation and check that the Total Estimated Monthly Cost in the letter matches what is displayed in the calculator.
    14. Add assertions after filling the form and making estimate.
    

## Help to run tests:
* To run all test need to use command:
    + '''python -m pytest'''

* To run some type of tests need to use command (mark names you can select in pytest.ini file, example - python -m pytest -m api): 
    + '''python -m pytest -m <mark name>'''

* To run test in paralel need to use command (need to be installed "pytest-xdist" module):
    + '''python -m pytest -n 4'''


* To see test names on console and its status need to use command:
    + '''python -m pytest -m personal_ui_2 -s -v'''

* To clean project folder from "__pychache__" (need to be installed "pyclean" module): 
    + '''pyclean .'''
