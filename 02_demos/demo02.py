from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# 1. Ouvrir un navigateur
# Télécharge automatiquement chromedriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 2. Aller sur un site
    driver.get("https://example.com")

    # 3. Vérifier le titre
    print(f"Titre: {driver.title}")

    # 4. Attendre un peu
    input("Appuyez sur Entrée pour fermer...")

finally:
    # 5. Fermer le navigateur
    driver.quit()