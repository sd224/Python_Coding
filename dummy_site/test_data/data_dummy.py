import os


url = "https://www.dummyticket.com/dummy-ticket-for-visa-application/"
url2 = "https://www.calculator.net/rent-calculator.html"
wait_time = 20
browser = "chrome"
headless_execution = True

chrome_driver_path = "D:\\Chrome\\chromedriver.exe"
firefox_driver_path = "D:\\Firefox_driver\\geckodriver.exe"
edge_driver_path = "D:\\Mircorsoft_Edge_driver\\msedgedriver.exe"

CUR_DIR = os.getcwd()
LOG_DIR = os.path.join(CUR_DIR, 'log')
IMAGE_DIR = os.path.join(CUR_DIR, 'image')
test_data_path = os.path.join(CUR_DIR, 'test_data')
excel_file_path = os.path.join(test_data_path, 'test_data_excel.xlsx')

month = 'Aug'
DOB = 29
year = 1970

month_2 = 'Feb'
DOB_2 = 25
year_2 = 1976

dep_month = 'Sep'
dep_date = 30
dep_year = 2020

res_state = 'Maharashtra'

#####################
##Calculator##
####################

status_option = "HeadofHousehold"
