import time

import allure

from Data.Pages.Siding.Steps.siding import SidingSteps


class SidingActions:
    steps = SidingSteps()

    def check_step(self, driver, step):
        self.steps.next_button_disabled(driver)
        self.steps.step_button_present(driver, step)
        self.steps.click_step_button(driver, step)
        self.steps.next_step(driver)

    def siding_complete_steps(self, driver, project, material, square_not_sure, stories, homeowner):
        with allure.step('Check elements on the siding page'):
            self.steps.zip_code_input_present(driver)
            self.steps.get_estimate_button_present(driver)
            with allure.step('Enter zipcode(09090 by default) and check validate icon'):
                self.steps.right_icon_is_not_visible(driver)
                self.steps.click_zip_code_input(driver)
                self.steps.enter_zip_code(driver)
                self.steps.right_icon_is_visible(driver)
            with allure.step('Click "Get estimate" button'):
                self.steps.click_get_estimate_button(driver)
                self.steps.steps_form_present(driver)
        with allure.step('Check type of project elements'):
            self.steps.type_of_project_title_present(driver)
            self.steps.type_of_project_elements_present(driver)
            self.check_step(driver, project)
        with allure.step('Check kind of siding elements'):
            self.steps.kind_of_siding_title_present(driver)
            self.steps.kind_of_siding_elements_present(driver)
            self.check_step(driver, material)
        with allure.step('Check square elements'):
            self.steps.square_title_present(driver)
            self.steps.square_input_present(driver)
            self.steps.square_not_sure_checkbox_present(driver)
            self.steps.next_button_disabled(driver)
            with allure.step('Enter square(123 by default)'):
                self.steps.click_square_input(driver)
                self.steps.enter_square(driver)
            if square_not_sure:
                with allure.step('Click "Not sure" checkbox'):
                    self.steps.click_square_not_sure_checkbox(driver)
            self.steps.next_step(driver)
        with allure.step('Check stories elements'):
            self.steps.story_title_present(driver)
            self.steps.story_elements_present(driver)
            self.check_step(driver, stories)
        with allure.step('Check homeowner elements'):
            self.steps.homeowner_title_present(driver)
            self.steps.homeowner_yes_button_present(driver)
            self.steps.homeowner_no_button_present(driver)
            self.steps.click_homeowner_yes_button(driver) if homeowner else self.steps.click_homeowner_no_button(driver)
            self.steps.next_step(driver)
        with allure.step('Check contact elements'):
            self.steps.contact_title_present(driver)
            self.steps.contact_full_name_input_present(driver)
            self.steps.contact_email_input_present(driver)
            self.steps.next_button_present(driver)
            with allure.step('Enter full name (Test User by default)'):
                self.steps.enter_contact_full_name(driver)
            with allure.step(f'Enter email {self.steps.random_email}'):
                self.steps.enter_contact_email(driver)
            self.steps.next_step(driver)
        with allure.step('Check phone number elements'):
            self.steps.phone_title_present(driver)
            self.steps.phone_input_present(driver)
            self.steps.phone_submit_my_request_button_present(driver)
            with allure.step(f'Enter phone number {self.steps.random_phone_with_code}'):
                self.steps.enter_phone_number(driver)
            self.steps.click_phone_submit_my_request_button(driver)
        if self.steps.is_confirm_phone_step(driver):
            with allure.step('Check confirm phone number elements'):
                self.steps.confirm_phone_title_present(driver)
                self.steps.confirm_phone_edit_number_button_present(driver)
                self.steps.confirm_phone_number_is_correct_button_present(driver)
                self.steps.phone_input_present(driver)
                self.steps.get_phone_number_and_check_it(driver)
                self.steps.click_confirm_phone_number_is_correct_button(driver)
        with allure.step('Check "Thank you" page elements'):
            self.steps.thank_title_present(driver)