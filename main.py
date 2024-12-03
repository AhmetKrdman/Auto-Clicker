from PyQt5 import QtCore, QtGui, QtWidgets
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, Key, KeyCode
from time import sleep
from threading import Thread
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(395, 266)
        MainWindow.setMinimumSize(QtCore.QSize(395, 266))
        MainWindow.setMaximumSize(QtCore.QSize(395, 266))
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ClickInvertal = QtWidgets.QGroupBox(self.centralwidget)
        self.ClickInvertal.setGeometry(QtCore.QRect(10, 10, 181, 141))
        self.ClickInvertal.setObjectName("ClickInvertal")
        self.SpinMilisecond = QtWidgets.QSpinBox(self.ClickInvertal)
        self.SpinMilisecond.setGeometry(QtCore.QRect(110, 100, 61, 22))
        self.SpinMilisecond.setRange(0, 100000)
        self.SpinMilisecond.setObjectName("SpinMilisecond")
        self.SpinSecond = QtWidgets.QSpinBox(self.ClickInvertal)
        self.SpinSecond.setGeometry(QtCore.QRect(110, 60, 61, 22))
        self.SpinSecond.setRange(0, 100000)
        self.SpinSecond.setObjectName("SpinSecond")
        self.SpinMinute = QtWidgets.QSpinBox(self.ClickInvertal)
        self.SpinMinute.setGeometry(QtCore.QRect(110, 20, 61, 22))
        self.SpinMinute.setRange(0, 100000)
        self.SpinMinute.setObjectName("SpinMinute")
        self.LabelMinute = QtWidgets.QLabel(self.ClickInvertal)
        self.LabelMinute.setGeometry(QtCore.QRect(10, 25, 81, 16))
        self.LabelMinute.setObjectName("LabelMinute")
        self.LabeSecond = QtWidgets.QLabel(self.ClickInvertal)
        self.LabeSecond.setGeometry(QtCore.QRect(10, 60, 81, 16))
        self.LabeSecond.setObjectName("LabeSecond")
        self.LabelMilisecond = QtWidgets.QLabel(self.ClickInvertal)
        self.LabelMilisecond.setGeometry(QtCore.QRect(10, 100, 81, 16))
        self.LabelMilisecond.setObjectName("LabelMilisecond")
        self.ClickOptions = QtWidgets.QGroupBox(self.centralwidget)
        self.ClickOptions.setGeometry(QtCore.QRect(200, 10, 181, 141))
        self.ClickOptions.setObjectName("ClickOptions")
        self.ComboButton = QtWidgets.QComboBox(self.ClickOptions)
        self.ComboButton.setGeometry(QtCore.QRect(90, 35, 69, 22))
        self.ComboButton.setObjectName("ComboButton")
        self.ComboButton.addItem("")
        self.ComboButton.addItem("")
        self.ComboType = QtWidgets.QComboBox(self.ClickOptions)
        self.ComboType.setGeometry(QtCore.QRect(90, 90, 69, 22))
        self.ComboType.setObjectName("ComboType")
        self.ComboType.addItem("")
        self.ComboType.addItem("")
        self.LabelClickButton = QtWidgets.QLabel(self.ClickOptions)
        self.LabelClickButton.setGeometry(QtCore.QRect(10, 35, 61, 20))
        self.LabelClickButton.setObjectName("LabelClickButton")
        self.LabelClickType = QtWidgets.QLabel(self.ClickOptions)
        self.LabelClickType.setGeometry(QtCore.QRect(10, 90, 61, 20))
        self.LabelClickType.setObjectName("LabelClickType")
        self.ButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonStart.setGeometry(QtCore.QRect(10, 160, 181, 31))
        self.ButtonStart.setObjectName("ButtonStart")
        self.ButtonStop = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonStop.setGeometry(QtCore.QRect(200, 160, 181, 31))
        self.ButtonStop.setEnabled(False)
        self.ButtonStop.setObjectName("ButtonStop")
        self.ButtonChange = QtWidgets.QPushButton(self.centralwidget)
        self.ButtonChange.setGeometry(QtCore.QRect(10, 200, 371, 31))
        self.ButtonChange.setObjectName("ButtonChange")
        self.LabelStatus = QtWidgets.QLabel(self.centralwidget)
        self.LabelStatus.setGeometry(QtCore.QRect(16, 240, 361, 20))
        self.LabelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelStatus.setObjectName("LabelStatus")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.SpinMinute, self.SpinSecond)
        MainWindow.setTabOrder(self.SpinSecond, self.SpinMilisecond)
        MainWindow.setTabOrder(self.SpinMilisecond, self.ComboButton)
        MainWindow.setTabOrder(self.ComboButton, self.ComboType)

        self.ButtonStart.clicked.connect(self.toggle_clicking)
        self.ButtonStop.clicked.connect(self.toggle_clicking)
        self.ButtonChange.clicked.connect(self.start_listening_for_key)

        self.button = getattr(Button, self.ComboButton.currentText().lower())
        self.click_count = self.ComboType.currentIndex() + 1
        self.clicking = False
        self.listening_key = False
        self.start_stop_key = KeyCode(char="f6")

        self.listener_keyboard = Listener(on_press=self.on_press_keyboard)
        self.listener_keyboard.start()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Auto Clicker"))
        self.ClickInvertal.setTitle(_translate("MainWindow", "Click Interval"))
        self.LabelMinute.setText(_translate("MainWindow", "Minute"))
        self.LabeSecond.setText(_translate("MainWindow", "Second"))
        self.LabelMilisecond.setText(_translate("MainWindow", "Milisecond"))
        self.ClickOptions.setTitle(_translate("MainWindow", "Click Options"))
        self.ComboButton.setItemText(0, _translate("MainWindow", "Left"))
        self.ComboButton.setItemText(1, _translate("MainWindow", "Right"))
        self.ComboType.setItemText(0, _translate("MainWindow", "Single"))
        self.ComboType.setItemText(1, _translate("MainWindow", "Double"))
        self.LabelClickButton.setText(_translate("MainWindow", "Click Button"))
        self.LabelClickType.setText(_translate("MainWindow", "Click Type"))
        self.ButtonStart.setText(_translate("MainWindow", "Start (F6)"))
        self.ButtonStop.setText(_translate("MainWindow", "Stop (F6)"))
        self.ButtonChange.setText(_translate("MainWindow", "Start Stop Hotkey Change"))
        self.LabelStatus.setText(_translate("MainWindow", "Status: Waiting"))

    def start_listening_for_key(self):
        self.listening_key = True
        self.pending_modifier_key = None
        self.LabelStatus.setText("Status: Press a key for Start/Stop Hotkey...")

    def get_key_display(self, key):
        if isinstance(key, KeyCode):
            return key.char or key.vk
        elif isinstance(key, Key):
            return key.name
        return str(key)

    def on_press_keyboard(self, key):
        if (self.listening_key):
            if isinstance(key, Key):
                self.LabelStatus.setText(f"Modifier key detected: {self.get_key_display(key).upper()}. Press another key...")
                self.pending_modifier_key = key
            elif self.pending_modifier_key:
                self.start_stop_key = (self.pending_modifier_key, key)
                self.ButtonStart.setText(f"Start ({self.get_key_display(self.pending_modifier_key).upper()} + {self.get_key_display(key).upper()})")
                self.ButtonStop.setText(f"Stop ({self.get_key_display(self.pending_modifier_key).upper()} + {self.get_key_display(key).upper()})")
                self.is_listening_for_key = False
                self.LabelStatus.setText("Status: Hotkey changed!")
                self.listening_key = False
            else:
                self.start_stop_key = key
                self.ButtonStart.setText(f"Start ({self.get_key_display(key).upper()})")
                self.ButtonStop.setText(f"Stop ({self.get_key_display(key).upper()})")
                self.LabelStatus.setText("Status: Hotkey changed!")
                self.listening_key = False
        else:
            if (isinstance(self.start_stop_key, tuple)):
                if (key == self.start_stop_key[1] and self.pending_modifier_key == self.start_stop_key[0]):
                    self.toggle_clicking()
            elif (key == self.start_stop_key):
                self.toggle_clicking()

    def toggle_clicking(self):
        if (not self.clicking):
            self.button = getattr(Button, self.ComboButton.currentText().lower())
            self.click_count = self.ComboType.currentIndex() + 1
            self.interval = (self.SpinMinute.value() * 60) + (self.SpinSecond.value()) + (self.SpinMilisecond.value() / 1000)
            if ((self.interval * 1000) == 0):
                self.LabelStatus.setText("Error: Click interval cannot be 0 milliseconds!")
            else:
                self.clicking = True
                self.ButtonStart.setEnabled(False)
                self.ButtonStop.setEnabled(True)
                self.LabelStatus.setText("Status: Clicking started!")
                self.click_thread = Thread(target=self.auto_click, daemon=True)
                self.click_thread.start()
        else:
            self.ButtonStop.setEnabled(False)
            self.ButtonStart.setEnabled(True)
            self.LabelStatus.setText("Status: Clicking stopped!")
            self.clicking = False
            if (self.click_thread):
                self.click_thread.join()

    def auto_click(self):
        mouse = Controller()
        while self.clicking:
            mouse.click(self.button, self.click_count)
            sleep(self.interval)
            

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())