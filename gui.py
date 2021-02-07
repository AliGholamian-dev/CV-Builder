import sys
import os
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
        self.AliceCV.mousePressEvent = self.alice_selected
        self.DeveloperCV.mousePressEvent = self.developer_selected
        self.ModernCV.mousePressEvent = self.modern_selected
        self.info_w = None

    def alice_selected(self, event):
        if self.info_w and self.info_w.isVisible():
            return
        _dict["Template"] = "AliceCV"
        self.info_w = InfoWindow()
        self.info_w.show()
        self.close()

    def developer_selected(self, event):
        if self.info_w and self.info_w.isVisible():
            return
        _dict["Template"] = "DeveloperCV"
        self.info_w = InfoWindow()
        self.info_w.show()
        self.close()

    def modern_selected(self, event):
        if self.info_w and self.info_w.isVisible():
            return
        _dict["Template"] = "ModernCV"
        self.info_w = InfoWindow()
        self.info_w.show()
        self.close()


class WorkerThread(QtCore.QThread):
    def __init__(self, window):
        QtCore.QThread.__init__(self, parent=window)

    def run(self):
        pass


# Run app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = MainGui()
    w.show()
    sys.exit(app.exec_())
