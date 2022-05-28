import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from playsound import playsound

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

data = {
    "nombre"        : "4",      #Change values
    "time_seconds"  : 5         #Change values
}
path = '.\chromedriver.exe'
s = Service(path)
browser = webdriver.Chrome(service=s, options= chrome_options)

browser.get('https://teleservices.paris.fr/rdvtitres/jsp/site/Portal.jsp?page=appointmentsearch&view=search&category=titres')
main_window = browser.current_window_handle
while True:


    name='nb_consecutive_slots'
    nombre = browser.find_element(by=By.NAME, value=name)
    nombre.clear()
    nombre.send_keys(data.get("nombre"))

    name2='action_search'
    browser.find_element(by=By.NAME, value=name2).click()

    text = "Aucun rendez-vous n'est actuellement disponible."

    if (text not in browser.page_source):
        playsound('victory.wav')
        print('RDV trouvé !')
        break
    else:
        print("PAS DE RDV")
        time.sleep(1)
        browser.refresh()
        #browser.quit()             #close and restart a new chrome instance 
        #playsound('nope.wav')      #play a sound when it fails
        time.sleep(data.get("time_seconds"))
