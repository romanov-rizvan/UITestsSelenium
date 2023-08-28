from enum import Enum


class TypeOfProjectEnum(Enum):
    VINYL = {
        'name': 'Replace existing siding',
        'locator': '//div[text()="Vinyl"]'
    }
    FIBER_CEMENT = {
        'name': 'Siding for new addition',
        'locator': '//div[text()="Fiber cement"]'
    }
    WOOD = {
        'name': 'Repair section(s) of siding',
        'locator': '//div[text()="Wood"]'
    }
    OTHER = {
        'name': 'Siding for new home',
        'locator': '//div[text()="Other"]'
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
        return self.locator + '//ancestor::div[@class="kindOfSiding__item"]'
