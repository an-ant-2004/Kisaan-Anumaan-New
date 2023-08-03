def PredictRainfall(model,year,temp,humidity):

    print('*'*75)
    print('\tचयनित मौसम के लिए राजस्थान में वर्षा की भविष्यवाणी')
    print('*'*75)
    
    rain = model.predict([[temp,humidity]])
    print('\nवर्ष में अनुमानित वर्षा : ',year,
          'given Temperature:  ',temp, ' \nand ', ' Humidity : ',humidity, ' is ',rain [0][0], ' mm\n')

    return rain
def PredictFertilizer(ph,soil):
    
    print('PH Value : ',ph,'\n',"type of ph",type(ph))
    print("obilerated")
    fert=' '
    if soil == "Alluvial":
        if 7<ph<11:
            fert = fert +'गाय का गोबर सबसे उपयुक्त उर्वरक है'
            
        elif 3<ph<6:
            fert = fert+'यूरिया और अमोनियम सल्फेट उर्वरकों का प्रयोग करना चाहिए'
            
        else:
            fert = fert +" मिट्टी कृषि के लिए उत्तम है"
    
    if soil == "Brown":
        print("bhuri")
        if 7<ph<11:
            fert = fert +'गाय का गोबर सबसे उपयुक्त उर्वरक है'
            
        elif 3<ph<6:
            fert = fert+'यूरिया और अमोनियम सल्फेट उर्वरकों का प्रयोग करना चाहिए'
            
        else:
            fert = fert +" मिट्टी कृषि के लिए उत्तम है"
        
    #ph='Suggested Fertilizer(s) : '
    #a=int(ph)
    #print(a)
    #return a;
    print(fert)
    return fert;  
            
        
    
    
def PredictCrop(rain,soil):
    print('SOIL : ', soil)
    print('*'*75)
    print('\t\t\tPREDICTION')
    print('*'*75)
    flag = False
    crop = 'सुझाई गई फसलें: '
    if soil == 'Alluvial':
        if ( 50 <= rain <= 100):
            crop += ' गेहूं, चावल, कपास और तंबाकू \n(₹30-₹154 प्रति किलोग्राम) की औसत कमाई के साथ'
            flag=True
    
    if soil == 'Brown':
        if ( 25 <= rain <= 55):
            crop += ' मकई और बाजरा \nऔसत कमाई (₹24-₹89 प्रति किलोग्राम) के साथ  '
            flag=True

    if flag == False:
        print('*'*75)
        print('*'*34,'चेतावनी ', '*'*34)
        print('   इस वर्ष की जलवायु राजस्थान में किसी भी फसल के लिए उपयुक्त नहीं है!!!')
        crop+= 'शून्य, इस वर्ष जलवायु उपयुक्त नहीं है!!!'
        print('*'*75)
    else:
        print (crop)
    
        
    return crop
