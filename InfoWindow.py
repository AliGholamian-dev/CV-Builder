import sys
import os
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

Form_InfoWindow = uic.loadUiType(os.path.join(os.getcwd(), "Resources/InfoWindow.ui"))[
    0
]

_dict = {
    "Template": "",
    "nameOfFile": "",
    "Picture": "",
    "Name": "",
    "LastName": "",
    "Title": "",
    "Address": "",
    "Phone": "",
    "Git": "",
    "Linkedin": "",
    "Site": "",
    "Mail": "",
    "Aboutme": "",
    "Skills": [],
    "Basic": [],
    "Intermediate": [],
    "Advanced": [],
    "Interests": "",
    "Gitrepos": [],
    "Education": [],
    "Awards": [],
    "Experience": [],
    "Info": "Nothin yet",
}


class InfoWindow(QMainWindow, Form_InfoWindow):
    def __init__(self):
        super(InfoWindow, self).__init__()
        self.setupUi(self)
