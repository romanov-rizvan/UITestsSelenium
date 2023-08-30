import time

import allure

from Data.Constants.General.common import BaseTest
from Data.Pages.Siding.Elements.Enums.kind_of_siding import KindOfSidingEnum
from Data.Pages.Siding.Elements.Enums.stories import StoriesEnum
from Data.Pages.Siding.Elements.Enums.type_of_project import TypeOfProjectEnum
from Data.Pages.Siding.Steps.siding import SidingSteps


class SidingActions:
    steps = SidingSteps()

    def check_step(self, driver, step):
        self.steps.next_button_disabled(driver)
        self.steps.step_button_present(driver, step)
        self.steps.click_step_button(driver, step)

    def check_step_and_go_next(self, driver, step):
        self.check_step(driver, step)
        self.steps.next_step(driver)

    def click_no_and_check_sorry_page(self, driver):
        self.steps.no_button_present(driver)
        self.steps.click_no_button(driver)
        with allure.step('Check "Sorry" page elements'):
            self.steps.sorry_text_present(driver)

    def check_zip_code_elements_and_go_to_next_step(self, driver):
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

    def check_type_of_project_elements_go_to_next_step(self, driver, project=TypeOfProjectEnum.REPAIR):
        with allure.step('Check type of project elements'):
            self.steps.type_of_project_title_present(driver)
            self.steps.type_of_project_elements_present(driver)
            self.check_step_and_go_next(driver, project)

    def check_kind_of_siding_elements_and_go_to_next_step(self, driver, material=KindOfSidingEnum.WOOD):
        with allure.step('Check kind of siding elements'):
            self.steps.kind_of_siding_title_present(driver)
            self.steps.kind_of_siding_elements_present(driver)
            self.check_step_and_go_next(driver, material)

    def check_square_elements_and_go_to_next_step(self, driver, square=123, square_not_sure=False):
        with allure.step('Check square elements'):
            self.steps.square_title_present(driver)
            self.steps.square_input_present(driver)
            self.steps.square_not_sure_checkbox_present(driver)
            self.steps.next_button_disabled(driver)
            with allure.step(f'Enter square {square}'):
                self.steps.click_square_input(driver)
                self.steps.enter_square(driver, square)
            if square_not_sure:
                with allure.step('Click "Not sure" checkbox'):
                    self.steps.click_square_not_sure_checkbox(driver)
            self.steps.next_step(driver)

    def check_stories_elements_and_go_to_next_step(self, driver, stories=StoriesEnum.STORY_3_PLUS):
        with allure.step('Check stories elements'):
            self.steps.story_title_present(driver)
            self.steps.story_elements_present(driver)
            self.check_step_and_go_next(driver, stories)

    def check_homeowner_elements_and_go_to_next_step(self, driver, homeowner=False):
        with allure.step('Check homeowner elements'):
            self.steps.homeowner_title_present(driver)
            self.steps.homeowner_yes_button_present(driver)
            self.steps.homeowner_no_button_present(driver)
            self.steps.click_homeowner_yes_button(driver) if homeowner else self.steps.click_homeowner_no_button(driver)
            self.steps.next_step(driver)

    def check_contact_elements_and_go_to_next_step(self, driver, email):
        with allure.step('Check contact elements'):
            self.steps.contact_title_present(driver)
            self.steps.contact_full_name_input_present(driver)
            self.steps.contact_email_input_present(driver)
            self.steps.next_button_present(driver)
            with allure.step('Enter full name (Test User by default)'):
                self.steps.enter_contact_full_name(driver)
            with allure.step(f'Enter email {email}'):
                self.steps.enter_contact_email(driver, email)
            self.steps.next_step(driver)

    def check_phone_elements_and_go_to_next_step(self, driver, phone, phone_with_code):
        with allure.step('Check phone number elements'):
            self.steps.phone_title_present(driver)
            self.steps.phone_input_present(driver)
            self.steps.phone_submit_my_request_button_present(driver)
            with allure.step(f'Enter phone number {phone_with_code}'):
                self.steps.enter_phone_number(driver, phone)
            self.steps.click_phone_submit_my_request_button(driver)

    def check_confirm_phone_elements_and_go_to_next_step(self, driver, phone_with_code):
        with allure.step('Check confirm phone number elements'):
            self.steps.confirm_phone_title_present(driver)
            self.steps.confirm_phone_edit_number_button_present(driver)
            self.steps.confirm_phone_number_is_correct_button_present(driver)
            self.steps.phone_input_present(driver)
            self.steps.get_phone_number_and_check_it(driver, phone_with_code)
            self.steps.click_confirm_phone_number_is_correct_button(driver)

    # positive checks

    def siding_complete_steps(self, driver, project, material, square, square_not_sure, stories, homeowner):
        random_phone = BaseTest.get_random_phone_number()
        random_phone_with_code = BaseTest.get_phone_number_with_code_format(random_phone)
        random_email = BaseTest.get_random_email(8)
        self.check_zip_code_elements_and_go_to_next_step(driver)
        self.check_type_of_project_elements_go_to_next_step(driver, project)
        self.check_kind_of_siding_elements_and_go_to_next_step(driver, material)
        self.check_square_elements_and_go_to_next_step(driver, square, square_not_sure)
        self.check_stories_elements_and_go_to_next_step(driver, stories)
        self.check_homeowner_elements_and_go_to_next_step(driver, homeowner)
        self.check_contact_elements_and_go_to_next_step(driver, random_email)
        self.check_phone_elements_and_go_to_next_step(driver, random_phone, random_phone_with_code)
        if self.steps.is_confirm_phone_step(driver):
            self.check_confirm_phone_elements_and_go_to_next_step(driver, random_phone_with_code)
        with allure.step('Check "Thank you" page elements'):
            self.steps.thank_title_present(driver)

    def siding_intercept_on_type_of_project(self, driver):
        self.check_zip_code_elements_and_go_to_next_step(driver)
        with allure.step('Select "Repair section(s) of siding" and click "No" button'):
            self.steps.type_of_project_title_present(driver)
            self.steps.type_of_project_elements_present(driver)
            self.check_step(driver, TypeOfProjectEnum.REPAIR)
            self.steps.type_of_project_repair_warning_message_present(driver)
            self.click_no_and_check_sorry_page(driver)

    def siding_intercept_on_stories(self, driver):
        self.check_zip_code_elements_and_go_to_next_step(driver)
        self.check_type_of_project_elements_go_to_next_step(driver)
        self.check_kind_of_siding_elements_and_go_to_next_step(driver)
        self.check_square_elements_and_go_to_next_step(driver)
        with allure.step('Select "3+ stories" and click "No" button'):
            self.steps.story_title_present(driver)
            self.steps.story_elements_present(driver)
            self.check_step(driver, StoriesEnum.STORY_3_PLUS)
            self.steps.story_warning_message_present(driver)
            self.click_no_and_check_sorry_page(driver)

    def siding_intercept_on_homeowner(self, driver):
        self.check_zip_code_elements_and_go_to_next_step(driver)
        self.check_type_of_project_elements_go_to_next_step(driver)
        self.check_kind_of_siding_elements_and_go_to_next_step(driver)
        self.check_square_elements_and_go_to_next_step(driver)
        self.check_stories_elements_and_go_to_next_step(driver)
        with allure.step('Select "No" and click "No" button'):
            self.steps.homeowner_title_present(driver)
            self.steps.homeowner_yes_button_present(driver)
            self.steps.homeowner_no_button_present(driver)
            self.steps.click_homeowner_no_button(driver)
            self.steps.homeowner_warning_message_present(driver)
            self.click_no_and_check_sorry_page(driver)

    # negative checks
    def check_zip_code_with_invalid_value(self, driver, zip_code):
        with allure.step('Check zip code'):
            self.steps.zip_code_input_present(driver)
            self.steps.get_estimate_button_present(driver)
        with allure.step(f'Enter zipcode empty and check validate icon'):
            self.steps.right_icon_is_not_visible(driver)
            self.steps.click_zip_code_input(driver)
            self.steps.enter_zip_code(driver, zip_code)
            self.steps.right_icon_is_not_visible(driver)
            self.steps.click_get_estimate_button(driver)
        if zip_code == "":
            with allure.step('Check zip code empty error is present'):
                self.steps.zip_code_error_message_empty(driver)
        else:
            with allure.step('Check zip code invalid error is present'):
                self.steps.zip_code_error_message_invalid(driver)

    def check_square_with_invalid_value(self, driver, square, square_not_sure):
        self.check_zip_code_elements_and_go_to_next_step(driver)
        self.check_type_of_project_elements_go_to_next_step(driver)
        self.check_kind_of_siding_elements_and_go_to_next_step(driver)
        with allure.step('Check square elements'):
            self.steps.square_title_present(driver)
            self.steps.square_input_present(driver)
            self.steps.square_not_sure_checkbox_present(driver)
            self.steps.next_button_disabled(driver)
        with allure.step(f'Enter square {square}'):
            self.steps.click_square_input(driver)
            self.steps.enter_square(driver, square)
            self.steps.square_error_message_present(driver)
        if square_not_sure:
            with allure.step('Click "Not sure" checkbox'):
                self.steps.click_square_not_sure_checkbox(driver)
        self.steps.next_button_disabled(driver)

    def check_contacts_name_with_invalid_value(self, driver, first_name, last_name, is_full):
        self.check_zip_code_elements_and_go_to_next_step(driver)
        self.check_type_of_project_elements_go_to_next_step(driver)
        self.check_kind_of_siding_elements_and_go_to_next_step(driver)
        self.check_square_elements_and_go_to_next_step(driver)
        self.check_stories_elements_and_go_to_next_step(driver)
        self.check_homeowner_elements_and_go_to_next_step(driver)
        with allure.step('Check contact elements'):
            self.steps.contact_title_present(driver)
            self.steps.contact_full_name_input_present(driver)
            self.steps.contact_email_input_present(driver)
            self.steps.next_button_present(driver)
            self.steps.enter_contact_email(driver)
        with allure.step(f'Enter name {first_name} {last_name}'):
            self.steps.enter_contact_full_name(driver, first_name, last_name, is_full)
            self.steps.click_next_button(driver)
            if first_name == "" and last_name == "":
                self.steps.contact_full_name_error_message_empty_present(driver)
            if first_name != "" and last_name == "":
                self.steps.contact_full_name_error_message_not_full_present(driver)
            if first_name != "" and last_name != "":
                self.steps.contact_full_name_error_message_invalid_present(driver)

    def check_contacts_email_with_invalid_value(self, driver, email):
        self.check_zip_code_elements_and_go_to_next_step(driver)
        self.check_type_of_project_elements_go_to_next_step(driver)
        self.check_kind_of_siding_elements_and_go_to_next_step(driver)
        self.check_square_elements_and_go_to_next_step(driver)
        self.check_stories_elements_and_go_to_next_step(driver)
        self.check_homeowner_elements_and_go_to_next_step(driver)
        with allure.step('Check contact elements'):
            self.steps.contact_title_present(driver)
            self.steps.contact_full_name_input_present(driver)
            self.steps.contact_email_input_present(driver)
            self.steps.next_button_present(driver)
            self.steps.enter_contact_full_name(driver)
        with allure.step(f'Enter name {email}'):
            self.steps.enter_contact_email(driver, email)
            self.steps.click_next_button(driver)
            if email == "":
                self.steps.contact_email_error_message_empty_present(driver)
            else:
                self.steps.contact_email_input_present(driver)
        time.sleep(1)
