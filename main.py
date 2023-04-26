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
        # self.abc = "abcdefghijklmnopqrstuvwxyz"

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

    def numbers_to_text(self, text):
        result = ""
        for row in text:
            for char in row:
                result += self.abc[char]
        return result

    def crypt_text(self, choice):
        text = []
        key = numpy.reshape(self.validate_key(), (self.matrix_size, self.matrix_size))
        det_key = numpy.linalg.det(key)
        if det_key == 0:
            return QMessageBox.information(self, "Ошибка", "Определитель == 0", QMessageBox.Ok)
        if choice == self.Action.DECRYPT.value:
            key = self.mod_matrix_inversion(key, len(self.abc))
        key = numpy.rint(key).astype(int)
        plaintext = self.validate_plain_text()
        plaintext = numpy.reshape(plaintext, (len(plaintext) // self.matrix_size, self.matrix_size))
        for item in plaintext:
            text.append(list(map(lambda x: int(x % len(self.abc)), numpy.matmul(key, item))))
        return self.numbers_to_text(text)

    def mod_matrix_inversion(self, matrix, p):
        n = len(matrix)
        A = numpy.matrix(matrix)
        adj = numpy.zeros(shape=(n, n))
        for i in range(0, n):
            for j in range(0, n):
                adj[i][j] = ((-1)**(i + j) * int(round(numpy.linalg.det(self.minor(matrix, j, i))))) % p
        return (self.mod_inversion(int(round(numpy.linalg.det(matrix))), p) * adj) % p

    def mod_inversion(self, a, p):
        for i in range(1, p):
            if (i * a) % p == 1:
                return i
        raise ValueError(str(a) + " has no inverse mod " + str(p))

    def minor(self, matrix, i, j):
        matrix = numpy.array(matrix)
        minor = numpy.zeros(shape=(len(matrix) - 1, len(matrix) - 1))
        p = 0
        for s in range(0, len(minor)):
            if p == i:
                p = p + 1
            q = 0
            for t in range(0, len(minor)):
                if q == j:
                    q = q + 1
                minor[s][t] = matrix[p][q]
                q = q + 1
            p = p + 1
        return minor

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
