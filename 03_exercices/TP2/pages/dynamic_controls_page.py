from selenium.webdriver.common.by import By
from .base_page import BasePage

class DynamicControlsPage(BasePage):
    PATH = "/dynamic_controls"

    PAGE_TITLE = (By.TAG_NAME, "h4")
    #CHECKBOX = (By.CSS_SELECTOR, "#checkbox input[type='checkbox']")
    CHECKBOX = (By.ID, "checkbox")
    REMOVE_ADD_BUTTON = (By.CSS_SELECTOR, "#checkbox-example button")
    MESSAGE = (By.ID, "message")

    INPUT_FIELD = (By.CSS_SELECTOR, "#input-example input[type='text']")
    ENABLE_DISABLE_BUTTON = (By.CSS_SELECTOR, "#input-example button")

    def open(self):
        super().open(self.PATH)

    def is_loaded(self):
        return self.wait_for_visibility(self.PAGE_TITLE).text.strip() == "Dynamic Controls"

    def is_checkbox_present(self):
        return len(self.driver.find_elements(*self.CHECKBOX)) > 0

    def click_remove_add(self):
        self.wait_for_clickable(self.REMOVE_ADD_BUTTON).click()

    def wait_for_checkbox_disappear(self):
        self.wait_for_invisibility(self.CHECKBOX)

    def wait_for_checkbox_appear(self):
        self.wait_for_presence(self.CHECKBOX)
        self.wait_for_visibility(self.CHECKBOX)

    def get_message(self):
        return self.wait_for_visibility(self.MESSAGE).text.strip()

    def is_input_enabled(self):
        return self.wait_for_presence(self.INPUT_FIELD).is_enabled()

    def click_enable_disable(self):
        self.wait_for_clickable(self.ENABLE_DISABLE_BUTTON).click()

    def wait_for_input_enabled(self):
        self.wait.until(lambda d: d.find_element(*self.INPUT_FIELD).is_enabled())

    def enter_text(self, text):
        field = self.wait_for_visibility(self.INPUT_FIELD)
        field.clear()
        field.send_keys(text)

    def get_input_value(self):
        return self.wait_for_presence(self.INPUT_FIELD).get_attribute("value")