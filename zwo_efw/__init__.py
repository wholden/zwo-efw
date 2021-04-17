from . import api


class EFW:

    def __init__(self, efwid=0):
        self.efwid = efwid

    def initialize(self):
        # based on suggested call order from SDK
        api.get_number_of_devices()
        api.get_id(self.efwid)
        api.open(self.efwid)
        api.get_property(self.efwid)
    
    def set_position(self, pos):
        api.set_position(self.efwid, pos - 1)

    def get_position(self):
        return api.get_position(self.efwid) + 1

    def calibrate(self):
        api.calibrate(self.efwid)
