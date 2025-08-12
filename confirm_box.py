from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_confirm")

    # Passer dans l'iframe
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframeResult")))

    # Cliquer sur le bouton pour afficher la boîte de confirmation
    driver.find_element(By.TAG_NAME, "button").click()

    # Attendre la boîte de confirmation
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    confirm = driver.switch_to.alert
    print(f"Texte de la confirmation : {confirm.text}")
    time.sleep(5)
    # Accepter la confirmation (ou utiliser confirm.dismiss() pour refuser)
    confirm.accept()
    print("Confirmation acceptée")

    time.sleep(1)

    # Vérifier le résultat affiché après confirmation
    result_text = driver.find_element(By.ID, "demo").text
    print(f"Résultat affiché : {result_text}")

    time.sleep(2)

finally:
    driver.quit()
