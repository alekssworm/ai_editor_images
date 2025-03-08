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
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

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
        self.splitter = QSplitter(self.groupBox_3)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(0)
        self.hide_unhide = QPushButton(self.splitter)
        self.hide_unhide.setObjectName(u"hide_unhide")
        icon = QIcon()
        icon.addFile(u"icons/arrow chevron down.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.hide_unhide.setIcon(icon)
        self.hide_unhide.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.hide_unhide)
        self.add_sub_sceen = QPushButton(self.splitter)
        self.add_sub_sceen.setObjectName(u"add_sub_sceen")
        sizePolicy.setHeightForWidth(self.add_sub_sceen.sizePolicy().hasHeightForWidth())
        self.add_sub_sceen.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"icons/plus-small.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_sub_sceen.setIcon(icon1)
        self.add_sub_sceen.setIconSize(QSize(30, 30))
        self.splitter.addWidget(self.add_sub_sceen)
        self.pushButton_14 = QPushButton(self.splitter)
        self.pushButton_14.setObjectName(u"pushButton_14")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_14.sizePolicy().hasHeightForWidth())
        self.pushButton_14.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u"icons/eye.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_14.setIcon(icon2)
        self.pushButton_14.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.pushButton_14)
        self.pen = QPushButton(self.splitter)
        self.pen.setObjectName(u"pen")
        sizePolicy.setHeightForWidth(self.pen.sizePolicy().hasHeightForWidth())
        self.pen.setSizePolicy(sizePolicy)
        icon3 = QIcon()
        icon3.addFile(u"icons/pencil.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pen.setIcon(icon3)
        self.pen.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.pen)
        self.pushButton_15 = QPushButton(self.splitter)
        self.pushButton_15.setObjectName(u"pushButton_15")
        sizePolicy.setHeightForWidth(self.pushButton_15.sizePolicy().hasHeightForWidth())
        self.pushButton_15.setSizePolicy(sizePolicy)
        icon4 = QIcon()
        icon4.addFile(u"icons/search.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_15.setIcon(icon4)
        self.splitter.addWidget(self.pushButton_15)
        self.comboBox_7 = QComboBox(self.splitter)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        sizePolicy.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.comboBox_7)

        self.gridLayout_6.addWidget(self.splitter, 1, 0, 1, 1)

        self.splitter_10 = QSplitter(self.groupBox_3)
        self.splitter_10.setObjectName(u"splitter_10")
        self.splitter_10.setOrientation(Qt.Orientation.Horizontal)
        self.splitter_10.setHandleWidth(0)
        self.pushButton_49 = QPushButton(self.splitter_10)
        self.pushButton_49.setObjectName(u"pushButton_49")
        sizePolicy.setHeightForWidth(self.pushButton_49.sizePolicy().hasHeightForWidth())
        self.pushButton_49.setSizePolicy(sizePolicy)
        icon5 = QIcon()
        icon5.addFile(u"icons/layers.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_49.setIcon(icon5)
        self.pushButton_49.setIconSize(QSize(24, 24))
        self.splitter_10.addWidget(self.pushButton_49)
        self.pushButton_50 = QPushButton(self.splitter_10)
        self.pushButton_50.setObjectName(u"pushButton_50")
        sizePolicy.setHeightForWidth(self.pushButton_50.sizePolicy().hasHeightForWidth())
        self.pushButton_50.setSizePolicy(sizePolicy)
        self.pushButton_50.setIcon(icon2)
        self.pushButton_50.setIconSize(QSize(24, 24))
        self.splitter_10.addWidget(self.pushButton_50)
        self.trash = QPushButton(self.splitter_10)
        self.trash.setObjectName(u"trash")
        sizePolicy.setHeightForWidth(self.trash.sizePolicy().hasHeightForWidth())
        self.trash.setSizePolicy(sizePolicy)
        icon6 = QIcon()
        icon6.addFile(u"icons/trash.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.trash.setIcon(icon6)
        self.trash.setIconSize(QSize(24, 24))
        self.splitter_10.addWidget(self.trash)

        self.gridLayout_6.addWidget(self.splitter_10, 0, 0, 1, 1)

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

        self.gridLayout_6.addWidget(self.splitter_17, 7, 0, 1, 1)

        self.scrollArea = QScrollArea(self.groupBox_3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 303, 54))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_6.addWidget(self.scrollArea, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Frame", u"Sceen 1", None))
        self.hide_unhide.setText("")
        self.add_sub_sceen.setText("")
        self.pushButton_14.setText("")
        self.pen.setText("")
        self.pushButton_15.setText("")
        self.comboBox_7.setItemText(0, QCoreApplication.translate("Frame", u"1", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("Frame", u"2", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("Frame", u"3", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("Frame", u"4", None))
        self.comboBox_7.setItemText(4, QCoreApplication.translate("Frame", u"5", None))
        self.comboBox_7.setItemText(5, QCoreApplication.translate("Frame", u"6", None))

        self.pushButton_49.setText("")
        self.pushButton_50.setText("")
        self.trash.setText("")
        self.pushButton_48.setText(QCoreApplication.translate("Frame", u"add obj", None))
        self.pushButton_52.setText(QCoreApplication.translate("Frame", u"render", None))
    # retranslateUi

