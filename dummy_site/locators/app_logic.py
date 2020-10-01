from dummy_site.browser_action.browser_action_dummy import *
from dummy_site.locators.locators_dummy import *
from dummy_site.locators.external_function import *
from time import sleep
import logging
logger = logging.getLogger(__name__)


class AppFunction(BrowserAction):
    def __init__(self,browser,url,wait_time):
        self.url = url
        super().__init__(browser,wait_time)
        self.launch_app()

    def launch_app(self):
        print("driver:", self.spdriver)
        self.spdriver.get(self.url)

    def choose_option(self):
        self.click_element(radio_button)

    def input_name_from_excel(self,first_name, last_name):
        self.input_element(input_first_name,first_name)
        self.input_element(input_last_name,last_name)

    def choose_date_of_birth(self):
        self.click_element(select_box_dob)
        self.click_element(select_month)
        self.click_element(select_year)
        self.click_element(select_date)
        sleep(5)

    def choose_gender(self):
        self.click_element(select_gender)

    def add_passenger(self):
        self.click_element(checkbox_pass)
        self.click_element(dropdown_pass_box)
        self.click_element(add_pass)

# Passenger 1
    def pass1_name_excel(self,first_name,last_name):
        self.input_element(pass1_first_name, first_name)
        self.input_element(pass1_last_name, last_name)

    def pass1_DOB(self):
        self.click_element(pass1_dob_button)
        self.click_element(pass1_month)
        self.click_element(pass1_year)
        self.click_element(pass1_date)

    def pass1_gender(self):
        self.click_element(pass1_gender)

    def passenger_catagory(self):
        self.click_element(pass_1_type)
        self.click_element(pass1_catagory)

    def type_of_trip(self):
        self.click_element(ticket_option)

    def travel_from_to(self,from_1,to_1):
        self.input_element(from_city,from_1)
        self.input_element(to_city,to_1)

    def departure_date(self):
        self.click_element(dep_date_box)
        self.click_element(dep_month)
        self.click_element(dep_year)
        self.click_element(dep_date_1)

    def contact_option(self):
        self.click_element(contact)

#billing details

    def full_name_details(self,value):
        self.input_element(Full_name,value)

    def phone_details(self,value):
        self.input_element(phone,value)

    def email_details(self,value):
        self.input_element(email,value)

    def country_details(self):
        self.click_element(country_box)
        self.click_element(select_country)

    def add_line_details(self,line1,line2):
        self.input_element(address_1,line1)
        self.input_element(address_2,line2)

    def city_details(self,value):
        self.input_element(city,value)

    def state_details(self):
        self.click_element(state_box)
        self.click_element(select_state)

    def postcode_details(self,value):
        self.input_element(postcode,value)

    def place_order_button(self):
        self.click_element(place_order_click)


    def pay_via_net_banking(self):
        self.click_element(select_bank)
        self.click_element(bank_icon)
        self.click_element(pay_now_net_banking)

# functions for calculator
#    def get_monthly_pay(self):
 #       self.click_element(calculate)
 #       print(self.get_element_text(mortgage_monthly_pay))

    def select_calculator(self):
        self.click_element(income_tax_cal)
        self.take_a_screenshot("calculator")

    def choose_status_dropdown(self):
        self.click_element(select_status_box)
        self.click_element(status)

    def no_of_young_dep(self,value):
        self.input_element(dependents,value)

    def no_of_other_dep(self,value):
        self.input_element(dependents_2,value)

    def wage_amount(self,value):
        self.input_element(wages,value)

    def fed_tax_withheld(self,value):
        self.input_element(federal_tax,value)

    def state_tax_withheld(self,value):
        self.input_element(state_tax,value)

    def local_tax_withheld(self,value):
        self.input_element(local_tax,value)

    def interest_income_amount(self,value):
        self.input_element(interest_income,value)

    def ordinary_div_amt(self,value):
        self.input_element(ordinary_div,value)

    def quali_div_amt(self,value):
        self.input_element(qualified_div,value)

    def passive_inc_amt(self,value):
        self.input_element(passive_income,value)

    def short_term_cap_gain(self,value):
        self.input_element(short_gain,value)

    def long_term_cap_gain(self,value):
        self.input_element(long_gain,value)

    def tax_rate_percentage(self,value):
        self.input_element(tax_rate,value)

#deduction

    def ira_deduction_amt(self,value):
        self.input_element(ira_ded,value)

    def mortgage_amt(self,value):
        self.input_element(mortgage,value)

    def charity_amt(self,value):
        self.input_element(charity,value)

    def collage_edu_amt(self,value):
        self.input_element(coll_education,value)

###submit

    def submit_button(self):
        self.click_element(calculate_button)

    def estimated_refund_details(self):
        #self.click_element(calculate_button)
        print(self.get_element_text(estimated_tax))
        print(self.get_element_text(total_income))
        print(self.get_element_text(total_deduction))
        print(self.get_element_text(total_exemption))
        print(self.get_element_text(taxable_income))
        print(self.get_element_text(regular_taxes))
        print(self.get_element_text(alt_min_tax))
        print(self.get_element_text(net_inv))
        print(self.get_element_text(all_tax_credit))
        print(self.get_element_text(total_tax_credit))
        print(self.get_element_text(marginal_tax))
        print(self.get_element_text(tax_pre_payment))
        print(self.get_element_text(estimated_reund))

    def get_calculation_table_content(self):
        elements = self.spdriver.find_elements_by_xpath(
            "//h1[contains(text(), 'Income Tax Calculator')]//following::table[2]//tr")

        for i in range(1, len(elements)+1):
            elem1 = self.spdriver.find_element_by_xpath(f"//h1[contains(text(), 'Income Tax Calculator')]//following::table[2]//tr[{i}]//td[1]")
            elem2 = self.spdriver.find_element_by_xpath(
                f"//h1[contains(text(), 'Income Tax Calculator')]//following::table[2]//tr[{i}]//td[2]")

            print(elem1.text," : ", elem2.text)




















