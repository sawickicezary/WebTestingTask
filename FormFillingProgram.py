# Code written by Cezary Sawicki [sawickicezary@outlook.com] for recruitment process only.

from selenium import webdriver
from selenium.webdriver.support.ui import Select


class FormFillingProgram:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='D:\Python Projects\WebTestingTask\chromedriver\chromedriver.exe')
        self.driver.get("https://dev-1.clicktrans.pl/register-test/courier")  # Load page
        self.inputData()
        self.fillForm()
        self.returnInformation()

    # Filling form with data
    def fillForm(self):
        registerCompanyName = self.driver.find_element_by_id("user_register_company_name")
        registerCompanyName.send_keys(self.companyName)
        registerEmail = self.driver.find_element_by_id("user_register_email")
        registerEmail.send_keys(self.email)
        registerFullName = self.driver.find_element_by_id("user_register_name")
        registerFullName.send_keys(self.fullName)
        registerPhoneCode = self.driver.find_element_by_id("user_register_phoneCode")
        registerPhoneNumber = self.driver.find_element_by_id("user_register_phone")
        registerPhoneNumber.send_keys(self.phoneNumber)
        registerUserPassword = self.driver.find_element_by_id("user_register_plainPassword")
        registerUserPassword.send_keys(self.phoneNumber)

        # Choosing Phone Code with HTML select
        select = Select(self.driver.find_element_by_id("user_register_phoneCode"))
        select.select_by_value(self.phoneCode)

        # Regulation checkbox
        if self.regulationsCheck == "YES":
            registerRegulationsCheck = self.driver.find_element_by_id("user_register_settings_agreementRegulations")
            registerRegulationsCheck.click()

        # Personal data checkbox
        if self.personalDataCheck == "YES":
            registerPersonalDataCheck = self.driver.find_element_by_id("user_register_settings_agreementPersonalData")
            registerPersonalDataCheck.click()

        # Marketing checkbox
        if self.personalDataCheck == "YES":
            registerMarketingCheck = self.driver.find_element_by_id("user_register_settings_agreementMarketing")
            registerMarketingCheck.click()

        # Submit form
        registerSubmitButton = self.driver.find_element_by_id("user_register_submit")
        registerSubmitButton.click()

    # Input data to fill form with
    def inputData(self):
        self.companyName = input("Company Name: ")
        self.email = input("Email address: ")
        self.fullName = input("Full Name: ")
        self.userPassword = input("Password: ")
        self.phoneCode = input("Phone code: +")
        self.phoneNumber = input("Phone number: ")
        self.regulationsCheck = input('Write "YES" if you agree with page regulations (required): ')
        self.personalDataCheck = input('Write "YES" if you agree with page personal data processing (required): ')
        self.marketingCheck = input('Write "YES" if you agree with page Marketing: ')

    # Get return information from webpage
    def returnInformation(self):
        message = self.driver.find_element_by_xpath("/html/body/div[@class='ui container flashmsg']/div")
        if message != None:
            print("Page return message: {} ".format(message.text))


FormFillingProgram()
