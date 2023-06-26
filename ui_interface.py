# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceDznBVF.ui'
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
        MainWindow.resize(1309, 877)
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
        self.verticalLayout_3 = QVBoxLayout(self.main_body)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.main_body)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.frame_21 = QFrame(self.frame)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_21)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_3 = QFrame(self.frame_21)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(80, 0))
        self.label_8.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_15.addWidget(self.label_8)

        self.comboBox_18 = QComboBox(self.frame_5)
        self.comboBox_18.addItem("")
        self.comboBox_18.setObjectName(u"comboBox_18")
        self.comboBox_18.setMinimumSize(QSize(0, 40))
        self.comboBox_18.setMaximumSize(QSize(16777215, 40))
        self.comboBox_18.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);\n"
"")

        self.horizontalLayout_15.addWidget(self.comboBox_18)


        self.verticalLayout_2.addWidget(self.frame_5)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(80, 0))
        self.label_13.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_16.addWidget(self.label_13)

        self.comboBox_19 = QComboBox(self.frame_9)
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")
        self.comboBox_19.setMinimumSize(QSize(0, 40))
        self.comboBox_19.setMaximumSize(QSize(16777215, 40))
        self.comboBox_19.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_16.addWidget(self.comboBox_19)


        self.verticalLayout_2.addWidget(self.frame_9)

        self.frame_19 = QFrame(self.frame_4)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_24 = QLabel(self.frame_19)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(80, 0))
        self.label_24.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_17.addWidget(self.label_24)

        self.comboBox_20 = QComboBox(self.frame_19)
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setMinimumSize(QSize(0, 40))
        self.comboBox_20.setMaximumSize(QSize(16777215, 40))
        self.comboBox_20.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_17.addWidget(self.comboBox_20)


        self.verticalLayout_2.addWidget(self.frame_19)


        self.horizontalLayout_6.addWidget(self.frame_4)

        self.frame_20 = QFrame(self.frame_3)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_14 = QLabel(self.frame_22)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(80, 0))
        self.label_14.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_18.addWidget(self.label_14)

        self.comboBox_21 = QComboBox(self.frame_22)
        self.comboBox_21.addItem("")
        self.comboBox_21.addItem("")
        self.comboBox_21.setObjectName(u"comboBox_21")
        self.comboBox_21.setMinimumSize(QSize(0, 40))
        self.comboBox_21.setMaximumSize(QSize(16777215, 40))
        self.comboBox_21.setSizeIncrement(QSize(0, 0))
        self.comboBox_21.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_18.addWidget(self.comboBox_21)


        self.verticalLayout_9.addWidget(self.frame_22)

        self.frame_23 = QFrame(self.frame_20)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_17 = QLabel(self.frame_23)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(80, 0))
        self.label_17.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_19.addWidget(self.label_17)

        self.keyCapcha_2 = QLineEdit(self.frame_23)
        self.keyCapcha_2.setObjectName(u"keyCapcha_2")
        self.keyCapcha_2.setMinimumSize(QSize(0, 40))
        self.keyCapcha_2.setMaximumSize(QSize(16777215, 40))
        self.keyCapcha_2.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_19.addWidget(self.keyCapcha_2)


        self.verticalLayout_9.addWidget(self.frame_23)

        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_15 = QLabel(self.frame_24)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(80, 0))
        self.label_15.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_20.addWidget(self.label_15)

        self.comboBox_22 = QComboBox(self.frame_24)
        self.comboBox_22.addItem("")
        self.comboBox_22.setObjectName(u"comboBox_22")
        self.comboBox_22.setMinimumSize(QSize(0, 40))
        self.comboBox_22.setMaximumSize(QSize(16777215, 40))
        self.comboBox_22.setSizeIncrement(QSize(0, 0))
        self.comboBox_22.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_20.addWidget(self.comboBox_22)


        self.verticalLayout_9.addWidget(self.frame_24)


        self.horizontalLayout_6.addWidget(self.frame_20)

        self.frame_25 = QFrame(self.frame_3)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_25)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_18 = QLabel(self.frame_26)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(80, 0))
        self.label_18.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_21.addWidget(self.label_18)

        self.comboBox_23 = QComboBox(self.frame_26)
        self.comboBox_23.addItem("")
        self.comboBox_23.setObjectName(u"comboBox_23")
        self.comboBox_23.setMinimumSize(QSize(0, 40))
        self.comboBox_23.setMaximumSize(QSize(16777215, 40))
        self.comboBox_23.setSizeIncrement(QSize(30, 0))
        self.comboBox_23.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_21.addWidget(self.comboBox_23)


        self.verticalLayout_10.addWidget(self.frame_26)

        self.frame_27 = QFrame(self.frame_25)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_20 = QLabel(self.frame_27)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(80, 0))
        self.label_20.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_22.addWidget(self.label_20)

        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.radioButton_10 = QRadioButton(self.frame_28)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setChecked(True)

        self.horizontalLayout_23.addWidget(self.radioButton_10)


        self.horizontalLayout_22.addWidget(self.frame_28)


        self.verticalLayout_10.addWidget(self.frame_27)

        self.frame_29 = QFrame(self.frame_25)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_25 = QLabel(self.frame_29)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(80, 0))
        self.label_25.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_24.addWidget(self.label_25)

        self.keyOtp = QLineEdit(self.frame_29)
        self.keyOtp.setObjectName(u"keyOtp")
        self.keyOtp.setMinimumSize(QSize(0, 40))
        self.keyOtp.setMaximumSize(QSize(16777215, 40))
        self.keyOtp.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_24.addWidget(self.keyOtp)


        self.verticalLayout_10.addWidget(self.frame_29)


        self.horizontalLayout_6.addWidget(self.frame_25)

        self.frame_30 = QFrame(self.frame_3)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_30)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_31 = QFrame(self.frame_30)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_19 = QLabel(self.frame_31)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(80, 0))
        self.label_19.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_25.addWidget(self.label_19)

        self.comboBox_24 = QComboBox(self.frame_31)
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.addItem("")
        self.comboBox_24.setObjectName(u"comboBox_24")
        self.comboBox_24.setMinimumSize(QSize(0, 40))
        self.comboBox_24.setMaximumSize(QSize(16777215, 40))
        self.comboBox_24.setSizeIncrement(QSize(0, 0))
        self.comboBox_24.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_25.addWidget(self.comboBox_24)


        self.verticalLayout_11.addWidget(self.frame_31)

        self.frame_32 = QFrame(self.frame_30)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_26 = QLabel(self.frame_32)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(80, 0))
        self.label_26.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_26.addWidget(self.label_26)

        self.comboBox_25 = QComboBox(self.frame_32)
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.addItem("")
        self.comboBox_25.setObjectName(u"comboBox_25")
        self.comboBox_25.setMinimumSize(QSize(0, 40))
        self.comboBox_25.setMaximumSize(QSize(16777215, 40))
        self.comboBox_25.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_26.addWidget(self.comboBox_25)


        self.verticalLayout_11.addWidget(self.frame_32)

        self.frame_33 = QFrame(self.frame_30)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_27 = QLabel(self.frame_33)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(80, 0))
        self.label_27.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_27.addWidget(self.label_27)

        self.comboBox_26 = QComboBox(self.frame_33)
        self.comboBox_26.addItem("")
        self.comboBox_26.addItem("")
        self.comboBox_26.setObjectName(u"comboBox_26")
        self.comboBox_26.setMinimumSize(QSize(0, 40))
        self.comboBox_26.setMaximumSize(QSize(16777215, 40))
        self.comboBox_26.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_27.addWidget(self.comboBox_26)


        self.verticalLayout_11.addWidget(self.frame_33)


        self.horizontalLayout_6.addWidget(self.frame_30)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.frame_34 = QFrame(self.frame_21)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.pushButton_3 = QPushButton(self.frame_34)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(120, 0))
        self.pushButton_3.setMaximumSize(QSize(120, 16777215))
        self.pushButton_3.setStyleSheet(u"text-align: left;")
        icon = QIcon()
        icon.addFile(u":/icons/icons/calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.pushButton_3)

        self.num_threads = QSpinBox(self.frame_34)
        self.num_threads.setObjectName(u"num_threads")
        self.num_threads.setMinimumSize(QSize(113, 40))
        self.num_threads.setMaximumSize(QSize(113, 16777215))
        self.num_threads.setSizeIncrement(QSize(0, 40))
        self.num_threads.setStyleSheet(u"\n"
"background-color: rgba(225,231,250,255);\n"
"color: rgb(0, 0, 0);")
        self.num_threads.setMaximum(999)
        self.num_threads.setValue(2)

        self.horizontalLayout_28.addWidget(self.num_threads)

        self.pushButton_4 = QPushButton(self.frame_34)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(113, 0))
        self.pushButton_4.setMaximumSize(QSize(113, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/clock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.pushButton_4)

        self.delay_time = QSpinBox(self.frame_34)
        self.delay_time.setObjectName(u"delay_time")
        self.delay_time.setMinimumSize(QSize(113, 40))
        self.delay_time.setMaximumSize(QSize(113, 16777215))
        self.delay_time.setSizeIncrement(QSize(0, 40))
        self.delay_time.setStyleSheet(u"color:rgb(0,0,0);\n"
"background-color: rgba(225,231,250,255);\n"
"")
        self.delay_time.setMaximum(999999999)
        self.delay_time.setValue(0)

        self.horizontalLayout_28.addWidget(self.delay_time)

        self.start_button = QPushButton(self.frame_34)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(113, 40))
        self.start_button.setMaximumSize(QSize(113, 16777215))
        self.start_button.setStyleSheet(u"background-color: rgba(85, 0, 255, 240);\n"
"color: rgb(255, 255, 255);\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_button.setIcon(icon2)
        self.start_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.start_button)

        self.stop_button = QPushButton(self.frame_34)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setMinimumSize(QSize(113, 40))
        self.stop_button.setMaximumSize(QSize(113, 16777215))
        self.stop_button.setStyleSheet(u"background-color: rgb(255, 99, 102);\n"
"color: rgb(255, 255, 255);\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_button.setIcon(icon3)
        self.stop_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.stop_button)

        self.pushButton_5 = QPushButton(self.frame_34)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(113, 0))
        self.pushButton_5.setMaximumSize(QSize(113, 16777215))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.pushButton_5)

        self.label_3 = QLabel(self.frame_34)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 0))
        self.label_3.setMaximumSize(QSize(30, 16777215))
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_28.addWidget(self.label_3)

        self.pushButton_6 = QPushButton(self.frame_34)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(113, 0))
        self.pushButton_6.setMaximumSize(QSize(113, 16777215))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.pushButton_6)

        self.label_28 = QLabel(self.frame_34)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMinimumSize(QSize(30, 0))
        self.label_28.setMaximumSize(QSize(30, 16777215))
        self.label_28.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_28.addWidget(self.label_28)

        self.label_2 = QLabel(self.frame_34)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(113, 0))
        self.label_2.setMaximumSize(QSize(113, 16777215))

        self.horizontalLayout_28.addWidget(self.label_2)


        self.verticalLayout_8.addWidget(self.frame_34)


        self.verticalLayout_12.addWidget(self.frame_21)


        self.verticalLayout_3.addWidget(self.frame)

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

        self.verticalLayout_3.addWidget(self.tableWidget)


        self.horizontalLayout.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ki\u1ec3u XMDT", None))
        self.comboBox_18.setItemText(0, QCoreApplication.translate("MainWindow", u"XMDT th\u1eb3ng ", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn ph\u00f4i", None))
        self.comboBox_19.setItemText(0, QCoreApplication.translate("MainWindow", u"L\u1ea5y ph\u00f4i \u1edf tool(C\u00f3 fake th\u00f4ng tin theo Via)", None))
        self.comboBox_19.setItemText(1, QCoreApplication.translate("MainWindow", u"T\u1ea3i l\u00ean ph\u00f4i(Ch\u1ec9nh s\u1eeda ph\u00f4i t\u1ef1 \u0111\u1ed9ng)", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u1ea2nh \u1edf ph\u00f4i", None))
        self.comboBox_20.setItemText(0, QCoreApplication.translate("MainWindow", u"T\u1ea3i online", None))
        self.comboBox_20.setItemText(1, QCoreApplication.translate("MainWindow", u"D\u00f9ng \u1ea3nh c\u00f3 s\u1eb5n", None))

        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Up Avatar:", None))
        self.comboBox_21.setItemText(0, QCoreApplication.translate("MainWindow", u"C\u00f3", None))
        self.comboBox_21.setItemText(1, QCoreApplication.translate("MainWindow", u"Kh\u00f4ng", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Key:", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Capcha:", None))
        self.comboBox_22.setItemText(0, QCoreApplication.translate("MainWindow", u"Anycapcha", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Nh\u00e0 m\u1ea1ng:", None))
        self.comboBox_23.setItemText(0, QCoreApplication.translate("MainWindow", u"T\u1ea5t c\u1ea3", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"OTP Phone:", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"Viotp.com", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Key OTP:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Get s\u1ed1, mail:", None))
        self.comboBox_24.setItemText(0, QCoreApplication.translate("MainWindow", u"1 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))
        self.comboBox_24.setItemText(1, QCoreApplication.translate("MainWindow", u"2 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))
        self.comboBox_24.setItemText(2, QCoreApplication.translate("MainWindow", u"3 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))
        self.comboBox_24.setItemText(3, QCoreApplication.translate("MainWindow", u"4 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))
        self.comboBox_24.setItemText(4, QCoreApplication.translate("MainWindow", u"5 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))

        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.comboBox_25.setItemText(0, QCoreApplication.translate("MainWindow", u"https://mbasic.facebook.com/", None))
        self.comboBox_25.setItemText(1, QCoreApplication.translate("MainWindow", u"https://m.facebook.com/", None))
        self.comboBox_25.setItemText(2, QCoreApplication.translate("MainWindow", u"https://www.facebook.com/", None))

        self.label_27.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.comboBox_26.setItemText(0, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_26.setItemText(1, QCoreApplication.translate("MainWindow", u"Proxy-Shoplike", None))

        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Lu\u1ed3ng ch\u1ea1y", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"B\u1eaft \u0111\u1ea7u", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"T\u1ea1m d\u1eebng", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"T\u1ea5t c\u1ea3:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0110\u00e3 ch\u1ecdn", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HSD: V\u0129nh vi\u1ec5n", None))
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
    # retranslateUi

