""" Make some tests with GitHub API - commits, users, repo, emojis"""

import pytest


# Testing commits-----------------------------------------------------------------------------------------
@pytest.mark.git_hub_api
def test_commit_list_not_empty(github_api):
    commit_list = github_api.get_commit_list()
    
    assert len(commit_list) != 0


@pytest.mark.git_hub_api
def test_first_commit_author_name(github_api):
    commit_list = github_api.get_commit_list()

    assert commit_list[0]['commit']['author']['name'] == 'Pavlo Lekhitskyi'


@pytest.mark.git_hub_api
def test_first_commit_author_email(github_api):
    commit_list = github_api.get_commit_list()

    assert commit_list[0]['commit']['author']['email'] == 'pashokman1@gmail.com'


# Testing users-----------------------------------------------------------------------------------------
@pytest.mark.git_hub_api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')

    assert user['login'] == 'defunkt'


@pytest.mark.git_hub_api
def test_user_not_exists(github_api):
    user = github_api.get_user('pavlolekhitskyi')

    assert user['message'] == 'Not Found'
     

# Testing repo-----------------------------------------------------------------------------------------
@pytest.mark.git_hub_api
def test_repo_can_be_found(github_api):
    repo = github_api.search_repo('become-qa-auto')
    
    assert 'become-qa-auto' in repo['items'][0]['name']


@pytest.mark.git_hub_api
def test_repo_can_be_found_count(github_api):
    repo = github_api.search_repo('become-qa-auto')

    assert repo['total_count'] == 52


@pytest.mark.git_hub_api
def test_repo_cannot_be_found(github_api):
    repo = github_api.search_repo('pavlo_lekhitskyi_repo_non_exist')

    assert repo['total_count'] == 0


@pytest.mark.git_hub_api
def test_repo_with_single_char_be_found(github_api):
    repo = github_api.search_repo('s')

    assert repo['total_count'] != 0


# Testing emojis-----------------------------------------------------------------------------------------
@pytest.mark.git_hub_api
def test_emoji_list_not_empty(github_api):
    emojis_list = github_api.get_emojis_list()

    assert len(emojis_list) != 0
