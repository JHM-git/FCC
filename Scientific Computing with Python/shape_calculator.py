

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    asterisk = '*'
    output = ''
    line = self.width * asterisk + '\n'
    count = self.height
    while count > 0:
      output = output + line
      count = count - 1
    return output 

  def get_amount_inside(self, shape):
    x = (self.width - (self.width % shape.width)) / shape.width
    y = (self.height - (self.height % shape.height)) / shape.height
    return int(x * y)

  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
  def __init__(self, length):
    self.width = length
    self.height = length

  def set_side(self, length):
    self.width = length
    self.height = length

  def set_width(self, width):
    super().set_width(width)
    self.height = width

  def set_height(self, height):
    super().set_height(height)
    self.width = height

  def __repr__(self):
    return f"Square(side={self.width})"
  