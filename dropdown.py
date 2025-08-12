from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")

    # Passer dans l’iframe où se trouve la liste déroulante
    driver.switch_to.frame("iframeResult")

    select_element = driver.find_element(By.ID, "cars")
    select = Select(select_element)

    # Sélection par valeur
    select.select_by_value("volvo")
    print("Sélection par valeur : volvo")
    time.sleep(1)

    # Sélection par index
    select.select_by_index(2)
    print("Sélection par index : 2")
    time.sleep(1)

    # Sélection par texte visible
    select.select_by_visible_text("Audi")
    print("Sélection par texte visible : Audi")
    time.sleep(1)

    # Cliquer sur le bouton Submit (ici c’est un bouton input de type submit)
    submit_button = driver.find_element(By.XPATH, '//input[@type="submit"]')
    submit_button.click()
    print("Bouton Submit cliqué")
    time.sleep(5)

finally:
    driver.quit()
