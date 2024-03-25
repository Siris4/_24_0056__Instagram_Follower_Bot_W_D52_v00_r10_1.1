
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException


# Constants
INSTAGRAM_EMAIL = "YOUR_EMAIL"
INSTAGRAM_PASSWORD = "YOUR_PASSWORD"
SIMILAR_ACCOUNT = "billnye"

class InstaFollower:
    URL_FOR_INSTAGRAM = "https://www.instagram.com/"

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.init_driver()

    def init_driver(self):
        options = Options()
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    def log_message(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{timestamp} - {message}")

    def login(self):
        start_timer = time.time()

        self.log_message("Starting login process")
        self.driver.get(self.URL_FOR_INSTAGRAM)
        time.sleep(5)

        username_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
        username_field.send_keys(self.username)
        self.log_message("Username/Email entered")

        password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
        password_field.send_keys(self.password)
        self.log_message("Password entered")

        password_field.send_keys(Keys.RETURN)
        self.log_message("Login submitted")
        time.sleep(5)

        self.click_first_not_now_button()
        self.click_second_not_now_button()
        self.click_third_not_now_button()

        end_timer = time.time()
        total_login_time = end_timer - start_timer
        self.log_message(f"Total login time: {total_login_time} seconds")

        return total_login_time


    def click_first_not_now_button(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Not now']")))
            self.log_message("The first popup 'Not now' button appeared.")
        except TimeoutException:
            self.log_message("No 'Not now' popup within 3 seconds.")
            return

        selectors = [
            {"by": By.XPATH, "value": "//div[text()='Not now']"},
            {"by": By.XPATH,
             "value": "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div"},
            {"by": By.CSS_SELECTOR,
             "value": "#mount_0_0_i\\+ > div > div > div.x9f619.x1n2onr6.x1ja2u2z > div > div > div.x78zum5.xdt5ytf.x1t2pt76.x1n2onr6.x1ja2u2z.x10cihs4 > div.x9f619.xvbhtw8.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1uhb9sk.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.x1q0g3np.xqjyukv.x1qjc9v5.x1oa3qoh.x1qughib > div.x1gryazu.xh8yej3.x10o80wk.x14k21rp.x17snn68.x6osk4m.x1porb0y > section > main > div > div > div > div > div"},
            {"by": By.CLASS_NAME, "value": "x1i10hfl"}
        ]

        for selector in selectors:
            try:
                element = self.driver.find_element(selector['by'], selector['value'])
                element.click()
                self.log_message(f"'Not now' button clicked using {selector['by']}='{selector['value']}'")
                break
            except NoSuchElementException:
                self.log_message(f"'Not now' button not found using {selector['by']}='{selector['value']}'")
            except Exception as e:
                self.log_message(f"Error clicking 'Not now' button using {selector['by']}='{selector['value']}': {e}")

    def click_second_not_now_button(self):
        time.sleep(3)  # Wait for 3 seconds before looking for the second button
        try:
            WebDriverWait(self.driver, 4).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
            self.log_message("The second 'Not now' button appeared.")
        except TimeoutException:
            self.log_message("No second 'Not now' popup within 4 seconds.")
            return

        selectors = [
            {"by": By.XPATH, "value": "//button[text()='Not Now']"},
            {"by": By.XPATH,
             "value": "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"},
            {"by": By.CSS_SELECTOR, "value": "button._a9--._ap36._a9_1"},
            {"by": By.CLASS_NAME, "value": "_a9--"}
        ]

        for selector in selectors:
            try:
                element = self.driver.find_element(selector["by"], selector["value"])
                element.click()
                self.log_message(f"Second 'Not now' button clicked using {selector['by']}='{selector['value']}'")
                break
            except NoSuchElementException:
                self.log_message(f"Second 'Not now' button not found using {selector['by']}='{selector['value']}'")
            except Exception as e:
                self.log_message(
                    f"Error clicking second 'Not now' button using {selector['by']}='{selector['value']}': {e}")

    def click_third_not_now_button(self):
        self.log_message("Checking for third 'Not Now' button.")
        selectors = [
            {"by": By.XPATH, "value": "//button[text()='Not Now']"},
            {"by": By.CSS_SELECTOR, "value": "button._a9--._ap36._a9_1"},
            {"by": By.XPATH,
             "value": "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"},
            {"by": By.CSS_SELECTOR,
             "value": "body > div > div > div > div > div > div > div > div > button._a9--._ap36._a9_1"},
            {"by": By.CLASS_NAME, "value": "_a9--"}
        ]

        start_time = time.time()
        found = False
        for selector in selectors:
            if time.time() - start_time > 4:
                break  # Exit the loop if total time exceeds 4 seconds

            try:
                element = WebDriverWait(self.driver, 4 - (time.time() - start_time)).until(
                    EC.presence_of_element_located((selector["by"], selector["value"])))
                self.log_message(f"Third 'Not now' button found using {selector['by']}='{selector['value']}'")
                element.click()
                self.log_message("Third 'Not now' button clicked.")
                found = True
                break
            except TimeoutException:
                self.log_message(
                    f"No 'Not now' button appeared using {selector['by']}='{selector['value']}' within the time frame.")
            except Exception as e:
                self.log_message(f"Error clicking 'Not now' button using {selector['by']}='{selector['value']}': {e}")

        if not found:
            self.log_message("Third 'Not now' button was not found after trying all selectors.")


    def find_followers(self):
        # Placeholder for future implementation
        pass

    def follow(self):
        # Placeholder for future implementation
        pass

    def close_browser(self):
        input("Press Enter to close the browser...")
        self.driver.quit()
        self.log_message("Browser closed.")

# Instantiate and use the Instagram bot
instagram_bot = InstaFollower(INSTAGRAM_EMAIL, INSTAGRAM_PASSWORD)
total_login_time = instagram_bot.login()
instagram_bot.find_followers()
instagram_bot.follow()
instagram_bot.close_browser()
