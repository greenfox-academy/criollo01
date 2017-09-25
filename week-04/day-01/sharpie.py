''' Create Sharpie class
We should know about each sharpie their color (which should be a string), width (which will be a floating point number), ink_amount (another floating point number)
When creating one, we need to specify the color and the width
Every sharpie is created with a default 100 as ink_amount
We can use() the sharpie objects
which decreases inkAmount '''

class Sharpie(object):
    def __init__(self, color, width, ink_amount):
        self.color = str(color)
        self.width = float(width)
        self.ink_amount = float(100)

    def use(self):
        self.ink_amount -= 9.5
        return self.ink_amount

yellow = Sharpie("yellow", "1.2", "ink_amount")
black = Sharpie("black", "2.3", "ink_amount")
blue = Sharpie("blue", "4", "ink_amount")

yellow.use()
print(yellow.ink_amount)
blue.use()
blue.use()
print(blue.ink_amount)