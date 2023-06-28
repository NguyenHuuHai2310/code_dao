from ui_interface import *
import sys
from PyQt5.QtWidgets import QApplication,\
                            QTableWidgetItem, \
                            QHeaderView, QStyle, QStyleOptionButton,QAction,  \
                             QMenu,QDesktopWidget

from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QRect, QMimeData
from Custom_Widgets.Widgets import *
from PyQt5 import QtWidgets, QtGui
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QPushButton, QVBoxLayout, QWidget, QLineEdit
from functions import * 
from ui_upPhoiWindow import *
from upPhoiWindow import UpPhoiWindow
from ui_login import *
from PyQt5.QtWidgets import QTextEdit, QMessageBox
from qtpy.QtCore import Signal
class MyHeader(QHeaderView):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.isOn = False
        self.setStyleSheet(u"background-color: #fffaeb;color: #000000;")
        
    def setTableWidget(self, tableWidget):
        self.tableWidget = tableWidget

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super().paintSection(painter, rect, logicalIndex)
        painter.restore()
        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(5, 5, 15, 15)
            option.state = QStyle.State_On if self.isOn else QStyle.State_Off
            self.style().drawPrimitive(QStyle.PE_IndicatorCheckBox, option, painter)

    def mousePressEvent(self, event):
        if self.logicalIndexAt(event.pos()) == 0:
            self.isOn = not self.isOn
            self.update()

        if self.tableWidget:
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 0)
                if item:
                    item.setCheckState(Qt.Checked if self.isOn else Qt.Unchecked)

        super().mousePressEvent(event)


class ShopLike(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Window")

        self.label = QLabel("Token:")
        self.textEdit = QLineEdit()
        self.saveButton = QPushButton("Save")
        self.saveButton.clicked.connect(self.saveText)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.textEdit)
        layout.addWidget(self.saveButton)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def saveText(self):
        text = self.textEdit.text()
        settings = QSettings(f"output/config.ini", QSettings.IniFormat)
        settings.beginGroup('section2')
        settings.setValue("token_shoplike", text)
        settings.sync()
        settings.endGroup()
        # self.hide()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        screen_rect = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        center_x = screen_rect.x() + screen_rect.width() // 2
        center_y = screen_rect.y() + screen_rect.height() // 2
        # Set the window size based on the screen size
        window_width = screen_rect.width() * 0.8  # Set the desired width (e.g., 80% of the screen width)
        window_height = screen_rect.height() * 0.8  # Set the desired height (e.g., 80% of the screen height)
        self.resize(window_width, window_height)
        self.move(center_x -window_width//2, center_y - window_height//2)
        self.data = []
        myHeader = MyHeader(Qt.Horizontal, self.ui.tableWidget)
        myHeader.setTableWidget(self.ui.tableWidget)
        myHeader.setStretchLastSection(True)
        self.get_values()
        self.ui.tableWidget.setHorizontalHeader(myHeader)
        self.ui.tableWidget.setColumnWidth(1, 300)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 100)
        self.ui.tableWidget.setColumnWidth(4, 100)
        
        # Add checkboxes to the table
        for row in range(self.ui.tableWidget.rowCount()):
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            item2 = QTableWidgetItem(str(row + 1))
            self.ui.tableWidget.setVerticalHeaderItem(row, item2)
            self.ui.tableWidget.setItem(row, 0, item)

        self.ui.start_button.clicked.connect(self.start_generation)
        self.ui.stop_button.clicked.connect(self.stop_generation)
        self.ui.stop_button.setEnabled(False)
        self.generator_threads = []
        self.count = 0
        self.ui.comboBox_19.activated.connect(self.openUpPhoiWindow)
        self.ui.keyCapcha_2.textChanged.connect(self.save_values)
        self.ui.keyOtp.textChanged.connect(self.save_values)
        self.ui.comboBox_26.activated.connect(self.save_shoplikes)
        self.show()
    def save_shoplikes(self):
        print(self.ui.comboBox_26.currentIndex())
        if (self.ui.comboBox_26.currentIndex() == 1):
            self.shoplike_window = ShopLike()
            self.shoplike_window.show()

    def save_values(self):
            settings = QSettings(f"output/config.ini", QSettings.IniFormat)
            settings.beginGroup('section2')
            settings.setValue("KeyOtp", self.ui.keyOtp.text())
            settings.setValue("KeyCaptcha",self.ui.keyCapcha.text())
            settings.setValue("Kieu_XMDT",self.ui.comboBox_18.currentIndex())
            settings.setValue("Chon_Phoi", self.ui.comboBox_19.currentIndex())
            settings.setValue("Anh_Phoi",self.ui.comboBox_19.currentIndex())
            settings.setValue("Up_Avatar",self.ui.comboBox_21.currentIndex())
            if self.radioButton_10.isChecked():
                settings.setValue("Otp_Phone", self.ui.radioButton_10.data())
            settings.setValue("Nha_Mang",self.ui.comboBox_23.currentIndex())
            settings.setValue("Captcha",self.ui.comboBox_22.currentIndex())
            settings.setValue("Get_So_Mail", self.ui.comboBox_24.currentIndex())
            settings.setValue("Login",self.ui.comboBox_25.currentIndex())
            settings.setValue("Ip",self.ui.comboBox_26.currentIndex())

            settings.sync()
            settings.endGroup()
            
    def get_values(self):
        settings = QSettings(f"output/config.ini", QSettings.IniFormat)
        settings.beginGroup('section2')
        self.ui.keyCapcha_2.setText(settings.value("KeyCapcha", ""))
        self.ui.keyOtp.setText(settings.value("KeyOtp", ""))
        settings.endGroup()
    
    # def loadSettingsValues(self):
    #     settings = QSettings("output/config.ini", QSettings.IniFormat)
    #     settings.beginGroup('section2')
        
    #     # Load values from the settings file
    #     keyOtp = settings.value("KeyOtp")
    #     keyCaptcha = settings.value("KeyCaptcha")
    #     kieuXMDT = settings.value("Kieu_XMDT")
    #     chonPhoi = settings.value("Chon_Phoi")
    #     anhPhoi = settings.value("Anh_Phoi")
    #     upAvatar = settings.value("Up_Avatar")
    #     otpPhone = settings.value("Otp_Phone")
    #     nhaMang = settings.value("Nha_Mang")
    #     captcha = settings.value("Captcha")
    #     getSoMail = settings.value("Get_So_Mail")
    #     login = settings.value("Login")
    #     ip = settings.value("Ip")
        
    #     # Set values in the UI elements
    #     self.ui.keyOtp.setText(keyOtp)
    #     self.ui.keyCapcha.setText(keyCaptcha)
    #     self.ui.comboBox_18.setCurrentIndex(int(kieuXMDT))
    #     self.ui.comboBox_19.setCurrentIndex(int(chonPhoi))
    #     self.ui.comboBox_20.setCurrentIndex(int(anhPhoi))
    #     self.ui.comboBox_21.setCurrentIndex(int(upAvatar))
    #     if otpPhone == self.ui.radioButton_10.data():
    #         self.ui.radioButton_10.setChecked(True)
    #     self.ui.comboBox_23.setCurrentIndex(int(nhaMang))
    #     self.ui.comboBox_22.setCurrentIndex(int(captcha))
    #     self.ui.comboBox_24.setCurrentIndex(int(getSoMail))
    #     self.ui.comboBox_25.setCurrentIndex(int(login))
    #     self.ui.comboBox_26.setCurrentIndex(int(ip))

    def openUpPhoiWindow(self):
        if  self.ui.comboBox_19.currentIndex() == 1:
            self.window2 = UpPhoiWindow()
            self.window2.show()
            
    def contextMenuEvent(self, event):
        # print("Coordinate",event.x(), event.y())
        x = 261
        y = 269
        w = self.ui.tableWidget.width()
        h = self.ui.tableWidget.height()
        if (event.y() >y and event.y() <y+h and event.x() >  x and event.x() < x + w):
            menu = QMenu(self)

            paste_delete_action = QAction("Paste tài khoản [Xóa tài khoản cũ]", self)
            paste_delete_action.triggered.connect(self.pasteDeleteAccount)
            menu.addAction(paste_delete_action)

            paste_no_delete_action = QAction("Paste tài khoản [Không xóa tài khoản cũ]", self)
            paste_no_delete_action.triggered.connect(self.pasteNoDeleteAccount)
            menu.addAction(paste_no_delete_action)

            click_selected_account_action = QAction("Click vào tài khoản đã bôi đen", self)
            click_selected_account_action.triggered.connect(self.clickSelectedAccount)
            menu.addAction(click_selected_account_action)

            menu.setStyleSheet("QMenu { background-color: rgb(255, 255, 255); }"
                            "QMenu::item {   background-color: #fffaeb; color: black; \
                                                padding: 4px solid #fffaeb;\
                                                padding-left: 2px solid #fffaeb;\
                                                border: 1px solid #fffaeb; }"
                            "QMenu::item:selected { background-color: blue; color: white; }")

            menu.exec_(event.globalPos())
            event.accept()
    def get_checked_rows(self):
        # Retrieve checked rows
        checked_rows = []
        for row in range(self.ui.tableWidget.rowCount()):
            check_item = self.ui.tableWidget.item(row, 0)
            if check_item.checkState() == Qt.Checked:
                checked_rows.append(row)
        return checked_rows
    def pasteDeleteAccount(self):
        if self.ui.tableWidget.rowCount() > 0:
            # print(self.ui.tableWidget.rowCount())
            self.ui.tableWidget.clearContents()
            # Add checkboxes to the table
        clipboard = QApplication.clipboard()
        clipboard_texts = clipboard.text().split("\n")
        self.ui.tableWidget.setRowCount(len(clipboard_texts))
        for item in clipboard_texts:
            self.data.append(item)
        if len(self.data) > 0:
            for row, item in enumerate(self.data):
                table_item = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, 1, table_item)
        for row in range(self.ui.tableWidget.rowCount()):
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            item2 = QTableWidgetItem(str(row + 1))
            self.ui.tableWidget.setVerticalHeaderItem(row, item2)
            self.ui.tableWidget.setItem(row, 0, item)

    def pasteNoDeleteAccount(self):
        if self.ui.tableWidget.rowCount() > 0:
            start_row = self.ui.tableWidget.rowCount()  
        
        clipboard = QApplication.clipboard()
        clipboard_texts = clipboard.text().split("\n")
        self.ui.tableWidget.setRowCount(start_row + len(clipboard_texts))
        for item in clipboard_texts:
            self.data.append(item)
        if len(self.data) > 0:
            for row, item in enumerate(self.data):
                table_item = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(start_row, 1, table_item)
        for row in range(self.ui.tableWidget.rowCount()):
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            item2 = QTableWidgetItem(str(row + 1))
            self.ui.tableWidget.setVerticalHeaderItem(row, item2)
            self.ui.tableWidget.setItem(row, 0, item)
    def clickSelectedAccount(self):
        clipboard = QApplication.clipboard()
        mimeData = QMimeData()
        selectedText = ""
        # QMessageBox.information(self, "Custom Action", "Click vào tài khoản đã bôi đen clicked!")
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row, 0)
            if item.checkState() == Qt.Checked:
                cell_text = self.ui.tableWidget.item(row, 1).text()
                selectedText += cell_text + "\n"
                # print(cell_text)
        mimeData.setText(selectedText)
        clipboard.setMimeData(mimeData)


    def start_generation(self):
        self.ui.start_button.setEnabled(False)
        self.ui.start_button.setStyleSheet("QPushButton {background-color: #c6c7c1;}")
        self.ui.stop_button.setEnabled(True)
        self.ui.stop_button.setStyleSheet("QPushButton {background-color: rgb(255, 99, 102);}")
        self.clearRow()
        self.num_threads = self.ui.num_threads.value()
        self.delay_time = self.ui.delay_time.value()
        self.checked_rows = self.get_checked_rows()
        self.num_threads = min(len(self.checked_rows), self.num_threads)
        # Create threads
        for i in range(0, self.ui.tableWidget.rowCount()):  # Create 4 generator threads
            if i in self.checked_rows:
                generator_thread = NumberGeneratorThread(i, i * 10 + 1, self.delay_time)
                generator_thread.number_generated.connect(self.handle_number_generated)
                generator_thread.thread_finished.connect(self.handle_thread_finished)
                self.generator_threads.append(generator_thread)
        # print( "len(self.generator_threads): " , len(self.generator_threads))
        self.current_thread_index = 0
        self.run_next_threads()

    def run_next_threads(self):
        num_threads_to_run = min(len(self.generator_threads) - self.current_thread_index, self.num_threads)
        # import ipdb; ipdb.set_trace();
        if num_threads_to_run > 0:
            for i in range(num_threads_to_run):
                generator_thread = self.generator_threads[self.current_thread_index]
                generator_thread.start()
                # if i == num_threads_to_run-1:
                self.current_thread_index += 1

    def stop_generation(self):
        self.ui.start_button.setEnabled(True)
        for generator_thread in self.generator_threads:
            generator_thread.requestInterruption()

    def handle_number_generated(self, number, thread_id):
        # print(f"Thread {thread_id}: {number}")
        item = QTableWidgetItem()
        item.setText(str(number))
        self.ui.tableWidget.setItem(thread_id, 4, item)

    def handle_thread_finished(self, thread_id):
        print(f"Thread {thread_id} finished")
        # print('current_thread_index: ', self.current_thread_index)
        # import ipdb; ipdb.set_trace();
        if self.current_thread_index < len(self.generator_threads):
            if thread_id % self.num_threads==0:
                self.run_next_threads() 
        else:
            self.finish_generation()

    def finish_generation(self):
        self.ui.stop_button.setEnabled(False)
        self.ui.stop_button.setStyleSheet("QPushButton {background-color: #c6c7c1; }")
        self.ui.start_button.setEnabled(True)
        self.ui.start_button.setStyleSheet("QPushButton {background-color: rgba(85, 0, 255, 240);}")
        self.current_thread_index = 0

        for generator_thread in self.generator_threads:
            generator_thread.requestInterruption()
            generator_thread.quit()
            generator_thread.wait()
        self.generator_threads = []
        
        # self.start_generation()
        print("All threads finished")
    def clearRow(self):
        for row in range(self.ui.tableWidget.rowCount()):
            item = QTableWidgetItem("")
            self.ui.tableWidget.setItem(row, 4, item)
class Login(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.centerWindow()
        
        pixmap = QPixmap("icons/icons8-male-user-94.png")
        pixmap = pixmap.scaled(200,200, Qt.AspectRatioMode.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.logo.setPixmap(pixmap)
        self.ui.logo.setAlignment(Qt.AlignCenter)
        self.ui.loginBtn.clicked.connect(self.openMainWindow)
        self.ui.username.returnPressed.connect(self.keyPressEvent)
        self.ui.password.returnPressed.connect(self.keyPressEvent)
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or  event.key() == Qt.Key_Enter:
            self.openMainWindow()
        else:
            super().keyPressEvent(event)
    def centerWindow(self):
        screen = QDesktopWidget().screenGeometry()
        center_x = screen.width() // 2
        center_y = screen.height() // 2
        window_x = center_x - self.width() // 2
        window_y = center_y - self.height() // 2
        self.move(window_x, window_y)
    def openMainWindow(self):
        if (self.ui.username.text() == "admin" and self.ui.password.text()=="admin"):
            self.main_window = MainWindow()
            self.hide()
            self.main_window.show()
        else:
           self.ui.label.setText('Invalid username or password.')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = MainWindow()
    login_window.show()
    sys.exit(app.exec_())
