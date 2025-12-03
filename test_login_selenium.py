import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLetsUseDataLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://letsusedata.com")

    def tearDown(self):
        self.driver.quit()

    def _login(self, username, password):
        driver = self.driver

        # Find a username/email field: try common patterns
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "input[name='name'], input[type='text'], input[type='email']"
                )
            )
        )

        # Find a password field
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[type='password']")
            )
        )

        # Try to find a login/submit button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "input[type='submit'], button[type='submit'], button, input[id='edit-submit']"
                )
            )
        )

        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)
        login_button.click()

    def test_success(self):
        """Valid login should succeed."""
        self._login("test1", "Test12456")

        # After successful login, look for something like a logout link or user area
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.PARTIAL_LINK_TEXT,
                    "Log out"
                )
            )
        )

    def test_fail(self):
        """Invalid login should show an error."""
        self._login("test1", "test1234")

        # Look for an error message.
        # Adjust the selector if the site uses a different class/id for errors.
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    ".messages--error, .error, .alert, .alert-danger"
                )
            )
        )


if __name__ == "__main__":
    unittest.main()
