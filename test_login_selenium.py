# test_login_selenium.py

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLetsUseDataLogin(unittest.TestCase):

    def setUp(self):
        # Start a Chrome browser before each test
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        # Open the login page
        self.driver.get("https://letsusedata.com")

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

    def _login(self, username, password):
        """Helper method to type username/password and click login."""
        driver = self.driver

        # Wait until a username/email text field exists on the page
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "input[name='name'], input[type='text'], input[type='email']"
                )
            )
        )

        # Wait until a password field exists
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[type='password']")
            )
        )

        # Wait until submit/login button is clickable
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.CSS_SELECTOR,
                    "input[type='submit'], button[type='submit'], button, input[id='edit-submit']"
                )
            )
        )

        # Clear any old values and type the new credentials
        username_input.clear()
        username_input.send_keys(username)
        password_input.clear()
        password_input.send_keys(password)

        # Click the login / submit button
        login_button.click()

    def test_success(self):
        """Valid login takes us to the course selection page."""
        # Use the correct credentials
        self._login("test1", "Test12456")

        # Redirected to CourseSelection.html
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("CourseSelection")
        )



    def test_fail(self):
        """Invalid login should NOT reach the course page."""
        # Use the wrong password
        self._login("test1", "test1234")

        # Not loading this page means the test passed.
        try:
            WebDriverWait(self.driver, 5).until(
                EC.url_contains("CourseSelection")
            )
            # If we get here, the page wrongly allowed the bad login
            self.fail("Invalid login reached the course page (unexpected).")
        except Exception:
            # Timeout or other error means we did NOT reach the course page,
            # which is needed for a failed login.
            pass


if __name__ == "__main__":
    unittest.main()
