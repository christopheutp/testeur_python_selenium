from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.dynamic_controls_page import DynamicControlsPage
from pages.dynamic_loading_page import DynamicLoadingPage
from pages.infinite_scroll_page import InfiniteScrollPage
from pages.notification_page import NotificationPage

def create_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver


def test_dynamic_controls():
    print("\n" + "=" * 60)
    print("TP2 - TEST 1 : DYNAMIC CONTROLS")
    print("=" * 60)

    driver = create_driver()

    try:
        page = DynamicControlsPage(driver)

        print("\n1. Ouverture de la page Dynamic Controls...")
        page.open()
        assert page.is_loaded(), "La page Dynamic Controls n'est pas correctement chargée"
        print("   Page chargée")

        print("2. Vérification de la présence de la checkbox...")
        assert page.is_checkbox_present(), "La checkbox devrait être présente au départ"
        print("   Checkbox présente")

        print("3. Clic sur Remove...")
        page.click_remove_add()

        print("4. Attente de la disparition de la checkbox...")
        page.wait_for_checkbox_disappear()
        assert not page.is_checkbox_present(), "La checkbox devrait avoir disparu"
        print("   Checkbox supprimée")

        print("5. Vérification du message affiché...")
        message = page.get_message()
        assert "It's gone!" in message, f"Message inattendu : {message}"
        print(f"   Message correct : {message}")

        print("6. Clic sur Add...")
        page.click_remove_add()

        print("7. Attente de la réapparition de la checkbox...")
        page.wait_for_checkbox_appear()
        assert page.is_checkbox_present(), "La checkbox devrait être revenue"
        print("   Checkbox réapparue")

        print("8. Vérification du message affiché...")
        message = page.get_message()
        assert "It's back!" in message, f"Message inattendu : {message}"
        print(f"   Message correct : {message}")

        print("9. Vérification que le champ texte est désactivé au départ...")
        assert not page.is_input_enabled(), "Le champ texte devrait être désactivé au départ"
        print("   Champ désactivé")

        print("10. Clic sur Enable...")
        page.click_enable_disable()

        print("11. Attente de l'activation du champ texte...")
        page.wait_for_input_enabled()
        assert page.is_input_enabled(), "Le champ texte devrait être activé"
        print("   Champ activé")

        print("12. Saisie d'un texte de test...")
        test_text = "Test Selenium TP2"
        page.enter_text(test_text)
        assert page.get_input_value() == test_text, "La valeur saisie dans le champ est incorrecte"
        print(f"   Texte saisi correctement : {page.get_input_value()}")

        print("\nTEST 1 RÉUSSI")

    except AssertionError as e:
        print(f"\nAssertion échouée : {e}")
        raise
    except Exception as e:
        print(f"\nErreur : {e}")
        raise
    finally:
        driver.quit()
        print("Navigateur fermé")


def test_dynamic_loading():
    print("\n" + "=" * 60)
    print("TP2 - TEST 2 : DYNAMIC LOADING")
    print("=" * 60)

    driver = create_driver()

    try:
        page = DynamicLoadingPage(driver)

        print("\n1. Ouverture de la page Dynamic Loading...")
        page.open()
        assert page.is_loaded(), "La page Dynamic Loading n'est pas correctement chargée"
        print("   Page chargée")

        print("2. Ouverture de Example 2...")
        page.open_example_2()
        assert "/dynamic_loading/2" in page.get_current_url(), "La navigation vers Example 2 a échoué"
        print("   Example 2 ouvert")

        print("3. Vérification du bouton Start...")
        assert page.is_start_button_present(), "Le bouton Start devrait être présent"
        print("   Bouton Start présent")

        print("4. Clic sur Start...")
        page.click_start()

        print("5. Attente du contenu dynamique...")
        result = page.wait_for_hello_world()
        assert result == "Hello World!", f"Texte inattendu : {result}"
        print(f"   Texte affiché correctement : {result}")

        print("\nTEST 2 RÉUSSI")

    except AssertionError as e:
        print(f"\nAssertion échouée : {e}")
        raise
    except Exception as e:
        print(f"\nErreur : {e}")
        raise
    finally:
        driver.quit()
        print("Navigateur fermé")


def test_notification_message():
    print("\n" + "=" * 60)
    print("TP2 - TEST 3 : NOTIFICATION MESSAGE")
    print("=" * 60)

    driver = create_driver()

    try:
        page = NotificationPage(driver)

        print("\n1. Ouverture de la page Notification Message...")
        page.open()
        assert page.is_loaded(), "La page Notification Message n'est pas correctement chargée"
        print("   Page chargée")

        print("2. Lecture du message initial...")
        initial_message = page.get_notification_message()
        assert initial_message != "", "Le message initial ne devrait pas être vide"
        print(f"   Message initial : {initial_message}")

        for i in range(1, 4):
            print(f"{i + 2}. Clic sur 'Click here'...")
            page.click_here()

            message = page.get_notification_message()
            assert message != "", "Le message après clic ne devrait pas être vide"
            assert page.is_expected_message(message), f"Message inattendu : {message}"
            print(f"   Message reçu : {message}")

        print("\nTEST 3 RÉUSSI")

    except AssertionError as e:
        print(f"\nAssertion échouée : {e}")
        raise
    except Exception as e:
        print(f"\nErreur : {e}")
        raise
    finally:
        driver.quit()
        print("Navigateur fermé")


def test_infinite_scroll():
    print("\n" + "=" * 60)
    print("TP2 - TEST 4 : INFINITE SCROLL")
    print("=" * 60)

    driver = create_driver()

    try:
        page = InfiniteScrollPage(driver)

        print("\n1. Ouverture de la page Infinite Scroll...")
        page.open()
        assert page.is_loaded(), "La page Infinite Scroll n'est pas correctement chargée"
        print("   Page chargée")

        print("2. Attente du contenu initial...")
        page.wait_for_initial_content()
        initial_count = page.get_paragraph_count()
        assert initial_count >= 1, "Au moins un bloc de contenu devrait être présent"
        print(f"   Nombre initial de blocs : {initial_count}")

        print("3. Scroll vers le bas...")
        page.scroll_to_bottom()

        print("4. Attente de contenu supplémentaire...")
        page.wait_for_more_content_than(initial_count)
        after_scroll_count = page.get_paragraph_count()
        assert after_scroll_count > initial_count, "Le nombre de blocs devrait avoir augmenté"
        print(f"   Nombre de blocs après scroll : {after_scroll_count}")

        print("\nTEST 4 RÉUSSI")

    except AssertionError as e:
        print(f"\nAssertion échouée : {e}")
        raise
    except Exception as e:
        print(f"\nErreur : {e}")
        raise
    finally:
        driver.quit()
        print("Navigateur fermé")