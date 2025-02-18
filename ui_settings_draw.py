# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_draw.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSplitter, QWidget)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(265, 170)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.gridLayout = QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.dockWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalSlider = QSlider(self.frame)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(0, 60, 201, 22))
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_2 = QSlider(self.frame)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(0, 100, 201, 22))
        self.horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 40, 56, 19))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 80, 91, 19))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(200, 60, 41, 20))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 100, 41, 20))
        self.splitter = QSplitter(self.frame)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 251, 32))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.splitter.setHandleWidth(0)
        self.pushButton_30 = QPushButton(self.splitter)
        self.pushButton_30.setObjectName(u"pushButton_30")
        icon = QIcon()
        icon.addFile(u"icons/attribution-pencil.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_30.setIcon(icon)
        self.pushButton_30.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.pushButton_30)
        self.pushButton_21 = QPushButton(self.splitter)
        self.pushButton_21.setObjectName(u"pushButton_21")
        icon1 = QIcon()
        icon1.addFile(u"icons/circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_21.setIcon(icon1)
        self.pushButton_21.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.pushButton_21)
        self.pushButton_27 = QPushButton(self.splitter)
        self.pushButton_27.setObjectName(u"pushButton_27")
        icon2 = QIcon()
        icon2.addFile(u"icons/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_27.setIcon(icon2)
        self.pushButton_27.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.pushButton_27)
        self.colour_2 = QPushButton(self.splitter)
        self.colour_2.setObjectName(u"colour_2")
        icon3 = QIcon()
        icon3.addFile(u"icons/algorithm.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.colour_2.setIcon(icon3)
        self.colour_2.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.colour_2)
        self.colour_3 = QPushButton(self.splitter)
        self.colour_3.setObjectName(u"colour_3")
        icon4 = QIcon()
        icon4.addFile(u"icons/palette.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.colour_3.setIcon(icon4)
        self.colour_3.setIconSize(QSize(24, 24))
        self.splitter.addWidget(self.colour_3)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"DockWidget", None))
        self.label.setText(QCoreApplication.translate("DockWidget", u"size", None))
        self.label_2.setText(QCoreApplication.translate("DockWidget", u"transparency", None))
        self.label_3.setText(QCoreApplication.translate("DockWidget", u"0 px", None))
        self.label_4.setText(QCoreApplication.translate("DockWidget", u"0 px", None))
        self.pushButton_30.setText("")
        self.pushButton_21.setText("")
        self.pushButton_27.setText("")
        self.colour_2.setText("")
        self.colour_3.setText("")
    # retranslateUi

