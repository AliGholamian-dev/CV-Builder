# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui03_info.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Gui03(object):
    def setupUi(self, Gui03):
        Gui03.setObjectName("Gui03")
        Gui03.resize(2000, 1500)
        Gui03.setMouseTracking(False)
        Gui03.setStyleSheet("color: rgb(139, 0, 0);")
        self.Background = QtWidgets.QGraphicsView(Gui03)
        self.Background.setGeometry(QtCore.QRect(-110, -880, 2131, 3241))
        self.Background.setStyleSheet("\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));")
        self.Background.setObjectName("Background")
        self.title = QtWidgets.QLabel(Gui03)
        self.title.setGeometry(QtCore.QRect(760, 10, 561, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(255, 255, 255);")
        self.title.setObjectName("title")
        self.title_design_by = QtWidgets.QLabel(Gui03)
        self.title_design_by.setGeometry(QtCore.QRect(800, 80, 481, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.title_design_by.setFont(font)
        self.title_design_by.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_design_by.setObjectName("title_design_by")
        self.name = QtWidgets.QTextEdit(Gui03)
        self.name.setGeometry(QtCore.QRect(610, 310, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setStyleSheet("\n"
"color: rgb(61, 61, 61);")
        self.name.setObjectName("name")
        self.last = QtWidgets.QTextEdit(Gui03)
        self.last.setGeometry(QtCore.QRect(610, 430, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.last.setFont(font)
        self.last.setStyleSheet("\n"
"color: rgb(61, 61, 61);")
        self.last.setObjectName("last")
        self.textEdit_birthday = QtWidgets.QTextEdit(Gui03)
        self.textEdit_birthday.setGeometry(QtCore.QRect(610, 550, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_birthday.setFont(font)
        self.textEdit_birthday.setStyleSheet("\n"
"color: rgb(61, 61, 61);")
        self.textEdit_birthday.setObjectName("textEdit_birthday")
        self.textEdit_Address = QtWidgets.QTextEdit(Gui03)
        self.textEdit_Address.setGeometry(QtCore.QRect(610, 670, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_Address.setFont(font)
        self.textEdit_Address.setStyleSheet("\n"
"color: rgb(61, 61, 61);")
        self.textEdit_Address.setObjectName("textEdit_Address")
        self.textEdit_Phone = QtWidgets.QTextEdit(Gui03)
        self.textEdit_Phone.setGeometry(QtCore.QRect(610, 790, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_Phone.setFont(font)
        self.textEdit_Phone.setStyleSheet("\n"
"color: rgb(61, 61, 61);")
        self.textEdit_Phone.setObjectName("textEdit_Phone")
        self.textEdit_Linkedin = QtWidgets.QTextEdit(Gui03)
        self.textEdit_Linkedin.setGeometry(QtCore.QRect(610, 910, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_Linkedin.setFont(font)
        self.textEdit_Linkedin.setStyleSheet("\n"
"color: rgb(61, 61, 61);")
        self.textEdit_Linkedin.setObjectName("textEdit_Linkedin")
        self.title_name = QtWidgets.QLabel(Gui03)
        self.title_name.setGeometry(QtCore.QRect(610, 260, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_name.setFont(font)
        self.title_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_name.setObjectName("title_name")
        self.title_last = QtWidgets.QLabel(Gui03)
        self.title_last.setGeometry(QtCore.QRect(610, 380, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_last.setFont(font)
        self.title_last.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_last.setObjectName("title_last")
        self.title_Birthday = QtWidgets.QLabel(Gui03)
        self.title_Birthday.setGeometry(QtCore.QRect(610, 500, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_Birthday.setFont(font)
        self.title_Birthday.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_Birthday.setObjectName("title_Birthday")
        self.title_address = QtWidgets.QLabel(Gui03)
        self.title_address.setGeometry(QtCore.QRect(610, 620, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_address.setFont(font)
        self.title_address.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_address.setObjectName("title_address")
        self.title_Phone = QtWidgets.QLabel(Gui03)
        self.title_Phone.setGeometry(QtCore.QRect(610, 740, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_Phone.setFont(font)
        self.title_Phone.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_Phone.setObjectName("title_Phone")
        self.title_linkedin = QtWidgets.QLabel(Gui03)
        self.title_linkedin.setGeometry(QtCore.QRect(610, 860, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_linkedin.setFont(font)
        self.title_linkedin.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_linkedin.setObjectName("title_linkedin")
        self.avatar = QtWidgets.QPushButton(Gui03)
        self.avatar.setGeometry(QtCore.QRect(60, 270, 231, 241))
        self.avatar.setStyleSheet("background-image: url(:/default_profile.png);")
        self.avatar.setText("")
        self.avatar.setObjectName("avatar")
        self.textEdit_Aboutme = QtWidgets.QTextEdit(Gui03)
        self.textEdit_Aboutme.setGeometry(QtCore.QRect(40, 1030, 961, 351))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_Aboutme.setFont(font)
        self.textEdit_Aboutme.setStyleSheet("\n"
"color: rgb(61, 61, 61);")
        self.textEdit_Aboutme.setObjectName("textEdit_Aboutme")
        self.title_Aboutme = QtWidgets.QLabel(Gui03)
        self.title_Aboutme.setGeometry(QtCore.QRect(40, 980, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_Aboutme.setFont(font)
        self.title_Aboutme.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_Aboutme.setObjectName("title_Aboutme")
        self.listView_skill = QtWidgets.QListView(Gui03)
        self.listView_skill.setGeometry(QtCore.QRect(1120, 370, 401, 251))
        self.listView_skill.setObjectName("listView_skill")
        self.name_2 = QtWidgets.QTextEdit(Gui03)
        self.name_2.setGeometry(QtCore.QRect(1120, 310, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.name_2.setFont(font)
        self.name_2.setStyleSheet("\n"
"color: rgb(61, 61, 61);")
        self.name_2.setObjectName("name_2")
        self.pushButton_add = QtWidgets.QPushButton(Gui03)
        self.pushButton_add.setGeometry(QtCore.QRect(1350, 310, 81, 51))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_delete = QtWidgets.QPushButton(Gui03)
        self.pushButton_delete.setGeometry(QtCore.QRect(1440, 310, 81, 51))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.title_Skillinfo = QtWidgets.QLabel(Gui03)
        self.title_Skillinfo.setGeometry(QtCore.QRect(1120, 260, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_Skillinfo.setFont(font)
        self.title_Skillinfo.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_Skillinfo.setObjectName("title_Skillinfo")
        self.name_3 = QtWidgets.QTextEdit(Gui03)
        self.name_3.setGeometry(QtCore.QRect(1120, 720, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.name_3.setFont(font)
        self.name_3.setStyleSheet("\n"
"color: rgb(61, 61, 61);")
        self.name_3.setObjectName("name_3")
        self.title_Skillinfo_2 = QtWidgets.QLabel(Gui03)
        self.title_Skillinfo_2.setGeometry(QtCore.QRect(1120, 670, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title_Skillinfo_2.setFont(font)
        self.title_Skillinfo_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_Skillinfo_2.setObjectName("title_Skillinfo_2")
        self.pushButton_add_2 = QtWidgets.QPushButton(Gui03)
        self.pushButton_add_2.setGeometry(QtCore.QRect(1350, 720, 81, 51))
        self.pushButton_add_2.setObjectName("pushButton_add_2")
        self.pushButton_delete_2 = QtWidgets.QPushButton(Gui03)
        self.pushButton_delete_2.setGeometry(QtCore.QRect(1440, 720, 81, 51))
        self.pushButton_delete_2.setObjectName("pushButton_delete_2")
        self.listView_skill_2 = QtWidgets.QListView(Gui03)
        self.listView_skill_2.setGeometry(QtCore.QRect(1120, 780, 401, 251))
        self.listView_skill_2.setObjectName("listView_skill_2")

        self.retranslateUi(Gui03)
        QtCore.QMetaObject.connectSlotsByName(Gui03)

    def retranslateUi(self, Gui03):
        _translate = QtCore.QCoreApplication.translate
        Gui03.setWindowTitle(_translate("Gui03", "gui"))
        self.title.setText(_translate("Gui03", "Rrsume Creator"))
        self.title_design_by.setText(_translate("Gui03", "Design & Create by Ali Safarpour & Ali Gholamian"))
        self.title_name.setText(_translate("Gui03", "Name"))
        self.title_last.setText(_translate("Gui03", "Last Name"))
        self.title_Birthday.setText(_translate("Gui03", "Birthday"))
        self.title_address.setText(_translate("Gui03", "Address"))
        self.title_Phone.setText(_translate("Gui03", "Phone Number"))
        self.title_linkedin.setText(_translate("Gui03", "Linkedin ID"))
        self.title_Aboutme.setText(_translate("Gui03", "About Me"))
        self.pushButton_add.setText(_translate("Gui03", "Add"))
        self.pushButton_delete.setText(_translate("Gui03", "Delete"))
        self.title_Skillinfo.setText(_translate("Gui03", "Skill Info"))
        self.title_Skillinfo_2.setText(_translate("Gui03", "Award"))
        self.pushButton_add_2.setText(_translate("Gui03", "Add"))
        self.pushButton_delete_2.setText(_translate("Gui03", "Delete"))
import mainresource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Gui03 = QtWidgets.QWidget()
    ui = Ui_Gui03()
    ui.setupUi(Gui03)
    Gui03.show()
    sys.exit(app.exec_())
