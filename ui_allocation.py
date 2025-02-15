# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'allocation.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSlider, QSplitter, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(227, 363)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.layoutWidget = QWidget(self.frame_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 130, 204, 164))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.black = QPushButton(self.layoutWidget)
        self.black.setObjectName(u"black")
        self.black.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"    background-color: #000000;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.black)

        self.red_6 = QPushButton(self.layoutWidget)
        self.red_6.setObjectName(u"red_6")
        self.red_6.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"    background-color: #ffffff;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.red_6)

        self.red_7 = QPushButton(self.layoutWidget)
        self.red_7.setObjectName(u"red_7")
        self.red_7.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"    background-color:  #d1d3d4\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.red_7)

        self.red_9 = QPushButton(self.layoutWidget)
        self.red_9.setObjectName(u"red_9")
        self.red_9.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"   background-color:#808285\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.red_9)

        self.red_17 = QPushButton(self.layoutWidget)
        self.red_17.setObjectName(u"red_17")
        self.red_17.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"     background-color: #58595b\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.red_17)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.red = QPushButton(self.layoutWidget)
        self.red.setObjectName(u"red")
        self.red.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"    background-color: #b31564\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.red)

        self.red_2 = QPushButton(self.layoutWidget)
        self.red_2.setObjectName(u"red_2")
        self.red_2.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"background-color : #e61b1b\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.red_2)

        self.red_5 = QPushButton(self.layoutWidget)
        self.red_5.setObjectName(u"red_5")
        self.red_5.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"background-color : #ff5500\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.red_5)

        self.red_3 = QPushButton(self.layoutWidget)
        self.red_3.setObjectName(u"red_3")
        self.red_3.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"background-color : #ffaa00\n"
"\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.red_3)

        self.red_18 = QPushButton(self.layoutWidget)
        self.red_18.setObjectName(u"red_18")
        self.red_18.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"background-color :#ffe600\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.red_18)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.red_10 = QPushButton(self.layoutWidget)
        self.red_10.setObjectName(u"red_10")
        self.red_10.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"background-color:#a2e61b\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.red_10)

        self.red_8 = QPushButton(self.layoutWidget)
        self.red_8.setObjectName(u"red_8")
        self.red_8.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"background-color: #26e600\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.red_8)

        self.red_16 = QPushButton(self.layoutWidget)
        self.red_16.setObjectName(u"red_16")
        self.red_16.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"background-color: #008055\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.red_16)

        self.red_11 = QPushButton(self.layoutWidget)
        self.red_11.setObjectName(u"red_11")
        self.red_11.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"    background-color: #00aacc\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.red_11)

        self.red_20 = QPushButton(self.layoutWidget)
        self.red_20.setObjectName(u"red_20")
        self.red_20.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"background-color: #004de6\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.red_20)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.red_15 = QPushButton(self.layoutWidget)
        self.red_15.setObjectName(u"red_15")
        self.red_15.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"background-color: #3d00b8\n"
"\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.red_15)

        self.red_14 = QPushButton(self.layoutWidget)
        self.red_14.setObjectName(u"red_14")
        self.red_14.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"background-color: #6600cc\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.red_14)

        self.red_13 = QPushButton(self.layoutWidget)
        self.red_13.setObjectName(u"red_13")
        self.red_13.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"background-color: #ff80ff\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.red_13)

        self.red_12 = QPushButton(self.layoutWidget)
        self.red_12.setObjectName(u"red_12")
        self.red_12.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"background-color: #80ff9e\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.red_12)

        self.red_19 = QPushButton(self.layoutWidget)
        self.red_19.setObjectName(u"red_19")
        self.red_19.setStyleSheet(u"QPushButton {\n"
"    border-radius: 15px;  /* \u0414\u0435\u043b\u0430\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0443 \u043a\u0440\u0443\u0433\u043b\u043e\u0439 */\n"
"    border: 2px solid black; /* \u0427\u0435\u0440\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 \u0432\u043e\u043a\u0440\u0443\u0433 */\n"
"    width: 30px;  /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0448\u0438\u0440\u0438\u043d\u0443 */\n"
"    height: 30px; /* \u0423\u0441\u0442\u0430\u043d\u0430\u0432\u043b\u0438\u0432\u0430\u0435\u0442 \u0432\u044b\u0441\u043e\u0442\u0443 */\n"
"background-color: #80d6ff\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.red_19)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalSlider = QSlider(self.frame_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(0, 320, 151, 22))
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 320, 41, 19))
        self.splitter = QSplitter(self.frame_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 201, 32))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(0)
        self.pushButton = QPushButton(self.splitter)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u"icons/attribution-pencil.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 24))
        self.splitter.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.splitter)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon1 = QIcon()
        icon1.addFile(u"icons/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(24, 20))
        self.splitter.addWidget(self.pushButton_2)
        self.pushButton_3 = QPushButton(self.splitter)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon2 = QIcon()
        icon2.addFile(u"icons/circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(24, 20))
        self.splitter.addWidget(self.pushButton_3)
        self.pushButton_4 = QPushButton(self.splitter)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon()
        icon3.addFile(u"icons/algorithm.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.pushButton_4)

        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.black.setText("")
        self.red_6.setText("")
        self.red_7.setText("")
        self.red_9.setText("")
        self.red_17.setText("")
        self.red.setText("")
        self.red_2.setText("")
        self.red_5.setText("")
        self.red_3.setText("")
        self.red_18.setText("")
        self.red_10.setText("")
        self.red_8.setText("")
        self.red_16.setText("")
        self.red_11.setText("")
        self.red_20.setText("")
        self.red_15.setText("")
        self.red_14.setText("")
        self.red_13.setText("")
        self.red_12.setText("")
        self.red_19.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"0 px", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
    # retranslateUi

