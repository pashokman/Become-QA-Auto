"""
Here I learned how to:
    handle with waiters,
    switch iframes,
    switch windows(browser tabs),
    add external answer to asserts,
    training to uses external module function (AdditionalFunctions.select_item_from_list);
    add test severity for allure report
    add testing in different browsers
"""

import pytest
import allure

SEARCH_VALUE = "Google Cloud Platform Pricing Calculator"

EXPECTED_DATA = {
    "page_title": "Google Cloud Pricing Calculator",
    "instances": "4 x",
    "os_software": "Free",
    "instance_type": "n1-standard-8",
    "ssd_config": "2x375 GiB",
    "datacenter": "Frankfurt",
    "commited_usage": "1 Year",
    "total_hours": "2,920",
    "prov_model": "Regular",
    "binding_sum": "USD 899.76",
    "total_sum": "1,081.20"
    }


# Method that add additional info string in logs about start of testing this module. ---------------------------------
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.google_calc
def test_start(google_cloud):
    google_cloud.start()


@allure.severity(allure.severity_level.MINOR)
@pytest.mark.google_calc
def test_find_google_calculator(google_cloud):
    google_cloud.find_calculator(SEARCH_VALUE)
    google_cloud.click_on_search_result()
    
    assert EXPECTED_DATA["page_title"] == google_cloud.get_page_title(), "Does not find Google calc."


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.google_calc
def test_cloud_service_price(google_calc):
    google_calc.fill_the_calc_form(4,'free','n1','CP-COMPUTEENGINE-VMIMAGE-N1-STANDARD-8',
                                'NVIDIA_TESLA_V100','1','2','europe-west3','1')
    assert EXPECTED_DATA["instances"] == google_calc.get_estimate_instances(), "Instances is not as expected."
    assert EXPECTED_DATA["os_software"] == google_calc.get_estimate_os_software(), "OS/Software is not as expected."
    assert EXPECTED_DATA["instance_type"] in google_calc.get_estimate_instance_type(), "Instance type is not as expected."
    assert EXPECTED_DATA["ssd_config"] in google_calc.get_estimate_ssd(), "SSD config is not as expected."
    assert EXPECTED_DATA["datacenter"] in google_calc.get_estimate_region(), "Datacenter region is not as expected."
    assert EXPECTED_DATA["commited_usage"] in google_calc.get_estimate_term(), "Commited usage term is not as expected."
    assert EXPECTED_DATA["total_hours"] in google_calc.get_estimate_hours(), "Total hours is not as expected."
    assert EXPECTED_DATA["prov_model"] in google_calc.get_estimate_prov_model(), "Provisioning model is not as expected."
    assert EXPECTED_DATA["binding_sum"] == google_calc.get_estimate_binding_sums(), "Binding sum is not as expected."
    assert EXPECTED_DATA["total_sum"] == google_calc.get_estimate_sum(), "Total sum is not as expected."


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.google_calc
def test_cloud_service_price_on_email(google_calc):
    google_calc.fill_the_calc_form(4,'free','n1','CP-COMPUTEENGINE-VMIMAGE-N1-STANDARD-8',
                                   'NVIDIA_TESLA_V100','1','2','europe-west3','1')
    google_calc.email_estimate_btn_click()
    main_window_handler = google_calc.get_current_window_handle()

    google_calc.open_mail_page()
    for window_handle in google_calc.get_window_handles():
        if window_handle != main_window_handler:
            google_calc.switch_window(window_handle)
            break
    mail_window_handler = google_calc.get_current_window_handle()
    email = google_calc.copy_email_address()

    google_calc.switch_window(main_window_handler)
    google_calc.send_email(email)

    google_calc.switch_window(mail_window_handler)
    google_calc.spam_close()
    google_calc.open_letter()
    total = google_calc.get_sum_in_letter()

    assert EXPECTED_DATA["total_sum"] in total, "Total sum in letter is not as expected."


# Method that add additional info string in logs about end of testing this module. -----------------------------------
@allure.severity(allure.severity_level.TRIVIAL)
@pytest.mark.google_calc
def test_end(google_cloud):
    google_cloud.end()