from dummy_site.test_data.data_dummy import *
from dummy_site.locators.external_function import get_cell_data
from time import sleep
import pytest

def test_select_radio_button(setup):
    setup.choose_option()

def test_input_first_and_last_name(setup):
    setup.input_name_from_excel(get_cell_data(1,2),get_cell_data(2,2))

def test_select_date_of_birth(setup):
    setup.choose_date_of_birth()

def test_select_gender(setup):
    setup.choose_gender()

def test_passenger(setup):
    setup.add_passenger()

def test_passenger1_name(setup):
    setup.pass1_name_excel(get_cell_data(3,2),get_cell_data(4,2))

def test_passenger1_dob(setup):
    setup.pass1_DOB()

def test_passeger1_gender(setup):
    setup.pass1_gender()

def test_pass_type(setup):
    setup.passenger_catagory()

def test_trip_type(setup):
    setup.type_of_trip()

def test_city(setup):
    setup.travel_from_to(get_cell_data(5,2),get_cell_data(6,2))

def test_departure_time(setup):
    setup.departure_date()

def test_how_to_contact(setup):
    setup.contact_option()

def test_billing_details(setup):
    setup.full_name_details(get_cell_data(8,2))
    setup.phone_details(get_cell_data(9,2))
    setup.email_details(get_cell_data(10,2))
    setup.country_details()
    setup.add_line_details(get_cell_data(11,2),get_cell_data(12,2))
    setup.city_details(get_cell_data(13,2))
    setup.state_details()
    setup.postcode_details(get_cell_data(15,2))

def test_final_order(setup):
    setup.spdriver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    setup.place_order_button()

def test_pay(setup):
    setup.pay_via_net_banking()
