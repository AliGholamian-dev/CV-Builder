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

# Loading UI file
Form_InfoWindow = uic.loadUiType(os.path.join(os.getcwd(), "Resources/InfoWindow.ui"))[
    0
]

# A Python Dictionary to Store User's Data and Easy Acces
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

# Get User's Information
class InfoWindow(QMainWindow, Form_InfoWindow):
    def __init__(self):
        """ 
        InfoWindow Constructor 
        """
        super(InfoWindow, self).__init__()
        self.setupUi(self)
        # Error Popup for showing errors
        self.error_dialog = QMessageBox()
        self.error_dialog.setWindowTitle("Hey User")
        # Loading Image (If Image clicked connect it to it's Function)
        self.Picture.mousePressEvent = self.upload_picture
        # Adding and Removing Interest (If Button clicked connect it to it's Function)
        self.addInterest.clicked.connect(self.addInterestFucntion)
        self.removeInterest.clicked.connect(self.removeInterestFucntion)
        # Adding and Removing Awards (If Button clicked connect it to it's Function)
        self.addAward.clicked.connect(self.addAwardFucntion)
        self.removeAward.clicked.connect(self.removeAwardFucntion)
        # Adding and Removing Work Experience (If Button clicked connect it to it's Function)
        self.addExp.clicked.connect(self.addExpFucntion)
        self.removeExp.clicked.connect(self.removeExpFucntion)
        # Adding and Removing Skill (If Button clicked connect it to it's Function)
        self.addSkill.clicked.connect(self.addSkillFucntion)
        self.removeSkill.clicked.connect(self.removeSkillFucntion)
        # Adding and Removing Education Degree (If Button clicked connect it to it's Function)
        self.addEd.clicked.connect(self.addEdFucntion)
        self.removeEd.clicked.connect(self.removeEdFucntion)
        # Button to fetch User's Github Repos Automatically
        self.fetchRepo.clicked.connect(self.goGetRepos)
        # Create PDF when Setting is selected from dropdown Menu
        self.actionGenerate_PDF.triggered.connect(self.generateFunction)
        self.repoResponse = None

    async def fetchRepository(self):
        """ 
        Fecth User's Repos
        """
        # Checking for Internet Connection
        try:
            # see if we can resolve the host name -- tells us if there is
            # a DNS listening
            host = socket.gethostbyname("one.one.one.one")
            # connect to the host -- tells us if the host is actually
            # reachable
            s = socket.create_connection((host, 80), 2)
            s.close()
        except:  # No internet
            self.error_dialog.setText("Check your Internet Connection")
            self.error_dialog.show()
            self.fetchRepo.setEnabled(True)
            return
        # Fecth User's Repos By Github API
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"https://api.github.com/users/{self.GitHub.text()}/repos"
            ) as response:
                self.repoResponse = None
                # Parse Response as JSON
                self.repoResponse = await response.json()
                # Check if Github ID was correct
                try:
                    temp = self.repoResponse[0]["name"]
                except:  # Wrong GitHub ID
                    self.error_dialog.setText("Wrong GitHub ID")
                    self.error_dialog.show()
                    self.fetchRepo.setEnabled(True)
                    return
                # Emty the table for new content
                for _ in range(self.repoWidget.rowCount()):
                    self.repoWidget.removeRow(0)
                self.repoWidget.clear()
                row = 0
                # Add All repos fetched to table
                for gitrepos_each in self.repoResponse:
                    self.repoWidget.insertRow(self.repoWidget.rowCount())
                    # Add name of repo
                    self.repoWidget.setItem(
                        row, 2, QTableWidgetItem(gitrepos_each["name"]),
                    )
                    # Add to CV CheckBox
                    chkBoxItem = QTableWidgetItem("Add to CV")
                    chkBoxItem.setFlags(
                        QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled
                    )
                    chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                    self.repoWidget.setItem(
                        row, 0, QTableWidgetItem(chkBoxItem),
                    )
                    # Add Readme CheckBox
                    chkBoxItem2 = QTableWidgetItem("Add Readme")
                    chkBoxItem2.setFlags(
                        QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled
                    )
                    chkBoxItem2.setCheckState(QtCore.Qt.Unchecked)
                    self.repoWidget.setItem(
                        row, 1, QTableWidgetItem(chkBoxItem2),
                    )
                    row += 1
        # Enable Fecth Button
        self.fetchRepo.setEnabled(True)

    def goGetRepos(self):
        """ 
        Called when Fecth Button Clicked
        """
        # Check if User Entered GitHub ID
        if self.GitHub.text() == "":
            self.error_dialog.setText("Fill All Fields Please !!!!")
            self.error_dialog.show()
            return
        self.fetchRepo.setEnabled(False)
        # Fetch Repos With aiohttp
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.fetchRepository())

    def upload_picture(self, event):
        """ 
        Uplaod User Picture
        """
        # Open Choose File Dialog
        fileDialog = QFileDialog(parent=self)
        # Fetch Picture Path
        _dict["Picture"] = fileDialog.getOpenFileUrl(
            parent=self, caption="Choose Your Profile Pictue"
        )[0].url()[8:]
        # Show Picture in App
        self.Picture.setPixmap(QPixmap(_dict["Picture"]))

    def addInterestFucntion(self):
        """ 
        Add interest
        """
        # check if inputlabel is filled
        if self.InterstInput.text() == "":
            self.error_dialog.setText("Fill All Fields Please !!!!")
            self.error_dialog.show()
            return
        # add interest to ListView
        self.Interests.addItem(self.InterstInput.text())
        # Clear Inputlabel
        self.InterstInput.clear()

    def removeInterestFucntion(self):
        """ 
        Remove interest
        """
        # Remove Selected Item
        for SelectedItem in self.Interests.selectedItems():
            self.Interests.takeItem(self.Interests.row(SelectedItem))
        # Clear Inputlabel
        self.InterstInput.clear()

    def addAwardFucntion(self):
        """ 
        Add Award
        """
        # check if inputlabel is filled
        if self.awardInput.text() == "":
            self.error_dialog.setText("Fill All Fields Please !!!!")
            self.error_dialog.show()
            return
        # add Award to ListView
        self.awards.addItem(
            f"Year {self.Date.date().year()} / {self.awardInput.text()}"
        )
        _dict["Awards"].append([f"{self.Date.date().year()}", self.awardInput.text()])
        # Clear Inputlabel
        self.awardInput.clear()

    def removeAwardFucntion(self):
        """ 
        Remove Award
        """
        # Remove Selected Item
        for SelectedItem in self.awards.selectedItems():
            temp_index = self.awards.row(SelectedItem)
            _dict["Awards"].pop(temp_index)
            self.awards.takeItem(temp_index)
        # Clear Inputlabel
        self.awardInput.clear()

    def addExpFucntion(self):
        """ 
        Add Experience
        """
        # check if inputlabel is filled
        if (
            self.exptitle.text() == ""
            or self.workplace.text() == ""
            or self.expdesc.text() == ""
        ):
            self.error_dialog.setText("Fill All Fields Please !!!!")
            self.error_dialog.show()
            return
        # add Experience to ListView
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
        # Clear Inputlabel
        self.exptitle.clear()
        self.workplace.clear()
        self.expdesc.clear()

    def removeExpFucntion(self):
        """ 
        Remove Experience
        """
        # Remove Selected Item
        for SelectedItem in self.expList.selectedItems():
            temp_index = self.expList.row(SelectedItem)
            _dict["Experience"].pop(temp_index)
            self.expList.takeItem(temp_index)
        # Clear Inputlabel
        self.exptitle.clear()
        self.workplace.clear()
        self.expdesc.clear()

    def addSkillFucntion(self):
        """ 
        Add Skill
        """
        # check if inputlabel is filled
        if self.Skill.text() == "":
            self.error_dialog.setText("Fill All Fields Please !!!!")
            self.error_dialog.show()
            return
        # add Skill to ListView
        self.skillList.addItem(
            f"{self.Skill.text()} -> {self.skillSpinBox.value()} / 100"
        )
        if _dict["Template"] == "AliceCV":
            _dict["Skills"].append(
                [self.Skill.text(), self.skillSpinBox.value() / 100 * 6]
            )
        else:
            _dict["Skills"].append([self.Skill.text(), self.skillSpinBox.value()])
        # Clear Inputlabel
        self.Skill.clear()

    def removeSkillFucntion(self):
        """ 
        Remove Skill
        """
        # Remove Selected Item
        for SelectedItem in self.skillList.selectedItems():
            temp_index = self.skillList.row(SelectedItem)
            _dict["Skills"].pop(temp_index)
            self.skillList.takeItem(temp_index)
        # Clear Inputlabel
        self.Skill.clear()

    def addEdFucntion(self):
        """ 
        Add Education
        """
        # check if inputlabel is filled
        if (
            self.edTitle.text() == ""
            or self.University.text() == ""
            or self.edDesc.text() == ""
        ):
            self.error_dialog.setText("Fill All Fields Please !!!!")
            self.error_dialog.show()
            return
        # add Education to ListView
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
        # Clear Inputlabel
        self.edTitle.clear()
        self.University.clear()
        self.edDesc.clear()

    def removeEdFucntion(self):
        """ 
        Remove Education
        """
        # Remove Selected Item
        for SelectedItem in self.edList.selectedItems():
            temp_index = self.edList.row(SelectedItem)
            _dict["Education"].pop(temp_index)
            self.edList.takeItem(temp_index)
        # Clear Inputlabel
        self.edTitle.clear()
        self.University.clear()
        self.edDesc.clear()

    def generateFunction(self):
        """
        Generate PDF
        """
        # Checking for Internet Connection(Install LATEX Libs)
        try:
            # see if we can resolve the host name -- tells us if there is
            # a DNS listening
            host = socket.gethostbyname("one.one.one.one")
            # connect to the host -- tells us if the host is actually
            # reachable
            s = socket.create_connection((host, 80), 2)
            s.close()
        except:  # No Internet
            self.error_dialog.setText("Check your Internet Connection")
            self.error_dialog.show()
            self.fetchRepo.setEnabled(True)
            return
        # Update Dict with User Info
        # In case No Picture Added
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
        # Generate PDF
        your_resume = CreatePDF(_dict)
        your_resume.update_template_context()
        your_resume.makeCV()

