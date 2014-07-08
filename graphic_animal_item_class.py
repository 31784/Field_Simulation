from graphic_field_item_class import *

class AnimalGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    """this class provides a pixmap items with a preset image for the animal"""

    #constructor
    def __init__(self, graphics_list):
        super().__init__(graphics_list)

        self.animal = None

    def update_status(self):
        if self.animal._status == "Baby":
            self.setPixmap(Qpixmap(self.available_graphics[0]).scaledToWidth(25,1))
        elif self.animal_status == "Poor":
            self.setPixmap(Qpixmap(self.available_graphics[1]).scaledToWidth(25,1))
        elif self.animal_status == "Fine":
            self.setPixmap(Qpixmap(self.available_graphics[2]).scaledToWidth(25,1))
        elif self.animal_status == "Prime":
            self.setPixmap(Qpixmap(self.available_graphics[3]).scaledToWidth(25,1))

