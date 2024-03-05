""" Make some tests with GitHub API - commits, users, repo, emojis"""

import pytest


# Testing commits ----------------------------------------------------------------------------------------------------
@pytest.mark.git_hub_api
def test_commit_list_not_empty(github_api):
    commit_list = github_api.get_commit_list()
    
    assert len(commit_list) != 0, "Commit list is empty"


@pytest.mark.git_hub_api
def test_first_commit_author_name(github_api):
    commit_list = github_api.get_commit_list()

    err_message = 'First commit author name is not Pavlo Lekhitskyi'
    assert commit_list[0]['commit']['author']['name'] == 'Pavlo Lekhitskyi', err_message


@pytest.mark.git_hub_api
def test_first_commit_author_email(github_api):
    commit_list = github_api.get_commit_list()

    err_message = 'First commit email is not pashokman1@gmail.com'
    assert commit_list[0]['commit']['author']['email'] == 'pashokman1@gmail.com', err_message


# Testing users ------------------------------------------------------------------------------------------------------
@pytest.mark.git_hub_api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')

    assert user['login'] == 'defunkt', "User login is not  - defunkt"


@pytest.mark.git_hub_api
def test_user_not_exists(github_api):
    user = github_api.get_user('pavlolekhitskyi')

    assert user['message'] == 'Not Found', "User with name - pavlolekhitskyi is exist"
     

# Testing repo -------------------------------------------------------------------------------------------------------
@pytest.mark.git_hub_api
def test_repo_can_be_found(github_api):
    repo = github_api.search_repo('become-qa-auto')
    
    assert 'become-qa-auto' in repo['items'][0]['name'], "There is not repo - become-qa-auto"


@pytest.mark.git_hub_api
def test_repo_can_be_found_count(github_api):
    repo = github_api.search_repo('become-qa-auto')

    assert repo['total_count'] == 52, "The amount of repos with name 'become-qa-auto' is not equal - 52"


@pytest.mark.git_hub_api
def test_repo_cannot_be_found(github_api):
    repo = github_api.search_repo('pavlo_lekhitskyi_repo_non_exist')

    assert repo['total_count'] == 0, "Repo with name 'pavlo_lekhitskyi_repo_non_exist' is exist"


@pytest.mark.git_hub_api
def test_repo_with_single_char_be_found(github_api):
    repo = github_api.search_repo('s')

    assert repo['total_count'] != 0, "There are no repos with name - 's'"


# Testing emojis -----------------------------------------------------------------------------------------------------
@pytest.mark.git_hub_api
def test_emoji_list_not_empty(github_api):
    emojis_list = github_api.get_emojis_list()

    assert len(emojis_list) != 0, "Emoji list is empty"
