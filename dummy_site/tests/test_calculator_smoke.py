from dummy_site.locators.external_function import get_cell_data
import logging
logger = logging.getLogger(__name__)

'''
def test_get_monthly_pay_result(cal_setup):
    cal_setup.get_monthly_pay()
'''

def test_navigate_to_calculator(cal_setup):
    logger.info("navigation to caluclator page started")
    cal_setup.select_calculator()
    cal_setup.choose_status_dropdown()

def test_input_income_details(cal_setup):
    logger.info("started to input data from excel sheet")
    cal_setup.no_of_young_dep(get_cell_data(22,2))
    cal_setup.no_of_other_dep(get_cell_data(23,2))
    cal_setup.wage_amount(get_cell_data(24,2))
    cal_setup.fed_tax_withheld(get_cell_data(25,2))
    cal_setup.state_tax_withheld(get_cell_data(26,2))
    cal_setup.local_tax_withheld(get_cell_data(27,2))
    cal_setup.interest_income_amount(get_cell_data(28,2))
    cal_setup.ordinary_div_amt(get_cell_data(29,2))
    cal_setup.quali_div_amt(get_cell_data(30,2))
    cal_setup.passive_inc_amt(get_cell_data(31,2))
    cal_setup.short_term_cap_gain(get_cell_data(32,2))
    cal_setup.long_term_cap_gain(get_cell_data(33,2))
    cal_setup.tax_rate_percentage(get_cell_data(34,2))
    cal_setup.ira_deduction_amt(get_cell_data(37,2))
    cal_setup.mortgage_amt(get_cell_data(38,2))
    cal_setup.charity_amt(get_cell_data(39,2))
    cal_setup.collage_edu_amt(get_cell_data(40,2))

def test_calculator_click_button(cal_setup):
    cal_setup.submit_button()
    #cal_setup.estimated_refund_details()
    cal_setup.get_calculation_table_content()



