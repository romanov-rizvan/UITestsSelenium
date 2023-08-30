import allure
import pytest

from Data.Pages.Siding.Actions.siding import SidingActions
from Data.Pages.Siding.Elements.Enums.kind_of_siding import KindOfSidingEnum as Material
from Data.Pages.Siding.Elements.Enums.stories import StoriesEnum as Story
from Data.Pages.Siding.Elements.Enums.type_of_project import TypeOfProjectEnum as Proj
from Data.Pages.Siding.Steps.siding import SidingSteps


class TestSidingPagePositive:
    actions = SidingActions()
    steps = SidingSteps()

    @pytest.fixture(scope="function", autouse=True)
    def go_to_siding_page(self, d):
        self.steps.go_to_siding_page(d)

    @allure.feature('Siding page')
    @allure.story('Siding page positive tests')
    @allure.title('Complete full steps scenario')
    @pytest.mark.parametrize('project, material, square, square_not_sure, stories, homeowner',
                             [pytest.param(Proj.REPLACE, Material.WOOD, "123", False, Story.STORY_1, True),
                              pytest.param(Proj.REPAIR, Material.OTHER, "321", True, Story.STORY_3_PLUS, False),
                              pytest.param(Proj.NOT_SURE, Material.NOT_SURE, "", True, Story.STORY_1, True)])
    def test_complete_steps(self, d, project, material, square, square_not_sure,  stories, homeowner):
        self.actions.siding_complete_steps(d, project, material, square, square_not_sure, stories, homeowner)

    @allure.feature('Siding page')
    @allure.story('Siding page positive tests')
    @allure.title('Intercept on type of project step')
    def test_intercept_on_type_of_project(self, d):
        self.actions.siding_intercept_on_type_of_project(d)

    @allure.feature('Siding page')
    @allure.story('Siding page positive tests')
    @allure.title('Intercept on stories step')
    def test_intercept_on_stories(self, d):
        self.actions.siding_intercept_on_stories(d)

    @allure.feature('Siding page')
    @allure.story('Siding page positive tests')
    @allure.title('Intercept on stories step')
    def test_intercept_on_homeowner(self, d):
        self.actions.siding_intercept_on_homeowner(d)
