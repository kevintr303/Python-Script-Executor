import subprocess

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
import sys
import easygui


global script
global stop

# Preferences
clearConsoleOnScriptChanged = True


class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        # QtDesigner Code
        self.setObjectName("self")
        self.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(800, 600))
        self.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.setFont(font)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 20, 741, 371))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.textBrowser.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setDocumentTitle("")
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setHtml(
            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
            "p, li { white-space: pre-wrap; }\n"
            "</style></head><body style=\" font-family:\'Source Sans Pro\'; font-size:10pt; font-weight:600; font-style:normal;\">\n"
            "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:125%; background-color:#f8f8f8;\"><span style=\" font-family:\'Courier New\'; font-weight:400; font-style:italic; color:#408080;\"># No script is currently opened. Use CTRL+O or File &gt; Open Python Script to open a script</span></p></body></html>")
        self.textBrowser.setOverwriteMode(False)
        self.textBrowser.setTabStopDistance(80.0)
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setPlaceholderText("")
        self.textBrowser.setObjectName("textBrowser")
        self.executeScript = QtWidgets.QPushButton(self.centralwidget)
        self.executeScript.setEnabled(False)
        self.executeScript.setGeometry(QtCore.QRect(660, 510, 111, 31))
        self.stopScript = QtWidgets.QPushButton(self.centralwidget)
        self.stopScript.setEnabled(True)
        self.stopScript.setGeometry(QtCore.QRect(660, 475, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.executeScript.setFont(font)
        self.executeScript.setObjectName("executeScript")
        self.stopScript.setFont(font)
        self.stopScript.setObjectName("stopScript")
        self.scriptName = QtWidgets.QLabel(self.centralwidget)
        self.scriptName.setGeometry(QtCore.QRect(30, -10, 741, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.scriptName.setFont(font)
        self.scriptName.setObjectName("scriptName")
        self.scriptConsole = QtWidgets.QTextBrowser(self.centralwidget)
        self.scriptConsole.setGeometry(QtCore.QRect(30, 450, 611, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(248, 248, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.scriptConsole.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.scriptConsole.setFont(font)
        self.scriptConsole.setObjectName("scriptConsole")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 400, 61, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 400, 61, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.delayAmount = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.delayAmount.setGeometry(QtCore.QRect(110, 421, 61, 20))
        self.delayAmount.setMaximum(999.0)
        self.delayAmount.setProperty("value", 0.5)
        self.delayAmount.setObjectName("delayAmount")
        self.repeatAmount = QtWidgets.QSpinBox(self.centralwidget)
        self.repeatAmount.setGeometry(QtCore.QRect(30, 421, 61, 21))
        self.repeatAmount.setMaximum(99999)
        self.repeatAmount.setProperty("value", 1)
        self.repeatAmount.setObjectName("repeatAmount")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(self)
        self.actionClose.setObjectName("actionClose")
        self.actionOpen_File = QtWidgets.QAction(self)
        self.actionOpen_File.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionOpen_File.setVisible(True)
        self.actionOpen_File.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actionOpen_File.setIconVisibleInMenu(True)
        self.actionOpen_File.setShortcutVisibleInContextMenu(True)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionClose_File = QtWidgets.QAction(self)
        self.actionClose_File.setShortcutContext(QtCore.Qt.ApplicationShortcut)
        self.actionClose_File.setShortcutVisibleInContextMenu(True)
        self.actionClose_File.setObjectName("actionClose_File")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionClose_File)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # Center Window
        geo = self.frameGeometry()
        center = QDesktopWidget().availableGeometry().center()
        geo.moveCenter(center)
        self.move(geo.topLeft())

        self.show()

        # Action Triggers
        self.actionOpen_File.triggered.connect(self.openfile)
        self.executeScript.clicked.connect(self.execute)
        self.stopScript.clicked.connect(self.cancelexecute)
        self.actionClose_File.triggered.connect(self.closefile)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Python Script Executor"))
        self.executeScript.setText(_translate("self", "Execute"))
        self.stopScript.setText(_translate("self", "Stop"))
        self.scriptName.setText(_translate("self", "No Script Selected"))
        self.scriptConsole.setHtml(_translate("self",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                              "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("self", "Repeat"))
        self.label_3.setText(_translate("self", "Delay"))
        self.menuFile.setTitle(_translate("self", "File"))
        self.actionClose.setText(_translate("self", "Close"))
        self.actionOpen_File.setText(_translate("self", "Open File"))
        self.actionOpen_File.setStatusTip(_translate("self", "Open a Python Script"))
        self.actionOpen_File.setShortcut(_translate("self", "Ctrl+O"))
        self.actionClose_File.setText(_translate("self", "Close File"))
        self.actionClose_File.setStatusTip(_translate("self", "Close Current Python Script"))
        self.actionClose_File.setShortcut(_translate("self", "Ctrl+W"))

    def openfile(self):
        path = easygui.fileopenbox(title="Open a Python Script", default="c:/*.py", filetypes=["*.py", "*.pyc", "Python files"])
        if path:
            if not path.endswith((".py", "pyc")):
                easygui.exceptionbox("This program only accepts Python files!", "Exception Occurred")
            else:
                import requests
                global script
                script = path

                self.scriptName.setText(path.split("\\")[-1])
                if clearConsoleOnScriptChanged:
                    self.scriptConsole.clear()

                with open(path) as f:
                    query = {"code": f.read(), "style": "default"}
                    response = requests.get("http://hilite.me/api", params=query).text
                    self.textBrowser.setHtml(response)
                    self.executeScript.setEnabled(True)

    def closefile(self):
        if self.executeScript.isEnabled():
            self.executeScript.setEnabled(False)
            self.scriptConsole.clear()
            self.textBrowser.clear()
            self.scriptName.setText("No Script Selected")

    def execute(self):
        import threading
        def execute_thread():
            if script:
                repeat = self.repeatAmount.value()
            self.executeScript.setEnabled(False)
            global stop
            stop = False
            while repeat > 0:
                if stop:
                    self.executeScript.setEnabled(False)
                    break
                import time
                proc = subprocess.Popen(['python', script], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                output = proc.communicate()[0].decode("utf-8")
                self.scriptConsole.append(output)
                self.scriptConsole.moveCursor(QtGui.QTextCursor.End)
                QApplication.processEvents()
                repeat -= 1
                if repeat != 0:
                    time.sleep(self.delayAmount.value())
            self.executeScript.setEnabled(True)

        x = threading.Thread(target=execute_thread)
        x.daemon = True
        x.start()

    def cancelexecute(self):
        global stop
        stop = True
        self.executeScript.setEnabled(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AppWindow()
    sys.exit(app.exec_())
