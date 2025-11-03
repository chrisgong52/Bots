"""
Simple Selenium bot to open a target website, wait until loaded,
take a screenshot, and exit.

Replace TARGET_URL with the URL you want to open.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

# CONFIG
# TARGET_URL = "https://www.target.com/p/pok-233-mon-trading-card-game-mega-evolution-8212-phantasmal-flames-elite-trainer-box/-/A-94860231#lnk=sametab"   # <-- change this to the site you want
TARGET_URL = "https://buff.ly/b85hA2Q"
TEMP_URL = "https://www.target.com/p/pokemon-tcg-25th-anniversary-pikachu-v-union-collection/-/A-1001040371#lnk=sametab"
HEADLESS = False                     # set True to run without opening a window
IMPLICIT_WAIT = 5                    # seconds for implicit waits
PAGE_LOAD_TIMEOUT = 30               # seconds for page load
SCREENSHOT_PATH = "site_screenshot.png"

def create_chrome_driver(headless: bool = False) -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    # Useful options:
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1280,800")
    # Optionally set a user-agent:
    # options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) ...")

    # Avoid the "Chrome is being controlled by automated software" infobar (cosmetic)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    if headless:
        options.add_argument("--headless=new")  # use new headless implementation when available

    # Create driver via webdriver-manager so you don't need chromedriver binary
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Optional: reduce bot fingerprinting (not guaranteed and don't use to evade site's policies)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined})
        """
    })

    driver.implicitly_wait(IMPLICIT_WAIT)
    driver.set_page_load_timeout(PAGE_LOAD_TIMEOUT)
    return driver

def open_site_and_capture(url: str):
    driver = None
    try:
        driver = create_chrome_driver(HEADLESS)
        print(f"Opening {url} ...")
        driver.get(url)

        # Wait until the <body> element is present and document.readyState is complete
        WebDriverWait(driver, PAGE_LOAD_TIMEOUT).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
        # Optionally wait for a particular element:
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        print("Page loaded. Sleeping briefly to allow dynamic content to settle...")
        # time.sleep(1)  # small pause to let JS-rendered pieces load (adjust if needed)

        # Save screenshot
        driver.save_screenshot(SCREENSHOT_PATH)
        print(f"Screenshot saved to {SCREENSHOT_PATH}")

        # Example: print the page title
        print("Page title:", driver.title)

        # Wait until the button is clickable and then click it
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@id, 'addToCartButtonOrText')]"))
        )
        button.click()
        print("✅ Button clicked!")

        # 💤 Add a delay after the click
        # time.sleep(1)  # wait 3 seconds (adjust to your needs)
        driver.find_element(By.LINK_TEXT, "View cart & check out").click()
        # time.sleep(2)  # wait 3 seconds (adjust to your needs)
        
        username_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "username"))
        )

        # Enter your username/email
        username_input.send_keys("19christopherg@alumni.harker.org")

        print("✅ Username entered!")

        try:
            # Wait until the login button is clickable
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "login"))
            )

            try:
                # Scroll into view and click normally
                driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
                login_button.click()
                print("✅ 'Continue' button clicked normally!")

            except ElementClickInterceptedException:
                # Fallback: JS click if normal click is blocked
                print("⚠️ Click intercepted, using JavaScript click instead")
                driver.execute_script("arguments[0].click();", login_button)
                print("✅ 'Continue' button clicked via JavaScript!")

            # time.sleep(2)  # optional pause to observe result

        except TimeoutException:
            print("❌ Timeout: 'Continue' button not found or not clickable.")

        try:
            # Wait until the div is clickable
            password_div = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "password"))
            )

            try:
                # Scroll into view and click normally
                driver.execute_script("arguments[0].scrollIntoView(true);", password_div)
                password_div.click()
                print("✅ Password div clicked normally!")

            except ElementClickInterceptedException:
                # Fallback: JS click if normal click is blocked
                print("⚠️ Click intercepted, using JavaScript click instead")
                driver.execute_script("arguments[0].click();", password_div)
                print("✅ Password div clicked via JavaScript!")

            # time.sleep(1)  # optional pause to observe result

        except TimeoutException:
            print("❌ Timeout: Password div not found or not clickable.")

        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "password"))
        )

        # Enter your password
        password_input.send_keys("ChrisTarget52!")

        print("✅ Password entered!")

        try:
            # Wait until the button with the exact text is clickable
            sign_in_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Sign in with password']"))
            )

            try:
                # Scroll into view and click normally
                driver.execute_script("arguments[0].scrollIntoView(true);", sign_in_button)
                sign_in_button.click()
                print("✅ 'Sign in with password' button clicked normally!")

            except ElementClickInterceptedException:
                # Fallback: JS click if normal click is blocked
                print("⚠️ Click intercepted, using JavaScript click instead")
                driver.execute_script("arguments[0].click();", sign_in_button)
                print("✅ 'Sign in with password' button clicked via JavaScript!")

            # time.sleep(1)  # optional pause to observe result

        except TimeoutException:
            print("❌ Timeout: 'Sign in with password' button not found or not clickable.")


        # Wait helper
        def wait_and_fill(by, identifier, value):
            element = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((by, identifier))
            )
            element.clear()
            element.send_keys(value)
            print(f"✅ Filled {identifier} with {value}")

        # Fill out the form
        wait_and_fill(By.ID, "first_name", "Chris")
        wait_and_fill(By.ID, "last_name", "Gong")
        wait_and_fill(By.ID, "address_line1", "20341 Chateau Drive")
        wait_and_fill(By.ID, "zip_code", "95070")  # replace with your random zip code
        wait_and_fill(By.ID, "city", "Saratoga")
        wait_and_fill(By.ID, "phone_number", "4087979839")  # replace with your random phone

        # Select state
        state_select = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "state"))
        )
        select = Select(state_select)
        select.select_by_visible_text("California")
        print("✅ Selected state California")

        # time.sleep(1)

    except Exception as e:
        print("Error:", e)
    finally:
        time.sleep(1000)
        # if driver:
        #     print("Closing browser.")
        #     driver.quit()

if __name__ == "__main__":
    open_site_and_capture(TARGET_URL)
    # open_site_and_capture(TEMP_URL)
