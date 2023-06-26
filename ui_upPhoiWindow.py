# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upPhoiWindowcfXmWS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_UpPhoiWindow(object):
    def setupUi(self, UpPhoiWindow):
        if not UpPhoiWindow.objectName():
            UpPhoiWindow.setObjectName(u"UpPhoiWindow")
        UpPhoiWindow.resize(1070, 917)
        UpPhoiWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(UpPhoiWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(420, 16777215))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_4.addWidget(self.label_3)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_5.addWidget(self.label_4)

        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.spinBox = QSpinBox(self.frame_12)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox.setMaximum(99999999)

        self.horizontalLayout_3.addWidget(self.spinBox)

        self.label_9 = QLabel(self.frame_12)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(20, 16777215))
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_3.addWidget(self.label_9, 0, Qt.AlignHCenter)

        self.spinBox_2 = QSpinBox(self.frame_12)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_2.setMaximum(999999)

        self.horizontalLayout_3.addWidget(self.spinBox_2)


        self.verticalLayout_5.addWidget(self.frame_12)


        self.verticalLayout_4.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_11)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.frame_11)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_6.addWidget(self.label_5)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.spinBox_3 = QSpinBox(self.frame_13)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_3.setMaximum(999999)

        self.horizontalLayout_4.addWidget(self.spinBox_3)

        self.label_10 = QLabel(self.frame_13)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_4.addWidget(self.label_10, 0, Qt.AlignHCenter)

        self.spinBox_4 = QSpinBox(self.frame_13)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_4.setMaximum(999999)

        self.horizontalLayout_4.addWidget(self.spinBox_4)

        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_4.addWidget(self.label_11, 0, Qt.AlignHCenter)

        self.spinBox_5 = QSpinBox(self.frame_13)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_5.setMinimum(-360)
        self.spinBox_5.setMaximum(360)

        self.horizontalLayout_4.addWidget(self.spinBox_5)


        self.verticalLayout_6.addWidget(self.frame_13)


        self.verticalLayout_4.addWidget(self.frame_11)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_31 = QLabel(self.frame_8)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMaximumSize(QSize(16777215, 20))
        self.label_31.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_7.addWidget(self.label_31)

        self.frame_14 = QFrame(self.frame_8)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_32 = QLabel(self.frame_14)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(16777215, 16777215))
        self.label_32.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_5.addWidget(self.label_32)

        self.comboBox_2 = QComboBox(self.frame_14)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"background-color: #d6d5d1;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_5.addWidget(self.comboBox_2)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_8)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_33 = QLabel(self.frame_15)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_6.addWidget(self.label_33)

        self.comboBox_3 = QComboBox(self.frame_15)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"background-color: #d6d5d1;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_6.addWidget(self.comboBox_3)


        self.verticalLayout_7.addWidget(self.frame_15)


        self.verticalLayout_2.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 20))
        self.label_15.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_8.addWidget(self.label_15)

        self.frame_18 = QFrame(self.frame_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(60, 0))
        self.label_20.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_7.addWidget(self.label_20)

        self.spinBox_23 = QSpinBox(self.frame_18)
        self.spinBox_23.setObjectName(u"spinBox_23")
        self.spinBox_23.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_23.setMaximum(9999999)

        self.horizontalLayout_7.addWidget(self.spinBox_23)

        self.label_29 = QLabel(self.frame_18)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_7.addWidget(self.label_29)

        self.spinBox_25 = QSpinBox(self.frame_18)
        self.spinBox_25.setObjectName(u"spinBox_25")
        self.spinBox_25.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_25.setMaximum(9999999)

        self.horizontalLayout_7.addWidget(self.spinBox_25)

        self.label_30 = QLabel(self.frame_18)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_7.addWidget(self.label_30, 0, Qt.AlignHCenter)

        self.spinBox_24 = QSpinBox(self.frame_18)
        self.spinBox_24.setObjectName(u"spinBox_24")
        self.spinBox_24.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_24.setMinimum(-360)
        self.spinBox_24.setMaximum(360)

        self.horizontalLayout_7.addWidget(self.spinBox_24)


        self.verticalLayout_8.addWidget(self.frame_18)

        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_16 = QLabel(self.frame_16)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(60, 0))
        self.label_16.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_8.addWidget(self.label_16)

        self.spinBox_15 = QSpinBox(self.frame_16)
        self.spinBox_15.setObjectName(u"spinBox_15")
        self.spinBox_15.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_15.setMaximum(9999999)

        self.horizontalLayout_8.addWidget(self.spinBox_15)

        self.label_24 = QLabel(self.frame_16)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_8.addWidget(self.label_24, 0, Qt.AlignHCenter)

        self.spinBox_14 = QSpinBox(self.frame_16)
        self.spinBox_14.setObjectName(u"spinBox_14")
        self.spinBox_14.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_14.setMaximum(9999999)

        self.horizontalLayout_8.addWidget(self.spinBox_14)

        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_8.addWidget(self.label_23, 0, Qt.AlignHCenter)

        self.spinBox_16 = QSpinBox(self.frame_16)
        self.spinBox_16.setObjectName(u"spinBox_16")
        self.spinBox_16.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_16.setMinimum(-360)
        self.spinBox_16.setMaximum(360)

        self.horizontalLayout_8.addWidget(self.spinBox_16)


        self.verticalLayout_8.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_17 = QLabel(self.frame_17)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(60, 0))
        self.label_17.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_9.addWidget(self.label_17)

        self.spinBox_18 = QSpinBox(self.frame_17)
        self.spinBox_18.setObjectName(u"spinBox_18")
        self.spinBox_18.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_18.setMaximum(9999999)

        self.horizontalLayout_9.addWidget(self.spinBox_18)

        self.label_26 = QLabel(self.frame_17)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_9.addWidget(self.label_26)

        self.spinBox_17 = QSpinBox(self.frame_17)
        self.spinBox_17.setObjectName(u"spinBox_17")
        self.spinBox_17.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_17.setMaximum(9999999)

        self.horizontalLayout_9.addWidget(self.spinBox_17)

        self.label_25 = QLabel(self.frame_17)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_9.addWidget(self.label_25)

        self.spinBox_19 = QSpinBox(self.frame_17)
        self.spinBox_19.setObjectName(u"spinBox_19")
        self.spinBox_19.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_19.setMinimum(-360)
        self.spinBox_19.setMaximum(360)

        self.horizontalLayout_9.addWidget(self.spinBox_19)


        self.verticalLayout_8.addWidget(self.frame_17)

        self.frame_19 = QFrame(self.frame_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_18 = QLabel(self.frame_19)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(60, 0))
        self.label_18.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_10.addWidget(self.label_18)

        self.spinBox_12 = QSpinBox(self.frame_19)
        self.spinBox_12.setObjectName(u"spinBox_12")
        self.spinBox_12.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_12.setMaximum(9999999)

        self.horizontalLayout_10.addWidget(self.spinBox_12)

        self.label_22 = QLabel(self.frame_19)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_10.addWidget(self.label_22)

        self.spinBox_11 = QSpinBox(self.frame_19)
        self.spinBox_11.setObjectName(u"spinBox_11")
        self.spinBox_11.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_11.setMaximum(9999999)

        self.horizontalLayout_10.addWidget(self.spinBox_11)

        self.label_21 = QLabel(self.frame_19)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_10.addWidget(self.label_21)

        self.spinBox_13 = QSpinBox(self.frame_19)
        self.spinBox_13.setObjectName(u"spinBox_13")
        self.spinBox_13.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")
        self.spinBox_13.setMinimum(-360)
        self.spinBox_13.setMaximum(360)

        self.horizontalLayout_10.addWidget(self.spinBox_13)


        self.verticalLayout_8.addWidget(self.frame_19)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(400, 0))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.verticalLayout_11.addWidget(self.label_2)

        self.scrollArea_2 = QScrollArea(self.frame_4)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.StyledPanel)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 619, 778))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_img = QLabel(self.scrollAreaWidgetContents_2)
        self.label_img.setObjectName(u"label_img")

        self.verticalLayout_12.addWidget(self.label_img)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_11.addWidget(self.scrollArea_2)

        self.frame_21 = QFrame(self.frame_4)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 50))
        self.frame_21.setMaximumSize(QSize(16777215, 50))
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.textEdit = QTextEdit(self.frame_21)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout_12.addWidget(self.textEdit)

        self.btn_preview = QPushButton(self.frame_21)
        self.btn_preview.setObjectName(u"btn_preview")
        self.btn_preview.setMaximumSize(QSize(90, 16777215))
        self.btn_preview.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_12.addWidget(self.btn_preview)

        self.pushButton = QPushButton(self.frame_21)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: #edeef0;\n"
"color: rgb(0,0,0);")

        self.horizontalLayout_12.addWidget(self.pushButton)


        self.verticalLayout_11.addWidget(self.frame_21)


        self.horizontalLayout.addWidget(self.frame_4)


        self.horizontalLayout_2.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        UpPhoiWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UpPhoiWindow)

        QMetaObject.connectSlotsByName(UpPhoiWindow)
    # setupUi

    def retranslateUi(self, UpPhoiWindow):
        UpPhoiWindow.setWindowTitle(QCoreApplication.translate("UpPhoiWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("UpPhoiWindow", u"Thi\u1ebft l\u1eadp \u1ea3nh ph\u00f4i", None))
        self.label_4.setText(QCoreApplication.translate("UpPhoiWindow", u"K\u00edch th\u01b0\u1edbc \u1ea3nh 1", None))
        self.label_9.setText(QCoreApplication.translate("UpPhoiWindow", u"X", None))
        self.label_5.setText(QCoreApplication.translate("UpPhoiWindow", u"V\u1ecb tr\u00ed \u0111\u1eb7t v\u00e0o ph\u00f4i", None))
        self.label_10.setText(QCoreApplication.translate("UpPhoiWindow", u"X", None))
        self.label_11.setText(QCoreApplication.translate("UpPhoiWindow", u"X", None))
        self.label_31.setText(QCoreApplication.translate("UpPhoiWindow", u"Thi\u1ebft l\u1eadp", None))
        self.label_32.setText(QCoreApplication.translate("UpPhoiWindow", u"K\u00edch c\u1ee1 ch\u1eef", None))
        self.label_33.setText(QCoreApplication.translate("UpPhoiWindow", u"Ki\u1ec3u ch\u1eef", None))
        self.label_15.setText(QCoreApplication.translate("UpPhoiWindow", u"V\u1ecb tr\u00ed[CHI\u1ec0U NGANG X CHI\u1ec0U D\u1eccC X XOAY CHI\u1ec0U]", None))
        self.label_20.setText(QCoreApplication.translate("UpPhoiWindow", u"T\u00ean", None))
        self.label_29.setText(QCoreApplication.translate("UpPhoiWindow", u"X", None))
        self.label_30.setText(QCoreApplication.translate("UpPhoiWindow", u"X", None))
        self.label_16.setText(QCoreApplication.translate("UpPhoiWindow", u"H\u1ecd ", None))
        self.label_24.setText(QCoreApplication.translate("UpPhoiWindow", u"X", None))
        self.label_23.setText(QCoreApplication.translate("UpPhoiWindow", u"X", None))
        self.label_17.setText(QCoreApplication.translate("UpPhoiWindow", u"Ng\u00e0y sinh", None))
        self.label_26.setText(QCoreApplication.translate("UpPhoiWindow", u"X", None))
        self.label_25.setText(QCoreApplication.translate("UpPhoiWindow", u"X", None))
        self.label_18.setText(QCoreApplication.translate("UpPhoiWindow", u"Code", None))
        self.label_22.setText(QCoreApplication.translate("UpPhoiWindow", u"X", None))
        self.label_21.setText(QCoreApplication.translate("UpPhoiWindow", u"X", None))
        self.label_2.setText(QCoreApplication.translate("UpPhoiWindow", u"Ph\u00f4i ch\u1ec9nh s\u1eeda", None))
        self.label_img.setText("")
        self.btn_preview.setText(QCoreApplication.translate("UpPhoiWindow", u"L\u01b0u c\u1ea5u h\u00ecnh", None))
        self.pushButton.setText(QCoreApplication.translate("UpPhoiWindow", u"Browse", None))
    # retranslateUi

