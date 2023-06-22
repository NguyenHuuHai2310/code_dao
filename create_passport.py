from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtGui import QPainter, QPixmap, QFont, QFontDatabase, QTransform
from PyQt5.QtCore import Qt, QUrl, QSettings
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QEventLoop
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QImageWriter, QPixmap
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt5.QtCore import QUrl, QIODevice
import sys


class passport:
    def __init__(self) -> None:
        super().__init__()

    # Create a QNetworkAccessManager
    manager = QNetworkAccessManager()

    # Define a function to handle network replies
    def handle_network_response(self, reply, url, facebook_id):
        try:
            if reply.error() == QNetworkReply.NoError:
                # Read the data from the reply
                data = reply.readAll()

                # Create a QPixmap from the data
                pixmap = QPixmap()
                pixmap.loadFromData(data)

                # Save the pixmap as a PNG file
                file_path = f"input_avatar/{facebook_id}.jpg"
                pixmap.save(file_path, "JPG")

                # Clean up
                reply.deleteLater()

                return json.dumps({
                    'status': 200,
                    'message': 'Tạo avatar thành công!',
                })
            else:
                return json.dumps({
                    'status': 200,
                    'message': 'Lỗi tạo avatar!',
                })
        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi tạo avatar'
            })

    def save_url_image(self, facebook_id, options, image_url,
                       givenname, surname, birthday, gender, address):
        try:
            # Make a network request
            url = QUrl(image_url)
            request = QNetworkRequest(url)
            reply = self.manager.get(request)

            # Wait for the reply to finish
            loop = QEventLoop()
            reply.finished.connect(loop.quit)
            loop.exec_()

            # Handle the network response
            self.handle_network_response(reply, url, facebook_id)

            # Retrieve the pixmap from the handle_network_response function
            avt = QPixmap(f"input_avatar/{facebook_id}.jpg")

            settings = QSettings('output/config.ini', QSettings.IniFormat)
            settings.setIniCodec("UTF-8")
            defaultValue = 0

            settings.beginGroup(f'section{options}')
            # load values from .ini fill
            avt_w = int(settings.value("Foreground_Width", defaultValue))
            avt_h = int(settings.value("Foreground_Height", defaultValue))
            avt_x = int(settings.value("Foreground_x", defaultValue))
            avt_y = int(settings.value("Foreground_y", defaultValue))
            avt_a = int(settings.value("Foreground_Angle", defaultValue))
            font_size = int(settings.value("Font_Size", defaultValue))
            font_family = settings.value("Font_Family", "")
            GivenName_x = int(settings.value("GivenName_x", defaultValue))
            GivenName_y = int(settings.value("GivenName_y", defaultValue))
            GivenName_Angle = int(settings.value("GivenName_Angle", defaultValue))
            FirstName_x = int(settings.value("FirstName_x", defaultValue))
            FirstName_y = int(settings.value("FirstName_y", defaultValue))
            FirstName_Angle = int(settings.value("FirstName_Angle", defaultValue))
            Birthday_x = int(settings.value("Birthday_x", defaultValue))
            Birthday_y = int(settings.value("Birthday_y", defaultValue))
            Birthday_Angle = int(settings.value("Birthday_Angle", defaultValue))
            Gender_x = int(settings.value("Gender_x", defaultValue))
            Gender_y = int(settings.value("Gender_y", defaultValue))
            Gender_Angle = int(settings.value("Gender_Angle", defaultValue))
            Address_x = int(settings.value("Address_x", defaultValue))
            Address_y = int(settings.value("Address_y", defaultValue))
            Address_Angle = int(settings.value("Address_Angle", defaultValue))
            if options == 1:
                URL_Phoi = 'input_phoi/input2.jpg'
            elif options == 2:
                URL_Phoi = settings.value("URL_Phoi", "")
            settings.endGroup()
            painter = QPainter()
            is_bold = True
            font = QFont()
            font.setFamily(font_family)
            font.setPointSize(font_size)
            font.setBold(is_bold)
            width = 591  # desired width
            height = 361  # desired height
            background_image = QPixmap(URL_Phoi)
            background_image = background_image.scaled(width, height)
            foreground_image = avt.scaled(avt_w, avt_h)
            transform = QTransform()
            transform.rotate(avt_a)
            rotated_image = foreground_image.transformed(transform)
            combined_image = QPixmap(background_image.size())
            combined_image.fill(Qt.transparent)

            # Draw the background image on the combined image
            painter = QPainter(combined_image)
            # painter.begin(combined_image)
            painter.drawPixmap(0, 0, background_image)
            painter.drawPixmap(avt_x, avt_y, rotated_image)

            painter.setFont(font)
            # Set the rotation angles for the texts
            angle_givenname = GivenName_Angle
            angle_surname = FirstName_Angle
            angle_birthday = Birthday_Angle
            angle_gender = Gender_Angle
            angle_address = Address_Angle
            # Create a transformation matrix for the rotation angle around the center
            transform_1 = QTransform()
            transform_1.translate(GivenName_x, GivenName_y)
            transform_1.rotate(angle_givenname)
            transform_1.translate(-GivenName_x, -GivenName_y)
            # Create a transformation matrix for the rotation angle around the center
            transform_2 = QTransform()
            transform_2.translate(FirstName_x, FirstName_y)
            transform_2.rotate(angle_surname)
            transform_2.translate(-FirstName_x, -FirstName_y)
            # Create a transformation matrix for the rotation angle around the center
            transform_3 = QTransform()
            transform_3.translate(Birthday_x, Birthday_y)
            transform_3.rotate(angle_birthday)
            transform_3.translate(-Birthday_x, -Birthday_y)
            # Create a transformation matrix for the rotation angle around the center
            transform_4 = QTransform()
            transform_4.translate(Gender_x, Gender_y)
            transform_4.rotate(angle_gender)
            transform_4.translate(-Gender_x, -Gender_y)
            # Create a transformation matrix for the rotation angle around the center
            transform_5 = QTransform()
            transform_5.translate(Address_x, Address_y)
            transform_5.rotate(angle_address)
            transform_5.translate(-Address_x, -Address_y)

            painter.setTransform(transform_1)
            painter.drawText(GivenName_x, GivenName_y, givenname)

            painter.setTransform(transform_2)
            painter.drawText(FirstName_x, FirstName_y, surname)

            painter.setTransform(transform_3)
            painter.drawText(Birthday_x, Birthday_y, birthday)

            painter.setTransform(transform_4)
            painter.drawText(Gender_x, Gender_y, gender)

            painter.setTransform(transform_5)
            painter.drawText(Address_x, Address_y, address)

            combined_image.save(f"output_xmdt/{facebook_id}.jpg", "JPG")
            return json.dumps({
                'status': 200,
                'message': 'Tạo phôi thành công'
            })
        except Exception as e:
            return json.dumps({
                'status': 404,
                'message': 'Lỗi tạo phôi'
            })
