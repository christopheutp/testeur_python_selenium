from selenium.webdriver.common.by import By
from .base_page import BasePage

class NotificationPage(BasePage):
    PATH = "/notification_message_rendered"

    PAGE_TITLE = (By.TAG_NAME, "h3")
    CLICK_HERE_LINK = (By.LINK_TEXT, "Click here")
    FLASH = (By.ID, "content")

    def open(self):
        super().open(self.PATH)

    def is_loaded(self):
        return self.wait_for_visibility(self.PAGE_TITLE).text.strip() == "Notification Message"

    def click_here(self):
        self.wait_for_clickable(self.CLICK_HERE_LINK).click()

    def get_notification_message(self):
        message = self.wait_for_visibility(self.FLASH).text.strip()
        return message.replace("x", "").strip()

    def is_expected_message(self, message):
        expected_messages = [
            "Action successful",
            "Action unsuccessful, please try again",
            "Action unsuccesful, please try again",
        ]
        return any(expected in message for expected in expected_messages)