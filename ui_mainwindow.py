################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow, QMenu,
                               QMenuBar, QPushButton, QRadioButton, QSizePolicy,
                               QTextEdit, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(481, 261)
        MainWindow.setMinimumSize(QSize(481, 261))
        MainWindow.setMaximumSize(QSize(481, 261))
        self.open_file = QAction(MainWindow)
        self.open_file.setObjectName(u"open_file")
        self.save_file = QAction(MainWindow)
        self.save_file.setObjectName(u"save_file")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plain_text = QTextEdit(self.centralwidget)
        self.plain_text.setObjectName(u"plain_text")
        self.plain_text.setGeometry(QRect(10, 10, 461, 81))
        self.plain_text.setInputMethodHints(Qt.ImhMultiLine)
        self.cipher_text = QTextEdit(self.centralwidget)
        self.cipher_text.setObjectName(u"cipher_text")
        self.cipher_text.setGeometry(QRect(10, 100, 461, 81))
        self.proc_button = QPushButton(self.centralwidget)
        self.proc_button.setObjectName(u"proc_button")
        self.proc_button.setGeometry(QRect(380, 190, 91, 41))
        self.line_key = QLineEdit(self.centralwidget)
        self.line_key.setObjectName(u"line_key")
        self.line_key.setGeometry(QRect(120, 190, 251, 41))
        self.line_key.setEchoMode(QLineEdit.Normal)
        self.btn_enc = QRadioButton(self.centralwidget)
        self.btn_enc.setObjectName(u"btn_enc")
        self.btn_enc.setEnabled(True)
        self.btn_enc.setGeometry(QRect(10, 190, 121, 22))
        self.btn_dec = QRadioButton(self.centralwidget)
        self.btn_dec.setObjectName(u"btn_dec")
        self.btn_dec.setGeometry(QRect(10, 210, 101, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 481, 21))
        self.menuFile = QMenu(self.menuBar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.open_file)
        self.menuFile.addAction(self.save_file)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u041b\u0430\u0431\u043e\u0440\u0430\u0442\u043e\u0440\u043d\u0430\u044f \u0440\u0430\u0431\u043e\u0442\u0430 11: \u0428\u0438\u0444\u0440 \u0425\u0438\u043b\u043b\u0430",
                                                             None))
        self.open_file.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.save_file.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.proc_button.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c",
                                       None))
        self.line_key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447", None))
        self.btn_enc.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0417\u0430\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c",
                                                        None))
        self.btn_dec.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c",
                                                        None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
    # retranslateUi

