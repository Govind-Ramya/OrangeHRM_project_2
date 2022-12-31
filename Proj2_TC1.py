from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogTest(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)


    @classmethod
    def test_Orange_setUpClass(self):
        self.driver.maximize_window()

    def test_TC_01_Menu (self):
        driver = webdriver.Chrome()
        wait1 = WebDriverWait(driver,5)

        #open_url
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        #enter_login_credential
        self.driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
        self.driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("admin123")
        self.driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Admin"]').click()

        # checkoptionsdisplayed
        xpath_search = '//input[@ placeholder="Search"]'
        searchbox_find = self.driver.find_element(By.XPATH, '//input[@ placeholder="Search"]')
        print("Textbox display status:", searchbox_find.is_displayed())
        print("Textbox Enable status:", searchbox_find.is_enabled())

        # createlist

        alloptions = []
        allop_upper = []
        get_options = self.driver.find_elements(By.XPATH,'//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"]')
        for i in get_options:
            alloptions.append(i.text)
            print(alloptions)
        for each in alloptions:
            searchbox_find.send_keys(each)
            result_of_search = self.driver.find_element(By.XPATH,'//li[@class="oxd-main-menu-item-wrapper"]//span')
            result_of_search_text = result_of_search.text
            print(f"the string is : {result_of_search.text}")
            assert result_of_search_text.lower() == each.lower()
            self.driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys(Keys.CONTROL + "a")
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys(Keys.BACKSPACE)

        for i in alloptions:
            allop_upper.append(i.upper())
            print(allop_upper)

        for one in allop_upper:
            searchbox_find.send_keys(one)
            result_of_search = self.driver.find_element(By.XPATH, '//li[@class="oxd-main-menu-item-wrapper"]//span')
            result_of_search_text = result_of_search.text
            print(f"the string is : {result_of_search.text}")
            assert result_of_search_text.lower() == one.lower()
            self.driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys(Keys.CONTROL + "a")
            time.sleep(1)
            self.driver.find_element(By.XPATH, '//input[@placeholder="Search"]').send_keys(Keys.BACKSPACE)

    def test_TC_02_drop_down(self):

        # give_login_credentials
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)
        self.driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys("Admin")
        time.sleep(2)
        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//span[text()="Admin"]').click()
        List_1 = []
        List_2 = ['PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory',
                  'Maintenance', 'Buzz']
        sidepanel_options = self.driver.find_elements(By.XPATH, '//a[@class="oxd-main-menu-item" ]//span')
        for i in sidepanel_options:
            List_1.append(i.text)
            print(List_1)
        if List_1 == List_2:
            print("All option in side panel is verified for its presence")
        else:
            print("missed in list")
        # go_to_usermanagement
        self.driver.find_element(By.CSS_SELECTOR,
                            "li[class='oxd-topbar-body-nav-tab --parent --visited'] span[class='oxd-topbar-body-nav-tab-item']").click()
        self.driver.find_element(By.XPATH, '//a[text()="Users"]').click()
        # click_user_role
        self.driver.find_element(By.XPATH, '//label[text()="User Role"]//following::div[4][text()="-- Select --"]').click()
        # select role and Status Enable
        self.driver.find_element(By.XPATH, '//label[text()="User Role"]/following::span[text()="Admin"]').click()
        self.driver.find_element(By.XPATH, '//label[text()="Status"]//following::div[4][text()="-- Select --"]').click()
        self.driver.find_element(By.XPATH, '//label[text()="Status"]/following::span[text()="Enabled"]').click()
        print("Testcase_2:","Role:", "Admin", "Status:", "Enabled")
        # select role and Status Disable
        self.driver.find_element(By.XPATH, '//label[text()="User Role"]//following::div[4][text()="Admin"]').click()
        self.driver.find_element(By.XPATH, '//label[text()="User Role"]/following::span[text()="ESS"]').click()
        self.driver.find_element(By.XPATH, '//label[text()="Status"]//following::div[4][text()="Enabled"]').click()
        self.driver.find_element(By.XPATH, '//label[text()="Status"]/following::span[text()="Disabled"]').click()
        print("Testcase_2:","Role:", "ESS", "Status:", "Disabled ")
    def test_TC_03_PIM_login(self):
        # TEST_CASE_3
        # give_login_credentials
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("Admin")

        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        self.driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
        pim_List_1 = []
        pim_List_2 = ['Admin', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory',
                      'Maintenance', 'Buzz']
        pim_sidepanel_options = self.driver.find_elements(By.XPATH, '//a[@class="oxd-main-menu-item" ]//span')
        for i in pim_sidepanel_options:
            pim_List_1.append(i.text)
            print(pim_List_1)
        if pim_List_1 == pim_List_2:
            print("All option in side panel of pim page is verified for its presence")
        else:
            print("missed in list")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        # Name_detail
        self.driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Jay")

        middle = "//input[@placeholder='Middle Name']"
        self.driver.find_element(By.XPATH, middle).send_keys("Ram")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Sri")
        time.sleep(3)
        EMP_ID = self.driver.find_element(By.XPATH, '//label[text()="Employee Id"]//following::input[1]')
        EMP_ID.send_keys(Keys.CONTROL + 'a')
        EMP_ID.send_keys(Keys.BACKSPACE)
        EMP_ID.send_keys("47573")
        self.driver.find_element(By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//label[text()="Username"]//following::div[1]/input').send_keys("use001")
        self.driver.find_element(By.XPATH, '//label[text()="Password"]//following::div[1]/input').send_keys("Welcome@2023")
        self.driver.find_element(By.XPATH, '//label[text()="Confirm Password"]//following::div[1]/input').send_keys("Welcome@2023")
        self.driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Employee List']").click()
        self.driver.find_element(By.XPATH, '//label[text()="Employee Name"]//following::input[1]').send_keys("Jay Ram Sri")
        verify = self.driver.find_element(By.XPATH, '//div[text()="Jay Ram"]').text
        if verify == "Jay Ram":
            print("Testcase_3:","Employee name appears in employee list")
    def test_TC_04_PIM_options_validate(self):
        # give_login_credentials
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("Admin")
        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        self.driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
        #search already created name in employee lits
        self.driver.find_element(By.XPATH,'//label[text()="Employee Name"]//following::input[1]').send_keys("Jay Ram Sri")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//div[text()="47573"]//following::i[@class="oxd-icon bi-pencil-fill"]').click()
        #validate pim options present on pim page
        detail_list = self.driver.find_elements(By.XPATH, '//img[@class="employee-image"]//following::div/a')
        Pimlist = []
        Pimlist_2 = ['Personal Details', 'Contact Details', 'Emergency Contacts', 'Dependents', 'Immigration', 'Job',
                     'Salary', 'Tax Exemptions', 'Report-to', 'Qualifications', 'Memberships']

        for i in detail_list:
            Pimlist.append(i.text)
            print(Pimlist)
        if Pimlist_2 == Pimlist:
            print("Testcase_4:","All tabs in PIM page is verified for its presence")
    def test_TC_05_PIM_personaldetails(self):

        # give_login_credentials
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("Admin")
        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        self.driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
        # search already created name in employee lits
        self.driver.find_element(By.XPATH, '//label[text()="Employee Name"]//following::input[1]').send_keys("Jay Ram Sri")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//div[text()="47573"]//following::i[@class="oxd-icon bi-pencil-fill"]').click()
        Ot_Id = self.driver.find_element(By.XPATH, '//label[text()="Other Id"]/following::div[1]/input').send_keys("002")
        time.sleep(3)
        driversliscenceno = self.driver.find_element(By.XPATH,'//label[text()="Other Id"]/following::input[2]').send_keys("LN1")
        time.sleep(3)
        driver_liscence_date = self.driver.find_element(By.XPATH,'//label[text()="License Expiry Date"]/following::div[1]//input').send_keys("2024-06-08")
        time.sleep(5)
        SSNnumber = self.driver.find_element(By.XPATH, '//label[text()="SSN Number"]/following::div[1]/input').send_keys("20")
        time.sleep(5)
        sinnumber = self.driver.find_element(By.XPATH, '//label[text()="SIN Number"]/following::div[1]/input').send_keys("2002")
        time.sleep(3)
        nationality = self.driver.find_element(By.XPATH,'//label[text()="Nationality"]/following::div[1]//div[text()="-- Select --"]').click()
        time.sleep(3)
        selectcounty = self.driver.find_element(By.XPATH,'//span[text()="Angolan"]').click()
        time.sleep(3)
        marital_status = self.driver.find_element(By.XPATH,'//label[text()="Marital Status"]/following::div[text()="-- Select --"][1]').click()
        time.sleep(5)
        click_single = self.driver.find_element(By.XPATH,'//span[text()="Single"]').click()
        time.sleep(5)
        DOB = self.driver.find_element(By.XPATH,'//label[text()="Date of Birth"]/following::div[3]/input[@placeholder="yyyy-mm-dd"]').send_keys("1990-09-19")
        time.sleep(5)
        selectgender = self.driver.find_element(By.XPATH, '//input[@value="1"]/following::span[1]').click()
        time.sleep(5)
        military = self.driver.find_element(By.XPATH,'//label[text()="Military Service"]/following::div[1]//input').send_keys("yes")
        time.sleep(5)
        Smoker = self.driver.find_element(By.XPATH, '//input[@value="1"]/following::span[3]').click()
        time.sleep(5)
        save_2 = self.driver.find_element(By.XPATH,'//div/p[text()=" * Required"]/following::button[@type="submit"][1]').click()
        time.sleep(5)
        blood = self.driver.find_element(By.XPATH, '//label[text()="Blood Type"]/following::div[4]').click()
        time.sleep(5)
        select_blood = self.driver.find_element(By.XPATH, '//span[text()="O+"]').click()
        time.sleep(5)
        save_3 = self.driver.find_element(By.XPATH,'//div/p[text()=" * Required"]/following::button[@type="submit"][2]').click()
        time.sleep(5)
        pop_msg = self.driver.find_element(By.ID, "oxd-toaster_1").text
        print(pop_msg)
        time.sleep(5)
        print("Testcase5:", "Personal details added sucessfully")


    def test_TC_06_PIM_contactdetails(self):
        # give_login_credentials
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("Admin")
        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        self.driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
        # search already created name in employee lits
        self.driver.find_element(By.XPATH, '//label[text()="Employee Name"]//following::input[1]').send_keys("Jay Ram Sri")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//div[text()="47573"]//following::i[@class="oxd-icon bi-pencil-fill"]').click()
        self.driver.find_element(By.XPATH, '//a[text()="Contact Details"]').click()
        self.driver.find_element(By.XPATH, '//label[text()="Street 1"]//following::div[1]/input').send_keys("Nehruji")
        self.driver.find_element(By.XPATH, '//label[text()="Street 2"]//following::div[1]/input').send_keys("lal")
        self.driver.find_element(By.XPATH, '//label[text()="City"]//following::div[1]/input').send_keys("cbe")
        self.driver.find_element(By.XPATH, '//label[text()="State/Province"]//following::div[1]/input').send_keys("TN")
        self.driver.find_element(By.XPATH, '//label[text()="Zip/Postal Code"]//following::div[1]/input').send_keys(
            "602 000")
        self.driver.find_element(By.XPATH, '//label[text()="Country"]/following::div[text()="-- Select --"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Albania"]').click()
        self.driver.find_element(By.XPATH, '//label[text()="Home"]//following::div[1]/input').send_keys("0422-25673")
        self.driver.find_element(By.XPATH, '//label[text()="Mobile"]//following::div[1]/input').send_keys("9093756462")
        self.driver.find_element(By.XPATH, '//label[text()="Work"]//following::div[1]/input').send_keys("9898942786")
        self.driver.find_element(By.XPATH, '//label[text()="Work Email"]//following::div[1]/input').send_keys(
            "workmail@gmail.com")
        self.driver.find_element(By.XPATH, '//label[text()="Other Email"]//following::div[1]/input').send_keys(
            "othermail@gmail.com")
        self.driver.find_element(By.XPATH, '//div/p[text()=" * Required"]/following::button[@type="submit"]').click()
        print("Testcase6:","contact Details are added sucessfully")

    def test_TC_07_PIM_Emergencycontactdetails(self):
        # give_login_credentials
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("Admin")

        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//span[text()="PIM"]').click()
        # search already created name in employee lits
        self.driver.find_element(By.XPATH, '//label[text()="Employee Name"]//following::input[1]').send_keys("Jay Ram Sri")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//div[text()="47573"]//following::i[@class="oxd-icon bi-pencil-fill"]').click()
        self.driver.find_element(By.XPATH, "//a[normalize-space()='Emergency Contacts']").click()
        self.driver.find_element(By.XPATH, '//h6[text()="Assigned Emergency Contacts"]//following::button[1]').click()
        self.driver.find_element(By.XPATH, '//label[text()="Name"]//following::div[1]/input').send_keys("NameG")
        self.driver.find_element(By.XPATH, '//label[text()="Relationship"]//following::div[1]/input').send_keys("Bro")
        self.driver.find_element(By.XPATH, '//label[text()="Home Telephone"]//following::div[1]/input').send_keys("9065432812")
        self.driver.find_element(By.XPATH, '//label[text()="Mobile"]//following::div[1]/input').send_keys("9065378798")
        self.driver.find_element(By.XPATH, '//label[text()="Work Telephone"]//following::div[1]/input').send_keys("6542768768")
        self.driver.find_element(By.XPATH, '//p[text()=" * Required"]//following::button[2]').click()
        time.sleep(3)
        record = self.driver.find_element(By.XPATH,'//h6[text()="Assigned Emergency Contacts"]//following::div[text()="NameG"]')
        emergency_name = record.text
        if emergency_name == "NameG":
         print("Testcase7:","Updated contact appears under Assigned Emergency Contacts")


    def test_TC_08_PIM_Dependancydetails(self):
        # give_login_credentials
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("Admin")
        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        self.driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
        # search already created name in employee lits
        self.driver.find_element(By.XPATH, '//label[text()="Employee Name"]//following::input[1]').send_keys( "Jay Ram Sri")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//div[text()="47573"]//following::i[@class="oxd-icon bi-pencil-fill"]').click()
        self.driver.find_element(By.XPATH, '//a[text()="Dependents"]').click()
        self.driver.find_element(By.XPATH, '//h6[text()="Assigned Dependents"]//following::button[1]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//label[text()="Name"]//following::div[1]/input').send_keys("NONAME")
        self.driver.find_element(By.XPATH, '//label[text()="Relationship"]//following::div[4]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Child"]').click()
        self.driver.find_element(By.XPATH, '//input[@placeholder="yyyy-mm-dd"]').send_keys("2022-09-09")
        self.driver.find_element(By.XPATH, '//p[text()=" * Required"]//following::button[2]').click()
        time.sleep(3)
        dependent_name = self.driver.find_element(By.XPATH,'//h6[text()="Assigned Dependents"]//following::div[text()="NONAME"]').text

        if dependent_name == "NONAME":
            print("Testcase8:","Updated contact appears under Assigned Dependents")

    def test_TC_09_PIM_Jobdetails(self):
        # give_login_credentials
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("Admin")
        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        self.driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
        # search already created name in employee lits
        self.driver.find_element(By.XPATH, '//label[text()="Employee Name"]//following::input[1]').send_keys("Jay Ram Sri")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//div[text()="47573"]//following::i[@class="oxd-icon bi-pencil-fill"]').click()
        #edit job details
        self.driver.find_element(By.XPATH,'//a[text()="Job"]').click()
        self.driver.find_element(By.XPATH,'//label[text()="Joined Date"]//following::div[3]/input').send_keys("2016-09-15")
        self.driver.find_element(By.XPATH,'//label[text()="Job Title"]//following::div[text()="-- Select --"][1]').click()
        self.driver.find_element(By.XPATH,'//span[text()="Chief Executive Officer"]').click()
        self.driver.find_element(By.XPATH,'//label[text()="Job Category"]//following::div[text()="-- Select --"][1]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Laborers and Helpers"]').click()
        self.driver.find_element(By.XPATH,'//label[text()="Sub Unit"]//following::div[text()="-- Select --"][1]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Engineering"]').click()
        self.driver.find_element(By.XPATH,'//label[text()="Location"]//following::div[text()="-- Select --"][1]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Canadian Regional HQ"]').click()
        self.driver.find_element(By.XPATH,'//label[text()="Employment Status"]//following::div[text()="-- Select --"][1]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Freelance"]').click()
        self.driver.find_element(By.XPATH,'//p[text()="Include Employment Contract Details"]//following::span[1]').click()
        self.driver.find_element(By.XPATH,'//p[text()="Include Employment Contract Details"]//following::div[9]/input').send_keys("2000-10-10")
        self.driver.find_element(By.XPATH,'//label[text()="Contract End Date"]//following::div[3]/input').send_keys("2002-05-04")
        self.driver.find_element(By.XPATH,'//input[@type="file"]').send_keys("C:/Users/WIN 10/Pictures/Saved Pictures")
        self.driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        print("Testcase9:", "Job details are present in job details page")

    def test_TC_10_terminateemploye(self):
        # give_login_credentials
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("Admin")
        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        self.driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
        # search already created name in employee lits
        self.driver.find_element(By.XPATH, '//label[text()="Employee Name"]//following::input[1]').send_keys("Jay Ram Sri")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//div[text()="47573"]//following::i[@class="oxd-icon bi-pencil-fill"]').click()
        # edit job details
        self.driver.find_element(By.XPATH, '//a[text()="Job"]').click()
        self.driver.find_element(By.XPATH,'//h6[text()="Employee Termination / Activiation"]//following::button[@type="button"][1]').click()
        self.driver.find_element(By.XPATH,'//label[text()="Termination Date"]//following::input[@placeholder="yyyy-mm-dd"]').send_keys("2022-06-16")
        self.driver.find_element(By.XPATH,'//label[text()="Termination Reason"]//following::div[4]').click()
        self.driver.find_element(By.XPATH,'//span[text()="Deceased"]').click()
        self.driver.find_element(By.XPATH,'//textarea[@placeholder="Type here"]').send_keys("due to lay off")
        self.driver.find_element(By.XPATH,'//textarea[@placeholder="Type here"]//following::button[@type="submit"]').click()
        time.sleep(3)
        terminated = self.driver.find_element(By.XPATH,'//p[text()="Terminated on: 2022-06-16"]')
        vl = terminated.text
        if vl == "Terminated on: 2022-06-16":
            print("termination is validated")

    def test_TC_11_Activateemploye(self):
        # give_login_credentials
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("Admin")
        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        self.driver.find_element(By.XPATH, '//span[text()="PIM"]').click()

        # search already created name in employee lits
        self.driver.find_element(By.XPATH, '//label[text()="Employee Name"]//following::input[1]').send_keys("Jay Ram Sri")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//div[text()="47573"]//following::i[@class="oxd-icon bi-pencil-fill"]').click()
        # edit job details
        self.driver.find_element(By.XPATH,'//a[text()="Job"]').click()
        self.driver.find_element(By.XPATH,'//h6[text()="Employee Termination / Activiation"]//following::button[@type="button"][1]').click()
        time.sleep(3)
        confirm_text = self.driver.find_element(By.XPATH,'//h6[text()="Employee Termination / Activiation"]//following::button[@type="button"][1]').text
        if confirm_text == "Terminate Employment":
           print("Activation is done")

    def test_TC_12_salarydetails(self):
        # give_login_credentials
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("Admin")
        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        self.driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
        # search already created name in employee lits
        self.driver.find_element(By.XPATH, '//label[text()="Employee Name"]//following::input[1]').send_keys("Jay Ram Sri")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//div[text()="47573"]//following::i[@class="oxd-icon bi-pencil-fill"]').click()
        # edit job details
        self.driver.find_element(By.XPATH,'//a[text()="Salary"]').click()
        self.driver.find_element(By.XPATH,'//h6[text()="Assigned Salary Components"]//following::button[1]').click()
        self.driver.find_element(By.XPATH,'//label[text()="Salary Component"]//following::div[1]/input').send_keys("308820")
        self.driver.find_element(By.XPATH,'//label[text()="Pay Grade"]//following::div[4]').click()
        self.driver.find_element(By.XPATH,'//span[text()="Grade 1"]').click()
        self.driver.find_element(By.XPATH, '//label[text()="Pay Frequency"]//following::div[4]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Monthly"]').click()
        self.driver.find_element(By.XPATH, '//label[text()="Currency"]//following::div[4]').click()
        self.driver.find_element(By.XPATH, '//span[text()="United States Dollar"]').click()
        self.driver.find_element(By.XPATH, '//label[text()="Amount"]//following::div[1]/input').send_keys("50000")
        self.driver.find_element(By.XPATH,'//label[text()="Comments"]//following::textarea').send_keys("Salary account")
        self.driver.find_element(By.XPATH,'//p[text()="Include Direct Deposit Details"]//following::span[1]').click()
        self.driver.find_element(By.XPATH,'//label[text()="Account Number"]//following::div[1]/input').send_keys("308757357897")
        self.driver.find_element(By.XPATH,'//label[text()="Account Type"]//following::div[4]').click()
        self.driver.find_element(By.XPATH,'//span[text()="Savings"]')
        self.driver.find_element(By.XPATH,'//label[text()="Routing Number"]//following::div[1]/input').send_keys("6895")
        self.driver.find_element(By.XPATH,'//label[text()="Routing Number"]//following::input[2]').send_keys("308820")
        self.driver.find_element(By.XPATH,'//p[text()=" * Required"]//following::button[2]').click()
        time.sleep(3)
        record = self.driver.find_element(By.XPATH,'//span[text()="(1) Record Found"]')
        comapre = record.text
        if comapre == "(1) Record Found":
            print("Salary details added sucessfully")

    def test_TC_13_Taxexpemption(self):
        # give_login_credentials
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH, '//input[@placeholder="Username"]').send_keys("Admin")
        xpath_password = "//input[@placeholder='Password']"
        self.driver.find_element(By.XPATH, xpath_password).send_keys("admin123")
        xpath_submit_button = "//button[@type='submit']"
        self.driver.find_element(By.XPATH, xpath_submit_button).click()
        self.driver.find_element(By.XPATH, '//span[text()="PIM"]').click()
        # search already created name in employee lits
        self.driver.find_element(By.XPATH, '//label[text()="Employee Name"]//following::input[1]').send_keys("Jay Ram Sri")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//div[text()="47573"]//following::i[@class="oxd-icon bi-pencil-fill"]').click()
        time.sleep(3)
        # edit job details
        self.driver.find_element(By.XPATH,'//label[text()="Status"]//following::div[18][text()="-- Select --"]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Single"]').click()

        self.driver.find_element(By.XPATH,'//h6[text()="State Income Tax"]//following::div[9][text()="-- Select --"]').click()
        self.driver.find_element(By.XPATH,'//span[text()="Alabama"]').click()
        self.driver.find_element(By.XPATH,'//h6[text()="State Income Tax"]//following::div[17]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Single"]').click()
        self.driver.find_element(By.XPATH,'//label[text()="Exemptions"]//following::input[2]').send_keys("11")
        self.driver.find_element(By.XPATH,'//h6[text()="State Income Tax"]//following::div[29]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Alabama"]').click()
        self.driver.find_element(By.XPATH,'//label[text()="Work State"]//following::div[4]').click()
        self.driver.find_element(By.XPATH, '//span[text()="Alabama"]').click()
        self.driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        self.driver.find_element(By.XPATH, '//a[text()="Tax Exemptions"]').click()
        self.driver.find_element(By.XPATH, '//h6[text()="Attachments"]//following::button').click()
        self.driver.find_element(By.XPATH, '//input[@type="file"]').send_keys("C:/Users/WIN 10/Pictures/Saved Pictures")




































    @classmethod
    def test_tearDownClass(self):
       self.driver.close()
       self.driver.quit()
       print("test sucessfuly completed")

if __name__ == '__main__':
    unittest.main()




        # List_1 = []
        # List_2 = ['PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard', 'Directory',
        #           'Maintenance', 'Buzz']
        # sidepanel_options = self.driver.find_elements(By.XPATH, '//a[@class="oxd-main-menu-item" ]//span')
        # for i in sidepanel_options:
        #     List_1.append(i.text)
        #     print(List_1)
        # if List_1 == List_2:
        #     print("All option in side panel is verified for its presence")
        # else:
        #     print("missed in list")
        # # go_to_usermanagement
        # self.driver.find_element(By.CSS_SELECTOR,
        #                     "li[class='oxd-topbar-body-nav-tab --parent --visited'] span[class='oxd-topbar-body-nav-tab-item']").click()
        # self.driver.find_element(By.XPATH, '//a[text()="Users"]').click()
        # # click_user_role
        # self.driver.find_element(By.XPATH, '//label[text()="User Role"]//following::div[4][text()="-- Select --"]').click()
        # # select role and Status Enable
        # self.driver.find_element(By.XPATH, '//label[text()="User Role"]/following::span[text()="Admin"]').click()
        # self.driver.find_element(By.XPATH, '//label[text()="Status"]//following::div[4][text()="-- Select --"]').click()
        # self.driver.find_element(By.XPATH, '//label[text()="Status"]/following::span[text()="Enabled"]').click()
        # print("Role:", "Admin", "Status:", "Enabled")
        # # select role and Status Disable
        # self.driver.find_element(By.XPATH, '//label[text()="User Role"]//following::div[4][text()="Admin"]').click()
        # self.driver.find_element(By.XPATH, '//label[text()="User Role"]/following::span[text()="ESS"]').click()
        # self.driver.find_element(By.XPATH, '//label[text()="Status"]//following::div[4][text()="Enabled"]').click()
        # self.driver.find_element(By.XPATH, '//label[text()="Status"]/following::span[text()="Disabled"]').click()
        # print("Role:", "ESS", "Status:", "Disabled ")













  







