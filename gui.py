import sys
import os
from distutils.spawn import find_executable
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from InfoWindow import InfoWindow, _dict


# Loading UI Files
Form = uic.loadUiType(os.path.join(os.getcwd(), "Resources/Mainui.ui"))[0]


# Main window
class MainGui(QMainWindow, Form):
    def __init__(self):
        super(MainGui, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("CV Builder")
        # Error Popup for showing errors
        self.error_dialog = QMessageBox()
        self.error_dialog.setWindowTitle("Hey User")
        # Connecting each Template to it's function
        self.AliceCV.mousePressEvent = self.alice_selected
        self.DeveloperCV.mousePressEvent = self.developer_selected
        self.ModernCV.mousePressEvent = self.modern_selected
        # Object for holding next window(Information window)
        self.info_w = None

    # In case AliceCV is selected
    def alice_selected(self, event):
        # Check if LATEX and PanDoc are installed on PC
        if not find_executable("pdflatex") or not find_executable("pandoc"):
            self.error_dialog.setText("Make Sure LATEX and PanDoc are installed")
            self.error_dialog.show()
            return
        elif self.info_w and self.info_w.isVisible():
            return
        # Setting Template Name to AliceCV
        _dict["Template"] = "AliceCV"
        # Openning new window (Information window)
        self.info_w = InfoWindow()
        self.info_w.show()
        # Closing Current Window
        self.close()

    # In case DeveloperCV is selected
    def developer_selected(self, event):
        # Check if LATEX and PanDoc are installed on PC
        if not find_executable("pdflatex") or not find_executable("pandoc"):
            self.error_dialog.setText("Make Sure LATEX and PanDoc are installed")
            self.error_dialog.show()
            return
        elif self.info_w and self.info_w.isVisible():
            return
        # Setting Template Name to DeveloperCV
        _dict["Template"] = "DeveloperCV"
        # Openning new window (Information window)
        self.info_w = InfoWindow()
        self.info_w.show()
        # Closing Current Window
        self.close()

    # In case ModernCV is selected
    def modern_selected(self, event):
        # Check if LATEX and PanDoc are installed on PC
        if not find_executable("pdflatex") or not find_executable("pandoc"):
            self.error_dialog.setText("Make Sure LATEX and PanDoc are installed")
            self.error_dialog.show()
            return
        elif self.info_w and self.info_w.isVisible():
            return
        # Setting Template Name to ModernCV
        _dict["Template"] = "ModernCV"
        # Openning new window (Information window)
        self.info_w = InfoWindow()
        self.info_w.show()
        # Closing Current Window
        self.close()


# Run app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = MainGui()
    w.show()
    sys.exit(app.exec_())
