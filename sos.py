from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


keywords = {
  "Natural_Disaster" : ('Earthquake', 'Flood', 'Tsunami', 'Cyclone', 'Hurricane', 'Typhoon', 'Blizzard', 'Snow Storm', 'Hail', 'Drought', 'Tornado', 'Cold Wave', 'Heat Wave', 'Wildfires', 'Reconstruction', 'Climate Change', 'Global Warming', 'Emission', 'Carbon cycle', 'Carbon Credit', 'El Nino', 'La Nina', 'Ecosystem', 'Greenhouse gases', 'Methane', 'Landslide', 'Mudslide', 'Avalanche', 'Ozone', 'Storm'),
  "Government_Policy_Change" : ('Government Shutdown', 'Brexit', 'Supreme Court', 'Justice department', 'Parliament', 'Congress', 'reserves', 'President', 'Prime Minister', 'Opposition Leader', 'Donald Trump', 'Theresa May', 'World Trade Organization', 'European Union', 'Subsidies', 'Elections', 'Impeachment', 'Jeremy Corbyn', 'Asylum', 'Immigrants', 'Border Wall', 'National Securities', 'Military'),
  "Financial_Policy_Change" : ('Budget', 'Tariff', 'Trade', 'Capital Market', 'Interest Rates', 'Central Bank', 'GDP', 'Deficits ', 'surpluses', 'Inflation', 'Unemployment', 'Nonfarm Payrolls', 'Consumer Confidence', 'CPI', 'Treasury', 'Federal Reserve', 'Fed', 'Import', 'Export', 'ForEx', 'EXIM', 'Foriegn Exchange', 'Monetary Policy', 'Fiscal Policy', 'Tax', 'Embargo', 'Money laundering', 'GNP', 'Exchange Rate', 'Economy', 'USD', 'Pound Sterling', 'US Dollar', 'Australian Dollar', 'GBP', 'AUD', 'EUR', 'Sanction'),
  "Social_Unrest" : ('Social Unrest', 'Terrorism', 'Protest ', 'Far Right', 'Nazi', 'KKK', 'Racism', 'Radicalism', 'Civil War', 'Attack', 'Nuclear', 'Revolution', 'Coup', 'Strikes', 'Riot', 'War', 'Election', 'Corruption', 'Civil Unrest', 'Extremist', 'Nationalist', 'Rebellion', 'movement', 'uprising', 'rioting', 'turmoil', 'Activist', 'Imprisonment', 'Overpopulation', 'Hunger', 'Poverty', 'NRA', 'Mass shooting', 'Shooting', 'Martial Law', 'National Emergency', 'Insurgency')
}


webdriver_path = 'C:/Users/E115228/Downloads/chromedriver'

def enable_headless_download(browser, download_path):
    # Add missing support for chrome "send_command" to selenium webdriver
    browser.command_executor._commands["send_command"] = \
        ("POST", '/session/$sessionId/chromium/send_command')
 
    params = {'cmd': 'Page.setDownloadBehavior',
              'params': {'behavior': 'allow', 'downloadPath': download_path}}
    browser.execute("send_command", params)

# Add arguments telling Selenium to not actually open a window


for keyword in keywords['Social_Unrest']:
    download_path = 'data/' + keyword
    chrome_options = Options()
    download_prefs = {'download.default_directory' : download_path,
                      'download.prompt_for_download' : False,
                      'profile.default_content_settings.popups' : 0}

    chrome_options.add_experimental_option('prefs', download_prefs)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1920x1080')
    url = 'https://trends.google.com/trends/explore?date=2018-10-01%202019-04-08&geo=FI&q=' + keyword
    # Start up browser
    browser = webdriver.Chrome(executable_path=webdriver_path,chrome_options=chrome_options)
    browser.get(url) 
    enable_headless_download(browser, download_path)
    # Load webpage
    browser.get(url)
    time.sleep(5)
    button = browser.find_element("css selector",'.widget-actions-item.export')
    button.click()
    time.sleep(5)
    browser.quit()
