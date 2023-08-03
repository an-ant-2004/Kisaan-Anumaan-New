import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Linear regression
from sklearn.linear_model import LinearRegression

import Regression
import Predict

       
class PredictWindow(QDialog):
    
    def __init__(self,language,parent=None):
        super().__init__()
        print('### CHECKPOINT 0 ###')

        self.language=language
        self. filename=""
        self.soilSelected=""
        # setting  the geometry of window
        self.setGeometry(0, 0, 600, 600)
        
        #self.resize(800,800)
        self.setWindowTitle("Kisaan Anuman")
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


        h1layout = QGridLayout()
        h1 = QLabel(self)
        h1.setText("KISAAN ANUMAAN")
        
        if  self.language == 0 :                # 0 : English
            h1.setText("KISAAN ANUMAAN")
        else:                                            # 1 : Hindi
            h1.setText("किसान अनुमान")
        
        h1.setFont(QFont('Arial Black', 15))
        h1.setStyleSheet("; font-size:30px;color:blue;")

        h1layout.addWidget(QLabel(self), 0, 0)
        h1layout.addWidget(h1, 0, 1)
        h1layout.addWidget(QLabel(self), 0, 2)    

        heading = QHBoxLayout()
        heading.addLayout(h1layout)
        

        season = QLabel(self)
        season.setText("Select Season")
        season.setFont(QFont('Arial', 11))

        
        # Create an outer layout
        outerLayout = QVBoxLayout()
        outerLayout.addStretch()
        outerLayout.addLayout(imglayout)
        outerLayout.addLayout(heading)
        outerLayout.addWidget(season)
        
        print('### CHECKPOINT 1 ###')
        
        crop = QGridLayout()
        
        season1 = QRadioButton("Rabi",)
        season1.setChecked(True)            #default
        self.filename='April.csv'                  #default
        season1.setFont(QFont('Arial', 11))
        season1.toggled.connect(lambda:self.btnstateSeason(season1))
        crop.addWidget(season1,0,1)      
		
        season2 = QRadioButton("Kharif")
        season2.setChecked(False)
        season2.toggled.connect(lambda:self.btnstateSeason(season2))
        season2.setFont(QFont('Arial', 11))
        crop.addWidget(season2,0,2)      

        season3 = QRadioButton("Zaid")
        season3.setChecked(False)
        season3.toggled.connect(lambda:self.btnstateSeason(season3))
        season3.setFont(QFont('Arial', 11))
        crop.addWidget(season3,0,3)      

        
        seasonGroup = QButtonGroup(self)  
        seasonGroup.addButton(season1)
        seasonGroup.addButton(season2)
        seasonGroup.addButton(season3)
        
        outerLayout.addLayout(crop)
        print('### CHECKPOINT 2   ###')
        
        soil = QLabel(self)
        soil.setText("Select Soil")
        soil.setFont(QFont('Arial', 11))

        outerLayout.addWidget(soil)
        soil1 = QRadioButton("Brown Soil")  
        soil1.setChecked(True)      #default
        self.soilSelected="Brown"  #default
        soil1.setFont(QFont('Arial', 11))
        soil1.toggled.connect(lambda:self.btnstateSoil(soil1))


        soil2 = QRadioButton("Alluvial Soil")
        soil2.setChecked(False)
        soil2.setFont(QFont('Arial', 11))
        soil2.toggled.connect(lambda:self.btnstateSoil(soil2))

        
        soilGroup = QButtonGroup(self)  
        soilGroup.addButton(soil1)
        soilGroup.addButton(soil2)
        
        print('### CHECKPOINT 3  ###')
        
        soilLayout = QHBoxLayout()
        soilLayout.addWidget(soil1)
        soilLayout.addWidget(soil2)

        outerLayout.addLayout(soilLayout)
        
        # Create a form layout for the label and line edit
        Edit1 = QHBoxLayout()
        self.yrCombo = QComboBox()
        self.yrCombo.setFont(QFont('Arial', 11))
        self.yrCombo.addItems(["2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032", "20333", "2034", "2035", "2036", "2037", "2038", "2039", "2040"])

        self.h2 = QLabel(self)
        self.h2.setText("Prediction required for the year")
        self.h2.setFont(QFont('Arial', 11))

        # Add a label and a line edit to the form layout
        Edit1.addWidget(self.h2)
        Edit1.addWidget(self.yrCombo)
        
                
        self.h3 = QLabel(self)
        self.h3.setText("Expected Temperature in the year")
        self.h3.setFont(QFont('Arial', 11))
        # Create a form layout for the label and line edit
        Edit2 = QHBoxLayout()
        self.yrTemp   = QLineEdit()
        
        # Add a label and a line edit to the form layout
        Edit2.addWidget(self.h3)
        Edit2.addWidget(self.yrTemp)
        
        print('### CHECKPOINT 4  ###')
        
        h4 = QLabel(self)
        h4.setText("Expected Humidity in the year")
        h4.setFont(QFont('Arial', 11))
        self.yrHumidity  = QLineEdit()
        # Create a form layout for the label and line edit
        Edit3 = QHBoxLayout()
        # Add a label and a line edit to the form layout
        Edit3.addWidget(h4)
        Edit3.addWidget(self.yrHumidity)

        h6 = QLabel(self)
        h6.setText("Enter PH Value")
        h6.setFont(QFont('Arial', 11))
        # Create a form layout for the label and line edit
        Edit5 = QHBoxLayout()
        self.PHValue = QLineEdit()
        #self.yrRainfall.setEnabled(True)
        # Add a label and a line edit to the form layout
        Edit5.addWidget(h6)
        Edit5.addWidget(self.PHValue)

        
        h5 = QLabel(self)
        h5.setText("Predicted Rainfall")
        h5.setFont(QFont('Arial', 11))
        # Create a form layout for the label and line edit
        Edit4 = QHBoxLayout()
        self.yrRainfall = QLineEdit()
        self.yrRainfall.setEnabled(False)
        # Add a label and a line edit to the form layout
        Edit4.addWidget(h5)
        Edit4.addWidget(self.yrRainfall)
            
        
        outerLayout.addLayout(Edit1)
        outerLayout.addLayout(Edit2)
        outerLayout.addLayout(Edit3)
        outerLayout.addLayout(Edit5)
        outerLayout.addLayout(Edit4)
        
        
        btnPredict = QPushButton(self)
        btnPredict.setText('PREDICT RAINFALL')

        #Predict Button
        btnPredict.clicked.connect(self.dialogPredict)
        btnPredict.setFont(QFont('Arial Black', 13))

        btnReset = QPushButton(self)
        btnReset.setText('Reset')
        #Reset Button
        btnReset.clicked.connect(self.dialogReset)
        btnReset.setFont(QFont('Arial Black', 13))

        btnClose = QPushButton(self)
        btnClose.setText('Close')
        #Close button
        btnClose.clicked.connect(self.dialogClose)
        btnClose.setFont(QFont('Arial Black', 13))

        print('### CHECKPOINT 5  ###')
        
        b1layout = QGridLayout()

        b1layout.addWidget(QLabel(self), 0, 0)
        b1layout.addWidget(btnPredict, 0, 1)
        b1layout.addWidget(QLabel(self), 0, 2)

        b2layout = QGridLayout()

        b2layout.addWidget(QLabel(self), 0, 0)
        b2layout.addWidget(btnReset, 0, 1)
        b2layout.addWidget(btnClose, 0, 2)
        b2layout.addWidget(QLabel(self), 0, 3)
                
        outerLayout.addLayout(b1layout)
        outerLayout.addLayout(b2layout)                 
        # Set the window's main layout
        self.setLayout(outerLayout)

        self.Output = QTextEdit(self)
        self.Output.setReadOnly(True)
        self.Output.setLineWrapMode(QTextEdit.NoWrap)

        font = self.Output.font()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.Output.moveCursor(QTextCursor.End)
        self.Output.setCurrentFont(font)
        #Output.setTextColor("green")
        Edit5 = QHBoxLayout()
        Edit5.addWidget(self.Output)
        outerLayout.addLayout(Edit5)
        
        print('### CHECKPOINT 6  ###')

        self.Output.setPlainText("Suggested Crops will be listed here.")

    def dialogPredict(self):
        print('*'*75)
        print('\t\tWELCOME TO KISAAN ANUMAAN\n') 
        print('\t\tMODELING RAINFALL IN RAJASTHAN ') 
        print('*'*75)
        print('\npress ENTER to continue......')    
        #input()
        print('*'*75)
        print('\tPlease see useful information....\n') 
        print('\tMain CROPS in RAJASTHAN : RICE, JOWAR, BAJRA, MAIZE, COTTON, \n\
            \t\t\t         JUTE,  SUGARCANE, SESAME, GROUNDNUT')
        print('*'*75)
        print('\npress ENTER to continue......')
        #Reading data file
        Regression.getCSV(self.filename)
        #Linear regression
        #instantiate
        linreg=LinearRegression()
        
        model = Regression.TrainTestModel(linreg)
        print('Model Trained')
        print('GUI YEAR: ',self.yrCombo.currentText())
        print('GUI TEMP: ',self.yrTemp.text())
        print('GUI HUMID: ',self.yrHumidity.text())
        print('GUI PH: ',self.PHValue.text())
        
        
        #rainfall = Predict.PredictRainfall(model,2040,50,70)   #dummy value

        rainfall = Predict.PredictRainfall(model,self.yrCombo.currentText(),int(self.yrTemp.text()),
                                           int(self.yrHumidity.text()))
        
        self.yrRainfall.setText(str(rainfall[0][0]))
        msg1 = Predict.PredictCrop(rainfall,self.soilSelected)
        
        print('### CHECKPOINT 7  ###')
        

        
        msg2 = Predict.PredictFertilizer(int(self.PHValue.text()),self.soilSelected)
        self.Output.setPlainText('Predicted Rainfall : ' + str(rainfall[0][0]) + '\n' + msg1 + '\n' +
                                 'Fertilizer suggested : ' + msg2)

        mbox = QMessageBox(self)
                
        mbox.setText("Crop Prediction successful")
        mbox.setDetailedText("Note the suggested crops. Good Luck ! ")
        mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mbox.setWindowTitle("Kisaan Anuman")        
        mbox.exec_()


    def dialogReset(self):
        self.yrHumidity.setText("")
        self.yrTemp.setText("")
        self.PHValue.setText("")
        self.yrRainfall.setText("")
        self.Output.setPlainText("Suggested Crops will be listed here.")


    def dialogClose(self):
          reply=QMessageBox.question(self,'Message','Are you sure you want to close Predictor?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No )
          if reply==QMessageBox.Yes:
                self.hide()
          else:
                pass

    
    def btnstateSeason(self,choice):
          season = self.sender()       
          if season.text() == "Rabi":
                if season.isChecked() == True:
                      self.filename='April.csv'

          if season.text() == "Kharif":
                if season.isChecked() == True:
                      self.filename='October.csv'

          
          if season.text() == "Zaid":
                if season.isChecked() == True:
                      self.filename='zaid.csv'

    def btnstateSoil(self,choice):
          soil = self.sender()       
          if soil.text() == "Brown Soil":
                if soil.isChecked() == True:
                      self.soilSelected="Brown"

          if soil.text() == "Alluvial Soil":
                if soil.isChecked() == True:
                      self.soilSelected="Alluvial"

