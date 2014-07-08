import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from graphic_field_scene_class import *
from graphic_wheat_item_class import *
from graphic_potato_item_class import *
from graphic_cow_item_class import *
from graphic_sheep_item_class import *

class FieldWindow(QMainWindow):
    """this class creates a main window to observe the growth of a simulated field"""
