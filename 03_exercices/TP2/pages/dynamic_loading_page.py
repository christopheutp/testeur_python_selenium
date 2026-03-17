from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class DynamicLoadingPage(BasePage):
    PATH = "/dynamic_loading"

    PAGE_TITLE = (By.TAG_NAME, "h3")
    EXAMPLE_2_LINK = (By.CSS_SELECTOR, "a[href='/dynamic_loading/2']")
    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    LOADING = (By.ID, "loading")
    FINISH = (By.ID, "finish")

    def open(self):
        super().open(self.PATH)

    def is_loaded(self):
        return self.wait_for_visibility(self.PAGE_TITLE).text.strip() == "Dynamically Loaded Page Elements"

    def open_example_2(self):
        self.wait_for_clickable(self.EXAMPLE_2_LINK).click()
        self.wait.until(EC.url_contains("/dynamic_loading/2"))

    def is_start_button_present(self):
        return self.wait_for_visibility(self.START_BUTTON).is_displayed()

    def click_start(self):
        self.wait_for_clickable(self.START_BUTTON).click()

    def wait_for_hello_world(self):
        self.wait_for_invisibility(self.LOADING)
        return self.wait_for_visibility(self.FINISH).text.strip()