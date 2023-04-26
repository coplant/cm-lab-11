import math
import string
from enum import Enum

import numpy as numpy
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
from ui_mainwindow import Ui_MainWindow


class Application(QMainWindow):
    class Action(Enum):
        ENCRYPT = -1
        DECRYPT = 1

    class Language(Enum):
        RUSSIAN = 0
        ENGLISH = 1

    def __init__(self):
        super(Application, self).__init__()
        self.matrix_size = None
        self.data = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.btn_enc.setChecked(True)

        self.abc = "abcdefghijklmnopqrstuvwxyzабвгдеёжзийклмнопрстуфхцчшщъыьэюя ."  # 61 - prime number
        # self.abc = "abcdefghijklmnopqrstuvwxyz"  # 61 - prime number

        self.ui.proc_button.clicked.connect(self.process_data)
        self.ui.open_file.triggered.connect(self.open)
        self.ui.save_file.triggered.connect(self.save)

    def process_data(self):
        self.data = self.ui.plain_text.toPlainText()
        try:
            if self.ui.btn_enc.isChecked():
                self.data = self.crypt_text(self.Action.ENCRYPT.value)
            elif self.ui.btn_dec.isChecked():
                self.data = self.crypt_text(self.Action.DECRYPT.value)
        except ValueError as e:
            ...
        self.ui.cipher_text.setText(str(self.data))

    def validate_key(self):
        plain_key = self.ui.line_key.text().lower().strip()
        key = []
        for char in plain_key:
            if char in self.abc:
                key.append(self.abc.index(char))
        while not math.sqrt(len(key)).is_integer():
            key.append(self.abc.index(" "))
        self.matrix_size = int(math.sqrt(len(key)))
        return key

    def validate_plain_text(self):
        text = []
        for char in self.ui.plain_text.toPlainText().lower().strip():
            if char not in self.abc:
                char = " "
            text.append(self.abc.index(char))
        while (len(text) + self.matrix_size) % self.matrix_size:
            text.append(self.abc.index(" "))
        return text

    def crypt_text(self, choice):
        text = []
        if choice == self.Action.ENCRYPT.value:
            key = numpy.reshape(self.validate_key(), (self.matrix_size, self.matrix_size))
            if numpy.linalg.det(key) == 0:
                return QMessageBox.information(self, "Ошибка", "Определитель == 0", QMessageBox.Ok)
            plaintext = self.validate_plain_text()
            plaintext = numpy.reshape(plaintext, (len(plaintext) // self.matrix_size, self.matrix_size))
            for item in plaintext:
                text.append(list(map(lambda x: x % len(self.abc), numpy.matmul(key, item))))
            return text

    def open(self):
        file_name = QFileDialog.getOpenFileName(self, "Открыть файл", ".", "All Files (*)")
        if file_name[0]:
            with open(file_name[0], "r") as file:
                self.data = file.read()
                self.ui.plain_text.setText(self.data)
        else:
            QMessageBox.information(self, "Ошибка", "Файл не выбран", QMessageBox.Ok)

    def save(self):
        file_name = QFileDialog.getSaveFileName(self, "Сохранить файл", ".", "All Files (*)")
        if file_name[0]:
            with open(file_name[0], "w") as file:
                file.write(self.ui.cipher_text.toPlainText())
        else:
            QMessageBox.information(self, "Ошибка", "Файл не выбран", QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication()
    window = Application()
    app.exec()
