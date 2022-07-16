class Cookie():
    def __init__(self, color):
        self.color = color
    def get_color(self):
        return self.color
    def set_color(self, color):
        self.color = color

cookie1 = Cookie('red')
cookie2 = Cookie('green')

print(cookie1.get_color())
cookie1.set_color('black')
print(cookie1.get_color())