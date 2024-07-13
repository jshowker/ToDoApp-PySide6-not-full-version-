# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TodoApp.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)
import source_img

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(912, 753)
        font = QFont()
        font.setFamilies([u"Caviar Dreams"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
"	font: 10pt \"Caviar Dreams\";\n"
"	border none;\n"
"	background-color: transparent;\n"
"	background: none;\n"
"	padding: 0 ;\n"
"	margin: 0 ;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget {\n"
"background: qlineargradient(x0: 0, y0: 1, x2: 1, y2: 1,\n"
"                                stop: 0.3 #222a41, \n"
"                                stop: 0.6 #0d182c);\n"
"}\n"
"\n"
"#UnderSubMenu{\n"
"	border: none;\n"
"}\n"
"#Swap{\n"
"	background-color:#1c1727\n"
"}\n"
"#UnderSubMenu QFrame{\n"
"background-color:rgba(1,1,1,0);\n"
"boarder: none;\n"
"}\n"
"#UnderSubMenu QPushButton {\n"
"    text-align: center;\n"
"    padding: 5px 10px; \n"
"    border-radius: 5px; \n"
"	background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"                            stop: 0 #333d5e,  \n"
"                            stop: 0.7 #192641);\n"
"    color: white;\n"
"    font-weight: bold;\n"
"	border: 2px solid qlineargradient(x1: 1, y1: 1, x2: 1, y2: 1,\n"
"                            stop: 0 #2a9587,  \n"
"                 "
                        "           stop: 0.5 #1a5979);\n"
"}\n"
"#centraMenu QPushButton{\n"
"    text-align: center;\n"
"    padding: 2px 2px; \n"
"    border-radius: 10px; \n"
"    background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"                            stop: 0 #7442fc,  \n"
"                            stop: 1 #a07dfd);  \n"
"\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"}\n"
"#NotesAndFinance QPushButton{\n"
" text-align: center;\n"
"    padding: 2px 2px; \n"
"    border-radius: 10px; \n"
"    background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"                            stop: 0 #7442fc,  \n"
"                            stop: 1 #a07dfd);  \n"
"\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border: none; \n"
"}\n"
"#Time QLabel{\n"
"	text-align: center;\n"
"	padding: 5px 25 px;\n"
"	border-top-left-radius: 10 px;\n"
"	border-bottom-left-radius: 10 px;\n"
"}\n"
"#ToDoMenu{\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"}\n"
"#InProgressMenu{\n"
"border: 1px soli"
                        "d rgba(255, 255, 255, 0.5);\n"
"}\n"
"#DoneMenu{\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"}\n"
"#StatMenu{\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"}\n"
"#NotesMain{\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"}\n"
"#FinanceMainF{\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"}\n"
"#mainBody{\n"
"	background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"                            stop: 0 #333d5e,   \n"
"                            stop: 0.7 #192641);\n"
"	border: 2px solid qlineargradient(x1: 1, y1: 1, x2: 1, y2: 1,\n"
"                            stop: 0 #2a9587,  \n"
"                            stop: 0.5 #1a5979);\n"
"padding: 2px 5px;\n"
"border-radius: 6px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"#FinanceMainF{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #333d5e,  \n"
"                            stop: 0.7 #192641);\n"
"padding: 2px 5px;\n"
"border-radius: 6px;\n"
"color: white;\n"
"font-weight: bold"
                        ";\n"
"}\n"
"#NotesMain{\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #333d5e,  \n"
"                            stop: 0.7 #192641);\n"
"padding: 2px 5px;\n"
"border-radius: 6px;\n"
"color: white;\n"
"font-weight: bold;\n"
"\n"
"\n"
"}")
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        MainWindow.setDocumentMode(True)
        MainWindow.setTabShape(QTabWidget.TabShape.Rounded)
        MainWindow.setDockNestingEnabled(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainBody = QWidget(self.centralwidget)
        self.mainBody.setObjectName(u"mainBody")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBody.sizePolicy().hasHeightForWidth())
        self.mainBody.setSizePolicy(sizePolicy)
        self.mainBody.setMinimumSize(QSize(0, 0))
        self.mainBody.setStyleSheet(u"")
        self.verticalLayout_34 = QVBoxLayout(self.mainBody)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 10, 20, 10)
        self.LogAndSet = QFrame(self.mainBody)
        self.LogAndSet.setObjectName(u"LogAndSet")
        self.LogAndSet.setStyleSheet(u"\n"
"padding: 2px 5px;\n"
"border-radius: 6px;\n"
"color: white;\n"
"font-weight: bold;\n"
"background-color: #172035;\n"
"")
        self.LogAndSet.setFrameShape(QFrame.Shape.StyledPanel)
        self.LogAndSet.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.LogAndSet)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 10, 0, 10)
        self.SettingsBtn = QPushButton(self.LogAndSet)
        self.SettingsBtn.setObjectName(u"SettingsBtn")
        self.SettingsBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/Icons/feather/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.SettingsBtn.setIcon(icon)

        self.horizontalLayout_11.addWidget(self.SettingsBtn)

        self.LogBtn = QPushButton(self.LogAndSet)
        self.LogBtn.setObjectName(u"LogBtn")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/feather/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.LogBtn.setIcon(icon1)

        self.horizontalLayout_11.addWidget(self.LogBtn)


        self.verticalLayout_34.addWidget(self.LogAndSet, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addWidget(self.mainBody)

        self.centraMenu = QWidget(self.centralwidget)
        self.centraMenu.setObjectName(u"centraMenu")
        self.horizontalLayout_2 = QHBoxLayout(self.centraMenu)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 0, 10, 0)
        self.ToDoMenu = QWidget(self.centraMenu)
        self.ToDoMenu.setObjectName(u"ToDoMenu")
        self.ToDoMenu.setStyleSheet(u"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #333d5e,   /* \u0421\u0430\u043c\u044b\u0439 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"                            stop: 0.7 #192641);\n"
"padding: 2px 5px;\n"
"border-radius: 6px;\n"
"color: white;\n"
"font-weight: bold;\n"
"\n"
"\n"
"")
        self.verticalLayout_16 = QVBoxLayout(self.ToDoMenu)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.ToDoMenuL = QFrame(self.ToDoMenu)
        self.ToDoMenuL.setObjectName(u"ToDoMenuL")
        self.ToDoMenuL.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"boarder: none")
        self.ToDoMenuL.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToDoMenuL.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.ToDoMenuL)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.ToText = QFrame(self.ToDoMenuL)
        self.ToText.setObjectName(u"ToText")
        self.ToText.setStyleSheet(u"background-color: rgba(255,255,255 0);\n"
"boarder: none")
        self.ToText.setFrameShape(QFrame.Shape.NoFrame)
        self.ToText.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.ToText)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 10, 0, 10)
        self.TextTodo = QLabel(self.ToText)
        self.TextTodo.setObjectName(u"TextTodo")
        self.TextTodo.setFrameShape(QFrame.Shape.NoFrame)

        self.verticalLayout_19.addWidget(self.TextTodo)


        self.verticalLayout_18.addWidget(self.ToText)

        self.TodoList_2 = QListWidget(self.ToDoMenuL)
        self.TodoList_2.setObjectName(u"TodoList_2")

        self.verticalLayout_18.addWidget(self.TodoList_2)


        self.verticalLayout_16.addWidget(self.ToDoMenuL)

        self.AddTF = QFrame(self.ToDoMenu)
        self.AddTF.setObjectName(u"AddTF")
        self.AddTF.setStyleSheet(u"background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"                            stop: 0 #7442fc,   /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u043f\u0440\u0430\u0432\u0430 */\n"
"                            stop: 1 #a07dfd);  /* \u0421\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u043b\u0435\u0432\u0430 */\n"
"\n"
"padding: 2px 10px; \n"
"border-radius: 5px; \n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.AddTF.setFrameShape(QFrame.Shape.NoFrame)
        self.AddTF.setFrameShadow(QFrame.Shadow.Raised)
        self.AddTF.setLineWidth(0)
        self.verticalLayout_17 = QVBoxLayout(self.AddTF)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.AddTB = QPushButton(self.AddTF)
        self.AddTB.setObjectName(u"AddTB")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.AddTB.sizePolicy().hasHeightForWidth())
        self.AddTB.setSizePolicy(sizePolicy1)
        self.AddTB.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)

        self.verticalLayout_17.addWidget(self.AddTB)


        self.verticalLayout_16.addWidget(self.AddTF)


        self.horizontalLayout_2.addWidget(self.ToDoMenu)

        self.InProgressMenu = QWidget(self.centraMenu)
        self.InProgressMenu.setObjectName(u"InProgressMenu")
        self.InProgressMenu.setStyleSheet(u"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #333d5e,   /* \u0421\u0430\u043c\u044b\u0439 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"                            stop: 0.7 #192641);\n"
"padding: 2px 5px;\n"
"border-radius: 6px;\n"
"color: white;\n"
"font-weight: bold;\n"
"\n"
"\n"
"")
        self.verticalLayout_20 = QVBoxLayout(self.InProgressMenu)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.InProgMeuL = QFrame(self.InProgressMenu)
        self.InProgMeuL.setObjectName(u"InProgMeuL")
        self.InProgMeuL.setStyleSheet(u"background-color:rgba(255,255,255,0)")
        self.InProgMeuL.setFrameShape(QFrame.Shape.StyledPanel)
        self.InProgMeuL.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.InProgMeuL)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.InText = QFrame(self.InProgMeuL)
        self.InText.setObjectName(u"InText")
        self.InText.setStyleSheet(u"background-color: rgba(255,255,255 0)")
        self.InText.setFrameShape(QFrame.Shape.NoFrame)
        self.InText.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.InText)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 10, 0, 10)
        self.InProgressText_2 = QLabel(self.InText)
        self.InProgressText_2.setObjectName(u"InProgressText_2")

        self.verticalLayout_23.addWidget(self.InProgressText_2)


        self.verticalLayout_22.addWidget(self.InText)

        self.InProgressList = QListWidget(self.InProgMeuL)
        self.InProgressList.setObjectName(u"InProgressList")
        self.InProgressList.setStyleSheet(u"background-color:rgba(255,255,255,0)")
        self.InProgressList.setFrameShape(QFrame.Shape.NoFrame)
        self.InProgressList.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.InProgressList.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout_22.addWidget(self.InProgressList)


        self.verticalLayout_20.addWidget(self.InProgMeuL)

        self.AddTF_2 = QFrame(self.InProgressMenu)
        self.AddTF_2.setObjectName(u"AddTF_2")
        self.AddTF_2.setStyleSheet(u"background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"                            stop: 0 #7442fc,   /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u043f\u0440\u0430\u0432\u0430 */\n"
"                            stop: 1 #a07dfd);  /* \u0421\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u043b\u0435\u0432\u0430 */\n"
"\n"
"padding: 2px 10px; \n"
"border-radius: 5px; \n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.AddTF_2.setFrameShape(QFrame.Shape.NoFrame)
        self.AddTF_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.AddTF_2)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.AddTB_2 = QPushButton(self.AddTF_2)
        self.AddTB_2.setObjectName(u"AddTB_2")
        self.AddTB_2.setStyleSheet(u"")

        self.verticalLayout_21.addWidget(self.AddTB_2)


        self.verticalLayout_20.addWidget(self.AddTF_2)


        self.horizontalLayout_2.addWidget(self.InProgressMenu)

        self.DoneMenu = QWidget(self.centraMenu)
        self.DoneMenu.setObjectName(u"DoneMenu")
        sizePolicy1.setHeightForWidth(self.DoneMenu.sizePolicy().hasHeightForWidth())
        self.DoneMenu.setSizePolicy(sizePolicy1)
        self.DoneMenu.setStyleSheet(u"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                            stop: 0 #333d5e,   /* \u0421\u0430\u043c\u044b\u0439 \u0441\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u0432\u0435\u0440\u0445\u0443 */\n"
"                            stop: 0.7 #192641);\n"
"padding: 2px 5px;\n"
"border-radius: 6px;\n"
"color: white;\n"
"font-weight: bold;\n"
"\n"
"\n"
"")
        self.verticalLayout_8 = QVBoxLayout(self.DoneMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.DoneMenuL = QFrame(self.DoneMenu)
        self.DoneMenuL.setObjectName(u"DoneMenuL")
        self.DoneMenuL.setStyleSheet(u"background-color:rgba(255,255,255,0)")
        self.DoneMenuL.setFrameShape(QFrame.Shape.StyledPanel)
        self.DoneMenuL.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.DoneMenuL)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.DoneText_2 = QFrame(self.DoneMenuL)
        self.DoneText_2.setObjectName(u"DoneText_2")
        self.DoneText_2.setStyleSheet(u"background-color: rgba(255,255,255 0)")
        self.DoneText_2.setFrameShape(QFrame.Shape.NoFrame)
        self.DoneText_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.DoneText_2)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 10, 0, 10)
        self.TextDone = QLabel(self.DoneText_2)
        self.TextDone.setObjectName(u"TextDone")

        self.verticalLayout_27.addWidget(self.TextDone)


        self.verticalLayout_25.addWidget(self.DoneText_2)

        self.listWidget = QListWidget(self.DoneMenuL)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"background-color:rgba(255,255,255,0)")
        self.listWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout_25.addWidget(self.listWidget)


        self.verticalLayout_8.addWidget(self.DoneMenuL)

        self.AddTF_3 = QFrame(self.DoneMenu)
        self.AddTF_3.setObjectName(u"AddTF_3")
        self.AddTF_3.setStyleSheet(u"background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"                            stop: 0 #7442fc,   /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u043f\u0440\u0430\u0432\u0430 */\n"
"                            stop: 1 #a07dfd);  /* \u0421\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u043b\u0435\u0432\u0430 */\n"
"\n"
"padding: 2px 10px; \n"
"border-radius: 5px; \n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;\n"
"")
        self.AddTF_3.setFrameShape(QFrame.Shape.NoFrame)
        self.AddTF_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.AddTF_3)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.AddTB_3 = QPushButton(self.AddTF_3)
        self.AddTB_3.setObjectName(u"AddTB_3")
        self.AddTB_3.setStyleSheet(u"")

        self.verticalLayout_26.addWidget(self.AddTB_3)


        self.verticalLayout_8.addWidget(self.AddTF_3)


        self.horizontalLayout_2.addWidget(self.DoneMenu)

        self.Stat = QFrame(self.centraMenu)
        self.Stat.setObjectName(u"Stat")
        sizePolicy1.setHeightForWidth(self.Stat.sizePolicy().hasHeightForWidth())
        self.Stat.setSizePolicy(sizePolicy1)
        self.Stat.setMaximumSize(QSize(16777215, 16777215))
        self.Stat.setStyleSheet(u"")
        self.Stat.setFrameShape(QFrame.Shape.NoFrame)
        self.Stat.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Stat)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 0, 0, 0)
        self.HideStat = QFrame(self.Stat)
        self.HideStat.setObjectName(u"HideStat")
        self.HideStat.setStyleSheet(u"")
        self.HideStat.setFrameShape(QFrame.Shape.NoFrame)
        self.HideStat.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.HideStat)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 10, 0, 10)
        self.horizontalLayout_3.addWidget(self.HideStat)

        self.StatMenu = QFrame(self.Stat)
        self.StatMenu.setObjectName(u"StatMenu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.StatMenu.sizePolicy().hasHeightForWidth())
        self.StatMenu.setSizePolicy(sizePolicy2)
        self.StatMenu.setMaximumSize(QSize(16777215, 16777215))
        self.StatMenu.setStyleSheet(u"\n"
"padding: 2px 5px;\n"
"border-radius: 6px;\n"
"color: white;\n"
"font-weight: bold;\n"
"\n"
"\n"
"")
        self.StatMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.StatMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.StatMenu)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.DiagramAndStatMain = QFrame(self.StatMenu)
        self.DiagramAndStatMain.setObjectName(u"DiagramAndStatMain")
        sizePolicy1.setHeightForWidth(self.DiagramAndStatMain.sizePolicy().hasHeightForWidth())
        self.DiagramAndStatMain.setSizePolicy(sizePolicy1)
        self.DiagramAndStatMain.setStyleSheet(u"")
        self.DiagramAndStatMain.setFrameShape(QFrame.Shape.NoFrame)
        self.DiagramAndStatMain.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.DiagramAndStatMain)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.StatSub = QFrame(self.DiagramAndStatMain)
        self.StatSub.setObjectName(u"StatSub")
        sizePolicy1.setHeightForWidth(self.StatSub.sizePolicy().hasHeightForWidth())
        self.StatSub.setSizePolicy(sizePolicy1)
        self.StatSub.setMinimumSize(QSize(0, 0))
        self.StatSub.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.StatSub.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.StatSub.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.StatSub.setStyleSheet(u"background-color: rgba(255,255,255 0)")
        self.StatSub.setFrameShape(QFrame.Shape.NoFrame)
        self.StatSub.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.StatSub)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_6.setContentsMargins(0, 10, 0, 10)
        self.StatIcons = QFrame(self.StatSub)
        self.StatIcons.setObjectName(u"StatIcons")
        sizePolicy1.setHeightForWidth(self.StatIcons.sizePolicy().hasHeightForWidth())
        self.StatIcons.setSizePolicy(sizePolicy1)
        self.StatIcons.setStyleSheet(u"background-color: rgba(255,255,255 0)")
        self.StatIcons.setFrameShape(QFrame.Shape.NoFrame)
        self.StatIcons.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.StatIcons)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.TodoIcon = QLabel(self.StatIcons)
        self.TodoIcon.setObjectName(u"TodoIcon")
        sizePolicy1.setHeightForWidth(self.TodoIcon.sizePolicy().hasHeightForWidth())
        self.TodoIcon.setSizePolicy(sizePolicy1)
        self.TodoIcon.setPixmap(QPixmap(u":/icons/icons/align-justify (1).svg"))

        self.verticalLayout_14.addWidget(self.TodoIcon, 0, Qt.AlignmentFlag.AlignLeft)

        self.InProgressIcon = QLabel(self.StatIcons)
        self.InProgressIcon.setObjectName(u"InProgressIcon")
        self.InProgressIcon.setPixmap(QPixmap(u":/icons/icons/activity (1).svg"))

        self.verticalLayout_14.addWidget(self.InProgressIcon, 0, Qt.AlignmentFlag.AlignLeft)

        self.DoneIcon = QLabel(self.StatIcons)
        self.DoneIcon.setObjectName(u"DoneIcon")
        sizePolicy1.setHeightForWidth(self.DoneIcon.sizePolicy().hasHeightForWidth())
        self.DoneIcon.setSizePolicy(sizePolicy1)
        self.DoneIcon.setPixmap(QPixmap(u":/icons/icons/check-circle (1).svg"))

        self.verticalLayout_14.addWidget(self.DoneIcon, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout_6.addWidget(self.StatIcons)

        self.StatText = QFrame(self.StatSub)
        self.StatText.setObjectName(u"StatText")
        self.StatText.setFrameShape(QFrame.Shape.NoFrame)
        self.StatText.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.StatText)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.ToDoText = QLabel(self.StatText)
        self.ToDoText.setObjectName(u"ToDoText")

        self.verticalLayout_15.addWidget(self.ToDoText)

        self.InProgressText = QLabel(self.StatText)
        self.InProgressText.setObjectName(u"InProgressText")

        self.verticalLayout_15.addWidget(self.InProgressText)

        self.DoneText = QLabel(self.StatText)
        self.DoneText.setObjectName(u"DoneText")

        self.verticalLayout_15.addWidget(self.DoneText)


        self.horizontalLayout_6.addWidget(self.StatText, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout_4.addWidget(self.StatSub)

        self.DiagramMenu = QFrame(self.DiagramAndStatMain)
        self.DiagramMenu.setObjectName(u"DiagramMenu")
        self.DiagramMenu.setFrameShape(QFrame.Shape.NoFrame)
        self.DiagramMenu.setFrameShadow(QFrame.Shadow.Raised)
        self.DiagramMenu.setLineWidth(0)
        self.horizontalLayout_5 = QHBoxLayout(self.DiagramMenu)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.DiagramaStat = QFrame(self.DiagramMenu)
        self.DiagramaStat.setObjectName(u"DiagramaStat")
        self.DiagramaStat.setStyleSheet(u"background-color: rgba(255,255,255 0)")
        self.DiagramaStat.setFrameShape(QFrame.Shape.StyledPanel)
        self.DiagramaStat.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.DiagramaStat)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.income = QLabel(self.DiagramaStat)
        self.income.setObjectName(u"income")
        self.income.setPixmap(QPixmap(u":/icons/icons/arrow-up-circle.svg"))

        self.verticalLayout_12.addWidget(self.income)

        self.loss = QLabel(self.DiagramaStat)
        self.loss.setObjectName(u"loss")
        self.loss.setPixmap(QPixmap(u":/icons/icons/arrow-down-circle.svg"))

        self.verticalLayout_12.addWidget(self.loss)


        self.horizontalLayout_5.addWidget(self.DiagramaStat)

        self.DiagramSub = QFrame(self.DiagramMenu)
        self.DiagramSub.setObjectName(u"DiagramSub")
        self.DiagramSub.setStyleSheet(u"background-color: rgba(255,255,255 0)")
        self.DiagramSub.setFrameShape(QFrame.Shape.StyledPanel)
        self.DiagramSub.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.DiagramSub)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.DiagramSub)


        self.horizontalLayout_4.addWidget(self.DiagramMenu)


        self.verticalLayout_10.addWidget(self.DiagramAndStatMain)

        self.Time = QFrame(self.StatMenu)
        self.Time.setObjectName(u"Time")
        self.Time.setMaximumSize(QSize(16777215, 50))
        self.Time.setFrameShape(QFrame.Shape.StyledPanel)
        self.Time.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Time)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Clock = QLabel(self.Time)
        self.Clock.setObjectName(u"Clock")

        self.verticalLayout_11.addWidget(self.Clock)


        self.verticalLayout_10.addWidget(self.Time, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.StatMenu)


        self.horizontalLayout_2.addWidget(self.Stat)


        self.verticalLayout.addWidget(self.centraMenu)

        self.NotesAndFinance = QFrame(self.centralwidget)
        self.NotesAndFinance.setObjectName(u"NotesAndFinance")
        self.NotesAndFinance.setStyleSheet(u"padding: 2px 5px; \n"
"border-radius: 10px; \n"
"color: white;\n"
"font-weight: bold;\n"
"border: none;")
        self.NotesAndFinance.setFrameShape(QFrame.Shape.NoFrame)
        self.NotesAndFinance.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.NotesAndFinance)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.NotesMain = QWidget(self.NotesAndFinance)
        self.NotesMain.setObjectName(u"NotesMain")
        self.NotesMain.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 0.5);")
        self.verticalLayout_30 = QVBoxLayout(self.NotesMain)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 10)
        self.NotesSubF = QFrame(self.NotesMain)
        self.NotesSubF.setObjectName(u"NotesSubF")
        self.NotesSubF.setStyleSheet(u"border: 1px solid rgba(255, 255, 255, 0);")
        self.NotesSubF.setFrameShape(QFrame.Shape.NoFrame)
        self.NotesSubF.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.NotesSubF)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.NotesList = QTabWidget(self.NotesSubF)
        self.NotesList.setObjectName(u"NotesList")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.NotesList.sizePolicy().hasHeightForWidth())
        self.NotesList.setSizePolicy(sizePolicy3)
        font1 = QFont()
        font1.setFamilies([u"Caviar Dreams"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setKerning(False)
        self.NotesList.setFont(font1)
        self.NotesList.setStyleSheet(u"background-color: #172035")
        self.NotesList.setTabPosition(QTabWidget.TabPosition.North)
        self.NotesList.setTabShape(QTabWidget.TabShape.Rounded)
        self.NotesList.setElideMode(Qt.TextElideMode.ElideNone)
        self.NotesList.setUsesScrollButtons(True)
        self.NotesList.setDocumentMode(False)
        self.NotesList.setTabsClosable(True)
        self.NotesList.setMovable(True)
        self.NotesList.setTabBarAutoHide(False)
        self.note1 = QWidget()
        self.note1.setObjectName(u"note1")
        self.verticalLayout_32 = QVBoxLayout(self.note1)
        self.verticalLayout_32.setSpacing(0)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.verticalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.NotesText = QPlainTextEdit(self.note1)
        self.NotesText.setObjectName(u"NotesText")
        self.NotesText.setStyleSheet(u"")
        self.NotesText.setFrameShape(QFrame.Shape.NoFrame)
        self.NotesText.setFrameShadow(QFrame.Shadow.Plain)
        self.NotesText.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.NotesText.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.verticalLayout_32.addWidget(self.NotesText)

        self.NotesList.addTab(self.note1, "")

        self.verticalLayout_31.addWidget(self.NotesList)

        self.NotesAdd = QFrame(self.NotesSubF)
        self.NotesAdd.setObjectName(u"NotesAdd")
        self.NotesAdd.setFrameShape(QFrame.Shape.NoFrame)
        self.NotesAdd.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.NotesAdd)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.NotesAddBtn = QPushButton(self.NotesAdd)
        self.NotesAddBtn.setObjectName(u"NotesAddBtn")
        self.NotesAddBtn.setStyleSheet(u"background: qlineargradient(x1: 1, y1: 0, x2: 0, y2: 0,\n"
"                            stop: 0 #7442fc,   /* \u0422\u0435\u043c\u043d\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u043f\u0440\u0430\u0432\u0430 */\n"
"                            stop: 1 #a07dfd);  /* \u0421\u0432\u0435\u0442\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0441\u043b\u0435\u0432\u0430 */\n"
"")

        self.verticalLayout_33.addWidget(self.NotesAddBtn)


        self.verticalLayout_31.addWidget(self.NotesAdd)


        self.verticalLayout_30.addWidget(self.NotesSubF)


        self.horizontalLayout_7.addWidget(self.NotesMain)


        self.verticalLayout.addWidget(self.NotesAndFinance)

        self.UnderMenu = QWidget(self.centralwidget)
        self.UnderMenu.setObjectName(u"UnderMenu")
        self.UnderMenu.setMaximumSize(QSize(16777215, 100))
        self.verticalLayout_2 = QVBoxLayout(self.UnderMenu)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.UnderSubMenu = QWidget(self.UnderMenu)
        self.UnderSubMenu.setObjectName(u"UnderSubMenu")
        self.UnderSubMenu.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.UnderSubMenu)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.TodoF = QFrame(self.UnderSubMenu)
        self.TodoF.setObjectName(u"TodoF")
        self.TodoF.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.TodoF.setAutoFillBackground(False)
        self.TodoF.setStyleSheet(u"")
        self.TodoF.setFrameShape(QFrame.Shape.NoFrame)
        self.TodoF.setFrameShadow(QFrame.Shadow.Sunken)
        self.TodoF.setLineWidth(0)
        self.TodoF.setMidLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.TodoF)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.Todobtn = QPushButton(self.TodoF)
        self.Todobtn.setObjectName(u"Todobtn")
        self.Todobtn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/feather/check-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Todobtn.setIcon(icon3)

        self.verticalLayout_3.addWidget(self.Todobtn)


        self.horizontalLayout.addWidget(self.TodoF, 0, Qt.AlignmentFlag.AlignBottom)

        self.InProgF = QFrame(self.UnderSubMenu)
        self.InProgF.setObjectName(u"InProgF")
        self.InProgF.setStyleSheet(u"")
        self.InProgF.setFrameShape(QFrame.Shape.NoFrame)
        self.InProgF.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.InProgF)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.Inprogressbtn = QPushButton(self.InProgF)
        self.Inprogressbtn.setObjectName(u"Inprogressbtn")
        self.Inprogressbtn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/Icons/feather/alert-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Inprogressbtn.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.Inprogressbtn)


        self.horizontalLayout.addWidget(self.InProgF, 0, Qt.AlignmentFlag.AlignBottom)

        self.DoneF = QFrame(self.UnderSubMenu)
        self.DoneF.setObjectName(u"DoneF")
        self.DoneF.setStyleSheet(u"")
        self.DoneF.setFrameShape(QFrame.Shape.NoFrame)
        self.DoneF.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.DoneF)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.Donebtn = QPushButton(self.DoneF)
        self.Donebtn.setObjectName(u"Donebtn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Donebtn.sizePolicy().hasHeightForWidth())
        self.Donebtn.setSizePolicy(sizePolicy4)
        icon5 = QIcon()
        icon5.addFile(u":/Icons/feather/archive.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.Donebtn.setIcon(icon5)

        self.verticalLayout_5.addWidget(self.Donebtn)


        self.horizontalLayout.addWidget(self.DoneF)

        self.Notes = QFrame(self.UnderSubMenu)
        self.Notes.setObjectName(u"Notes")
        self.Notes.setStyleSheet(u"")
        self.Notes.setFrameShape(QFrame.Shape.NoFrame)
        self.Notes.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Notes)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.NotesBtn = QPushButton(self.Notes)
        self.NotesBtn.setObjectName(u"NotesBtn")
        self.NotesBtn.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/Icons/feather/file-text.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.NotesBtn.setIcon(icon6)

        self.verticalLayout_9.addWidget(self.NotesBtn)


        self.horizontalLayout.addWidget(self.Notes)


        self.verticalLayout_2.addWidget(self.UnderSubMenu)


        self.verticalLayout.addWidget(self.UnderMenu)

        MainWindow.setCentralWidget(self.centralwidget)
        self.mainBody.raise_()
        self.UnderMenu.raise_()
        self.centraMenu.raise_()
        self.NotesAndFinance.raise_()
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        self.NotesList.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.SettingsBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.LogBtn.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.TextTodo.setText(QCoreApplication.translate("MainWindow", u"To Do", None))
        self.AddTB.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        self.InProgressText_2.setText(QCoreApplication.translate("MainWindow", u"In Progress", None))
        self.AddTB_2.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        self.TextDone.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.AddTB_3.setText(QCoreApplication.translate("MainWindow", u"+ Add a card", None))
        self.TodoIcon.setText("")
        self.InProgressIcon.setText("")
        self.DoneIcon.setText("")
        self.ToDoText.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.InProgressText.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.DoneText.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.income.setText("")
        self.loss.setText("")
        self.Clock.setText(QCoreApplication.translate("MainWindow", u"21.02.2004 13.54", None))
        self.NotesText.setPlainText("")
        self.NotesList.setTabText(self.NotesList.indexOf(self.note1), QCoreApplication.translate("MainWindow", u"First note", None))
        self.NotesAddBtn.setText(QCoreApplication.translate("MainWindow", u"+ Add Note", None))
        self.Todobtn.setText(QCoreApplication.translate("MainWindow", u"To-Do", None))
        self.Inprogressbtn.setText(QCoreApplication.translate("MainWindow", u"In progress", None))
        self.Donebtn.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.NotesBtn.setText(QCoreApplication.translate("MainWindow", u"Notes", None))
    # retranslateUi

