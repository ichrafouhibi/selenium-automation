from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_win_open")

    # Passer dans l'iframe avec le bouton
    driver.switch_to.frame("iframeResult")

    # Enregistrer la fenêtre principale
    main_window = driver.current_window_handle
    print(f"Fenêtre principale : {main_window}")

    # Cliquer sur le bouton qui ouvre une nouvelle fenêtre
    driver.find_element(By.TAG_NAME, "button").click()
    print("Nouvelle fenêtre ouverte")

    time.sleep(2)  # Attendre l'ouverture

    # Récupérer toutes les fenêtres ouvertes
    all_windows = driver.window_handles
    print(f"Fenêtres ouvertes : {all_windows}")

    # Trouver la nouvelle fenêtre (différente de la principale)
    for window in all_windows:
        if window != main_window:
            new_window = window
            break

    # Basculer vers la nouvelle fenêtre
    driver.switch_to.window(new_window)
    print("Basculé vers la nouvelle fenêtre")

    time.sleep(2)

    # Faire une action simple (par exemple récupérer le titre)
    print(f"Titre de la nouvelle fenêtre : {driver.title}")

    # Fermer la nouvelle fenêtre
    driver.close()
    print("Nouvelle fenêtre fermée")

    # Revenir à la fenêtre principale
    driver.switch_to.window(main_window)
    print("Revenu à la fenêtre principale")

    time.sleep(2)

finally:
    driver.quit()
