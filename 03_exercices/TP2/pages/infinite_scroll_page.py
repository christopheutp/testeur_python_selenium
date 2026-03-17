from selenium.webdriver.common.by import By
from .base_page import BasePage

class InfiniteScrollPage(BasePage):
    PATH = "/infinite_scroll"

    PAGE_TITLE = (By.TAG_NAME, "h3")
    PARAGRAPHS = (By.CSS_SELECTOR, ".jscroll-added")

    def open(self):
        super().open(self.PATH)

    def is_loaded(self):
        return self.wait_for_visibility(self.PAGE_TITLE).text.strip() == "Infinite Scroll"

    def get_paragraph_count(self):
        return len(self.driver.find_elements(*self.PARAGRAPHS))

    def wait_for_initial_content(self):
        self.wait.until(lambda d: len(d.find_elements(*self.PARAGRAPHS)) >= 1)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_for_more_content_than(self, previous_count):
        self.wait.until(lambda d: len(d.find_elements(*self.PARAGRAPHS)) > previous_count)