# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editor.ui'
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
    QLabel, QLineEdit, QProgressBar, QPushButton,
    QSizePolicy, QSplitter, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1296, 801)
        self.progressBar = QProgressBar(Dialog)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 770, 151, 23))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.progressBar.setValue(24)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(1000, 20, 291, 779))
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.toolButton = QToolButton(self.widget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(260, 0, 31, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy1)
        self.toolButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(190, 740, 80, 27))
        sizePolicy1.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy1)
        self.pushButton_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(7, 720, 261, 20))
        sizePolicy1.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy1)
        self.line_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 20, 271, 141))
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.pushButton_2 = QPushButton(self.widget_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 100, 61, 27))
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.line_3 = QFrame(self.widget_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(0, 130, 271, 20))
        sizePolicy1.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy1)
        self.line_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)
        self.layoutWidget = QWidget(self.widget_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(11, 15, 251, 74))
        sizePolicy1.setHeightForWidth(self.layoutWidget.sizePolicy().hasHeightForWidth())
        self.layoutWidget.setSizePolicy(sizePolicy1)
        self.layoutWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.penorfigure = QFrame(self.layoutWidget)
        self.penorfigure.setObjectName(u"penorfigure")
        sizePolicy1.setHeightForWidth(self.penorfigure.sizePolicy().hasHeightForWidth())
        self.penorfigure.setSizePolicy(sizePolicy1)
        self.penorfigure.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.penorfigure.setFrameShape(QFrame.Shape.StyledPanel)
        self.penorfigure.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.penorfigure, 2, 1, 1, 1)

        self.hide_unhide = QFrame(self.layoutWidget)
        self.hide_unhide.setObjectName(u"hide_unhide")
        sizePolicy1.setHeightForWidth(self.hide_unhide.sizePolicy().hasHeightForWidth())
        self.hide_unhide.setSizePolicy(sizePolicy1)
        self.hide_unhide.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.hide_unhide.setFrameShape(QFrame.Shape.StyledPanel)
        self.hide_unhide.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.hide_unhide, 4, 0, 1, 1)

        self.colour_2 = QFrame(self.layoutWidget)
        self.colour_2.setObjectName(u"colour_2")
        sizePolicy1.setHeightForWidth(self.colour_2.sizePolicy().hasHeightForWidth())
        self.colour_2.setSizePolicy(sizePolicy1)
        self.colour_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.colour_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.colour_2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.colour_2, 4, 2, 1, 1)

        self.colour_3 = QFrame(self.layoutWidget)
        self.colour_3.setObjectName(u"colour_3")
        sizePolicy1.setHeightForWidth(self.colour_3.sizePolicy().hasHeightForWidth())
        self.colour_3.setSizePolicy(sizePolicy1)
        self.colour_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.colour_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.colour_3.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.colour_3, 2, 4, 1, 1)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy1)
        self.lineEdit_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.lineEdit_2, 4, 3, 1, 1)

        self.penorfigure_2 = QFrame(self.layoutWidget)
        self.penorfigure_2.setObjectName(u"penorfigure_2")
        sizePolicy1.setHeightForWidth(self.penorfigure_2.sizePolicy().hasHeightForWidth())
        self.penorfigure_2.setSizePolicy(sizePolicy1)
        self.penorfigure_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.penorfigure_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.penorfigure_2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.penorfigure_2, 4, 1, 1, 1)

        self.colour_4 = QFrame(self.layoutWidget)
        self.colour_4.setObjectName(u"colour_4")
        sizePolicy1.setHeightForWidth(self.colour_4.sizePolicy().hasHeightForWidth())
        self.colour_4.setSizePolicy(sizePolicy1)
        self.colour_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.colour_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.colour_4.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.colour_4, 4, 4, 1, 1)

        self.colour = QFrame(self.layoutWidget)
        self.colour.setObjectName(u"colour")
        sizePolicy1.setHeightForWidth(self.colour.sizePolicy().hasHeightForWidth())
        self.colour.setSizePolicy(sizePolicy1)
        self.colour.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.colour.setFrameShape(QFrame.Shape.StyledPanel)
        self.colour.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.colour, 2, 2, 1, 1)

        self.hide_unhide_2 = QFrame(self.layoutWidget)
        self.hide_unhide_2.setObjectName(u"hide_unhide_2")
        sizePolicy1.setHeightForWidth(self.hide_unhide_2.sizePolicy().hasHeightForWidth())
        self.hide_unhide_2.setSizePolicy(sizePolicy1)
        self.hide_unhide_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.hide_unhide_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.hide_unhide_2.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.hide_unhide_2, 2, 0, 1, 1)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout.addWidget(self.lineEdit, 2, 3, 1, 1)

        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 533, 27))
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.pushButton_13 = QPushButton(self.splitter)
        self.pushButton_13.setObjectName(u"pushButton_13")
        sizePolicy1.setHeightForWidth(self.pushButton_13.sizePolicy().hasHeightForWidth())
        self.pushButton_13.setSizePolicy(sizePolicy1)
        self.pushButton_13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.splitter.addWidget(self.pushButton_13)
        self.pushButton_10 = QPushButton(self.splitter)
        self.pushButton_10.setObjectName(u"pushButton_10")
        sizePolicy1.setHeightForWidth(self.pushButton_10.sizePolicy().hasHeightForWidth())
        self.pushButton_10.setSizePolicy(sizePolicy1)
        self.pushButton_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.splitter.addWidget(self.pushButton_10)
        self.pushButton = QPushButton(self.splitter)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.splitter.addWidget(self.pushButton)
        self.pushButton_3 = QPushButton(self.splitter)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.splitter.addWidget(self.pushButton_3)
        self.toolButton_2 = QToolButton(self.splitter)
        self.toolButton_2.setObjectName(u"toolButton_2")
        sizePolicy1.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy1)
        self.toolButton_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.splitter.addWidget(self.toolButton_2)
        self.pushButton_5 = QPushButton(self.splitter)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy1.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy1)
        self.pushButton_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.splitter.addWidget(self.pushButton_5)
        self.pushButton_6 = QPushButton(self.splitter)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.splitter.addWidget(self.pushButton_6)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 30, 51, 701))
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 51, 20))
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.widget1 = QWidget(self.frame)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(0, 30, 51, 671))
        self.verticalLayout = QVBoxLayout(self.widget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_15 = QFrame(self.widget1)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_15)

        self.frame_2 = QFrame(self.widget1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_2)

        self.frame_16 = QFrame(self.widget1)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_16)

        self.frame_4 = QFrame(self.widget1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.widget1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_3)

        self.frame_17 = QFrame(self.widget1)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_17)

        self.frame_6 = QFrame(self.widget1)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.widget1)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.widget1)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.widget1)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.widget1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_11)

        self.frame_5 = QFrame(self.widget1)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_5)

        self.frame_9 = QFrame(self.widget1)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_9)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.toolButton.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"act", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"render", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Dialog", u"Scene", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog", u"Object", None))
        self.pushButton_13.setText(QCoreApplication.translate("Dialog", u"\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c ", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u043f\u0440\u0438\u0432\u044c\u044e", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"setting", None))
        self.toolButton_2.setText(QCoreApplication.translate("Dialog", u"ai edit", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"\u0442\u0435\u043a\u0441\u0442\u0443\u0440\u044b", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"\u044d\u0444\u0435\u043a\u0442\u044b", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u044d\u0444\u0435\u043a\u0442\u044b", None))
    # retranslateUi

