class Button:
    def click(self):
        pass

class IOSButton(Button):
    def click(self):
        print("iOS button clicked")

class AndroidButton(Button):
    def click(self):
        print("Android button clicked")

class ButtonFactory:
    @staticmethod
    def create_button(os):
        if os == 'ios':
            return IOSButton()
        elif os == 'android':
            return AndroidButton()
        else:
            raise ValueError("Invalid operating system")

# Usage
os = 'android'
factory = ButtonFactory()
button = factory.create_button(os)
button.click()
