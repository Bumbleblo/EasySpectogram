from PySide2.QtWidgets import QMainWindow, QAction, QCheckBox, QVBoxLayout

class MainWindow(QMainWindow):

    __slots__ = ['menu', 'status']
    def __init__(self):

        QMainWindow.__init__(self) # < qt stuff
        self.setWindowTitle("Easy Spectogram")
        self.menu = self.menuBar()

        self.__status_bar()
        self.__exit_menu()
        self.__box()

    def __status_bar(self):
        self.status = self.statusBar()
        self.status.showMessage('placeholder')

    def __exit_menu(self):

        self.exit_menu = self.menu.addMenu("Exit")

        exit_action = QAction("Exit without saving", self)
        exit_action.triggered.connect(self.close)
        
        self.exit_menu.addAction(exit_action)

    def __box(self):

        self.box = QVBoxLayout()

        check1 = QCheckBox("teste 1", self)
        check2 = QCheckBox("teste 2", self)

        self.box.addWidget(check1)
        self.box.addWidget(check2)

        self.setLayout(self.box)
