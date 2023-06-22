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

# Create a QApplication instance
app = QApplication(sys.argv)

# Create a QNetworkAccessManager
manager = QNetworkAccessManager()

# Define a function to handle network replies
def handle_network_response(reply, url, fb_id):
    if reply.error() == QNetworkReply.NoError:
        # Read the data from the reply
        data = reply.readAll()

        # Create a QPixmap from the data
        pixmap = QPixmap()
        pixmap.loadFromData(data)

        # Save the pixmap as a PNG file
        file_path = f"input_avatar/{fb_id}.jpg"
        pixmap.save(file_path, "JPG")

        print("Image saved successfully.")

        # Clean up
        reply.deleteLater()
        app.quit()
    else:
        print("Error:", reply.errorString())
        app.quit()
def save_url_image(facebook_id, options,  image_url, image, 
                   givenname, surname, birthday, gender, address):
        # if options == 1:
            # Make a network request
        url = QUrl(image_url)
        request = QNetworkRequest(url)
        reply = manager.get(request)

            # Wait for the reply to finish
        loop = QEventLoop()
        reply.finished.connect(loop.quit)
        loop.exec_()
        handle_network_response(reply, url, facebook_id)
        avt = QPixmap(f"input_avatar/{facebook_id}.jpg")
        from configparser import ConfigParser

        configur = ConfigParser()
        configur.read('output/config.ini')

        defaultValue = 0

        avt_w = int(configur.get('section2', 'Foreground_Width', fallback=defaultValue))
        avt_h = int(configur.get('section2', 'Foreground_Height', fallback=defaultValue))
        avt_x = int(configur.get('section2', 'Foreground_x', fallback=defaultValue))
        avt_y = int(configur.get('section2', 'Foreground_y', fallback=defaultValue))
        avt_a = int(configur.get('section2', 'Foreground_Angle', fallback=defaultValue))
        font_size = int(configur.get('section2', 'Font_Size', fallback=defaultValue))
        font_family = configur.get('section2', 'Font_Family', fallback="")
        GivenName_x = int(configur.get('section2', 'GivenName_x', fallback=defaultValue))
        GivenName_y = int(configur.get('section2', 'GivenName_y', fallback=defaultValue))
        GivenName_Angle = int(configur.get('section2', 'GivenName_Angle', fallback=defaultValue))
        FirstName_x = int(configur.get('section2', 'FirstName_x', fallback=defaultValue))
        FirstName_y = int(configur.get('section2', 'FirstName_y', fallback=defaultValue))
        FirstName_Angle = int(configur.get('section2', 'FirstName_Angle', fallback=defaultValue))
        Birthday_x = int(configur.get('section2', 'Birthday_x', fallback=defaultValue))
        Birthday_y = int(configur.get('section2', 'Birthday_y', fallback=defaultValue))
        Birthday_Angle = int(configur.get('section2', 'Birthday_Angle', fallback=defaultValue))
        Gender_x = int(configur.get('section2', 'Gender_x', fallback=defaultValue))
        Gender_y = int(configur.get('section2', 'Gender_y', fallback=defaultValue))
        Gender_Angle = int(configur.get('section2', 'Gender_Angle', fallback=defaultValue))
        Address_x = int(configur.get('section2', 'Address_x', fallback=defaultValue))
        Address_y = int(configur.get('section2', 'Address_y', fallback=defaultValue))
        Address_Angle = int(configur.get('section2', 'Address_Angle', fallback=defaultValue))
        if options==1:
            URL_Phoi = ""
        else: 
            URL_Phoi = configur.get('section2', 'URL_Phoi', fallback="").replace("/","\\")
        painter = QPainter()
        is_bold = True
        font = QFont()
        font.setFamily(font_family)
        font.setPointSize(font_size)
        font.setBold(is_bold)
        width = 591  # desired width
        height = 361  # desired height
        if options == 1:
            background_image = QPixmap('input_phoi/input2.jpg')
            # print(background_image)
        else:
            print(URL_Phoi)
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

        combined_image.save("output_xmdt/preview.jpg", "JPG")
        print("Done")
        return combined_image
    


save_url_image( '231284214', 2,  'https://ozgrozer.github.io/100k-faces/0/2/002764.jpg', None, 
                       'givenname', 'surname', 'birthday', 'gender', 'address')

# Start the application event loop
sys.exit(app.exec_())