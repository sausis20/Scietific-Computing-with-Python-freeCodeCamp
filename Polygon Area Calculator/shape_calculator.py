class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + \
        str(self.height) + ")"
        
    def set_width(self, new_width):
        self.width = new_width
        
    def set_height(self, new_height):
        self.height = new_height
        
    def get_area(self):
        area = self.width * self.height
        return area
        
    def get_perimeter(self):
        perimeter = self.width*2 + self.height*2
        return perimeter
        
    def get_diagonal(self):
        diagonal = (self.width**2 + self.height**2)**0.5
        return diagonal
        
    def get_picture(self):
        s = ''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        for y in range(self.height):
            for i in range(self.width):
                s += '*'
            s += '\n'
        return s
    
    def get_amount_inside(self, shape):
        fit_width = self.width // shape.width
        fit_height = self.height // shape.height
        return fit_width * fit_height
        
class Square(Rectangle):
    def __init__(self, lenght):
        super().__init__(lenght, lenght)
    
    def __str__(self):
        return "Square(side=" + str(self.width) + ")"
        
    def set_side(self, new_lenght):
        self.width = new_lenght
        self.height = new_lenght
        
    def set_width(self, new_lenght):
        self.width = new_lenght
        self.height = new_lenght
        
    def set_height(self, new_lenght):
        self.width = new_lenght
        self.height = new_lenght
