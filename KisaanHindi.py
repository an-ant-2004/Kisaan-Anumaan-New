import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#Linear regression
from sklearn.linear_model import LinearRegression

import Regression
import PredictHindi

       
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
        self.setWindowTitle("किसान अनुमान")
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
        h1.setText("किसान अनुमान")
        
        h1.setFont(QFont('Arial Black', 15))
        h1.setStyleSheet("; font-size:30px;color:blue;")

        h1layout.addWidget(QLabel(self), 0, 0)
        h1layout.addWidget(h1, 0, 1)
        h1layout.addWidget(QLabel(self), 0, 2)    

        heading = QHBoxLayout()
        heading.addLayout(h1layout)
        

        season = QLabel(self)
        season.setText("मौसम चुनें")
        season.setFont(QFont('Arial', 11))

        
        # Create an outer layout
        outerLayout = QVBoxLayout()
        outerLayout.addStretch()
        outerLayout.addLayout(imglayout)
        outerLayout.addLayout(heading)
        outerLayout.addWidget(season)
        
        print('### CHECKPOINT 1 ###')
        
        crop = QGridLayout()
        
        season1 = QRadioButton("राबी",)
        season1.setChecked(True)            #default
        self.filename='April.csv'                  #default
        season1.setFont(QFont('Arial', 11))
        season1.toggled.connect(lambda:self.btnstateSeason(season1))
        crop.addWidget(season1,0,1)      
		
        season2 = QRadioButton("खरीफ")
        season2.setChecked(False)
        season2.toggled.connect(lambda:self.btnstateSeason(season2))
        season2.setFont(QFont('Arial', 11))
        crop.addWidget(season2,0,2)      

        season3 = QRadioButton("ज़ैद")
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
        soil.setText("मिट्टी चुनें")
        soil.setFont(QFont('Arial', 11))

        outerLayout.addWidget(soil)
        soil1 = QRadioButton("भूरी मिट्टी")  
        soil1.setChecked(True)      #default
        self.soilSelected="Brown"  #default
        soil1.setFont(QFont('Arial', 11))
        soil1.toggled.connect(lambda:self.btnstateSoil(soil1))


        soil2 = QRadioButton("जलोढ़ मिट्टी")
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
        self.h2.setText("वर्ष के लिए आवश्यक भविष्यवाणी")
        self.h2.setFont(QFont('Arial', 11))

        # Add a label and a line edit to the form layout
        Edit1.addWidget(self.h2)
        Edit1.addWidget(self.yrCombo)
        
                
        self.h3 = QLabel(self)
        self.h3.setText("वर्ष में अपेक्षित तापमान")
        self.h3.setFont(QFont('Arial', 11))
        # Create a form layout for the label and line edit
        Edit2 = QHBoxLayout()
        self.yrTemp   = QLineEdit()
        
        # Add a label and a line edit to the form layout
        Edit2.addWidget(self.h3)
        Edit2.addWidget(self.yrTemp)
        
        print('### CHECKPOINT 4  ###')
        
        h4 = QLabel(self)
        h4.setText("वर्ष में अपेक्षित आर्द्रता")
        h4.setFont(QFont('Arial', 11))
        self.yrHumidity  = QLineEdit()
        # Create a form layout for the label and line edit
        Edit3 = QHBoxLayout()
        # Add a label and a line edit to the form layout
        Edit3.addWidget(h4)
        Edit3.addWidget(self.yrHumidity)

        h6 = QLabel(self)
        h6.setText("PH मान दर्ज करें")
        h6.setFont(QFont('Arial', 11))
        # Create a form layout for the label and line edit
        Edit5 = QHBoxLayout()
        self.PHValue = QLineEdit()
        #self.yrRainfall.setEnabled(True)
        # Add a label and a line edit to the form layout
        Edit5.addWidget(h6)
        Edit5.addWidget(self.PHValue)


        h5 = QLabel(self)
        h5.setText("पूर्वानुमानित वर्षा")
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
        btnPredict.setText('भविष्यवाणी करे')

        #Predict Button
        btnPredict.clicked.connect(self.dialogPredict)
        btnPredict.setFont(QFont('Arial Black', 13))

        btnReset = QPushButton(self)
        btnReset.setText('रीसेट')
        #Reset Button
        btnReset.clicked.connect(self.dialogReset)
        btnReset.setFont(QFont('Arial Black', 13))

        btnClose = QPushButton(self)
        btnClose.setText('बंद कर')
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

        self.Output.setPlainText("सुझाई गई फसलें यहां सूचीबद्ध की जाएंगी..")

    def dialogPredict(self):
        print('*'*75)
        print('\t\tकिसान अनुमान आपका स्वागत है\n') 
        print('\t\tराजस्थान में मॉडलिंग रेनफॉल ') 
        print('*'*75)
        
        print('\tराजस्थान में मुख्य फसलें: चावल, ज्वार, बाजरा, मक्का, कपास, \n\
            \t\t\t         जूट, सरसों, गन्ना, तिल, मूंगफली')
        print('*'*75)
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
        
        print('Calling Predict')
        rainfall = PredictHindi.PredictRainfall(model,self.yrCombo.currentText(),
                                           int(self.yrTemp.text()),int(self.yrHumidity.text()))
        
        
        self.yrRainfall.setText(str(rainfall[0][0]))

        msg1 = PredictHindi.PredictCrop(rainfall,self.soilSelected)

        print('Back in Kisaan module: ',msg1)

        print('### CHECKPOINT 7  ###')
        msg2 = PredictHindi.PredictFertilizer(int(self.PHValue.text()),self.soilSelected)
        #self.Output.setPlainText('अनुमानित वर्षा  : ' + str(rainfall[0][0]) + '\n' + msg)
        self.Output.setPlainText('अनुमानित वर्षा : ' + str(rainfall[0][0]) + '\n' + msg1 + '\n' +
                                 'खाद का सुझाव दिया : ' + msg2
                                 )
        mbox = QMessageBox(self)
                
        mbox.setText("फसल भविष्यवाणी सफल")
        mbox.setDetailedText("सुझाई गई फसलों पर ध्यान दें। शुभ लाभ! ")
        mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        mbox.setWindowTitle("किसान अनुमान")        
        mbox.exec_()


    def dialogReset(self):
        self.yrHumidity.setText("")
        self.yrTemp.setText("")
        self.yrRainfall.setText("")
        self.Output.setPlainText("सुझाई गई फसलों को यहां सूचीबद्ध किया जाएगा।")


    def dialogClose(self):
          reply=QMessageBox.question(self,'संदेश', 'क्या आप सुनिश्चित हैं कि आप प्रेडिक्टर को बंद करना चाहते हैं?',QMessageBox.Yes|QMessageBox.No,QMessageBox.No )
          if reply==QMessageBox.Yes:
                self.hide()
          else:
                pass

    
    def btnstateSeason(self,choice):
          season = self.sender()       
          if season.text() == "राबी":
                if season.isChecked() == True:
                      self.filename='April.csv'

          if season.text() == "खरीफ":
                if season.isChecked() == True:
                      self.filename='October.csv'

          
          if season.text() == "ज़ैद":
                if season.isChecked() == True:
                      self.filename='zaid.csv'

    def btnstateSoil(self,choice):
          soil = self.sender()       
          if soil.text() == "भूरी मिट्टी":
                if soil.isChecked() == True:
                      self.soilSelected="Brown"

          if soil.text() == "जलोढ़ मिट्टी":
                if soil.isChecked() == True:
                      self.soilSelected="Alluvial"

