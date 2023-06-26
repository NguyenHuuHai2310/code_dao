import json
import multiprocessing
import threading
import time

from PyQt5.QtCore import pyqtSignal, QObject
from PySide2.QtCore import QRunnable

# Tạo một lớp WorkerSignals để định nghĩa tín hiệu
from PySide2.QtWidgets import QMessageBox, QTableWidget

from request import request_fb


class WorkerSignals(QObject):
    resultReady = pyqtSignal(int, int, str)
    result_fineshed = pyqtSignal()


# Tạo một lớp kế thừa từ QRunnable để thực hiện công việc trong tiến trình
class Worker_Multi_Thread(QRunnable):
    def __init__(self, list_index_processes, total_processes, batch_size, wait_time, option_XMDT, tableWidget_vias, client_token, token):
        super().__init__()
        self.list_index_processes = list_index_processes
        self.total_processes = total_processes
        self.batch_size = batch_size
        self.wait_time = wait_time
        self.option_XMDT = option_XMDT
        self.tableWidget_vias = tableWidget_vias
        self.client_token = client_token
        self.token = token
        self.default_user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'
        self.isStop = False
        self.signals = WorkerSignals()  # Tạo một đối tượng tín hiệu trong Worker
        self.signals_fineshed = WorkerSignals()  # Tín hiệu kết thúc luồng chạy

    def run(self):
        # Thực hiện công việc ở đây và trả về kết quả

        self.isStop = False
        for i in range(0, self.total_processes, self.batch_size):
            self.threads = []
            for j in range(i, i + self.batch_size):
                if j < self.total_processes:
                    thread = threading.Thread(target=self.worker_process, args=(self.list_index_processes[j], self.option_XMDT, self.tableWidget_vias,
                                                                                self.client_token, self.token))
                    thread.setName('thread-' + str(self.list_index_processes[j]))
                    self.threads.append(thread)
                    thread.start()

            for thread in self.threads:
                thread.join()
            # Dừng trong khoảng thời gian cho trước trước khi chạy tiếp
            time.sleep(self.wait_time / 1000)
        self.signals_fineshed.result_fineshed.emit()

        # Gửi kết quả về cho MainWindow thông qua tín hiệu
        # self.signals.resultReady.emit(result)

    def woker_stop_threading(self):
        self.isStop = True


    def worker_process(self, thread_id, option_XMDT, tableWidget_vias, client_token, token):
        if self.isStop:
            pass
        else:
            # Get acc fb
            info_acc = tableWidget_vias.item(thread_id, 1).text()
            info_acc_arr = str(info_acc).split('|')
            id_fb = info_acc_arr[0]
            pass_fb = info_acc_arr[1]
            code_2fa = info_acc_arr[2]
            access_token_fb = info_acc_arr[3]
            # client_token = self.ui.keyCapcha.toPlainText()
            # token = self.ui.keyOtp.toPlainText()
            request = request_fb(client_token, token, access_token_fb, option_XMDT)

            # Check client_token and token
            if (client_token != '') and (token != ''):
                # Check đã có cookie hay chưa
                item_cookie = tableWidget_vias.item(thread_id, 2)
                if item_cookie is not None:
                    cookie_login_success = item_cookie.text()
                else:
                    cookie_login_success = ''
                if cookie_login_success == '':
                    response = request.get_cookie_before_login_facebook_mbasic(self.default_user_agent)
                    response = json.loads(response)
                    if response['status'] != 200:
                        self.signals.resultReady.emit(thread_id, 4, response['message'])
                    else:
                        self.signals.resultReady.emit(thread_id, 4, response['message'])
                        response = request.get_cookie_checkpoint_2fa(id_fb, pass_fb, response['cookie'],
                                                                     response['lsd'],
                                                                     response['jazoest'],
                                                                     response['m_ts'], response['li'],
                                                                     response['login'],
                                                                     response['bi_xrwh'], self.default_user_agent)
                        response = json.loads(response)
                        if response['status'] != 200:
                            self.signals.resultReady.emit(thread_id, 4, response['message'])
                        else:
                            self.signals.resultReady.emit(thread_id, 4, response['message'])
                            response = request.check_approvals_code(response['cookie'], code_2fa,
                                                                    self.default_user_agent)
                            response = json.loads(response)
                            if response['status'] != 200:
                                self.signals.resultReady.emit(thread_id, 4, response['message'])
                            else:
                                self.signals.resultReady.emit(thread_id, 4, response['message'])
                                response = request.submit_code_2fa(response['fb_dtsg'], response['jazoest'],
                                                                   response['approvals_code'], response['nh'],
                                                                   response['cookie'], self.default_user_agent,
                                                                   response['submit_name'], response['submit_value'])
                                response = json.loads(response)
                                if response['status'] != 200:
                                    self.signals.resultReady.emit(thread_id, 4, response['message'])
                                else:
                                    self.signals.resultReady.emit(thread_id, 4, response['message'])
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
                                        self.signals.resultReady.emit(thread_id, 4, response['message'])
                                    else:
                                        cookie_login_success = response['cookie']
                                        self.signals.resultReady.emit(thread_id, 4, response['message'])
                                        self.signals.resultReady.emit(thread_id, 2, cookie_login_success)
                                        response = request.check_account_quality(id_fb, response['cookie'],
                                                                                 self.default_user_agent)
                                        response = json.loads(response)
                                        if (response['status'] == 200) and (response['acc_is_restricted'] == True):
                                            self.signals.resultReady.emit(thread_id, 4, response['message'])
                                            response = request.get_view_checkpoint_282(cookie_login_success,
                                                                                       self.default_user_agent)
                                            response = json.loads(response)
                                            if (response['status'] == 200) and (response['action'] == 'action_proceed'):
                                                self.signals.resultReady.emit(thread_id, 4, response['message'])
                                                response = request.submit_continue_checkpoint(
                                                    response['number_checkpoint'],
                                                    cookie_login_success,
                                                    self.default_user_agent)
                                            elif (response['status'] == 200) and (response['action'] == 'captcha'):
                                                self.signals.resultReady.emit(thread_id, 4, response['message'])
                                                response = request.submit_code_checkpoint(response['number_checkpoint'],
                                                                                          cookie_login_success,
                                                                                          self.default_user_agent,
                                                                                          client_token)
                                            elif (response['status'] == 200) and (
                                                    response['action'] == 'add_phone_number'):
                                                self.signals.resultReady.emit(thread_id, 4, response['message'])
                                                response = request.submit_phone_number(response['number_checkpoint'],
                                                                                       cookie_login_success,
                                                                                       self.default_user_agent, token,
                                                                                       7)
                                            elif (response['status'] == 200) and (
                                                    response['action'] == 'upload_your_id'):
                                                self.signals.resultReady.emit(thread_id, 4, response['message'])
                                                response = request.submit_your_id(response['number_checkpoint'],
                                                                                  cookie_login_success,
                                                                                  self.default_user_agent,
                                                                                  access_token_fb,
                                                                                  option_XMDT['option_choise_Phoi'])
                                            else:
                                                self.signals.resultReady.emit(thread_id, 4, response['message'])
                                            response = json.loads(response)
                                            self.signals.resultReady.emit(thread_id, 4, response['message'])
                                        else:
                                            self.signals.resultReady.emit(thread_id, 4, response['message'])
                else:
                    response = request.check_account_quality(id_fb, cookie_login_success,
                                                             self.default_user_agent)
                    response = json.loads(response)
                    if (response['status'] == 200) and (response['acc_is_restricted'] == True):
                        self.signals.resultReady.emit(thread_id, 4, response['message'])
                        response = request.get_view_checkpoint_282(cookie_login_success,
                                                                   self.default_user_agent)
                        response = json.loads(response)
                        if (response['status'] == 200) and (response['action'] == 'action_proceed'):
                            self.signals.resultReady.emit(thread_id, 4, response['message'])
                            response = request.submit_continue_checkpoint(response['number_checkpoint'],
                                                                          cookie_login_success,
                                                                          self.default_user_agent)
                        elif (response['status'] == 200) and (response['action'] == 'captcha'):
                            self.signals.resultReady.emit(thread_id, 4, response['message'])
                            response = request.submit_code_checkpoint(response['number_checkpoint'],
                                                                      cookie_login_success,
                                                                      self.default_user_agent, client_token)
                        elif (response['status'] == 200) and (response['action'] == 'add_phone_number'):
                            self.signals.resultReady.emit(thread_id, 4, response['message'])
                            response = request.submit_phone_number(response['number_checkpoint'],
                                                                   cookie_login_success,
                                                                   self.default_user_agent, token, 7)
                        elif (response['status'] == 200) and (response['action'] == 'upload_your_id'):
                            self.signals.resultReady.emit(thread_id, 4, response['message'])
                            response = request.submit_your_id(response['number_checkpoint'],
                                                              cookie_login_success, self.default_user_agent,
                                                              access_token_fb,
                                                              option_XMDT['option_choise_Phoi'])
                        else:
                            self.signals.resultReady.emit(thread_id, 4, response['message'])
                        response = json.loads(response)
                        self.signals.resultReady.emit(thread_id, 4, response['message'])
                    else:
                        self.signals.resultReady.emit(thread_id, 4, response['message'])
            else:
                if client_token == '':
                    QMessageBox.warning(None, 'WARNING', 'Chưa điền Key Captcha')
                elif token == '':
                    QMessageBox.warning(None, 'WARNING', 'Chưa điền Key OTP')
