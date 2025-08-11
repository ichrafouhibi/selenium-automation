from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Remplace le chemin par celui de ton chromedriver si besoin
driver = webdriver.Chrome()

try:
    # Ouvre une page exemple
    driver.get("https://www.w3schools.com/html/html_forms.asp")

    # Exemple : clique sur le bouton "Submit" du formulaire (modifie le sélecteur si besoin)
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Submit")]'))
    )
    submit_button.click()

    # Ici tu peux ajouter une vérification, par exemple un message ou un changement de page
    print("Bouton cliqué avec succès !")

finally:
    driver.quit()
