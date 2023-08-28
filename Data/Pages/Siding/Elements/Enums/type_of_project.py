from enum import Enum


class TypeOfProjectEnum(Enum):
    REPLACE = {
        'name': 'Replace existing siding',
        'locator': '//div[text()="Replace " and text()=" existing siding"]'
    }
    NEW_ADDITION = {
        'name': 'Siding for new addition',
        'locator': '//div[text()="Siding " and text()=" for new addition"]'
    }
    REPAIR = {
        'name': 'Repair section(s) of siding',
        'locator': '//div[text()="Repair " and text()=" section(s) of siding"]'
    }
    NEW_HOME = {
        'name': 'Siding for new home',
        'locator': '//div[text()="Siding " and text()=" for new home"]'
    }
    NOT_SURE = {
        'name': 'Not Sure',
        'locator': '//div[text()="Not Sure"]'
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

    @property
    def get_button(self):
        return self.locator + '//ancestor::div[@class="typeOfProject__item"]'