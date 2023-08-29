import pytest

from Data.Pages.Siding.Actions.siding import SidingActions
from Data.Pages.Siding.Elements.Enums.kind_of_siding import KindOfSidingEnum as Material
from Data.Pages.Siding.Elements.Enums.stories import StoriesEnum as Story
from Data.Pages.Siding.Elements.Enums.type_of_project import TypeOfProjectEnum as Proj


class TestRun:
    actions = SidingActions()

    @pytest.mark.parametrize('project, material, square, stories, homeowner',
                             [pytest.param(Proj.REPLACE, Material.WOOD, True, Story.STORY_1, False),
                              ])
    def test_complete_steps_positive(self, d, project, material, square, stories, homeowner):
        self.actions.siding_complete_steps(d, project, material, square, stories, homeowner)
