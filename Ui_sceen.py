# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_sceen.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSplitter, QWidget)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(325, 198)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_3 = QGroupBox(Frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setLocale(QLocale(QLocale.Ukrainian, QLocale.Ukraine))
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setCheckable(False)
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.groupBox_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 303, 54))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_6.addWidget(self.scrollArea, 2, 0, 1, 1)

        self.splitter_17 = QSplitter(self.groupBox_3)
        self.splitter_17.setObjectName(u"splitter_17")
        sizePolicy.setHeightForWidth(self.splitter_17.sizePolicy().hasHeightForWidth())
        self.splitter_17.setSizePolicy(sizePolicy)
        self.splitter_17.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_17.setHandleWidth(0)
        self.pushButton_48 = QPushButton(self.splitter_17)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.splitter_17.addWidget(self.pushButton_48)
        self.pushButton_52 = QPushButton(self.splitter_17)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.splitter_17.addWidget(self.pushButton_52)

        self.gridLayout_6.addWidget(self.splitter_17, 6, 0, 1, 1)

        self.splitter_14 = QSplitter(self.groupBox_3)
        self.splitter_14.setObjectName(u"splitter_14")
        self.splitter_14.setOrientation(Qt.Orientation.Vertical)
        self.splitter_14.setHandleWidth(0)
        self.splitter_16 = QSplitter(self.splitter_14)
        self.splitter_16.setObjectName(u"splitter_16")
        self.splitter_16.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_16.setHandleWidth(0)
        self.add_sub_sceen = QPushButton(self.splitter_16)
        self.add_sub_sceen.setObjectName(u"add_sub_sceen")
        sizePolicy.setHeightForWidth(self.add_sub_sceen.sizePolicy().hasHeightForWidth())
        self.add_sub_sceen.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icons/plus-small.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_sub_sceen.setIcon(icon)
        self.add_sub_sceen.setIconSize(QSize(30, 30))
        self.splitter_16.addWidget(self.add_sub_sceen)
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
        self.pushButton_13 = QPushButton(self.splitter_16)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u"icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_13.setIcon(icon3)
        self.splitter_16.addWidget(self.pushButton_13)
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
        self.splitter_14.addWidget(self.splitter_16)

        self.gridLayout_6.addWidget(self.splitter_14, 1, 0, 1, 1)

        self.splitter_10 = QSplitter(self.groupBox_3)
        self.splitter_10.setObjectName(u"splitter_10")
        self.splitter_10.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_10.setHandleWidth(0)
        self.pushButton_49 = QPushButton(self.splitter_10)
        self.pushButton_49.setObjectName(u"pushButton_49")
        sizePolicy.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u"icons/layers.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_49.setIcon(icon4)
        self.pushButton_49.setIconSize(QSize(24, 24))
        self.splitter_10.addWidget(self.pushButton_49)
        self.pushButton_50 = QPushButton(self.splitter_10)
        self.pushButton_50.setObjectName(u"pushButton_50")
        sizePolicy.setHeightForWidth(self.pushButton_50.sizePolicy().hasHeightForWidth())
        self.pushButton_50.setSizePolicy(sizePolicy)
        self.pushButton_50.setIcon(icon1)
        self.pushButton_50.setIconSize(QSize(24, 24))
        self.splitter_10.addWidget(self.pushButton_50)
        self.pushButton_51 = QPushButton(self.splitter_10)
        self.pushButton_51.setObjectName(u"pushButton_51")
        sizePolicy.setHeightForWidth(self.pushButton_51.sizePolicy().hasHeightForWidth())
        self.pushButton_51.setSizePolicy(sizePolicy)
        self.pushButton_51.setIcon(icon2)
        self.pushButton_51.setIconSize(QSize(24, 24))
        self.splitter_10.addWidget(self.pushButton_51)

        self.gridLayout_6.addWidget(self.splitter_10, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Frame", u"Sceen 1", None))
        self.pushButton_48.setText(QCoreApplication.translate("Frame", u"add obj", None))
        self.pushButton_52.setText(QCoreApplication.translate("Frame", u"render", None))
        self.add_sub_sceen.setText("")
        self.pushButton_12.setText("")
        self.pen.setText("")
        self.pushButton_13.setText("")
        self.comboBox_6.setItemText(0, QCoreApplication.translate("Frame", u"1", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("Frame", u"2", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("Frame", u"3", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("Frame", u"4", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("Frame", u"5", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("Frame", u"6", None))

        self.pushButton_49.setText("")
        self.pushButton_50.setText("")
        self.pushButton_51.setText("")
    # retranslateUi

