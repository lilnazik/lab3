# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.3
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1080, 746)
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 121, 145, 255), stop:1 rgba(120, 255, 214, 255));\n"
"font-family: Noto Sans SC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.window_title = QLabel(self.centralwidget)
        self.window_title.setObjectName(u"window_title")
        self.window_title.setMinimumSize(QSize(500, 30))
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setPointSize(18)
        self.window_title.setFont(font1)
        self.window_title.setStyleSheet(u"background: none;")
        self.window_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.window_title)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.X_label = QLabel(self.centralwidget)
        self.X_label.setObjectName(u"X_label")
        self.X_label.setMinimumSize(QSize(150, 50))
        self.X_label.setMaximumSize(QSize(150, 50))
        font2 = QFont()
        font2.setFamilies([u"Noto Sans SC"])
        font2.setPointSize(16)
        self.X_label.setFont(font2)
        self.X_label.setStyleSheet(u"background: none;")
        self.X_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.X_label)

        self.X_input = QLineEdit(self.centralwidget)
        self.X_input.setObjectName(u"X_input")
        self.X_input.setMinimumSize(QSize(350, 30))
        self.X_input.setMaximumSize(QSize(500, 30))
        font3 = QFont()
        font3.setFamilies([u"Noto Sans SC"])
        font3.setPointSize(14)
        self.X_input.setFont(font3)
        self.X_input.setStyleSheet(u"background: #F9F9F9;")
        self.X_input.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_3.addWidget(self.X_input)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Y_label = QLabel(self.centralwidget)
        self.Y_label.setObjectName(u"Y_label")
        self.Y_label.setMinimumSize(QSize(150, 50))
        self.Y_label.setMaximumSize(QSize(150, 50))
        self.Y_label.setFont(font2)
        self.Y_label.setStyleSheet(u"background: none;")

        self.verticalLayout.addWidget(self.Y_label)

        self.Y_input = QLineEdit(self.centralwidget)
        self.Y_input.setObjectName(u"Y_input")
        self.Y_input.setMinimumSize(QSize(350, 30))
        self.Y_input.setMaximumSize(QSize(500, 30))
        self.Y_input.setFont(font3)
        self.Y_input.setStyleSheet(u"background: #F9F9F9;")

        self.verticalLayout.addWidget(self.Y_input)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.img_place = QLabel(self.centralwidget)
        self.img_place.setObjectName(u"img_place")
        self.img_place.setMinimumSize(QSize(600, 450))
        self.img_place.setMaximumSize(QSize(600, 450))
        self.img_place.setStyleSheet(u"background: #F9F9F9;")
        self.img_place.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.img_place)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.horizontalLayout_5.setContentsMargins(-1, 0, 0, -1)
        self.calc_btn = QPushButton(self.centralwidget)
        self.calc_btn.setObjectName(u"calc_btn")
        self.calc_btn.setMinimumSize(QSize(250, 50))
        self.calc_btn.setMaximumSize(QSize(250, 50))
        self.calc_btn.setStyleSheet(u"QPushButton{\n"
"background: #F9F9F9;\n"
"border-radius: 20px;\n"
"\n"
"font-family: 'Noto Sans SC';\n"
"font-size: 16px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #95BFFF;     \n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  background-color: #DFECFF;\n"
"}")

        self.horizontalLayout_5.addWidget(self.calc_btn)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.window_title.setText(QCoreApplication.translate("MainWindow", u"I\u043d\u0442\u0435\u0440\u043f\u043e\u043b\u044f\u0446i\u044f \u0442\u0430 \u0435\u043a\u0441\u0442\u0440\u0430\u043f\u043e\u043b\u044f\u0446i\u044f, \u0430\u043f\u0440\u043e\u043a\u0441\u0438\u043c\u0430\u0446i\u044f, \u0440\u0435\u0433\u0440\u0435\u0441i\u044f", None))
        self.X_label.setText(QCoreApplication.translate("MainWindow", u"\u0425 \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0438:", None))
        self.Y_label.setText(QCoreApplication.translate("MainWindow", u"Y \u043a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0438:", None))
        self.img_place.setText("")
        self.calc_btn.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0437\u0440\u0430\u0445\u0443\u0432\u0430\u0442\u0438", None))
    # retranslateUi

