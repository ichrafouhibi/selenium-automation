from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    # 1. Ouvrir la page TryIt
    driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit")

    # 2. Passer dans l'iframe du formulaire
    driver.switch_to.frame("iframeResult")

    # 3. Remplir les champs
    first_name = driver.find_element(By.NAME, "fname")
    first_name.clear()
    first_name.send_keys("Ichraf")

    last_name = driver.find_element(By.NAME, "lname")
    last_name.clear()
    last_name.send_keys("Ouhibi")

    # 4. Soumettre le formulaire
    submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    submit_button.click()

    # 5. Attendre un peu pour que la nouvelle page charge
    time.sleep(2)

    # 6. Récupérer le texte affiché dans la nouvelle page
    page_text = driver.find_element(By.TAG_NAME, "body").text

    # 7. Vérifier les valeurs
    if "Ichraf" in page_text and "Ouhibi" in page_text:
        print("✅ Test réussi : valeurs correctes affichées")
    else:
        print("❌ Test échoué : valeurs incorrectes")

    print("\n--- Contenu de la page ---")
    print(page_text)

    time.sleep(3)

finally:
    driver.quit()
