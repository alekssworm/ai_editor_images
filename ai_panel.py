# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ai_panel.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QSplitter, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(505, 759)
        self.splitter_4 = QSplitter(Dialog)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setGeometry(QRect(0, 0, 100, 30))
        self.splitter_4.setOrientation(Qt.Orientation.Vertical)
        self.splitter_5 = QSplitter(Dialog)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setGeometry(QRect(0, 0, 100, 30))
        self.splitter_5.setOrientation(Qt.Orientation.Vertical)
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 690, 95, 47))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_13 = QPushButton(self.frame_3)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.horizontalLayout.addWidget(self.pushButton_13)

        self.splitter_6 = QSplitter(self.frame)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setGeometry(QRect(0, 0, 484, 348))
        self.splitter_6.setOrientation(Qt.Orientation.Vertical)
        self.splitter_6.setHandleWidth(1)
        self.frame_2 = QFrame(self.splitter_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.splitter_3 = QSplitter(self.frame_2)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_3.setHandleWidth(0)
        self.pushButton_29 = QPushButton(self.splitter_3)
        self.pushButton_29.setObjectName(u"pushButton_29")
        icon = QIcon()
        icon.addFile(u"icons/layers.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_29.setIcon(icon)
        self.pushButton_29.setIconSize(QSize(24, 24))
        self.splitter_3.addWidget(self.pushButton_29)
        self.pushButton_17 = QPushButton(self.splitter_3)
        self.pushButton_17.setObjectName(u"pushButton_17")
        icon1 = QIcon()
        icon1.addFile(u"icons/eye.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_17.setIcon(icon1)
        self.pushButton_17.setIconSize(QSize(24, 24))
        self.splitter_3.addWidget(self.pushButton_17)
        self.pushButton_26 = QPushButton(self.splitter_3)
        self.pushButton_26.setObjectName(u"pushButton_26")
        icon2 = QIcon()
        icon2.addFile(u"icons/pencil.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_26.setIcon(icon2)
        self.pushButton_26.setIconSize(QSize(24, 24))
        self.splitter_3.addWidget(self.pushButton_26)
        self.pushButton_27 = QPushButton(self.splitter_3)
        self.pushButton_27.setObjectName(u"pushButton_27")
        icon3 = QIcon()
        icon3.addFile(u"icons/palette.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_27.setIcon(icon3)
        self.pushButton_27.setIconSize(QSize(24, 24))
        self.splitter_3.addWidget(self.pushButton_27)

        self.verticalLayout.addWidget(self.splitter_3)

        self.splitter = QSplitter(self.frame_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(0)
        self.pushButton_20 = QPushButton(self.splitter)
        self.pushButton_20.setObjectName(u"pushButton_20")
        icon4 = QIcon()
        icon4.addFile(u"icons/arrow-turn-left-down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_20.setIcon(icon4)
        self.pushButton_20.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.pushButton_20)
        self.pushButton = QPushButton(self.splitter)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.pushButton)
        self.pushButton_2 = QPushButton(self.splitter)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.pushButton_2)
        self.pushButton_3 = QPushButton(self.splitter)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.pushButton_3)
        self.pushButton_4 = QPushButton(self.splitter)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon5 = QIcon()
        icon5.addFile(u"icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon5)
        self.splitter.addWidget(self.pushButton_4)
        self.plainTextEdit = QPlainTextEdit(self.splitter)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.splitter.addWidget(self.plainTextEdit)
        self.pushButton_22 = QPushButton(self.splitter)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setIcon(icon)
        self.pushButton_22.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.pushButton_22)

        self.verticalLayout.addWidget(self.splitter)

        self.pushButton_19 = QPushButton(self.frame_2)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.verticalLayout.addWidget(self.pushButton_19)

        self.pushButton_18 = QPushButton(self.frame_2)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.verticalLayout.addWidget(self.pushButton_18)

        self.splitter_6.addWidget(self.frame_2)
        self.frame_4 = QFrame(self.splitter_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton_28 = QPushButton(self.frame_4)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setGeometry(QRect(0, 10, 481, 31))
        icon6 = QIcon()
        icon6.addFile(u"icons/plus-small.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_28.setIcon(icon6)
        self.pushButton_28.setIconSize(QSize(40, 40))
        self.splitter_6.addWidget(self.frame_4)

        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_13.setText(QCoreApplication.translate("Dialog", u"all render", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"scene \u21161", None))
        self.pushButton_29.setText("")
        self.pushButton_17.setText("")
        self.pushButton_26.setText("")
        self.pushButton_27.setText("")
        self.pushButton_20.setText("")
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Dialog", u"add how animated object", None))
        self.pushButton_22.setText("")
        self.pushButton_19.setText(QCoreApplication.translate("Dialog", u"add obj", None))
        self.pushButton_18.setText(QCoreApplication.translate("Dialog", u"render", None))
        self.pushButton_28.setText("")
    # retranslateUi

