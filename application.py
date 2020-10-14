# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
import numpy as np


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(755, 455)
        Form.setStyleSheet("background-color: rgb(100, 100, 100);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 381, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("color: rgb(158, 195, 255);\n"
"background-color: rgb(61, 61, 61);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.process)
        self.label_image = QtWidgets.QLabel(Form)
        self.label_image.setGeometry(QtCore.QRect(346, 90, 391, 261))
        self.label_image.setText("")
        self.label_image.setObjectName("label_image")
        self.label_result = QtWidgets.QLabel(Form)
        self.label_result.setGeometry(QtCore.QRect(350, 410, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(255, 134, 123);\n"
"color: rgb(0, 195, 0);")
        self.label_result.setText("")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 731, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 134, 123);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(350, 370, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 134, 123);\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(360, 50, 361, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 134, 123);\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(20, 110, 311, 201))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 134, 123);")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 134, 123);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 134, 123);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 134, 123);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit_logic = QtWidgets.QTextEdit(self.widget)
        self.textEdit_logic.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_logic.setObjectName("textEdit_logic")
        self.verticalLayout_2.addWidget(self.textEdit_logic)
        self.textEdit_lags = QtWidgets.QTextEdit(self.widget)
        self.textEdit_lags.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_lags.setObjectName("textEdit_lags")
        self.verticalLayout_2.addWidget(self.textEdit_lags)
        self.textEdit_resources = QtWidgets.QTextEdit(self.widget)
        self.textEdit_resources.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_resources.setObjectName("textEdit_resources")
        self.verticalLayout_2.addWidget(self.textEdit_resources)
        self.textEdit_constraints = QtWidgets.QTextEdit(self.widget)
        self.textEdit_constraints.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_constraints.setObjectName("textEdit_constraints")
        self.verticalLayout_2.addWidget(self.textEdit_constraints)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        pixmap = QPixmap("model_loss.png").scaled(self.label_image.size())
        self.label_image.setPixmap(pixmap)
        self.label_image.show()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QEBS"))
        self.pushButton.setText(_translate("Form", "Show Result"))
        self.label_5.setText(_translate("Form", "Quantitative Evaluation for baseline schedule"))
        self.label_6.setText(_translate("Form", "BEI"))
        self.label_7.setText(_translate("Form", "Model Analysis"))
        self.label.setText(_translate("Form", "Logic"))
        self.label_2.setText(_translate("Form", "Lags"))
        self.label_3.setText(_translate("Form", "Resources"))
        self.label_4.setText(_translate("Form", "Hard Constraints"))

    def process(self):
        data = pd.read_excel("Neural Network Data - Copy.xlsx")
        X = data[["Input 1", "Input 2", "Input 3", "Input 4"]].drop(0)
        y = data["Output"].drop(0)

        # define the keras model
        model = Sequential()
        model.add(Dense(32, input_dim=4, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))

        # compile the keras model
        model.compile(loss='mse', optimizer='adam', metrics=['mse', 'mae'])

        # fit model
        history = model.fit(X, y, epochs=350, verbose=1, validation_split=0.15)

        """
        # "Loss"
        plt.plot(history.history['loss'])
        plt.plot(history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'validation'], loc='upper left')
        plt.savefig("model_loss.png")

        """

        self.logic = self.textEdit_logic.toPlainText()
        self.lags = self.textEdit_lags.toPlainText()
        self.resources = self.textEdit_resources.toPlainText()
        self.constraints = self.textEdit_constraints.toPlainText()

        self.values = [float(self.logic), float(self.lags), float(self.resources), float(self.constraints)]
        self.values = np.array(self.values).reshape(1, -1)
        res = model.predict(self.values)[0][0]

        self.label_result.setText(str(res))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
