from PyQt5.QtWidgets import *

import perimeter
from MainWindow import *
import Square
import Rectangle
import Circle
import Triangle
import Shapes_Selector
import area


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        """
        This is the init function.
        It imports the ui classes from all the other programs
        It also converts them into their individual QtWidget
        """
        self.setupUi(self)

        self.Area_button.clicked.connect(self.area)
        self.Perimeter_button.clicked.connect(self.perimeter)

        self.window = QtWidgets.QMainWindow()
        self.ui_selector = Shapes_Selector.Ui_Shapes_Selecter()

        self.window_2 = QtWidgets.QMainWindow()
        self.ui_circle = Circle.Ui_MainWindow()

        self.window_3 = QtWidgets.QMainWindow()
        self.ui_triangle = Triangle.Ui_MainWindow()

        self.window_4 = QtWidgets.QMainWindow()
        self.ui_square = Square.Ui_MainWindow()

        self.window_5 = QtWidgets.QMainWindow()
        self.ui_rectangle = Rectangle.Ui_MainWindow()

    def area(self):
        """
        This function opens the shapes menu with the area choices
        :return: It will open the selected shape menu.
        """
        self.ui_selector.setupUi(self.window)
        self.window.show()
        self.ui_selector.Circle_Button.clicked.connect(self.area_Circle)
        self.ui_selector.Square_Button.clicked.connect(self.area_Square)
        self.ui_selector.Triangle_Button.clicked.connect(self.area_Triangle)
        self.ui_selector.Rectangle_Button.clicked.connect(self.area_Rectangle)

    def area_Circle(self):
        """
        This function opens the widget of the circle and connects to area.
        """
        self.ui_circle.setupUi(self.window_2)
        self.window_2.show()
        self.ui_circle.Circle_Submit.clicked.connect(self.Circle_math)

    def Circle_math(self):
        """
        This function uses the area program to find the circles area and round to 2 decimals.
        :return: Circles area if successful. Otherwise, it displays invalid character error.
        """
        radius = self.ui_circle.Circle_Radius.text()
        try:
            if int(radius) <= 0:
                self.ui_circle.Circle_Label.setText('Invalid character')
            else:
                area_ = area.circle(int(radius))
                self.ui_circle.Circle_Label.setText(f'Area = {area_:.2f}')
        except ValueError:
            self.ui_circle.Circle_Label.setText('Invalid character')

    def area_Triangle(self):
        """
        This function opens the widget of the Triangle and connects to area.
        It hides two of the sides of the triangle and only leaves the base and height visible.
        """
        self.ui_triangle.setupUi(self.window_3)
        self.ui_triangle.Triangle_Side_1.hide()
        self.ui_triangle.Triangle_Side_2.hide()
        self.window_3.show()
        self.ui_triangle.Triangle_Submit.clicked.connect(self.Triangle_math)

    def Triangle_math(self):
        """
        This function uses the area program to find the triangles area and round to 2 decimals.
        :return: Triangle area if successful. Otherwise, it displays invalid character error.
        """

        base = self.ui_triangle.Triangle_Base.text()
        height = self.ui_triangle.Triangle_Height.text()
        try:
            if int(base) <= 0 or int(height) <= 0:
                self.ui_triangle.Triangle_Label.setText('Invalid Character(s)')
            else:
                area_ = area.triangle(int(base), int(height))
                self.ui_triangle.Triangle_Label.setText(f'Area = {area_:.2f}')
        except ValueError:
            self.ui_triangle.Triangle_Label.setText('Invalid Character(s)')

    def area_Square(self):
        """
        This function opens the widget of the square and connects to area.
        """
        self.ui_square.setupUi(self.window_4)
        self.window_4.show()
        self.ui_square.Square_Submit.clicked.connect(self.Square_math)

    def Square_math(self):
        """
        This function uses the area program to find the squares area and round to 2 decimals.
        :return: Square area if successful. Otherwise, it displays invalid character error.
        """
        side = self.ui_square.Square_Side.text()
        try:
            if int(side) <= 0:
                self.ui_square.Square_Label.setText('Invalid Character')
            else:
                area_ = area.square(int(side))
                self.ui_square.Square_Label.setText(f'Area = {area_:.2f}')
        except ValueError:
            self.ui_square.Square_Label.setText('Invalid Character')

    def area_Rectangle(self):
        """
        This function opens the widget of the rectangle and connects to area.
        """
        self.ui_rectangle.setupUi(self.window_5)
        self.window_5.show()
        self.ui_rectangle.Rectangle_Submit.clicked.connect(self.Rectangle_math)

    def Rectangle_math(self):
        """
        This function uses the area program to find the rectangles area and round to 2 decimals.
        :return: Rectangle area if successful. Otherwise, it displays invalid character error.
        """
        width = self.ui_rectangle.Rectangle_Width.text()
        height = self.ui_rectangle.Rectangle_Height.text()
        try:
            if int(width) <= 0 or int(height) <= 0:
                self.ui_rectangle.Rectangle_Label.setText('Invalid Character(s)')
            else:
                area_ = area.rectangle(int(width), int(height))
                self.ui_rectangle.Rectangle_Label.setText(f'Area = {area_:.2f}')
        except ValueError:
            self.ui_rectangle.Rectangle_Label.setText('Invalid Character(s)')

    def perimeter(self):
        """
        This function opens the shapes menu with the perimeter choices
        :return: It will open the selected shape menu in perimeter mode.
        """
        self.ui_selector.setupUi(self.window)
        self.window.show()
        self.ui_selector.Circle_Button.clicked.connect(self.perimeter_Circle)
        self.ui_selector.Square_Button.clicked.connect(self.perimeter_Square)
        self.ui_selector.Triangle_Button.clicked.connect(self.perimeter_Triangle)
        self.ui_selector.Rectangle_Button.clicked.connect(self.perimeter_Rectangle)

    def perimeter_Circle(self):
        """
        This function opens the widget of the circle and connects to perimeter.
        """
        self.ui_circle.setupUi(self.window_2)
        self.window_2.show()
        self.ui_circle.Circle_Submit.clicked.connect(self.Circle_math_perimeter)

    def Circle_math_perimeter(self):
        """
        This function uses the perimeter program to find the circles perimeter and round to 2 decimals.
        :return: circle perimeter if successful. Otherwise, it displays invalid character error.
        """
        radius = self.ui_circle.Circle_Radius.text()
        try:
            if int(radius) <= 0:
                self.ui_circle.Circle_Label.setText('Invalid Character')
            else:
                perimeter_ = perimeter.circle(int(radius))
                self.ui_circle.Circle_Label.setText(f'perimeter = {perimeter_:.2f}')
        except ValueError:
            self.ui_circle.Circle_Label.setText('Invalid Character')

    def perimeter_Square(self):
        """
        This function opens the widget of the square and connects to perimeter.
        """
        self.ui_square.setupUi(self.window_4)
        self.window_4.show()
        self.ui_square.Square_Submit.clicked.connect(self.Square_math_perimeter)

    def Square_math_perimeter(self):
        """
        This function uses the perimeter program to find the square perimeter and round to 2 decimals.
        :return: square perimeter if successful. Otherwise, it displays invalid character error.
        """
        side = self.ui_square.Square_Side.text()
        try:
            if int(side) <= 0:
                self.ui_square.Square_Label.setText('Invalid Character')
            else:
                perimeter_ = perimeter.square(int(side))
                self.ui_square.Square_Label.setText(f'perimeter = {perimeter_:.2f}')
        except ValueError:
            self.ui_square.Square_Label.setText('Invalid Character')

    def perimeter_Triangle(self):
        """
        This function opens the widget of the Triangle and connects to perimeter.
        It will hide the height value and leave the three sides visible.
        """
        self.ui_triangle.setupUi(self.window_3)
        self.ui_triangle.Triangle_Height.hide()
        self.ui_triangle.Triangle_Label.setText('Enter Three sides')
        self.window_3.show()
        self.ui_triangle.Triangle_Submit.clicked.connect(self.Triangle_math_perimeter)

    def Triangle_math_perimeter(self):
        """
        This function uses the perimeter program to find the triangles perimeter and round to 2 decimals.
        :return: triangle perimeter if successful. Otherwise, it displays invalid character error.
        """
        side_1 = self.ui_triangle.Triangle_Side_1.text()
        side_2 = self.ui_triangle.Triangle_Side_2.text()
        side_3 = self.ui_triangle.Triangle_Base.text()
        try:
            if int(side_1) <= 0 or int(side_2) <= 0 or int(side_3) <= 0:
                self.ui_triangle.Triangle_Label.setText('Invalid Character(s)')
            else:
                perimeter_ = perimeter.triangle(int(side_1), int(side_2), int(side_3))
                self.ui_triangle.Triangle_Label.setText(f'perimeter = {perimeter_:.2f}')
        except ValueError:
            self.ui_triangle.Triangle_Label.setText('Invalid Character(s)')

    def perimeter_Rectangle(self):
        """
        This function opens the widget of the Rectangle and connects to perimeter.
        """
        self.ui_rectangle.setupUi(self.window_5)
        self.window_5.show()
        self.ui_rectangle.Rectangle_Submit.clicked.connect(self.Rectangle_math_perimeter)

    def Rectangle_math_perimeter(self):
        """
        This function uses the perimeter program to find the rectangles perimeter and round to 2 decimals.
        :return: Rectangle perimeter if successful. Otherwise, it displays invalid character error.
        """
        width = self.ui_rectangle.Rectangle_Width.text()
        height = self.ui_rectangle.Rectangle_Height.text()
        try:
            if int(width) <= 0 or int(height) <= 0:
                self.ui_rectangle.Rectangle_Label.setText('Invalid Character')
            else:
                perimeter_ = perimeter.rectangle(int(width), int(height))
                self.ui_rectangle.Rectangle_Label.setText(f'perimeter = {perimeter_:.2f}')
        except ValueError:
            self.ui_rectangle.Rectangle_Label.setText('Invalid Character')
