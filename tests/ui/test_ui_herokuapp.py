import pytest


@pytest.mark.personal_ui_2
def test_start(herokuapp):
    herokuapp.start()


@pytest.mark.personal_ui_2
def test_element_not_exist(herokuapp):
    herokuapp.go_to_add_remove_elem_page()

    herokuapp.elements_count_assertion("//button[@class='added-manually']", 0)


@pytest.mark.personal_ui_2
def test_one_element_exist(herokuapp):
    herokuapp.go_to_add_remove_elem_page()
    herokuapp.click_add_elem(1)

    herokuapp.elements_count_assertion("//button[@class='added-manually']", 1)


@pytest.mark.personal_ui_2
def test_two_elements_exist(herokuapp):
    herokuapp.go_to_add_remove_elem_page()
    herokuapp.click_add_elem(2)
    
    herokuapp.elements_count_assertion("//button[@class='added-manually']", 2)


@pytest.mark.personal_ui_2
def test_delete_one_of_two_elem(herokuapp):
    herokuapp.go_to_add_remove_elem_page()
    herokuapp.click_add_elem(2)
    herokuapp.click_del_elem(1)

    herokuapp.elements_count_assertion("//button[@class='added-manually']", 1)


@pytest.mark.personal_ui_2
def test_drag_and_drop(herokuapp):
    herokuapp.go_to_drag_and_drop_page()
    herokuapp.drag_elem_and_drop()

    herokuapp.drag_and_drop_assertion()


@pytest.mark.personal_ui_2
def test_end(herokuapp):
    herokuapp.end()