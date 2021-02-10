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
from PDFCreate import CreatePDF

Form_InfoWindow = uic.loadUiType(os.path.join(os.getcwd(), "Resources/InfoWindow.ui"))[
    0
]

_dict = {
    "Template": "",
    "nameOfFile": "Resume",
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
    "Info": "",
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

        self.addEd.clicked.connect(self.addEdFucntion)
        self.removeEd.clicked.connect(self.removeEdFucntion)

        self.fetchRepo.clicked.connect(self.goGetRepos)

        self.actionGenerate_PDF.triggered.connect(self.generateFunction)
        self.repoResponse = None

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
                self.repoResponse = None
                self.repoResponse = await response.json()
                try:
                    temp = self.repoResponse[0]["name"]
                except:
                    self.error_dialog.setText("Wrong GitHub ID")
                    self.error_dialog.show()
                    self.fetchRepo.setEnabled(True)
                    return

                for _ in range(self.repoWidget.rowCount()):
                    self.repoWidget.removeRow(0)
                self.repoWidget.clear()
                row = 0
                for gitrepos_each in self.repoResponse:
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
        _dict["Awards"].append([f"{self.Date.date().year()}", self.awardInput.text()])
        self.awardInput.clear()

    def removeAwardFucntion(self):
        for SelectedItem in self.awards.selectedItems():
            temp_index = self.awards.row(SelectedItem)
            _dict["Awards"].pop(temp_index)
            self.awards.takeItem(temp_index)
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
            f"{self.expDate.date().year()} -> {self.exptitle.text()} @ {self.workplace.text()}"
        )
        _dict["Experience"].append(
            [
                f"{self.expDate.date().year()}",
                self.exptitle.text(),
                self.workplace.text(),
                self.expdesc.text(),
            ]
        )
        self.exptitle.clear()
        self.workplace.clear()
        self.expdesc.clear()

    def removeExpFucntion(self):
        for SelectedItem in self.expList.selectedItems():
            temp_index = self.expList.row(SelectedItem)
            _dict["Experience"].pop(temp_index)
            self.expList.takeItem(temp_index)
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
        if _dict["Template"] == "AliceCV":
            _dict["Skills"].append(
                [self.Skill.text(), self.skillSpinBox.value() / 100 * 6]
            )
        else:
            _dict["Skills"].append([self.Skill.text(), self.skillSpinBox.value()])
        self.Skill.clear()

    def removeSkillFucntion(self):
        for SelectedItem in self.skillList.selectedItems():
            temp_index = self.skillList.row(SelectedItem)
            _dict["Skills"].pop(temp_index)
            self.skillList.takeItem(temp_index)
        self.Skill.clear()

    def addEdFucntion(self):
        if (
            self.edTitle.text() == ""
            or self.University.text() == ""
            or self.edDesc.text() == ""
        ):
            self.error_dialog.setText("Fill All Fields Please !!!!")
            self.error_dialog.show()
            return
        self.edList.addItem(
            f"{self.edDatefrom.date().year()} -- {self.edDateTo.date().year()} /-> {self.edTitle.text()} @ {self.University.text()}"
        )
        _dict["Education"].append(
            [
                f"{self.edDatefrom.date().year()}",
                f"{self.edDateTo.date().year()}",
                self.edTitle.text(),
                self.University.text(),
                self.edDesc.text(),
            ]
        )
        self.edTitle.clear()
        self.University.clear()
        self.edDesc.clear()

    def removeEdFucntion(self):
        for SelectedItem in self.edList.selectedItems():
            temp_index = self.edList.row(SelectedItem)
            _dict["Education"].pop(temp_index)
            self.edList.takeItem(temp_index)
        self.edTitle.clear()
        self.University.clear()
        self.edDesc.clear()

    def generateFunction(self):
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
        if _dict["Picture"] == "":
            _dict["Picture"] = "picture/default_profile.png"
        _dict["Name"] = self.Name.text()
        _dict["LastName"] = self.LastName.text()
        _dict["Title"] = self.jobTitle.text()
        _dict["Address"] = self.Address.text()
        _dict["Phone"] = self.Phone.text()
        _dict["Mail"] = self.Email.text()
        _dict["Git"] = self.GitHub.text()
        _dict["Linkedin"] = self.LinkedIn.text()
        _dict["Site"] = self.Site.text()
        _dict["Aboutme"] = self.Aboutme.toPlainText()
        if _dict["Template"] == "ModernCV":
            _dict["Interests"] = []
            for i in range(self.Interests.count()):
                _dict["Interests"].append(self.Interests.item(i).text())
        elif _dict["Template"] == "DeveloperCV":
            if self.Interests.count() > 0:
                _dict["Interests"] = f"{self.Interests.item(0).text()}"
                for i in range(1, self.Interests.count()):
                    _dict["Interests"] += f", {self.Interests.item(i).text()}"
        else:
            if self.Interests.count() > 0:
                _dict["Interests"] = f"{self.Interests.item(0).text()}"
                for i in range(1, self.Interests.count()):
                    _dict["Interests"] += f"\n{self.Interests.item(i).text()}"
        for i in range(self.repoWidget.rowCount()):
            if self.repoWidget.item(i, 0).checkState() == QtCore.Qt.Checked and (
                not self.repoWidget.item(i, 1).checkState() == QtCore.Qt.Checked
            ):
                _dict["Gitrepos"].append(
                    [
                        "Private"
                        if self.repoResponse[i]["private"] == "false"
                        else "Public",
                        self.repoWidget.item(i, 2).text(),
                        f"https://github.com/{self.GitHub.text()}/{self.repoWidget.item(i, 2).text()}/blob/master/readme.md",
                        self.repoWidget.item(i, 1).checkState() == QtCore.Qt.Checked,
                    ]
                )
        for i in range(self.repoWidget.rowCount()):
            if (
                self.repoWidget.item(i, 0).checkState() == QtCore.Qt.Checked
                and self.repoWidget.item(i, 1).checkState() == QtCore.Qt.Checked
            ):
                _dict["Gitrepos"].append(
                    [
                        "Private"
                        if self.repoResponse[i]["private"] == "false"
                        else "Public",
                        self.repoWidget.item(i, 2).text(),
                        f"https://github.com/{self.GitHub.text()}/{self.repoWidget.item(i, 2).text()}/blob/master/readme.md",
                        self.repoWidget.item(i, 1).checkState() == QtCore.Qt.Checked,
                    ]
                )
        your_resume = CreatePDF(_dict)
        your_resume.update_template_context()
        your_resume.makeCV()

