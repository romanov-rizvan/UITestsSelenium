from enum import Enum


class StoriesEnum(Enum):
    STORY_1 = {
        'value_name': '1 story',
        'locator': '//div[text()="1 story"]'
    }
    STORY_2 = {
        'value_name': '2 stories',
        'locator': '//div[text()="2 stories"]'
    }
    STORY_3 = {
        'value_name': '3 stories',
        'locator': '//div[text()="2 stories"]'
    }
    STORY_3_PLUS = {
        'value_name': '3+ stories',
        'locator': '//div[text()="3+ stories"]'
    }

    def __init__(self, vals):
        self.value_name = vals['value_name']
        self.locator = vals['locator']

    @property
    def get_value_name(self):
        return self.value_name

    @property
    def get_locator(self):
        return self.locator
