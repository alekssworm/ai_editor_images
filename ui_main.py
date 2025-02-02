# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QScrollBar, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(585, 652)
        MainWindow.setStyleSheet(u"/* === \u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439 \u0444\u043e\u043d \u043e\u043a\u043d\u0430 === */\n"
"QMainWindow {\n"
"    background-color: #1E1F2B;\n"
"    color: #FFFFFF;\n"
"    font-family: \"Inter\", \"SF Pro\", sans-serif;\n"
"}\n"
"\n"
"/* === \u041a\u043d\u043e\u043f\u043a\u0438 === */\n"
"QPushButton {\n"
"    background-color: #6A5ACD;\n"
"    color: #FFFFFF;\n"
"    border-radius: 8px;\n"
"    padding: 8px 12px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    border: 1px solid #4F3DB2;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #7D6DEB;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #4F3DB2;\n"
"}\n"
"\n"
"/* === \u041a\u043d\u043e\u043f\u043a\u0430 \u043d\u0430\u0441\u0442\u0440\u043e\u0435\u043a \u0438\u043b\u0438 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f (\u0437\u0435\u043b\u0451\u043d\u0430\u044f) === */\n"
"QPushButton#settings, QPushButton#confirm {\n"
"    background-color: #4CAF50;\n"
"}\n"
"\n"
"QP"
                        "ushButton#settings:hover, QPushButton#confirm:hover {\n"
"    background-color: #66BB6A;\n"
"}\n"
"\n"
"/* === \u041f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 === */\n"
"QLineEdit {\n"
"    background-color: #2A2B3A;\n"
"    border: 1px solid #6A5ACD;\n"
"    border-radius: 6px;\n"
"    padding: 6px;\n"
"    color: #FFFFFF;\n"
"    selection-background-color: #6A5ACD;\n"
"}\n"
"\n"
"/* === \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e-\u0444\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u0430\u044f \u043e\u0431\u043b\u0430\u0441\u0442\u044c \u043f\u0440\u043e\u043a\u0440\u0443\u0442\u043a\u0438 === */\n"
"QScrollArea {\n"
"    background-color: rgba(106, 90, 205, 80); /* \u0424\u0438\u043e\u043b\u0435\u0442\u043e\u0432\u044b\u0439 \u0441 \u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c\u044e */\n"
"    border: none;\n"
"}\n"
"\n"
"/* === \u0421\u043a\u0440\u043e\u043b\u043b\u0431\u0430\u0440 === */\n"
"QScrollBar:vertical {\n"
"    background: #333544;\n"
"    width: 8px;\n"
""
                        "    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #6A5ACD;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #7D6DEB;\n"
"}\n"
"\n"
"/* === \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 === */\n"
"QLabel#title {\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF;\n"
"}\n"
"\n"
"/* === \u0412\u044b\u0434\u0435\u043b\u0435\u043d\u043d\u044b\u0435 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u044b (\u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0430\u043a\u0442\u0438\u0432\u043d\u044b\u0435) === */\n"
"QLabel#accent {\n"
"    color: #FFA500;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 151, 41))
        self.custom_image = QPushButton(self.centralwidget)
        self.custom_image.setObjectName(u"custom_image")
        self.custom_image.setGeometry(QRect(10, 59, 151, 41))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 109, 151, 41))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(180, 10, 401, 631))
        self.scrollArea.setStyleSheet(u"color : rgb(255, 170, 0)red\n"
"rgb(26, 13, 200)")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 401, 631))
        self.lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 0, 381, 41))
        self.lineEdit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.lineEdit.setStyleSheet(u"")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.verticalScrollBar = QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setGeometry(QRect(380, 80, 16, 541))
        self.verticalScrollBar.setOrientation(Qt.Orientation.Vertical)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"activate  image", None))
        self.custom_image.setText(QCoreApplication.translate("MainWindow", u"custom image", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"input image ", None))
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"images", None))
    # retranslateUi

