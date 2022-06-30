from copyreg import constructor
import csv
import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

if (len(sys.argv) < 1):
    raise Exception('Argument Missing: run with "blockchain explorer" "number of pages (opt)"')
elif (len(sys.argv) > 3):
    raise Exception('Too Many Arguments: run with "blockchain explorer" "number of pages (opt)"')
elif (len(sys.argv) > 1):
    if (sys.argv[1].isnumeric()):
        raise Exception('Argument Error: first argument must be the blockchain explorer')
    if (len(sys.argv) > 2):
            NUMBER_OF_PAGES = int(sys.argv[2])
    else:
        NUMBER_OF_PAGES = -1

SCAN = sys.argv[1].strip('https://').strip('http://').strip('/')

f = open(f'./{SCAN}_wellKnownAddresses.csv', 'w')
writer = csv.writer(f)
header = ['Address', 'Name']

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get(f'https://{SCAN}/accounts/1')

if (NUMBER_OF_PAGES == -1):
    NUMBER_OF_PAGES = int(driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_pageRecords"]/ul/li[3]/span/strong[2]').text)

for page in range(NUMBER_OF_PAGES):
    print(f'Parsing page {page}...')
    table = driver.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_divTable"]/table/tbody')
    rows = table.find_elements(By.TAG_NAME, "tr")
    
    for row in rows:
        elements = row.find_elements(By.TAG_NAME, 'td')
        
        address = elements[1].text
        name = elements[2].text

        if (len(name) > 0 and 
        'Tornado' not in name and
        'Exploiter' not in name and
        'Hacker' not in name):
            writer.writerow([address, name])

    driver.get(f'https://{SCAN}/accounts/{page}')

f.close()