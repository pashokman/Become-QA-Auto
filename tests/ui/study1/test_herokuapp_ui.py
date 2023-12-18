"""
Here I figure out how to:
    - check existing of an element;
    - drag and drop element and check their position.
"""

import pytest


# Constants (input data and expected results data) -------------------------------------------------------------------
# Added/deleted elements count ---------------------------------------------------------------------------------------
NONE_ELEMENTS_ADDED = 0
ONE_ELEMENT_ADDED = 1
TWO_ELEMENTS_ADDED = 2
EXPECTED_ELEMENTS_COUNT_AFTER_DELETING = 1

# Drag and drop elements text before drag and drop operation ---------------------------------------------------------
FIRST_ELEMENT_TEXT = "A"
SECOND_ELEMENT_TEXT = "B"


# Tests --------------------------------------------------------------------------------------------------------------
# Method that add additional info string in logs about start of testing this module. ---------------------------------
@pytest.mark.herokuapp_ui
def test_start(herokuapp):
    herokuapp.start()


@pytest.mark.herokuapp_ui
def test_element_not_added(herokuapp):
    herokuapp.go_to_add_remove_elem_page()
    herokuapp.click_add_elem_times(0)

    assert herokuapp.get_added_elements_count() == NONE_ELEMENTS_ADDED, "No element added test error"


@pytest.mark.herokuapp_ui
def test_one_element_added(herokuapp):
    herokuapp.go_to_add_remove_elem_page()
    herokuapp.click_add_elem_times(1)

    assert herokuapp.get_added_elements_count() == ONE_ELEMENT_ADDED, "One element added test error"


@pytest.mark.herokuapp_ui
def test_two_elements_added(herokuapp):
    herokuapp.go_to_add_remove_elem_page()
    herokuapp.click_add_elem_times(2)
    
    assert herokuapp.get_added_elements_count() == TWO_ELEMENTS_ADDED, "Two element added test error"


@pytest.mark.herokuapp_ui
def test_delete_one_of_two_added_elem(herokuapp):
    herokuapp.go_to_add_remove_elem_page()
    herokuapp.click_add_elem_times(2)
    herokuapp.click_del_elem_times(1)

    assert herokuapp.get_added_elements_count() == EXPECTED_ELEMENTS_COUNT_AFTER_DELETING, "Delete one of two elements test error"


@pytest.mark.herokuapp_ui
def test_elem_text_before_drag_and_drop(herokuapp):
    herokuapp.go_to_drag_and_drop_page()
    elem_list_before_drag_and_drop = herokuapp.get_drag_and_drop_elem_list()
    first_element_text = elem_list_before_drag_and_drop[0].text
    second_element_text = elem_list_before_drag_and_drop[1].text

    assert (first_element_text == FIRST_ELEMENT_TEXT and second_element_text == SECOND_ELEMENT_TEXT), "Before drug and drop test error"


@pytest.mark.herokuapp_ui
def test_elem_text_after_drag_and_drop(herokuapp):
    herokuapp.go_to_drag_and_drop_page()
    herokuapp.drag_and_drop_elem()
    elem_list_before_drag_and_drop = herokuapp.get_drag_and_drop_elem_list()
    first_element_text = elem_list_before_drag_and_drop[0].text
    second_element_text = elem_list_before_drag_and_drop[1].text

    assert first_element_text == SECOND_ELEMENT_TEXT and second_element_text == FIRST_ELEMENT_TEXT, "After drug and drop test error"


# Method that add additional info string in logs about end of testing this module. -----------------------------------
@pytest.mark.herokuapp_ui
def test_end(herokuapp):
    herokuapp.end()