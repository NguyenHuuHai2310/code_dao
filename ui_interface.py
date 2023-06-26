# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceDQlQtc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1245, 898)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #ffffff;\n"
"}\n"
"#header{\n"
"background-color: #ffffff;\n"
"	color: rgb(255, 250, 235);\n"
"}\n"
"#side_menu{\n"
"	background-color: #fffaeb;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: #fffaeb;\n"
"	border-radius: 5px;\n"
"color: rgb(0,0,0);\n"
"\n"
"}\n"
"QComboBox{\n"
"	padding: 10px;\n"
"	background-color: #ffffff;\n"
"	border-radius: 5px;\n"
"	color: rgb(0,0,0);\n"
"\n"
"}\n"
"#main_body{\n"
"	background-color: #fffaeb;\n"
"	border-radius: 10px;\n"
"}\n"
"#pushButton_view{\n"
"	text-align: left;\n"
"}\n"
"#pushButton_contact{\n"
"	text-align: left;\n"
"}\n"
"#pushButton_config{\n"
"	text-align: left;\n"
"}\n"
"#comboBox{\n"
"	text-align: left;\n"
"}\n"
"#pushButton_xmdt{\n"
"	text-align: left;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_body = QFrame(self.frame_2)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.main_body)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 20):
            self.tableWidget.setRowCount(20)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, __qtablewidgetitem25)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 299, 1231, 581))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(0, 300))
        self.tableWidget.setStyleSheet(u"background-color: #ffffff;\n"
"color: rgb(0,0,0);\n"
"border-color: rgb(0, 0, 0);")
        self.tableWidget.setFrameShape(QFrame.Box)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.tableWidget.setDefaultDropAction(Qt.IgnoreAction)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(10)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.frame = QFrame(self.main_body)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1231, 291))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.comboBox_15 = QComboBox(self.frame)
        self.comboBox_15.addItem("")
        self.comboBox_15.setObjectName(u"comboBox_15")
        self.comboBox_15.setGeometry(QRect(520, 100, 141, 40))
        self.comboBox_15.setMinimumSize(QSize(0, 40))
        self.comboBox_15.setMaximumSize(QSize(16777215, 40))
        self.comboBox_15.setSizeIncrement(QSize(30, 0))
        self.comboBox_15.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 60, 67, 17))
        self.comboBox_7 = QComboBox(self.frame)
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(120, 0, 281, 40))
        self.comboBox_7.setMinimumSize(QSize(0, 40))
        self.comboBox_7.setMaximumSize(QSize(16777215, 40))
        self.comboBox_7.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);\n"
"")
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(420, 110, 81, 17))
        self.comboBox_12 = QComboBox(self.frame)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setGeometry(QRect(520, 0, 301, 40))
        self.comboBox_12.setMinimumSize(QSize(0, 40))
        self.comboBox_12.setMaximumSize(QSize(16777215, 40))
        self.comboBox_12.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.comboBox_19 = QComboBox(self.frame)
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")
        self.comboBox_19.setGeometry(QRect(520, 150, 301, 40))
        self.comboBox_19.setMinimumSize(QSize(0, 40))
        self.comboBox_19.setMaximumSize(QSize(350, 40))
        self.comboBox_19.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(670, 110, 71, 17))
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(670, 60, 31, 17))
        self.comboBox_11 = QComboBox(self.frame)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setGeometry(QRect(930, 0, 271, 40))
        self.comboBox_11.setMinimumSize(QSize(0, 40))
        self.comboBox_11.setMaximumSize(QSize(16777215, 40))
        self.comboBox_11.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.frame_14 = QFrame(self.frame)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(120, 100, 281, 40))
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.radioButton_9 = QRadioButton(self.frame_14)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setChecked(True)

        self.horizontalLayout_10.addWidget(self.radioButton_9)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 110, 81, 17))
        self.comboBox_8 = QComboBox(self.frame)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setGeometry(QRect(120, 50, 281, 40))
        self.comboBox_8.setMinimumSize(QSize(0, 40))
        self.comboBox_8.setMaximumSize(QSize(16777215, 40))
        self.comboBox_8.setSizeIncrement(QSize(0, 0))
        self.comboBox_8.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.keyCapcha = QLineEdit(self.frame)
        self.keyCapcha.setObjectName(u"keyCapcha")
        self.keyCapcha.setGeometry(QRect(740, 50, 461, 40))
        self.keyCapcha.setMinimumSize(QSize(0, 40))
        self.keyCapcha.setMaximumSize(QSize(16777215, 40))
        self.keyCapcha.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 160, 81, 17))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(420, 10, 81, 17))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 10, 81, 17))
        self.comboBox_16 = QComboBox(self.frame)
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.setObjectName(u"comboBox_16")
        self.comboBox_16.setGeometry(QRect(120, 150, 281, 40))
        self.comboBox_16.setMinimumSize(QSize(0, 40))
        self.comboBox_16.setMaximumSize(QSize(16777215, 40))
        self.comboBox_16.setSizeIncrement(QSize(0, 0))
        self.comboBox_16.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(430, 140, 20, 53))
        self.label_23.setMinimumSize(QSize(20, 0))
        self.label_23.setMaximumSize(QSize(20, 16777215))
        self.keyOtp = QLineEdit(self.frame)
        self.keyOtp.setObjectName(u"keyOtp")
        self.keyOtp.setGeometry(QRect(740, 100, 461, 40))
        self.keyOtp.setMinimumSize(QSize(0, 40))
        self.keyOtp.setMaximumSize(QSize(16777215, 40))
        self.keyOtp.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(840, 10, 91, 17))
        self.comboBox_10 = QComboBox(self.frame)
        self.comboBox_10.addItem("")
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setGeometry(QRect(520, 50, 141, 40))
        self.comboBox_10.setMinimumSize(QSize(0, 40))
        self.comboBox_10.setMaximumSize(QSize(16777215, 40))
        self.comboBox_10.setSizeIncrement(QSize(0, 0))
        self.comboBox_10.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(420, 60, 67, 17))
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 210, 1201, 71))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(734, 20, 90, 41))
        icon = QIcon()
        icon.addFile(u":/icons/icons/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(24, 24))
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(248, 22, 91, 41))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/clock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(24, 24))
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(970, 20, 31, 41))
        self.label_8.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(-2, 22, 131, 41))
        self.pushButton_3.setStyleSheet(u"text-align: left;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(24, 24))
        self.stop_button = QPushButton(self.frame_3)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(618, 22, 111, 40))
        self.stop_button.setMinimumSize(QSize(0, 40))
        self.stop_button.setStyleSheet(u"background-color: rgb(255, 99, 102);\n"
"color: rgb(255, 255, 255);\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_button.setIcon(icon3)
        self.stop_button.setIconSize(QSize(24, 24))
        self.delay_time = QSpinBox(self.frame_3)
        self.delay_time.setObjectName(u"delay_time")
        self.delay_time.setGeometry(QRect(378, 22, 81, 40))
        self.delay_time.setMinimumSize(QSize(20, 40))
        self.delay_time.setMaximumSize(QSize(150, 16777215))
        self.delay_time.setSizeIncrement(QSize(0, 40))
        self.delay_time.setStyleSheet(u"color:rgb(0,0,0);\n"
"background-color: rgba(225,231,250,255);\n"
"")
        self.delay_time.setMaximum(999999999)
        self.delay_time.setValue(0)
        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(869, 19, 91, 44))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QSize(24, 24))
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(1048, 32, 121, 20))
        self.start_button = QPushButton(self.frame_3)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(488, 22, 121, 40))
        self.start_button.setMinimumSize(QSize(0, 40))
        self.start_button.setStyleSheet(u"background-color: rgba(85, 0, 255, 240);\n"
"color: rgb(255, 255, 255);\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_button.setIcon(icon5)
        self.start_button.setIconSize(QSize(24, 24))
        self.num_threads = QSpinBox(self.frame_3)
        self.num_threads.setObjectName(u"num_threads")
        self.num_threads.setGeometry(QRect(128, 22, 81, 40))
        self.num_threads.setMinimumSize(QSize(20, 40))
        self.num_threads.setMaximumSize(QSize(150, 16777215))
        self.num_threads.setSizeIncrement(QSize(0, 40))
        self.num_threads.setStyleSheet(u"\n"
"background-color: rgba(225,231,250,255);\n"
"color: rgb(0, 0, 0);")
        self.num_threads.setMaximum(999)
        self.num_threads.setValue(2)
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(830, 20, 34, 41))
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.comboBox_21 = QComboBox(self.frame)
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")
        self.comboBox_21.setGeometry(QRect(940, 150, 261, 40))
        self.comboBox_21.setMinimumSize(QSize(0, 40))
        self.comboBox_21.setMaximumSize(QSize(16777215, 40))
        self.comboBox_21.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.label_25 = QLabel(self.frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(850, 152, 50, 41))
        self.label_25.setMinimumSize(QSize(40, 0))
        self.label_25.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"@T\u00e0i kho\u1ea3n[Id|Pw|2Fa]", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"@Cookie", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"@Ip", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"@Tr\u1ea1ng th\u00e1i", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"@Limit", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        self.comboBox_15.setItemText(0, QCoreApplication.translate("MainWindow", u"T\u1ea5t c\u1ea3", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Up Avatar:", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"XMDT th\u1eb3ng ", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nh\u00e0 m\u1ea1ng:", None))
        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"L\u1ea5y ph\u00f4i \u1edf tool(C\u00f3 fake th\u00f4ng tin theo Via)", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"T\u1ea3i l\u00ean ph\u00f4i(Ch\u1ec9nh s\u1eeda ph\u00f4i t\u1ef1 \u0111\u1ed9ng)", None))

        self.comboBox_19.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_19.setItemText(1, QCoreApplication.translate("MainWindow", u"Proxy-Shoplike", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Key OTP:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Key:", None))
        self.comboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"T\u1ea3i online", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"D\u00f9ng \u1ea3nh c\u00f3 s\u1eb5n", None))

        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"Viotp.com", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"OTP Phone:", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"C\u00f3", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"Kh\u00f4ng", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Get s\u1ed1, mail:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn ph\u00f4i", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ki\u1ec3u XMDT", None))
        self.comboBox_16.setItemText(0, QCoreApplication.translate("MainWindow", u"1 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))
        self.comboBox_16.setItemText(1, QCoreApplication.translate("MainWindow", u"2 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))
        self.comboBox_16.setItemText(2, QCoreApplication.translate("MainWindow", u"3 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))
        self.comboBox_16.setItemText(3, QCoreApplication.translate("MainWindow", u"4 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))
        self.comboBox_16.setItemText(4, QCoreApplication.translate("MainWindow", u"5 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))

        self.label_23.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u1ea2nh \u1edf ph\u00f4i", None))
        self.comboBox_10.setItemText(0, QCoreApplication.translate("MainWindow", u"Anycapcha", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Capcha:", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"T\u1ea5t c\u1ea3:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Lu\u1ed3ng ch\u1ea1y", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"T\u1ea1m d\u1eebng", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0110\u00e3 ch\u1ecdn", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HSD: V\u0129nh vi\u1ec5n", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"B\u1eaft \u0111\u1ea7u", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_21.setItemText(0, QCoreApplication.translate("MainWindow", u"https://mbasic.facebook.com/", None))
        self.comboBox_21.setItemText(1, QCoreApplication.translate("MainWindow", u"https://m.facebook.com/", None))
        self.comboBox_21.setItemText(2, QCoreApplication.translate("MainWindow", u"https://www.facebook.com/", None))

        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Login", None))
    # retranslateUi

