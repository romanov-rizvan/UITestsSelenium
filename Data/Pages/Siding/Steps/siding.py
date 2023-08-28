from Data.Constants.General.common import BaseTest
from Data.Pages.Siding.Elements.siding import SidingElements


class SidingSteps(BaseTest):
    elements = SidingElements()

    # zip code
    def zip_code_input_present(self, driver):
        element = self.elements.zipCodeInput
        assert self.wait_present(driver.instance, element), "Zip Code input not found"

    def click_zip_code_input(self, driver):
        element = self.elements.zipCodeBox
        self.click_on(driver.instance, element)

    def enter_zip_code(self, driver, code="09090"):
        element = self.elements.zipCodeInput
        driver.instance.find_element("xpath", element).send_keys(code)

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