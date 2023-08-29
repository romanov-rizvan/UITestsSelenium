from enum import Enum


class TypeOfProjectEnum(Enum):
    REPLACE = {
        'value_name': 'Replace existing siding',
        'locator': '//div[text()="Replace " and text()=" existing siding"]'
    }
    NEW_ADDITION = {
        'value_name': 'Siding for new addition',
        'locator': '//div[text()="Siding " and text()=" for new addition"]'
    }
    REPAIR = {
        'value_name': 'Repair section(s) of siding',
        'locator': '//div[text()="Repair " and text()=" section(s) of siding"]'
    }
    NEW_HOME = {
        'value_name': 'Siding for new home',
        'locator': '//div[text()="Siding " and text()=" for new home"]'
    }
    NOT_SURE = {
        'value_name': 'Not Sure',
        'locator': '//div[text()="Not sure"]'
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
