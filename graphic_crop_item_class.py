from graphic_field_item_class import *

class CropGraphicsPixmapItem(FieldItemGraphicsPixmapItem):
    """this class provides a pixmap items with a preset image for the crop"""

    #constructor
    def __init__(self, graphics_list):
        super().__init__(graphics_list)

        self.crop = None

    def update_status(self):
        if self.crop._status == "Seed":
            self.setPixmap(Qpixmap(self.available_graphics[0]).scaledToWidth(25,1))
        elif self.crop_status == "Seedling":
            self.setPixmap(Qpixmap(self.available_graphics[1]).scaledToWidth(25,1))
        elif self.crop_status == "Young":
            self.setPixmap(Qpixmap(self.available_graphics[2]).scaledToWidth(25,1))
        elif self.crop_status == "Mature":
            self.setPixmap(Qpixmap(self.available_graphics[3]).scaledToWidth(25,1))
        elif self.crop_status == "Old":
            self.setPixmap(Qpixmap(self.available_graphics[4]).scaledToWidth(25,1))
