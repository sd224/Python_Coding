from selenium.webdriver.common.by import By
from dummy_site.test_data.data_dummy import *

XPATH = By.XPATH
NAME = By.NAME
CSS = By.CSS_SELECTOR
ID = By.ID
LINKTEXT = By.LINK_TEXT

radio_button = (XPATH,"//input[@id='product_551']")
input_first_name = (XPATH,"//input[@id='travname']")
input_last_name = (XPATH,"//input[@id='travlastname']")
dob_button = (XPATH,"//select[@class='ui-datepicker-month']")
select_box_dob = (XPATH,"//input[@id='dob']")
select_month = (XPATH,f"//select[@class='ui-datepicker-month']//following :: option[contains(text(),'{month}')]")
select_year = (XPATH,f"//select[@class='ui-datepicker-year']//following :: option[contains(text(),'{year}')]")
select_date = (XPATH,f"//a[@class='ui-state-default' and contains(text(),'{DOB}')]")
select_gender = (XPATH,"//input[@id='sex_2']")
checkbox_pass = (XPATH,"//input[@id='addmorepax']")
dropdown_pass_box = (XPATH,"//span[@id='select2-addpaxno-container']")
#add_pass = (XPATH,"//span[@id='select2-addpaxno-container' and text()='add 1 more passenger']")
add_pass = (XPATH,"//li[contains(text(), 'add 1 more passenge')]")

#passenger 1
pass1_first_name = (XPATH,"//input[@name='travname2']")
pass1_last_name = (XPATH,"//input[@name='travlastname2']")
pass1_dob_button = (XPATH,"//input[@id='dob2']")
pass1_month = (XPATH,f"//select[@class='ui-datepicker-month']//following :: option[contains(text(),'{month_2}')]")
pass1_year = (XPATH,f"//select[@class='ui-datepicker-year']//following :: option[contains(text(),'{year_2}')]")
pass1_date = (XPATH,f"//a[@class='ui-state-default' and contains(text(),'{DOB_2}')]")
pass1_gender = (XPATH,"//input[@id='sex2_1']")
pass_1_type = (XPATH,"//span[@id='select2-paxtype2-container']")
pass1_catagory = (XPATH,"//li[contains(text(),'Adult')]")

ticket_option = (XPATH,"//input[@id='traveltype_1']")
from_city = (XPATH, "//input[@id='fromcity']")
to_city = (XPATH,"//input[@id='tocity']")

dep_date_box = (XPATH,"//input[@id='departon']")
dep_month = (XPATH,f"//select[@class='ui-datepicker-month']//following :: option[contains(text(),'{dep_month}')]")
dep_year = (XPATH,f"//select[@class='ui-datepicker-year']//following :: option[contains(text(),'{dep_year}')]")
dep_date_1 = (XPATH,f"//a[@class='ui-state-default' and contains(text(),'{dep_date}')]")

contact = (XPATH,"//input[@id='deliverymethod_3']")

#billing details
Full_name = (XPATH,"//input[@id='billname']")
phone = (XPATH,"//input[@id='billing_phone']")
email = (XPATH,"//input[@id='billing_email']")
country_box = (XPATH,"//span[@id='select2-billing_country-container']")
select_country = (XPATH,"(//li[contains(text(),'India')])[2]")
address_1 = (XPATH,"//input[@id='billing_address_1']")
address_2 = (XPATH,"//input[@id='billing_address_2']")
city = (XPATH,"//input[@id='billing_city']")
state_box = (XPATH,"//span[@id='select2-billing_state-container']")
select_state = (XPATH,f"//li[contains(text(),'{res_state}')]")
state = (XPATH,"//input[@id='billing_state']")
postcode = (XPATH,"//input[@id='billing_postcode']")
#chat_box = (XPATH,"//jdiv[@class='closeIcon_f63']")

#place_order_click = (XPATH,"//button[@id='place_order']")
place_order_click = (XPATH,"//button[@class='button alt']")

#payment page card details
credit_card = (XPATH,"//input[@class='form-control simplebox numbersOnly unknown']")
exp_date = (XPATH,"//input[@class='form-control simplebox']")
CVV = (XPATH,"//input[@class='form-control simplebox numbersOnly']")
name_on_card = (XPATH,"//input[@class='form-control simplebox charOnly']")
pay_now_button = (XPATH,"//button[@id='citrusCardPayButton']")

#payment page net banking details
select_bank = (XPATH,"//span[contains(text(),'Banks')]")
bank_icon = (XPATH,"//span[@class ='hdfcbank']")
pay_now_net_banking = (XPATH,"//button[@id ='citrusNetbankingButton']")

# locators for calculator
#mortgage_monthly_pay = (XPATH,"//h2[@class='h2result']")
#calculate = (XPATH,"//input[@value='Calculate']")

income_tax_cal = (XPATH,"(//a[contains(text(),'Income Tax')])[2]")
select_status_box = (XPATH,"//select[@name='cfilestatus']")
status = (XPATH,f"//select[@name='cfilestatus']//following::option[@value='{status_option}']")
dependents = (XPATH,"//input[@name='callowance']")
dependents_2 = (XPATH,"//input[@name='callowanceold']")
wages = (XPATH,"//input[@name='csalaryincome']")
federal_tax = (XPATH,"//input[@name='cwithheld']")
state_tax = (XPATH,"//input[@name='csalarystate']")
local_tax = (XPATH,"//input[@name='csalarylocal']")
interest_income = (XPATH,"//input[@name='cinterestincome']")
ordinary_div = (XPATH,"//input[@name='cordinarydividends']")
qualified_div = (XPATH,"//input[@name='cqualifieddividends']")
passive_income = (XPATH,"//input[@name='crentalincome']")
short_gain = (XPATH,"//input[@name='cshortcapitalgain']")
long_gain = (XPATH,"//input[@name='clongcapitalgain']")
tax_rate = (XPATH,"//input[@name='cstatetaxrate']")

######deductions######
ira_ded = (XPATH,"//input[@name='cira']")
mortgage = (XPATH,"//input[@name='cmortgage']")
charity = (XPATH,"//input[@name='cdonations']")
coll_education = (XPATH,"//input[@name='ctuition']")

###submit button###
calculate_button = (XPATH,"//input[@value='Calculate']")

#mortgage_monthly_pay = (XPATH,"//h2[@class='h2result']")
#calculate = (XPATH,"//input[@value='Calculate']")
#print value
estimated_tax = (XPATH,"//h2[@class='panel']")
total_income = (XPATH,"//b[contains(text(),'Total Income')]")
total_deduction = (XPATH,"//td[contains(text(),'Total Deductions')]")
total_exemption = (XPATH,"//td[contains(text(),'Total Exemptions')]")
taxable_income = (XPATH,"//td[contains(text(),'Taxable Income')]")
regular_taxes = (XPATH,"//b[contains(text(),'Regular Taxes')]")
alt_min_tax = (XPATH,"//td[contains(text(),'Alternative Minimum Tax')]")
net_inv = (XPATH,"//td[contains(text(),'Net Investment Income Tax')]")
all_tax_credit = (XPATH,"//td[contains(text(),'All Tax Credits')]")
total_tax_credit = (XPATH,"//b[contains(text(),'Total Tax with Credits')]")
marginal_tax = (XPATH,"//td[contains(text(),'Marginal Tax Rate')]")
tax_pre_payment = (XPATH,"//td[contains(text(),'Tax Pre-payments')]")
estimated_reund = (XPATH,"//b[contains(text(),'Estimated Refund')]")











