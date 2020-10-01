import pytest
from dummy_site.locators.app_logic import AppFunction
from dummy_site.test_data.data_dummy import *

@pytest.fixture(scope="module")
def setup():
    obj = AppFunction(browser,url, wait_time)
    return obj

@pytest.fixture(scope="module")
def cal_setup():
    obj = AppFunction(browser,url2,wait_time)
    return obj