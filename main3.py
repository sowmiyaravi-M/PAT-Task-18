from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CookieAutomation:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome() 
        self.driver.maximize_window()

    def login_and_display_cookies(self, username, password):
        # Open the URL
        self.driver.get(self.url)
        
        # Display cookies before login
        print("Cookies before login:")
        cookies_before_login = self.driver.get_cookies()
        for cookie in cookies_before_login:
            print(cookie)
        
        # Login
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "login-button")))

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()
        
        # Wait for the login process to complete
        time.sleep(2) 
        
        # Display cookies after login
        print("\nCookies after login:")
        cookies_after_login = self.driver.get_cookies()
        for cookie in cookies_after_login:
            print(cookie)

        # Logout
        burger_menu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "bm-burger-button")))
        burger_menu.click()
        logout_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
        logout_button.click()
        
        # Close the browser
        self.driver.quit()


if __name__ == "__main__":
    url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

    automation = CookieAutomation(url)
    automation.login_and_display_cookies(username, password)
