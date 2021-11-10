
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('/Users/opazmino/Downloads/chromedriver')
browser = webdriver.Chrome(service=s)
url = 'https://cleveronly.com/brainbucket/index.php?route=account/login'
browser.get(url)
browser.maximize_window()
logo = browser.find_element_by_xpath("//img[@title='Brainbucket']")
newregistrantbtn = browser.find_element_by_xpath("//a[contains(text(),'Continue')]")

customerType = "RETURNING"

if customerType == "NEW":

    newregistrantbtn.click()

    firstname_field = browser.find_element_by_xpath("//fieldset/div[2]")
    firstname_field_class = firstname_field.get_attribute("class")
    assert "required" in firstname_field_class
    firstname_input = browser.find_element_by_id("input-firstname")
    firstname_input.clear()
    firstname_input.send_keys("Olesia")

    lastname_field = browser.find_element_by_xpath("//fieldset/div[3]")
    lastname_field_class = firstname_field.get_attribute("class")
    assert "required" in lastname_field_class
    lastname_input = browser.find_element_by_id("input-lastname")
    lastname_input.clear()
    lastname_input.send_keys("Paz")

    email_field = browser.find_element_by_xpath("//fieldset/div[4]")
    email_field_class = email_field.get_attribute("class")
    assert "required" in email_field_class
    email_input = browser.find_element_by_id("input-email")
    email_input.clear()
    email_input.send_keys("testing1@gmail.com")

    telephone_field = browser.find_element_by_xpath("//fieldset/div[5]")
    telephone_field_class = telephone_field.get_attribute("class")
    assert "required" in telephone_field_class
    telephone_input = browser.find_element_by_id("input-telephone")
    telephone_input.clear()
    telephone_input.send_keys("3147689098")

    fax_field = browser.find_element_by_xpath("//fieldset/div[6]")
    fax_field_class = fax_field.get_attribute("class")
    fax_input = browser.find_element_by_id("input-fax")
    fax_input.clear()
    fax_input.send_keys("456-098-090")

    company_field = browser.find_element_by_xpath("//fieldset[2]/div[1]")
    company_field_class = company_field.get_attribute("class")
    company_input = browser.find_element_by_id("input-company")
    company_input.clear()
    company_input.send_keys("Global M")

    address1_field = browser.find_element_by_xpath("//fieldset[2]/div[2]")
    address1_field_class = address1_field.get_attribute("class")
    assert "required" in address1_field_class
    address1_input = browser.find_element_by_id("input-address-1")
    address1_input.clear()
    address1_input.send_keys("45 Madre Linda Blvd")

    address2_field = browser.find_element_by_xpath("//fieldset[2]/div[3]")
    address2_field_class = address2_field.get_attribute("class")
    address2_input = browser.find_element_by_id("input-address-2")
    address2_input.clear()
    address2_input.send_keys("APT 56")

    city_field = browser.find_element_by_xpath("//fieldset[2]/div[4]")
    city_field_class = city_field.get_attribute("class")
    assert "required" in city_field_class
    city_input = browser.find_element_by_id("input-city")
    city_input.clear()
    city_input.send_keys("Los Angeles")

    postcode_field = browser.find_element_by_xpath("//fieldset[2]/div[5]")
    postcode_field_class = address2_field.get_attribute("class")
    postcode_input = browser.find_element_by_id("input-postcode")
    postcode_input.clear()
    postcode_input.send_keys("90210")

    country_field = browser.find_element_by_xpath("//fieldset[2]/div[6]")
    country_field_class = country_field.get_attribute("class")
    assert "required" in country_field_class
    country_input = browser.find_element_by_id("input-country")
    # country_input.clear()
    country_input.send_keys("Ecuador")


    password_field = browser.find_element_by_xpath("//fieldset[3]/div[1]")
    password_field_class = password_field.get_attribute("class")
    assert "required" in password_field_class
    password_input = browser.find_element_by_id("input-password")
    password_input.clear()
    password_input.send_keys("Pass234word")

    confirmpassword_field = browser.find_element_by_xpath("//fieldset[3]/div[2]")
    confirmpassword_field_class = confirmpassword_field.get_attribute("class")
    assert "required" in confirmpassword_field_class
    confirmpassword_input = browser.find_element_by_id("input-confirm")
    confirmpassword_input.clear()
    confirmpassword_input.send_keys("Pass234word")
elif customerType == "RETURNING":
    email_field = browser.find_element_by_xpath("//div[@id='content']/div/div[2]/div/form/div[1]")
    email_field_class = email_field.get_attribute("class")
    email_input = browser.find_element_by_id("input-email")
    email_input.clear()
    email_input.send_keys("testing1@gmail.com")

    password_field = browser.find_element_by_xpath("//div[@id='content']/div/div[2]/div/form/div[2]")
    password_field_class = password_field.get_attribute("class")
    password_input = browser.find_element_by_id("input-password")
    password_input.clear()
    password_input.send_keys("Pass234word")

    loginbtn = browser.find_element_by_xpath("//input[@type='submit']")
    loginbtn.click()









