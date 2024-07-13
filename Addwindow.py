# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Add.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainBody(object):
    def setupUi(self, MainBody):
        if not MainBody.objectName():
            MainBody.setObjectName(u"MainBody")
        MainBody.resize(400, 300)
        MainBody.setStyleSheet(u"background: qlineargradient(x0: 0, y0: 1, x2: 1, y2: 1,\n"
"                                stop: 0.3 #222a41, \n"
"                                stop: 0.6 #0d182c);\n"
"font: 10pt \"Caviar Dreams\";\n"
"text-align: center;\n"
"")
        self.verticalLayout = QVBoxLayout(MainBody)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainFrame = QFrame(MainBody)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setStyleSheet(u"background-color: #172035;\n"
"padding: 1px 5px; \n"
"border-radius: 10px; \n"
"color: white;\n"
"text-align: center;")
        self.MainFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.InfoFrame = QFrame(self.MainFrame)
        self.InfoFrame.setObjectName(u"InfoFrame")
        self.InfoFrame.setStyleSheet(u"background-color: #172035;\n"
"padding: 1px 5px; \n"
"border-radius: 10px; \n"
"color: white;\n"
"text-align: center;")
        self.InfoFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.InfoFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.InfoFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.TextBody = QFrame(self.InfoFrame)
        self.TextBody.setObjectName(u"TextBody")
        self.TextBody.setStyleSheet(u"background-color: #172035;\n"
"padding: 1px 5px; \n"
"border-radius: 10px; \n"
"color: white;\n"
"text-align: center;")
        self.TextBody.setFrameShape(QFrame.Shape.StyledPanel)
        self.TextBody.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.TextBody)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.TextInput = QLineEdit(self.TextBody)
        self.TextInput.setObjectName(u"TextInput")
        self.TextInput.setStyleSheet(u"	background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"                            stop: 0 #333d5e,   /* \u0421\u0430\u043c\u044b\u0439 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"                            stop: 0.7 #192641);\n"
"	border: 2px solid qlineargradient(x1: 1, y1: 1, x2: 1, y2: 1,\n"
"                            stop: 0 #2a9587,   /* \u0421\u0430\u043c\u044b\u0439 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"                            stop: 0.5 #1a5979);\n"
"\n"
"padding: 2px 10px; \n"
"border-radius: 5px; \n"
"color: white;\n"
"font-weight: bold;\n"
"text-align: center;")

        self.verticalLayout_5.addWidget(self.TextInput)


        self.verticalLayout_4.addWidget(self.TextBody)

        self.InfoBody = QFrame(self.InfoFrame)
        self.InfoBody.setObjectName(u"InfoBody")
        self.InfoBody.setStyleSheet(u"	background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"                            stop: 0 #333d5e,   /* \u0421\u0430\u043c\u044b\u0439 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"                            stop: 0.7 #192641);\n"
"	border: 2px solid qlineargradient(x1: 1, y1: 1, x2: 1, y2: 1,\n"
"                            stop: 0 #2a9587,   /* \u0421\u0430\u043c\u044b\u0439 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"                            stop: 0.5 #1a5979);\n"
"\n"
"padding: 2px 10px; \n"
"border-radius: 5px; \n"
"color: white;\n"
"font-weight: bold;\n"
"text-align: center;")
        self.InfoBody.setFrameShape(QFrame.Shape.StyledPanel)
        self.InfoBody.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.InfoBody)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Complexity = QLabel(self.InfoBody)
        self.Complexity.setObjectName(u"Complexity")
        self.Complexity.setStyleSheet(u"	background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"                            stop: 0 #333d5e,   /* \u0421\u0430\u043c\u044b\u0439 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"                            stop: 0.7 #192641);\n"
"	border: 2px solid qlineargradient(x1: 1, y1: 1, x2: 1, y2: 1,\n"
"                            stop: 0 #2a9587,   /* \u0421\u0430\u043c\u044b\u0439 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"                            stop: 0.5 #1a5979);\n"
"\n"
"padding: 2px 10px; \n"
"border-radius: 5px; \n"
"color: white;\n"
"font-weight: bold;\n"
"text-align: center;")

        self.verticalLayout_3.addWidget(self.Complexity)

        self.ComplaxitiFrame = QFrame(self.InfoBody)
        self.ComplaxitiFrame.setObjectName(u"ComplaxitiFrame")
        self.ComplaxitiFrame.setStyleSheet(u"border: none ")
        self.ComplaxitiFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ComplaxitiFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.ComplaxitiFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.ChoseComplexity = QComboBox(self.ComplaxitiFrame)
        self.ChoseComplexity.addItem("")
        self.ChoseComplexity.addItem("")
        self.ChoseComplexity.addItem("")
        self.ChoseComplexity.setObjectName(u"ChoseComplexity")
        font = QFont()
        font.setFamilies([u"Caviar Dreams"])
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setHintingPreference(QFont.PreferDefaultHinting)
        self.ChoseComplexity.setFont(font)
        self.ChoseComplexity.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.ChoseComplexity.setStyleSheet(u"")
        self.ChoseComplexity.setInsertPolicy(QComboBox.InsertPolicy.InsertBeforeCurrent)
        self.ChoseComplexity.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.ChoseComplexity.setFrame(True)

        self.verticalLayout_6.addWidget(self.ChoseComplexity)


        self.verticalLayout_3.addWidget(self.ComplaxitiFrame)

        self.ImportantBtn = QCheckBox(self.InfoBody)
        self.ImportantBtn.setObjectName(u"ImportantBtn")
        self.ImportantBtn.setStyleSheet(u"border: none ")

        self.verticalLayout_3.addWidget(self.ImportantBtn)


        self.verticalLayout_4.addWidget(self.InfoBody, 0, Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_2.addWidget(self.InfoFrame)

        self.AddFrame = QFrame(self.MainFrame)
        self.AddFrame.setObjectName(u"AddFrame")
        self.AddFrame.setStyleSheet(u"	background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"                            stop: 0 #333d5e,   /* \u0421\u0430\u043c\u044b\u0439 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"                            stop: 0.7 #192641);\n"
"	border: 2px solid qlineargradient(x1: 1, y1: 1, x2: 1, y2: 1,\n"
"                            stop: 0 #2a9587,   /* \u0421\u0430\u043c\u044b\u0439 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"                            stop: 0.5 #1a5979);\n"
"\n"
"padding: 2px 10px; \n"
"border-radius: 5px; \n"
"color: white;\n"
"font-weight: bold;\n"
"text-align: center;")
        self.AddFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.AddFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.AddFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AddBtn = QPushButton(self.AddFrame)
        self.AddBtn.setObjectName(u"AddBtn")
        self.AddBtn.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.AddBtn.setStyleSheet(u"	background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"                            stop: 0 #333d5e,   /* \u0421\u0430\u043c\u044b\u0439 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"                            stop: 0.7 #192641);\n"
"	border: none;\n"
"\n"
"padding: 2px 10px; \n"
"border-radius: 5px; \n"
"color: white;\n"
"font-weight: bold;\n"
"text-align: center;")
        self.AddBtn.setFlat(False)

        self.horizontalLayout.addWidget(self.AddBtn)


        self.verticalLayout_2.addWidget(self.AddFrame)


        self.verticalLayout.addWidget(self.MainFrame)


        self.retranslateUi(MainBody)

        self.AddBtn.setDefault(False)


        QMetaObject.connectSlotsByName(MainBody)
    # setupUi

    def retranslateUi(self, MainBody):
        MainBody.setWindowTitle(QCoreApplication.translate("MainBody", u"Dialog", None))
        self.TextInput.setText("")
        self.Complexity.setText(QCoreApplication.translate("MainBody", u"Complexity", None))
        self.ChoseComplexity.setItemText(0, QCoreApplication.translate("MainBody", u"Hard", None))
        self.ChoseComplexity.setItemText(1, QCoreApplication.translate("MainBody", u"Medium", None))
        self.ChoseComplexity.setItemText(2, QCoreApplication.translate("MainBody", u"Easy", None))

        self.ImportantBtn.setText(QCoreApplication.translate("MainBody", u"Important!?", None))
        self.AddBtn.setText(QCoreApplication.translate("MainBody", u"Add!", None))
    # retranslateUi

