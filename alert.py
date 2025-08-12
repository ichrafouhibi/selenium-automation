from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")

    # Attendre que l'iframe soit présente puis switcher dedans
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframeResult")))

    # Cliquer sur le bouton pour déclencher l'alerte
    driver.find_element(By.TAG_NAME, "button").click()

    # Attendre que l'alerte soit présente
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    print(f"Message d'alerte : {alert.text}")
    time.sleep(5)

    alert.accept()
    print("Alerte acceptée")

    time.sleep(2)

finally:
    driver.quit()
