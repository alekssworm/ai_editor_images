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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1035, 833)
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1035, 33))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuimport = QMenu(self.menuBar)
        self.menuimport.setObjectName(u"menuimport")
        self.menusave = QMenu(self.menuBar)
        self.menusave.setObjectName(u"menusave")
        self.menu_preview = QMenu(self.menuBar)
        self.menu_preview.setObjectName(u"menu_preview")
        self.menu_ai_tools = QMenu(self.menuBar)
        self.menu_ai_tools.setObjectName(u"menu_ai_tools")
        self.menutools = QMenu(self.menuBar)
        self.menutools.setObjectName(u"menutools")
        self.menusetting = QMenu(self.menuBar)
        self.menusetting.setObjectName(u"menusetting")
        self.menueffects = QMenu(self.menuBar)
        self.menueffects.setObjectName(u"menueffects")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuimport.menuAction())
        self.menuBar.addAction(self.menusave.menuAction())
        self.menuBar.addAction(self.menu_preview.menuAction())
        self.menuBar.addAction(self.menu_ai_tools.menuAction())
        self.menuBar.addAction(self.menutools.menuAction())
        self.menuBar.addAction(self.menusetting.menuAction())
        self.menuBar.addAction(self.menueffects.menuAction())
        self.menueffects.addSeparator()
        self.menueffects.addAction(self.action1)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.menuimport.setTitle(QCoreApplication.translate("MainWindow", u"import", None))
        self.menusave.setTitle(QCoreApplication.translate("MainWindow", u"save", None))
        self.menu_preview.setTitle(QCoreApplication.translate("MainWindow", u"\n"
"preview", None))
        self.menu_ai_tools.setTitle(QCoreApplication.translate("MainWindow", u"ai tools", None))
        self.menutools.setTitle(QCoreApplication.translate("MainWindow", u"tools", None))
        self.menusetting.setTitle(QCoreApplication.translate("MainWindow", u"setting", None))
        self.menueffects.setTitle(QCoreApplication.translate("MainWindow", u"effects", None))
    # retranslateUi

