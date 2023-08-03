"""
    1. Similar to the way you had implemented your Login Functionality, this can also be achieved.
    Here, I have made a small demo window which you can use for your purpose.

    2. Just call the application codes you have for Hindi/English in the respective functions.
    
    3. This is just a concept which you can implement yourself too. (in your own way/ in a better way)
"""

#from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

import loginScreenEnglish
import loginScreenHindi

# language  0: English, 1 : Hindi

class LanguageSelectorWindow(object):

    language = 0
    
    def setupUI(self, MainWindow):
        MainWindow.setGeometry(0,0,500, 500)
        MainWindow.setWindowTitle("Kisaan Anumaan")

        # loading image
        imglabel = QLabel()
        pixmap = QPixmap('image.png')
        # adding image to label
        imglabel.setPixmap(pixmap)
        # Optional, resize label to image size
        imglabel.resize(pixmap.width(),pixmap.height())

        imglayout = QGridLayout()
        imglayout.addWidget(QLabel(), 0, 0)
        imglayout.addWidget(imglabel, 0, 1)
        imglayout.addWidget(QLabel(), 0, 2)    

        outerLayout = QVBoxLayout()
        outerLayout.addStretch()


        centralWidget = QWidget()
        
        centralwidgetLayout = QVBoxLayout()
        self.hindi_button = QPushButton("हिंदी")
        self.english_button = QPushButton("English")
        self.hindi_button.setFont(QFont('Arial Black', 13))
        self.english_button.setFont(QFont('Arial Black', 13))
        language = QLabel()
        language.setText("Select The Preferred Language")
        language.setFont(QFont('Arial', 11))

        centralwidgetLayout.addWidget(language)
        centralwidgetLayout.addWidget(self.hindi_button)
        centralwidgetLayout.addWidget(self.english_button)
    
        self.hindi_button.clicked.connect(self.hindi_selected)
        self.english_button.clicked.connect(self.english_selected)
        
        outerLayout.addLayout(imglayout)
        outerLayout.addLayout(centralwidgetLayout)

        centralWidget.setLayout(outerLayout)
        MainWindow.setCentralWidget(centralWidget)


    def hindi_selected(self):
        # Call The Hindi Version of The App Here
        print("हिंदी संस्करण चयनित")
        LanguageSelectorWindow.language= 1 # Hindi language
        
        # start the app
        self.LaunchLogin()

    def english_selected(self):
        # Call The English Version of The App Here
        print("English Version Called")

        LanguageSelectorWindow.language = 0 #English Language
        self.LaunchLogin()
        
    def LaunchLogin(self):
       
        if LanguageSelectorWindow.language == 0:
            form = loginScreenEnglish.LoginForm(LanguageSelectorWindow.language)
        else:
            form = loginScreenHindi.LoginForm(LanguageSelectorWindow.language)
        #self.close()       # giving error in launching the form if we close main application
        form.show()
        form.exec_()
        
app = QApplication(sys.argv)
MainWindow = QMainWindow()
language_window = LanguageSelectorWindow()
language_window.setupUI(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

