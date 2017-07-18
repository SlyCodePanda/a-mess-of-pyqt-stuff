import sys
from PyQt4 import QtGui, QtCore

# Window inherits from the Qt widget 'MainWindow'
class Window(QtGui.QMainWindow):

    # Any core application stuff goes in the 'init' function.
    def __init__(self):
        # With 'super' what we return is the parent object and so our parent object would be out main window object.
        super(Window, self).__init__()
        # x: 50, y: 50, width: 500, height: 300.
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("PyQt tuts")
        self.setWindowIcon(QtGui.QIcon('index.png'))

        # Main menu.
        # Adding Items to the main menu:
        extractAction = QtGui.QAction("&GET TO THE CHOPPAH!!!", self)
        extractAction.setShortcut("Ctrl+Q")
        extractAction.setStatusTip('Leave The App')
        extractAction.triggered.connect(self.close_application)

        anotherAction = QtGui.QAction("It's a trap!!", self)
        anotherAction.setShortcut("Ctrl+A")
        anotherAction.setStatusTip('This does nothing lol')
        anotherAction.triggered.connect(self.get_tricky)

        # Editor.
        openEditor = QtGui.QAction("&Editor", self)
        openEditor.setShortcut("Ctrl+E")
        openEditor.setStatusTip('Open Editor')
        openEditor.triggered.connect(self.editor)

        # Open.
        openFile = QtGui.QAction("&Open", self)
        openFile.setShortcut("Ctrl+O")
        openFile.setStatusTip('Open File')
        openFile.triggered.connect(self.file_open)

        # Save.
        saveFile = QtGui.QAction("&Save", self)
        saveFile.setShortcut("Ctrl+S")
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.file_save)



        self.statusBar()


        # Menu definitions:
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')

        editMenu = mainMenu.addMenu('&Edit')
        fileMenu.addAction(extractAction)
        editMenu.addAction(anotherAction)
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)

        editorMenu = mainMenu.addMenu("&Editor")
        editorMenu.addAction(openEditor)



        self.home()

    # Stuff that is specific to that certain page that you are on.
    def home(self):
        btn = QtGui.QPushButton("Quit", self)
        # What happens when the button is clicked.
        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(0,100)

        # Adding the Toolbar:
        extractAction = QtGui.QAction(QtGui.QIcon('todachoppa.png'), 'Flea the Scene', self)
        extractAction.triggered.connect(self.close_application)     

        self.toolBar = self.addToolBar("Extraction")
        self.toolBar.addAction(extractAction)

        # Adding Font Widget:
        fontChoice = QtGui.QAction('Font', self)
        fontChoice.triggered.connect(self.font_choice)      

        self.toolBar.addAction(fontChoice)

        # Adding Colour Picker Widget. Changes the background colour of the font background:
        colour = QtGui.QColor(0, 0, 0)
        fontColour = QtGui.QAction('Font bg Colour', self)
        fontColour.triggered.connect(self.colour_picker)

        self.toolBar.addAction(fontColour)

        # Adding Check Box:
        checkBox = QtGui.QCheckBox('Enlarge Window', self)
        checkBox.move(300, 25)
        checkBox.stateChanged.connect(self.enlarge_window)

        # Adding Progress Bar:
        self.progress = QtGui.QProgressBar(self)
        self.progress.setGeometry(200, 80, 250, 20)

        self.btn = QtGui.QPushButton("Download", self)
        self.btn.move(200, 120)
        self.btn.clicked.connect(self.download)

        # Adding Drop Down Button. That allows you to set the GUI style :
        # This prints out the default style that you GUI is set to to your terminal.
        print(self.style().objectName())
        self.styleChoice = QtGui.QLabel("GTK+", self)

        comboBox = QtGui.QComboBox(self)
        # A selection of GUI styles from the QStyleFactory.
        comboBox.addItem("motif")
        comboBox.addItem("Windows")
        comboBox.addItem("cde")
        comboBox.addItem("Plastique")
        comboBox.addItem("Cleanlooks")
        comboBox.addItem("gtk+")

        comboBox.move(20, 250)
        self.styleChoice.move(50, 150)
        comboBox.activated[str].connect(self.style_choice)


        # Adding Calendar Widget:
        cal = QtGui.QCalendarWidget(self)
        cal.move(500, 200)
        cal.resize(200, 200)


        self.show()


    def colour_picker(self):
        colour = QtGui.QColorDialog.getColor()
        self.styleChoice.setStyleSheet("QWidget { background-color: %s}" % colour.name())


    def editor(self):
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)


    def file_open(self):
        name = QtGui.QFileDialog.getOpenFileName(self, 'Open File')
        # Opening with the intention to read ('r').
        file = open(name, 'r')

        # Need to call the editor, because it is not there by default. 
        self.editor()

        with file:
            text = file.read()
            self.textEdit.setText(text)


    def file_save(self):
        name = QtGui.QFileDialog.getSaveFileName(self, 'Save File')
        # Intention to write the file ('w')
        file = open(name, 'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()


    def font_choice(self):
        font, valid = QtGui.QFontDialog.getFont()
        if valid:
            self.styleChoice.setFont(font)


    def style_choice(self, text):
        self.styleChoice.setText(text)
        # Sets the style of your GUI.
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create(text))


    def download(self):
        self.completed = 0

        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)


    def enlarge_window(self, state):
        if state == QtCore.Qt.Checked:
            self.setGeometry(50, 50, 1000, 600)
        else:
            self.setGeometry(50, 50, 500, 300)


    def close_application(self):
        # Pop-Up Message:
        choice = QtGui.QMessageBox.question(self, 'Extract',
                                            "Get into the chopper?",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print( "Extracting now")
            sys.exit()
        else:
            pass


    def get_tricky(self):
        self.setWindowTitle("OH SHIT DAT TRICKY!")




# Our 'main'.
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())

run()

'''NOTES:
To convert a .ui file to a .py file you need to run the pyuic using the following command:
pyuic4 -o ui_form.py form.ui