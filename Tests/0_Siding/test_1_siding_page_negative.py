import allure
import pytest

from Data.Pages.Siding.Actions.siding import SidingActions
from Data.Pages.Siding.Steps.siding import SidingSteps


class TestSidingPageNegative:
    actions = SidingActions()
    steps = SidingSteps()

    @pytest.fixture(scope="function", autouse=True)
    def go_to_siding_page(self, d):
        self.steps.go_to_siding_page(d)

    @allure.feature('Siding page')
    @allure.story('Siding page negative tests')
    @allure.title('Try to enter invalid or empty zip code')
    @pytest.mark.parametrize('zipcode', ["", "o9o9o", "@9@9@"])
    def test_invalid_zip_code(self, d, zipcode):
        self.actions.check_zip_code_with_invalid_value(d, zipcode)

    @allure.feature('Siding page')
    @allure.story('Siding page negative tests')
    @allure.title('Try to enter invalid square')
    @pytest.mark.parametrize('square, not_sure',
                             [pytest.param("hundred", True),
                              pytest.param("-100", False),
                              pytest.param("1@@", True)])
    def test_invalid_square(self, d, square, not_sure):
        self.actions.check_square_with_invalid_value(d, square, not_sure)

    @allure.feature('Siding page')
    @allure.story('Siding page negative tests')
    @allure.title('Try to enter invalid contact')
    @pytest.mark.parametrize('first, last, is_full',
                             [pytest.param("", "", False),
                              pytest.param("John", "", False),
                              pytest.param("J0hn", "Dou", True),
                              pytest.param("John", "D0u", True)])
    def test_invalid_contact_name(self, d, first, last, is_full):
        self.actions.check_contacts_name_with_invalid_value(d, first, last, is_full)

    @allure.feature('Siding page')
    @allure.story('Siding page negative tests')
    @allure.title('Try to enter invalid contact email')
    @pytest.mark.parametrize('email', ["", "@testemail.com", "testemail@com", "test@ema!l.com"])
    def test_invalid_contact_email(self, d, email):
        self.actions.check_contacts_email_with_invalid_value(d, email)