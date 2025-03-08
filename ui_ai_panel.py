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
from PySide6.QtWidgets import (QApplication, QDockWidget, QHBoxLayout, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(357, 649)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.horizontalLayout = QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.dockWidgetContents)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.add_sceen = QPushButton(self.widget)
        self.add_sceen.setObjectName(u"add_sceen")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_sceen.sizePolicy().hasHeightForWidth())
        self.add_sceen.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"icons/plus-small.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.add_sceen.setIcon(icon)
        self.add_sceen.setIconSize(QSize(40, 40))

        self.verticalLayout.addWidget(self.add_sceen)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 317, 495))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.all_render = QPushButton(self.widget)
        self.all_render.setObjectName(u"all_render")
        sizePolicy.setHeightForWidth(self.all_render.sizePolicy().hasHeightForWidth())
        self.all_render.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.all_render)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.widget)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"DockWidget", None))
        self.add_sceen.setText("")
        self.all_render.setText(QCoreApplication.translate("DockWidget", u"all render", None))
    # retranslateUi

