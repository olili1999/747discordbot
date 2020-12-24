from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
driver = webdriver.Chrome(executable_path="./chromedriver.exe")
# Some versions are incompatible with selenium, try https://ftp.mozilla.org/pub/firefox/releases/30.0/win32/en-US/

# Request Dominos
driver.get("https://www.dominos.com/en/pages/order/?locations=1#/locations/")
driver.implicitly_wait(5)  # Allow page loading

# Enter Address Information (Type: Apartment)
Type = driver.find_element_by_id("Address_Type_Select")
for option in Type.find_elements_by_tag_name("option"):
    if option.text == "House":
        option.click()
        break
        # Fill information out prior to use

# clear autofill garbage
driver.find_element_by_id("Street").clear()  # <--- Street
driver.find_element_by_id("Address_Line_2").clear()  # <--- Apartment
driver.find_element_by_id("City_Sep").clear()
driver.find_element_by_id("Postal_Code_Sep").clear()

driver.find_element_by_id("Street").send_keys("747 Packard St")  # <--- Street
driver.find_element_by_id("Address_Line_2").send_keys("")  # <--- Apartment
driver.find_element_by_id("City_Sep").send_keys("Ann Arbor")  # <--- City
driver.find_element_by_id("Postal_Code_Sep").send_keys("48104")  # <--- Zip

State = driver.find_element_by_id("Region")
for option in State.find_elements_by_tag_name("option"):
    if option.text == "MI":  # <--- State (Ex. MA, NJ, NY)
        option.click()
        break

# Search for locations
driver.find_element(
    By.XPATH, ".//*[@id='locationSearchForm']/div/div[4]/button").click()
driver.implicitly_wait(10)  # Allow page loading

# click store pickup for nearby store
driver.find_element(
    By.XPATH,
    ".//*[@id='locationsResultsPage']/div[4]/div[2]/div[1]/div[2]/div/div[2]/div[1]/a"
).click()

single = True
double = False
driver.implicitly_wait(10)  # Allow page loading

driver.get("https://dominos.com")
driver.implicitly_wait(10)  # Allow page loading


def loop(string, max_attempts=3):
    attempt = 1
    while True:
        try:
            driver.execute_script(
                "arguments[0].click();",
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, string))))
            break
        except StaleElementReferenceException:
            if attempt == max_attempts:
                raise
            attempt += 1


# coupon code 9174
# https://www.dominos.com/en/pages/order/#/product/S_PIZZA/builder/?couponCode=9174&code=14SCREEN

# driver.get("https://dominos.com")
# driver.find_element_by_xpath(
#     ".//*[@id='homeWrapper']/main/section[5]/div/div[2]/div/span[4]/span/a"
# ).click()

# driver.find_element_by_xpath(
#     ".//*[@id='genericOverlay']/section/div/div[5]/section[1]/header/h2/button"
# ).click()
if (single == True):
    #Get to Pizza Ordering Screen
    driver.get(
        "https://www.dominos.com/en/pages/order/#/product/S_PIZZA/builder/?couponCode=9174&code=14SCREEN"
    )

    #Skip to Toppings Page
    driver.find_element_by_xpath(".//*[@id='toppings']").click()

    # Click "No Thanks" button
    # Below fixes the not clickable at this point error.
    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(
                (By.XPATH, ".//*[@id='stepUpsell']/div/button[1]"))))
    driver.implicitly_wait(10)  # Allow page loading

    # ADD INGREDIENTS SECTION
    loop(
        ".//*[contains(text(),'Ham')]/preceding-sibling::input[@type='checkbox']"
    )

    loop(
        ".//*[contains(text(),'Italian Sausage')]/preceding-sibling::input[@type='checkbox']"
    )
    loop(
        ".//*[contains(text(),'Bacon')]/preceding-sibling::input[@type='checkbox']"
    )

    #Click "Add to Order" button
    driver.find_element_by_xpath(
        ".//*[@id='pizzaSummaryInColumn']/div[1]/div[2]/div[2]/button").click(
        )
    # navigate to coupons page
    driver.get(
        "https://www.dominos.com/en/pages/order/#!/section/Coupons/category/All/"
    )
    #click "Add Coupon" button
    driver.execute_script(
        "arguments[0].click();",
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((
                By.XPATH,
                ".//*[@id='js-pageSplit']/section/div[2]/div/div[1]/div[9]/a/div[2]/button"
            ))))

    # Click "No Thanks to Donations" Button
    # loop(".//*[@id='genericOverlay']/section/div/div/div[2]/div/div[4]/a[2]")

    # Click "Done With This Coupon" Button
    loop(".//*[@id='genericOverlay']/section/div/div[6]/div[2]/a")

    # # Click "Continue Checkout" Button
    # loop(".//*[@id='js-checkoutColumns']/aside/div[3]/div[1]/a")

# coupon code 9133
# https://www.dominos.com/en/pages/order/#/product/S_PIZZA/builder/?couponCode=9193&code=12SCREEN
# if (double == True):

# # Straight to checkout
# driver.get("https://www.dominos.com/en/pages/order/payment.jsp")

# # Enter contact information                                              # Fill information out prior to use
# driver.find_element_by_id("First_Name").send_keys(
#     "[FIRST NAME]")  # <--- First Name
# driver.find_element_by_id("Last_Name").send_keys(
#     "[LAST NAME]")  # <--- Last Name
# driver.find_element_by_id("Email").send_keys("[EMAIL]")  # <--- Email
# driver.find_element_by_id("Callback_Phone").send_keys("[PHONE]")  # <--- Phone
# driver.find_element_by_id(
#     "Email_Opt_In").click()  # Opt in is preselected, click again to Opt out

# # Pay with cash upon delivery
# driver.find_element(
#     By.XPATH,
#     ".//*[@id='orderPaymentPage']/form/div[5]/div/div[2]/div/div[3]/label/input"
# ).click()
