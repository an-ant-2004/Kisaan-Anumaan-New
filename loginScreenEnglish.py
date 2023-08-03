#username Ramlal
#password ram12!
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import mysql.connector as mc
import sys

import Kisaan

#from languagechangewindow import LanguageSelectorWindow as lsw

class LoginForm(QDialog):

    
    def __init__(self, language,parent=None):
        super().__init__()
        # setting  the geometry of window
        self.setGeometry(0, 0, 300, 300)
        self.setWindowTitle("Kisaan Anuman")
        self.language=language
            
        self.setWindowTitle("Kisaan Login")
        # creating label
        imglabel = QLabel(self)
        # loading image
        pixmap = QPixmap('image.png')
        # adding image to label
        imglabel.setPixmap(pixmap)
  
        # Optional, resize label to image size
        imglabel.resize(pixmap.width(),pixmap.height())
        imglayout = QGridLayout()
        imglayout.addWidget(QLabel(self), 0, 0)
        imglayout.addWidget(imglabel, 0, 1)
        imglayout.addWidget(QLabel(self), 0, 2)    

        h1 = QLabel(self)
        #print('printing value')
        #print(lang)     #Giving error
        h1.setText("KISAAN ANUMAAN")
        
        h1.setFont(QFont('Arial Black'))
        h1.setStyleSheet("; font-size:30px;color:blue;")
        h1.setAlignment(Qt.AlignCenter)   
        self.info = QLabel(self)
        self.info.setFont(QFont('Arial Black', 10))
        self.info.setStyleSheet("; color:red;")
        self.info.setAlignment(Qt.AlignCenter)

        heading = QGridLayout()
        heading.addWidget(QLabel(self), 0, 0)
        heading.addWidget(h1, 0, 1)
        heading.addWidget(QLabel(self), 0, 2)    
        heading.addWidget(QLabel(self), 1, 0)
        heading.addWidget(self.info, 1, 1)
        heading.addWidget(QLabel(self), 1, 2)    
        #image : imgLayout
        #heading: h1
        
        self.txtUsername = QLineEdit(self)
        self.QUserLabel = QLabel("USERNAME")

        self.txtPassword = QLineEdit(self)
        self.QPasswordLabel = QLabel("PASSWORD")
        self.txtPassword.setEchoMode(QLineEdit.Password)
        self.btnLogin = QPushButton("LOGIN")
        self.btnRegister = QPushButton("REGISTER")
        self.btnClose = QPushButton("CLOSE")
        self.btnLogin.setToolTip('Proceed with login of existing farmer')
        self.btnRegister.setToolTip('Register for new farmer')
        
        #for testing
        self.txtUsername.setText('Ramlal')
        self.txtPassword.setText('ram12!')
        
      
        loginlayout = QFormLayout()
        loginlayout.addRow(self.QUserLabel,self.txtUsername)
        loginlayout.addRow(self.QPasswordLabel,self.txtPassword)
        btnlayout = QGridLayout()
        btnlayout.addWidget(self.btnRegister, 0, 0)
        btnlayout.addWidget(self.btnLogin, 0, 1)
        btnlayout.addWidget(self.btnClose, 0, 2)    

        
        outerLayout = QVBoxLayout()
        outerLayout.addStretch()
        outerLayout.addLayout(imglayout)
        outerLayout.addLayout(heading)
        
        outerLayout.addLayout(loginlayout)
        outerLayout.addLayout(btnlayout)
        self.setLayout(outerLayout)
        
        self.btnRegister.clicked.connect(self.Register)
        self.btnLogin.clicked.connect(self.loginSubmit)
        self.btnClose.clicked.connect(self.closeApp)
        
    def Register(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        try:
              mydb=mc.connect(host='localhost', user='root', passwd='1234', db='kisaan')
              mycursor = mydb.cursor()
              mycursor.execute("SELECT * FROM Farmers")
              mycursor.fetchall()
              rc = mycursor.rowcount
             
              query = "INSERT INTO Farmers VALUES(" + str(rc+1) + ',\'' + username + '\',\'' + password + '\');'
              
              mycursor.execute(query)
              mydb.commit()
              mydb.close()
        except Exception as e:
              print(e)
              msg = QMessageBox()
              msg.setText('Database connection Error!')
              msg.setStandardButtons(QMessageBox.Ok)
              msg.setWindowTitle("Kisaan Anuman")        
              msg.exec_()

    
    def authLogin(self,username,password):
        try:
              mydb=mc.connect(host='localhost', user='root', passwd='1234', db='kisaan')
              mycursor = mydb.cursor()
              query = "SELECT * FROM Farmers WHERE user = \""+username+ "\" AND  password = \"" + password + "\""
              result = mycursor.execute(query)
              result = mycursor.fetchall()
              #self.printMsg()        
              if (len(result) > 0):
                  return True
              else:
                  return False
              mydb.close()
        except Exception as e:
              print(e)
              msg = QMessageBox()
              msg.setText('Database connection Error!')
              msg.setStandardButtons(QMessageBox.Ok)
              msg.setWindowTitle("Kisaan Anuman")        
              msg.exec_()
   
        
    def loginSubmit(self):
        # create the instance of our Window
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        isValidUser = self.authLogin(username,password)
        print('language ',self.language)    
        if (isValidUser == True):
                    
                    self.info.setText('Login successful')
                    print('Login successful')
                    window = Kisaan.PredictWindow(self.language)
                    window.show()
                    #window.exec_()
                    
        else:
                    self.info.setText("Invalid username or password!")
                    self.txtUsername.setText("")
                    self.txtPassword.setText("")
                    
    def closeApp(self):
          reply=QMessageBox.question(self,'Message','Are you sure you want to close application?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No )
          if reply==QMessageBox.Yes:
                sys.exit()
          else:
                pass
