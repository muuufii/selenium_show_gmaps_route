import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from excel import search_long_lat

#==============================

TESTCASE = 'testcase1'
RESULT_FILE = 'test_result.json'

open_file = open('test_result/' + RESULT_FILE)
data = json.load(open_file)

#Get data gudang pickup (gudang asal)
#breakdown data from result.json
gudang_pickup = data['response']['pickup']['nama_perusahaan']
asal_lat_lang = search_long_lat(TESTCASE, gudang_pickup , 'asal')

#Get data gudang tujuan
list_koordinat_tujuan = []
list_order = data['response']['list_order'][2]
for i in list_order:
    id_order = i['id_order']
    tujuan_lat_lang = search_long_lat(TESTCASE, id_order, 'tujuan')
    list_koordinat_tujuan.append(tujuan_lat_lang)

#==============================
#Data is Ready

# Function =======
def fill_koordinat_form(xpath ,koordinat):
    wait = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, xpath)))
    form_input_koordinat = driver.find_element(By.XPATH, xpath)
    time.sleep(1)
    form_input_koordinat.send_keys(koordinat)
    time.sleep(1)
    form_input_koordinat.send_keys(Keys.ENTER)
    time.sleep(1)
    
def tambah_tujuan():
    time.sleep(1)
    tambah_tujuan = driver.find_element(By.XPATH, '//*[@id="omnibox-directions"]/div/div[3]/button/div[1]/div' )
    tambah_tujuan.click()
# Function =======

#open browser
chrome_driver = 'chrome/tes.exe'
options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=options)
driver.implicitly_wait(10) # seconds
driver.get("https://www.google.com/maps/")
#open browser

#Go to search route page
time.sleep(5)
rute_btn = driver.find_element(By.XPATH, '//*[@id="hArJGc"]')
rute_btn.click()
time.sleep(5)
#Go to search route page

#fill koordinat form asal
fill_koordinat_form('//*[@id="sb_ifc51"]/input' , asal_lat_lang)
#fill koordinat form asal

#fill koordinat form tujuan
#because we probably have >1 tujuan, so i using a for loop
counter_xpath = 2
for i in list_koordinat_tujuan:
    xpath = '//*[@id="sb_ifc5{}"]/input'.format(counter_xpath)
    fill_koordinat_form(xpath, i)
    counter_xpath = counter_xpath + 1
    tambah_tujuan()
    
    
    

