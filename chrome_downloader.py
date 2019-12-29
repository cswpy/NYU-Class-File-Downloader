from parse_urls_nyu import parse_urls
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Relative path of the html file where files are located
href = 'nyu_class.html'
# Relative path of the desired download path
download_dir = '\\downloads'

chrome_options = Options()
chrome_options.add_experimental_option('prefs',  {
    "download.default_directory": download_dir,
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True
    }
)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://newclasses.nyu.edu/")
driver.maximize_window()
time.sleep(2)

#Your credentials, netid as in username
username = '******'
password = '************'

driver.find_element_by_id('netid').click()
driver.find_element_by_id('netid').clear()
driver.find_element_by_id('netid').send_keys(username)

driver.find_element_by_id('password').click()
driver.find_element_by_id('password').clear()
driver.find_element_by_id('password').send_keys(password)

driver.find_element_by_name('_eventId_proceed').click()

#Waiting for DUO MFA Approval

time.sleep(10)
urls = parse_urls(href)
for url in urls:
    driver.execute_script("window.open('','_blank');")
    driver.get(url)
    time.sleep(1)
    driver.close()
driver.quit()