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
        self.error_dialog = QMessageBox()
        self.error_dialog.setWindowTitle("Hey User")
        self.AliceCV.mousePressEvent = self.alice_selected
        self.DeveloperCV.mousePressEvent = self.developer_selected
        self.ModernCV.mousePressEvent = self.modern_selected
        self.info_w = None

    def alice_selected(self, event):
        if not find_executable("pdflatex"):
            self.error_dialog.setText("Make Sure LATEX is installed")
            self.error_dialog.show()
            return
        elif self.info_w and self.info_w.isVisible():
            return
        _dict["Template"] = "AliceCV"
        self.info_w = InfoWindow()
        self.info_w.show()
        self.close()

    def developer_selected(self, event):
        if not find_executable("pdflatex"):
            self.error_dialog.setText("Make Sure LATEX is installed")
            self.error_dialog.show()
            return
        elif self.info_w and self.info_w.isVisible():
            return
        _dict["Template"] = "DeveloperCV"
        self.info_w = InfoWindow()
        self.info_w.show()
        self.close()

    def modern_selected(self, event):
        if not find_executable("pdflatex"):
            self.error_dialog.setText("Make Sure LATEX is installed")
            self.error_dialog.show()
            return
        elif self.info_w and self.info_w.isVisible():
            return
        _dict["Template"] = "ModernCV"
        self.info_w = InfoWindow()
        self.info_w.show()
        self.close()


# Run app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = MainGui()
    w.show()
    sys.exit(app.exec_())
