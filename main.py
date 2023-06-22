import json
import time
import os

from request import request_fb
from ui_interface import *
import sys

from PyQt5.QtWidgets import QApplication, QWidget, \
    QInputDialog, QLineEdit, \
    QFileDialog, QTableWidget, \
    QTableWidgetItem, QMessageBox, \
    QHeaderView, QStyle, QStyleOptionButton, QAction, \
    QCheckBox, QVBoxLayout, QMenu, QDesktopWidget

from PyQt5.QtGui import QPainter, QPixmap, QFont, QFontDatabase, QTransform, QDesktopServices, QClipboard
from PyQt5.QtCore import Qt, QRect, QUrl
from Custom_Widgets.Widgets import *
from PyQt5 import QtWidgets
from functions import *
from ui_upPhoiWindow import *
from upPhoiWindow import UpPhoiWindow
from PyQt5.QtWidgets import QTextEdit


class MyHeader(QHeaderView):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.isOn = False
        # self.setStyleSheet(u"background-color: rgb(46, 52, 54);")

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


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        self.centerWindow()
        self.ui.toolBox_3.currentChanged.connect(self.menuChanged)
        # self.ui.BtnListMail.clicked.connect(self.openFileDialog)
        self.data = []
        myHeader = MyHeader(Qt.Horizontal, self.ui.tableWidget)
        myHeader.setTableWidget(self.ui.tableWidget)
        myHeader.setStretchLastSection(True)
        self.get_values()
        self.ui.tableWidget.setHorizontalHeader(myHeader)


        # Đặt stylesheet để thay đổi màu nền cho QTableWidget
        self.ui.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: rgb(46, 52, 54);  /* Đổi màu nền của QTableWidget */
                color: rgb(255, 255, 255);  /* Đổi màu văn bản của QTableWidget */
            }
            QTableWidget::item {
                background-color: rgb(46, 52, 54);  /* Đổi màu nền của các item (cell) */
            }
            QHeaderView::section {
                background-color: rgb(46, 52, 54);  /* Đổi màu nền của header */
                color: rgb(255, 255, 255);  /* Đổi màu văn bản của header */
            }
        """)

        self.ui.tableWidget.setColumnWidth(0, 5)
        self.ui.tableWidget.setColumnWidth(1, 200)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 100)
        self.ui.tableWidget.setColumnWidth(4, 300)

        # Add checkboxes to the table
        for row in range(self.ui.tableWidget.rowCount()):
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            item2 = QTableWidgetItem(str(row + 1))
            self.ui.tableWidget.setVerticalHeaderItem(row, item2)
            # self.ui.tableWidget.setItem(row, 0, item)

        self.ui.start_button.clicked.connect(self.start_generation)
        self.ui.stop_button.clicked.connect(self.stop_generation)
        self.ui.stop_button.setEnabled(False)
        self.generator_threads = []
        self.count = 0
        self.ui.comboBox_12.activated.connect(self.openUpPhoiWindow)
        self.ui.keyCapcha.textChanged.connect(self.save_values)
        self.ui.keyOtp.textChanged.connect(self.save_values)
        self.show()

    def save_values(self):
        settings = QSettings(f"output/config.ini", QSettings.IniFormat)
        settings.beginGroup('section2')
        settings.setValue("KeyOtp", self.ui.keyOtp.toPlainText())
        settings.setValue("KeyCapcha", self.ui.keyCapcha.toPlainText())
        settings.sync()
        settings.endGroup()

    def get_values(self):
        settings = QSettings(f"output/config.ini", QSettings.IniFormat)
        settings.beginGroup('section2')
        self.ui.keyCapcha.setPlainText(settings.value("KeyCapcha", ""))
        self.ui.keyOtp.setPlainText(settings.value("KeyOtp", ""))
        settings.endGroup()

    def centerWindow(self):
        # Get the screen's geometry
        screen = QDesktopWidget().screenGeometry()
        print(screen.width(), screen.height())
        # Calculate the center point of the screen
        center_x = screen.width() // 2
        center_y = screen.height() // 2

        # Calculate the top-left position of the window
        window_x = center_x - self.width() // 2
        window_y = center_y - self.height() // 2
        print(self.width(), self.height())
        print(window_x, window_y)
        # Set the window's position
        self.move(window_x, window_y)

    def menuChanged(self):
        if self.ui.toolBox_3.currentIndex() == 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_view)
        elif self.ui.toolBox_3.currentIndex() == 1:
            if self.ui.button_function.clicked:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_function)
        elif self.ui.toolBox_3.currentIndex() == 2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_config)
        elif self.ui.toolBox_3.currentIndex() == 3:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_contact)

    # def openFileDialog(self):
    #     fname = QFileDialog.getOpenFileName(self, "Open File", "", "Text files (*.txt)")
    #     if fname:
    #         self.ui.BtnListMail.setText(str(fname).replace("Text files (*.txt)", "")[2:-6])
    #     return 0

    def openUpPhoiWindow(self):
        if self.ui.comboBox_12.currentIndex() == 1:
            self.window2 = UpPhoiWindow()
            self.window2.show()

    def contextMenuEvent(self, event):
        # print("Coordinate",event.x(), event.y())
        x = 261
        y = 269
        w = self.ui.tableWidget.width()
        h = self.ui.tableWidget.height()
        if (event.y() > y and event.y() < y + h and event.x() > x and event.x() < x + w):
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

            menu.setStyleSheet("QMenu { background-color: rgb(46, 52, 54); }"
                               "QMenu::item {   background-color: rgb(46, 52, 54); color: white; \
                                                padding: 4px solid rgb(46, 52, 54);\
                                                padding-left: 2px solid rgb(46, 52, 54);\
                                                border: 1px solid rgb(46, 52, 54); }"
                               "QMenu::item:selected { background-color: blue; }")

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
        # QMessageBox.information(self, "Custom Action", "Click vào tài khoản đã bôi đen clicked!")
        pass

    def start_generation(self):
        self.ui.start_button.setEnabled(False)
        self.ui.stop_button.setEnabled(True)
        self.clearRow()
        self.num_threads = self.ui.num_threads.value()
        self.delay_time = self.ui.delay_time.value()
        self.checked_rows = self.get_checked_rows()
        self.num_threads = min(len(self.checked_rows), self.num_threads)
        # Create threads
        for i in range(0, self.ui.tableWidget.rowCount()):  # Create 4 generator threads
            if i in self.checked_rows:
                generator_thread = NumberGeneratorThread(i, i * 10 + 1, self.delay_time)
                generator_thread.setObjectName('Thread ' + str(i))
                generator_thread.do_work.connect(self.handle_do_work)
                # generator_thread.number_generated.connect(self.handle_number_generated)
                generator_thread.thread_finished.connect(self.handle_thread_finished)
                self.generator_threads.append(generator_thread)
        # print( "len(self.generator_threads): " , len(self.generator_threads))
        self.current_thread_index = 0
        self.index_loop = 0
        self.count_thread_done = 0
        self.default_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
        # So vong lap de chay het
        if self.num_threads != 0:
            if (len(self.generator_threads) % self.num_threads) == 0:
                self.count_loop = int(len(self.generator_threads) / self.num_threads)
            else:
                self.count_loop = int(len(self.generator_threads) / self.num_threads) + 1
            self.run_next_threads(self.index_loop)

    def run_next_threads(self, index_loop):
        if (index_loop + 1) != self.count_loop:
            for j in range(index_loop * self.num_threads, index_loop * self.num_threads + self.num_threads):
                (self.generator_threads[j]).start()
        else:
            for j in range(index_loop * self.num_threads, len(self.generator_threads)):
                (self.generator_threads[j]).start()

    def stop_generation(self):
        self.ui.start_button.setEnabled(True)
        for generator_thread in self.generator_threads:
            generator_thread.requestInterruption()

    def handle_do_work(self, thread_id, cookie_login_success):
        # Get option XMDT
        option_choise_Phoi = self.ui.comboBox_12.currentIndex()
        option_XMDT = {
            "option_choise_Phoi": option_choise_Phoi,
        }
        # Get acc fb
        info_acc = self.ui.tableWidget.item(thread_id, 1).text()
        info_acc_arr = str(info_acc).split('|')
        id_fb = info_acc_arr[0]
        pass_fb = info_acc_arr[1]
        code_2fa = info_acc_arr[2]
        access_token_fb = info_acc_arr[3]
        client_token = self.ui.keyCapcha.toPlainText()
        token = self.ui.keyOtp.toPlainText()
        request = request_fb(client_token, token, access_token_fb, option_XMDT)

        # Check client_token and token
        if (client_token != '') and (token != ''):
            # Check đã có cookie hay chưa
            item_cookie = self.ui.tableWidget.item(thread_id, 2)
            if item_cookie is not None:
                cookie_login_success = item_cookie.text()
            else:
                cookie_login_success = ''
            if cookie_login_success == '':
                response = request.get_cookie_before_login_facebook_mbasic(self.default_user_agent)
                response = json.loads(response)
                if response['status'] != 200:
                    self.handle_write_table(thread_id, 4, response['message'])
                else:
                    self.handle_write_table(thread_id, 4, response['message'])
                    response = request.get_cookie_checkpoint_2fa(id_fb, pass_fb, response['cookie'], response['lsd'],
                                                                 response['jazoest'],
                                                                 response['m_ts'], response['li'], response['login'],
                                                                 response['bi_xrwh'], self.default_user_agent)
                    response = json.loads(response)
                    if response['status'] != 200:
                        self.handle_write_table(thread_id, 4, response['message'])
                    else:
                        self.handle_write_table(thread_id, 4, response['message'])
                        response = request.check_approvals_code(response['cookie'], code_2fa, self.default_user_agent)
                        response = json.loads(response)
                        if response['status'] != 200:
                            self.handle_write_table(thread_id, 4, response['message'])
                        else:
                            self.handle_write_table(thread_id, 4, response['message'])
                            response = request.submit_code_2fa(response['fb_dtsg'], response['jazoest'],
                                                               response['approvals_code'], response['nh'],
                                                               response['cookie'], self.default_user_agent,
                                                               response['submit_name'], response['submit_value'])
                            response = json.loads(response)
                            if response['status'] != 200:
                                self.handle_write_table(thread_id, 4, response['message'])
                            else:
                                self.handle_write_table(thread_id, 4, response['message'])
                                response = request.get_cookie_dont_save_browser(response['fb_dtsg'],
                                                                                response['jazoest'],
                                                                                response['nh'], response['cookie'],
                                                                                self.default_user_agent,
                                                                                response['submit_name'],
                                                                                response['submit_value'])
                                response = json.loads(response)
                                while response['status'] == 302:
                                    response = request.review_recent_login(response['fb_dtsg'], response['jazoest'],
                                                                           response['nh'], response['cookie'],
                                                                           self.default_user_agent,
                                                                           response['submit_name'],
                                                                           response['submit_value'])
                                    response = json.loads(response)
                                # response = request.check_login_to_home(response['cookie'], self.default_user_agent)
                                # response = json.loads(response)
                                if response['status'] != 200:
                                    self.handle_write_table(thread_id, 4, response['message'])
                                else:
                                    cookie_login_success = response['cookie']
                                    self.handle_write_table(thread_id, 4, response['message'])
                                    self.handle_write_table(thread_id, 2, cookie_login_success)
                                    response = request.check_account_quality(id_fb, response['cookie'],
                                                                             self.default_user_agent)
                                    response = json.loads(response)
                                    if (response['status'] == 200) and (response['acc_is_restricted'] == True):
                                        self.handle_write_table(thread_id, 4, response['message'])
                                        response = request.get_view_checkpoint_282(cookie_login_success,
                                                                                   self.default_user_agent)
                                        response = json.loads(response)
                                        if (response['status'] == 200) and (response['action'] == 'action_proceed'):
                                            self.handle_write_table(thread_id, 4, response['message'])
                                            response = request.submit_continue_checkpoint(response['number_checkpoint'],
                                                                                          cookie_login_success,
                                                                                          self.default_user_agent)
                                        elif (response['status'] == 200) and (response['action'] == 'captcha'):
                                            self.handle_write_table(thread_id, 4, response['message'])
                                            response = request.submit_code_checkpoint(response['number_checkpoint'],
                                                                                      cookie_login_success,
                                                                                      self.default_user_agent,
                                                                                      client_token)
                                        elif (response['status'] == 200) and (response['action'] == 'add_phone_number'):
                                            self.handle_write_table(thread_id, 4, response['message'])
                                            response = request.submit_phone_number(response['number_checkpoint'],
                                                                                   cookie_login_success,
                                                                                   self.default_user_agent, token, 7)
                                        elif (response['status'] == 200) and (response['action'] == 'upload_your_id'):
                                            self.handle_write_table(thread_id, 4, response['message'])
                                            response = request.submit_your_id(response['number_checkpoint'],
                                                                              cookie_login_success,
                                                                              self.default_user_agent,
                                                                              access_token_fb,
                                                                              option_XMDT['option_choise_Phoi'])
                                        else:
                                            self.handle_write_table(thread_id, 4, response['message'])
                                        response = json.loads(response)
                                        self.handle_write_table(thread_id, 4, response['message'])
                                    else:
                                        self.handle_write_table(thread_id, 4, response['message'])
            else:
                response = request.check_account_quality(id_fb, cookie_login_success,
                                                         self.default_user_agent)
                response = json.loads(response)
                if (response['status'] == 200) and (response['acc_is_restricted'] == True):
                    self.handle_write_table(thread_id, 4, response['message'])
                    response = request.get_view_checkpoint_282(cookie_login_success,
                                                               self.default_user_agent)
                    response = json.loads(response)
                    if (response['status'] == 200) and (response['action'] == 'action_proceed'):
                        self.handle_write_table(thread_id, 4, response['message'])
                        response = request.submit_continue_checkpoint(response['number_checkpoint'],
                                                                      cookie_login_success,
                                                                      self.default_user_agent)
                    elif (response['status'] == 200) and (response['action'] == 'captcha'):
                        self.handle_write_table(thread_id, 4, response['message'])
                        response = request.submit_code_checkpoint(response['number_checkpoint'],
                                                                  cookie_login_success,
                                                                  self.default_user_agent, client_token)
                    elif (response['status'] == 200) and (response['action'] == 'add_phone_number'):
                        self.handle_write_table(thread_id, 4, response['message'])
                        response = request.submit_phone_number(response['number_checkpoint'],
                                                               cookie_login_success,
                                                               self.default_user_agent, token, 7)
                    elif (response['status'] == 200) and (response['action'] == 'upload_your_id'):
                        self.handle_write_table(thread_id, 4, response['message'])
                        response = request.submit_your_id(response['number_checkpoint'],
                                                          cookie_login_success, self.default_user_agent,
                                                          access_token_fb,
                                                          option_XMDT['option_choise_Phoi'])
                    else:
                        self.handle_write_table(thread_id, 4, response['message'])
                    response = json.loads(response)
                    self.handle_write_table(thread_id, 4, response['message'])
                else:
                    self.handle_write_table(thread_id, 4, response['message'])
        else:
            if client_token == '':
                QMessageBox.warning(None, 'WARNING', 'Chưa điền Key Captcha')
            elif token == '':
                QMessageBox.warning(None, 'WARNING', 'Chưa điền Key OTP')

    def handle_write_table(self, row, column, content):
        item = QTableWidgetItem()
        item.setText(str(content))
        self.ui.tableWidget.setItem(row, column, item)
        QApplication.processEvents()  # Đồng bộ hóa giao diện

    def handle_number_generated(self, number, thread_id):
        # print(f"Thread {thread_id}: {number}")
        item = QTableWidgetItem()
        item.setText(str(number))
        self.ui.tableWidget.setItem(thread_id, 4, item)

    def handle_thread_finished(self, thread_id):
        print(f"Thread {thread_id} finished")
        self.count_thread_done += 1
        if (self.count_thread_done % self.num_threads) == 0 and self.count_thread_done != len(self.generator_threads):
            self.index_loop += 1
            time.sleep(self.delay_time / 1000)
            self.run_next_threads(self.index_loop)
        elif self.count_thread_done == len(self.generator_threads):
            self.finish_generation()

        # print('current_thread_index: ', self.current_thread_index)
        # import ipdb; ipdb.set_trace();
        # if self.current_thread_index < len(self.generator_threads):
        #     if thread_id % self.num_threads == 0:
        #         self.run_next_threads()
        # else:
        #     self.finish_generation()

    def finish_generation(self):
        self.ui.stop_button.setEnabled(False)
        self.ui.start_button.setEnabled(True)
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


if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCREEN_SCALE_FACTORS"] = "<list_of_screen_scale_factors>"
    os.environ["QT_SCALE_FACTOR"] = "<global_scale_factor>"
    app = QApplication(sys.argv)
    window = MainWindow()
    # window = UpPhoiWindow()
    window.show()
    sys.exit(app.exec_())
