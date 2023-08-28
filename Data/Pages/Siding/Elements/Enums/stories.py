from enum import Enum


class TypeOfProjectEnum(Enum):
    STORY_1 = {
        'name': '1 story',
        'locator': '//div[text()="1 story"]'
    }
    STORY_2 = {
        'name': '2 stories',
        'locator': '//div[text()="2 stories"]'
    }
    STORY_3 = {
        'name': '3 stories',
        'locator': '//div[text()="2 stories"]'
    }
    STORY_3_PLUS = {
        'name': '3+ stories',
        'locator': '//div[text()="3+ stories"]'
    }

    def __init__(self, vals):
        self.name = vals['name']
        self.locator = vals['locator']

    @property
    def get_name(self):
        return self.name

    @property
    def get_locator(self):
        return self.locator
