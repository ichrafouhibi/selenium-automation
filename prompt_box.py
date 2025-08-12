from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt")

    # Passer dans l'iframe
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "iframeResult")))

    # Cliquer sur le bouton pour afficher la boîte de prompt
    driver.find_element(By.TAG_NAME, "button").click()

    # Attendre la boîte de prompt
    WebDriverWait(driver, 10).until(EC.alert_is_present())

    prompt = driver.switch_to.alert
    print(f"Texte du prompt : {prompt.text}")

    # Envoyer un texte dans le prompt
    prompt.send_keys("Ichraf")
    time.sleep(1)

    # Accepter (OK)
    prompt.accept()
    print("Texte envoyé et prompt accepté")

    time.sleep(2)

    # Récupérer le texte affiché dans la page via JavaScript
    result_text = driver.execute_script("return document.getElementById('demo').innerText;")
    print(f"Résultat affiché (via JS) : {result_text}")

finally:
    driver.quit()
