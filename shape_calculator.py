class Rectangle:

    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f'{self.__class__.__name__.capitalize()}(width={self.width}, height={self.height})'
    
    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)
    
    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        pic = ''
        for _ in range(0, self.height):
            pic += f'{"*" * self.width}\n'
        return pic
    
    def get_amount_inside(self, shape):
        area = self.get_area()
        shape_area = shape.get_area()
        return int(area/shape_area)


class Square(Rectangle):    
    
    def __init__(self, side) -> None:
        super().__init__(width=side, height=side)
        self.side = side
        
    def __str__(self) -> str:
        self.side = self.height = self.width
        return f'{self.__class__.__name__.capitalize()}(side={self.side})'

    def set_side(self, new_side):
        self.side = self.height = self.width = new_side    
    