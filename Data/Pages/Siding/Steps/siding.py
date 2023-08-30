import time

from Data.Constants.General.common import BaseTest
from Data.Constants.General.config import Config
from Data.Pages.Siding.Elements.Enums.kind_of_siding import KindOfSidingEnum
from Data.Pages.Siding.Elements.Enums.stories import StoriesEnum
from Data.Pages.Siding.Elements.Enums.type_of_project import TypeOfProjectEnum
from Data.Pages.Siding.Elements.siding import SidingElements


class SidingSteps(BaseTest):
    elements = SidingElements()

    def go_to_siding_page(self, driver):
        if self.current_url(driver) != Config.url_host():
            driver.instance.get(Config.url_host())
        else:
            self.refresh_page(driver)

    # zip code
    def zip_code_input_present(self, driver):
        element = self.elements.zipCodeInput
        assert self.wait_present(driver.instance, element), "Zip Code input not found"

    def click_zip_code_input(self, driver):
        element = self.elements.zipCodeBox
        self.click_on(driver.instance, element)

    def enter_zip_code(self, driver, code="09090"):
        element = self.elements.zipCodeInput
        driver.instance.find_element("xpath", element).clear()
        driver.instance.find_element("xpath", element).send_keys(code)

    def zip_code_error_message_invalid(self, driver):
        element = self.elements.zipCOdeErrorMessageInvalid
        assert self.wait_present(driver.instance, element), "Zip Code invalid error message not found"

    def zip_code_error_message_empty(self, driver):
        element = self.elements.zipCOdeErrorMessageEmpty
        assert self.wait_present(driver.instance, element), "Zip Code empty error message not found"

    def right_icon_is_visible(self, driver):
        element = self.elements.rightIconVisible
        assert self.wait_present(driver.instance, element), '"Right" icon is not visible'

    def right_icon_is_not_visible(self, driver):
        element = self.elements.rightIconVisible
        assert self.wait_not_present(driver.instance, element), '"Right" icon is visible'

    def get_estimate_button_present(self, driver):
        element = self.elements.getEstimateButton
        assert self.wait_present(driver.instance, element), '"Get estimate" button not found'

    def click_get_estimate_button(self, driver):
        element = self.elements.getEstimateButton
        self.click_on(driver.instance, element)

    # steps elements
    def steps_form_present(self, driver):
        element = self.elements.stepsForm
        assert self.wait_present(driver.instance, element), "Steps form not found"

    def next_button_present(self, driver):
        element = self.elements.nextButton
        assert self.wait_present(driver.instance, element), "Next button not found"

    def next_button_disabled(self, driver):
        element = self.elements.nextButtonDisabled
        assert self.wait_present(driver.instance, element), "Next button not in disable state"

    def next_button_enabled(self, driver):
        element = self.elements.nextButtonDisabled
        assert self.wait_not_present(driver.instance, element), "Next button not in enable state"

    def next_step(self, driver):
        if self.wait_present(driver.instance, self.elements.nextButton, 0.5):
            self.next_button_enabled(driver)
            self.click_next_button(driver)
        else:
            self.yes_button_present(driver)
            self.click_yes_button(driver)

    def click_next_button(self, driver):
        element = self.elements.nextButton
        self.click_on(driver.instance, element)

    def sorry_text_present(self, driver):
        element = self.elements.sorryText
        assert self.wait_present(driver.instance, element), '"Sorry text" not found'

    def yes_button_present(self, driver):
        element = self.elements.yesButton
        assert self.wait_present(driver.instance, element), '"Yes" button not found'

    def click_yes_button(self, driver):
        element = self.elements.yesButton
        self.click_on(driver.instance, element)

    def no_button_present(self, driver):
        element = self.elements.noButton
        assert self.wait_present(driver.instance, element), '"No" button not found'

    def click_no_button(self, driver):
        element = self.elements.noButton
        self.click_on(driver.instance, element)

    def go_to_homepage_button_present(self, driver):
        element = self.elements.goToHomepageButton
        assert self.wait_present(driver.instance, element), '"Go to homepage" button not found'

    def click_go_to_homepage_button(self, driver):
        element = self.elements.goToHomepageButton
        self.click_on(driver.instance, element)

    def step_elements_present(self, driver, enum):
        for enum_element in enum:
            element = enum_element.get_locator
            assert self.wait_present(driver.instance, element), '"{}" button not found'.format(enum_element.
                                                                                               get_value_name)

    def step_button_present(self, driver, enum):
        element = enum.get_locator
        assert self.wait_present(driver.instance, element), '"{}" button not found'.format(enum.get_value_name)

    def click_step_button(self, driver, enum):
        element = enum.get_locator
        self.click_on(driver.instance, element)

    # step 1: Type of project
    def type_of_project_title_present(self, driver):
        element = self.elements.typeOfProjectTitle
        assert self.wait_present(driver.instance, element), 'Type of project title not found'

    def type_of_project_elements_present(self, driver):
        self.step_elements_present(driver, TypeOfProjectEnum)

    def type_of_project_repair_warning_message_present(self, driver):
        element = self.elements.typeOfProjectRepairWarningMessage
        assert self.wait_present(driver.instance, element), 'Repair warning message not found'

    # step 2: Kind of siding
    def kind_of_siding_title_present(self, driver):
        element = self.elements.kindOfSidingTitle
        assert self.wait_present(driver.instance, element), 'Kind of siding title not found'

    def kind_of_siding_elements_present(self, driver):
        self.step_elements_present(driver, KindOfSidingEnum)

    # step 3: square
    def square_title_present(self, driver):
        element = self.elements.squareTitle
        assert self.wait_present(driver.instance, element), 'Square title not found'

    def square_input_present(self, driver):
        element = self.elements.squareInput
        assert self.wait_present(driver.instance, element), 'Square input not found'

    def click_square_input(self, driver):
        element = self.elements.squareInput
        self.click_on(driver.instance, element)

    def enter_square(self, driver, square):
        element = self.elements.squareInput
        driver.instance.find_element("xpath", element).clear()
        driver.instance.find_element("xpath", element).send_keys(square)

    def square_not_sure_checkbox_present(self, driver):
        element = self.elements.squareNotSureCheckbox
        assert self.wait_present(driver.instance, element), '"Not sure" checkbox not found'

    def click_square_not_sure_checkbox(self, driver):
        element = self.elements.squareNotSureCheckbox
        self.click_on(driver.instance, element)

    def square_error_message_present(self, driver):
        element = self.elements.squareErrorMessage
        assert self.wait_present(driver.instance, element), 'Square error message not found'

    # step 4: stories
    def story_title_present(self, driver):
        element = self.elements.storyTitle
        assert self.wait_present(driver.instance, element), 'Story title not found'

    def story_elements_present(self, driver):
        self.step_elements_present(driver, StoriesEnum)

    def story_warning_message_present(self, driver):
        element = self.elements.storyWarningMessage
        assert self.wait_present(driver.instance, element), 'Story warning message not found'

    # step 5: homeowner
    def homeowner_title_present(self, driver):
        element = self.elements.homeownerTitle
        assert self.wait_present(driver.instance, element), 'Homeowner title not found'

    def homeowner_warning_message_present(self, driver):
        element = self.elements.homeownerWarningMessage
        assert self.wait_present(driver.instance, element), 'Homeowner warning message not found'

    def homeowner_yes_button_present(self, driver):
        element = self.elements.homeownerYes
        assert self.wait_present(driver.instance, element), 'Homeowner "Yes" button not found'

    def click_homeowner_yes_button(self, driver):
        element = self.elements.homeownerYes
        self.click_on(driver.instance, element)

    def homeowner_no_button_present(self, driver):
        element = self.elements.homeownerNo
        assert self.wait_present(driver.instance, element), 'Homeowner "No" button not found'

    def click_homeowner_no_button(self, driver):
        element = self.elements.homeownerNo
        self.click_on(driver.instance, element)

    # step 6: name and email
    def contact_title_present(self, driver):
        element = self.elements.contactTitle
        assert self.wait_present(driver.instance, element), 'Contact title not found'

    def contact_full_name_input_present(self, driver):
        element = self.elements.contactFullNameInput
        assert self.wait_present(driver.instance, element), 'Full name input not found'

    def click_contact_full_name_box(self, driver):
        element = self.elements.contactFullNameInput
        self.click_on(driver.instance, element)

    def enter_contact_full_name(self, driver, first_name="Test", last_name="User", is_full=True):
        element = self.elements.contactFullNameInput
        name = first_name + " " + last_name if is_full else first_name
        driver.instance.find_element("xpath", element).clear()
        driver.instance.find_element("xpath", element).send_keys(name)

    def contact_full_name_error_message_empty_present(self, driver):
        element = self.elements.contactFullNameErrorMessageEmpty
        assert self.wait_present(driver.instance, element), 'Error message about empty name not found'

    def contact_full_name_error_message_invalid_present(self, driver):
        element = self.elements.contactFullNameErrorMessageInvalid
        assert self.wait_present(driver.instance, element), 'Error message about invalid name not found'

    def contact_full_name_error_message_not_full_present(self, driver):
        element = self.elements.contactFullNameErrorMessageNotFull
        assert self.wait_present(driver.instance, element), 'Error message about not full name not found'

    def contact_email_input_present(self, driver):
        element = self.elements.contactEmailInput
        assert self.wait_present(driver.instance, element), 'Email input not found'

    def click_contact_email_box(self, driver):
        element = self.elements.contactEmailInput
        self.click_on(driver.instance, element)

    def enter_contact_email(self, driver, email="test@email.com"):
        element = self.elements.contactEmailInput
        driver.instance.find_element("xpath", element).clear()
        driver.instance.find_element("xpath", element).send_keys(email)

    def contact_email_error_message_empty_present(self, driver):
        element = self.elements.contactEmailErrorMessageEmpty
        assert self.wait_present(driver.instance, element), 'Error message about empty email not found'

    def contact_email_error_message_invalid_present(self, driver):
        element = self.elements.contactEmailErrorMessageInvalid
        assert self.wait_present(driver.instance, element), 'Error message invalid empty email not found'

    # step 7: phone
    def phone_title_present(self, driver):
        element = self.elements.phoneTitle
        assert self.wait_present(driver.instance, element), 'Phone title not found'

    def phone_input_present(self, driver):
        element = self.elements.phoneInput
        assert self.wait_present(driver.instance, element), 'Phone input not found'

    def click_phone_box(self, driver):
        element = self.elements.phoneInput
        self.click_on(driver.instance, element)

    def enter_phone_number(self, driver, phone):
        element = self.elements.phoneInput
        driver.instance.find_element("xpath", element).send_keys(phone)

    def get_phone_number_and_check_it(self, driver, expected):
        time.sleep(0.5)
        element = self.elements.phoneInput
        actual = self.get_web_element(driver, element).get_attribute("value")
        assert actual == expected, "Actual phone number is not as expected"

    def phone_submit_my_request_button_present(self, driver):
        element = self.elements.phoneSubmitMyRequestButton
        assert self.wait_present(driver.instance, element), '"Submit my request" button not found'

    def click_phone_submit_my_request_button(self, driver):
        element = self.elements.phoneSubmitMyRequestButton
        self.click_on(driver.instance, element)

    # step 8: confirm phone
    def is_confirm_phone_step(self, driver):
        element = self.elements.confirmPhoneTitle
        return self.wait_present(driver.instance, element)

    def confirm_phone_title_present(self, driver):
        element = self.elements.confirmPhoneTitle
        assert self.wait_present(driver.instance, element), 'Phone title not found'

    def confirm_phone_number_is_correct_button_present(self, driver):
        element = self.elements.confirmPhoneNumberIsCorrectButton
        assert self.wait_present(driver.instance, element), '"Phone number is correct" button not found'

    def click_confirm_phone_number_is_correct_button(self, driver):
        element = self.elements.confirmPhoneNumberIsCorrectButton
        self.click_on(driver.instance, element)

    def confirm_phone_edit_number_button_present(self, driver):
        element = self.elements.confirmPhoneEditNumberButton
        assert self.wait_present(driver.instance, element), '"Edit phone number" button not found'

    def click_confirm_phone_edit_number_button(self, driver):
        element = self.elements.confirmPhoneEditNumberButton
        self.click_on(driver.instance, element)

    # step 9: thank you
    def thank_title_present(self, driver, first_name="Test"):
        time.sleep(1.4)
        element = self.elements.thankTitle.format(first_name)
        assert self.wait_present(driver.instance, element, 5), 'Thank you title not found'
