import sys
import os
import socket
from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QFileDialog,
    QCheckBox,
    QTableWidgetItem,
)
from PyQt5.QtGui import QPixmap
import aiohttp
import asyncio

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
        self.error_dialog = QMessageBox()
        self.error_dialog.setWindowTitle("Hey User")

        self.Picture.mousePressEvent = self.upload_picture

        self.addInterest.clicked.connect(self.addInterestFucntion)
        self.removeInterest.clicked.connect(self.removeInterestFucntion)

        self.addAward.clicked.connect(self.addAwardFucntion)
        self.removeAward.clicked.connect(self.removeAwardFucntion)

        self.addExp.clicked.connect(self.addExpFucntion)
        self.removeExp.clicked.connect(self.removeExpFucntion)

        self.addSkill.clicked.connect(self.addSkillFucntion)
        self.removeSkill.clicked.connect(self.removeSkillFucntion)

        self.fetchRepo.clicked.connect(self.goGetRepos)

    async def fetchRepository(self):
        try:
            # see if we can resolve the host name -- tells us if there is
            # a DNS listening
            host = socket.gethostbyname("one.one.one.one")
            # connect to the host -- tells us if the host is actually
            # reachable
            s = socket.create_connection((host, 80), 2)
            s.close()
        except:
            self.error_dialog.setText("Check your Internet Connection")
            self.error_dialog.show()
            self.fetchRepo.setEnabled(True)
            return
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://api.github.com/users/{self.GitHub.text()}/repos"
            ) as response:
                repoResponse = await response.json()
                try:
                    temp = repoResponse[0]["name"]
                except:
                    self.error_dialog.setText("Wrong GitHub ID")
                    self.error_dialog.show()
                    self.fetchRepo.setEnabled(True)
                    return
                self.repoWidget.clear()
                row = 0
                for gitrepos_each in repoResponse:
                    self.repoWidget.insertRow(self.repoWidget.rowCount())
                    self.repoWidget.setItem(
                        row, 2, QTableWidgetItem(gitrepos_each["name"]),
                    )
                    chkBoxItem = QTableWidgetItem("Add to CV")
                    chkBoxItem.setFlags(
                        QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled
                    )
                    chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                    self.repoWidget.setItem(
                        row, 0, QTableWidgetItem(chkBoxItem),
                    )
                    chkBoxItem2 = QTableWidgetItem("Add Readme")
                    chkBoxItem2.setFlags(
                        QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled
                    )
                    chkBoxItem2.setCheckState(QtCore.Qt.Unchecked)
                    self.repoWidget.setItem(
                        row, 1, QTableWidgetItem(chkBoxItem2),
                    )
                    row += 1
        self.fetchRepo.setEnabled(True)

    def dataFetched(self):
        self.fetchRepo.setEnabled(True)

    def goGetRepos(self):
        if self.GitHub.text() == "":
            self.error_dialog.setText("Fill All Fields Please !!!!")
            self.error_dialog.show()
            return
        self.fetchRepo.setEnabled(False)
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.fetchRepository())

    def upload_picture(self, event):
        fileDialog = QFileDialog(parent=self)
        _dict["Picture"] = fileDialog.getOpenFileUrl(
            parent=self, caption="Choose Your Profile Pictue"
        )[0].url()[8:]
        self.Picture.setPixmap(QPixmap(_dict["Picture"]))

    def addInterestFucntion(self):
        if self.InterstInput.text() == "":
            self.error_dialog.setText("Fill All Fields Please !!!!")
            self.error_dialog.show()
            return
        self.Interests.addItem(self.InterstInput.text())
        self.InterstInput.clear()

    def removeInterestFucntion(self):
        for SelectedItem in self.Interests.selectedItems():
            self.Interests.takeItem(self.Interests.row(SelectedItem))
        self.InterstInput.clear()

    def addAwardFucntion(self):
        if self.awardInput.text() == "":
            self.error_dialog.setText("Fill All Fields Please !!!!")
            self.error_dialog.show()
            return
        self.awards.addItem(
            f"Year {self.Date.date().year()} / {self.awardInput.text()}"
        )
        self.awardInput.clear()

    def removeAwardFucntion(self):
        for SelectedItem in self.awards.selectedItems():
            self.awards.takeItem(self.awards.row(SelectedItem))
        self.awardInput.clear()

    def addExpFucntion(self):
        if (
            self.exptitle.text() == ""
            or self.workplace.text() == ""
            or self.expdesc.text() == ""
        ):
            self.error_dialog.setText("Fill All Fields Please !!!!")
            self.error_dialog.show()
            return

        self.expList.addItem(
            f"{self.expDateFrom.date().year()} -- {self.expDateTo.date().year()} -> {self.exptitle.text()} @ {self.workplace.text()}"
        )
        self.exptitle.clear()
        self.workplace.clear()
        self.expdesc.clear()

    def removeExpFucntion(self):
        for SelectedItem in self.expList.selectedItems():
            self.expList.takeItem(self.expList.row(SelectedItem))
        self.exptitle.clear()
        self.workplace.clear()
        self.expdesc.clear()

    def addSkillFucntion(self):
        if self.Skill.text() == "":
            self.error_dialog.setText("Fill All Fields Please !!!!")
            self.error_dialog.show()
            return
        self.skillList.addItem(
            f"{self.Skill.text()} -> {self.skillSpinBox.value()} / 100"
        )
        self.Skill.clear()

    def removeSkillFucntion(self):
        for SelectedItem in self.skillList.selectedItems():
            self.skillList.takeItem(self.skillList.row(SelectedItem))
        self.Skill.clear()

