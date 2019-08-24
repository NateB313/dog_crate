class Device:
    def __init__(self, name):
        self.name = name
        self.power = False

    def set_power(self, power):
        if power:
            if self.power == True:
                print("The {} is already turned on...".format(self.name))
            else:
                print("Turning the {} on...".format(self.name))
                self.power = True
        else:
            if self.power == False:
                print("The {} is already turned off...".format(self.name))
            else:
                print("Turning {} off...".format(self.name))
                self.power = False
    
    def get_power(self):
        if self.power:
            return "ON"
        else:
            return "OFF"