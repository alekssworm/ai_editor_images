# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sub_box.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QPushButton, QSizePolicy, QSplitter, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(353, 56)
        self.horizontalLayout = QHBoxLayout(Frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter_16 = QSplitter(Frame)
        self.splitter_16.setObjectName(u"splitter_16")
        self.splitter_16.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_16.setHandleWidth(0)
        self.pushButton_47 = QPushButton(self.splitter_16)
        self.pushButton_47.setObjectName(u"pushButton_47")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_47.sizePolicy().hasHeightForWidth())
        self.pushButton_47.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icons/plus-small.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_47.setIcon(icon)
        self.pushButton_47.setIconSize(QSize(30, 30))
        self.splitter_16.addWidget(self.pushButton_47)
        self.pushButton_12 = QPushButton(self.splitter_16)
        self.pushButton_12.setObjectName(u"pushButton_12")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_12.sizePolicy().hasHeightForWidth())
        self.pushButton_12.setSizePolicy(sizePolicy1)
        icon1 = QIcon()
        icon1.addFile(u"icons/eye.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_12.setIcon(icon1)
        self.pushButton_12.setIconSize(QSize(24, 24))
        self.splitter_16.addWidget(self.pushButton_12)
        self.pen = QPushButton(self.splitter_16)
        self.pen.setObjectName(u"pen")
        sizePolicy.setHeightForWidth(self.pen.sizePolicy().hasHeightForWidth())
        self.pen.setSizePolicy(sizePolicy)
        icon2 = QIcon()
        icon2.addFile(u"icons/pencil.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pen.setIcon(icon2)
        self.pen.setIconSize(QSize(24, 24))
        self.splitter_16.addWidget(self.pen)
        self.trash = QPushButton(self.splitter_16)
        self.trash.setObjectName(u"trash")
        sizePolicy.setHeightForWidth(self.trash.sizePolicy().hasHeightForWidth())
        self.trash.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u"icons/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.trash.setIcon(icon3)
        self.trash.setIconSize(QSize(24, 24))
        self.splitter_16.addWidget(self.trash)
        self.comboBox_6 = QComboBox(self.splitter_16)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        sizePolicy.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy)
        self.splitter_16.addWidget(self.comboBox_6)

        self.horizontalLayout.addWidget(self.splitter_16)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.pushButton_47.setText("")
        self.pushButton_12.setText("")
        self.pen.setText("")
        self.trash.setText("")
        self.comboBox_6.setItemText(0, QCoreApplication.translate("Frame", u"1", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("Frame", u"2", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("Frame", u"3", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("Frame", u"4", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("Frame", u"5", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("Frame", u"6", None))

    # retranslateUi

