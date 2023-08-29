from enum import Enum


class KindOfSidingEnum(Enum):
    VINYL = {
        'value_name': 'Replace existing siding',
        'locator': '//div[text()="Vinyl"]'
    }
    FIBER_CEMENT = {
        'value_name': 'Siding for new addition',
        'locator': '//div[text()="Fiber cement"]'
    }
    WOOD = {
        'value_name': 'Repair section(s) of siding',
        'locator': '//div[text()="Wood"]'
    }
    OTHER = {
        'value_name': 'Siding for new home',
        'locator': '//div[text()="Other"]'
    }
    NOT_SURE = {
        'value_name': 'Not Sure',
        'locator': '//div[text()="Not sure"]'
    }

    def __init__(self, vals):
        self.value_name= vals['value_name']
        self.locator = vals['locator']

    @property
    def get_value_name(self):
        return self.value_name

    @property
    def get_locator(self):
        return self.locator
