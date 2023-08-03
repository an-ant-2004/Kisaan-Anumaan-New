def PredictRainfall(model,year,temp,humidity):

    print('*'*75)
    print('\tPredictng the rainfall in Rajasthan for selected season')
    print('*'*75)
    
    rain = model.predict([[temp,humidity]])
    print('\nPREDICTED RAIN in the year : ',year,
          'given Temperature:  ',temp, ' \nand ', ' Humidity : ',humidity, ' is ',rain [0][0], ' mm\n')

    return rain
def PredictFertilizer(ph,soil):
    
    print('PH Value : ',ph,'\n',"type of ph",type(ph))

    fert=' '
    if soil == "Alluvial":
        if 7<ph<11:
            fert = fert +'Cow Dung is the most suitable Fertilizer'
            
        elif 3<ph<6:
            fert = fert+'Urea and Ammonium Sulphate Fertilizers must be used'
            
        else:
            fert = fert +" The Soil is Perfect for Agriculture"
    
    if soil == "Black Soil":
        if 7<ph<11:
            fert = fert +'Cow Dung is the most suitable Fertilizer'
            
        elif 3<ph<6:
            fert = fert+'Urea and Ammonium Sulphate Fertilizers must be used'
            
        else:
            fert = fert +" The Soil is Perfect for Agriculture"
        
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
    crop = 'Suggested Crop(s) : '
    if soil == 'Alluvial':
        if ( 50 <= rain <= 100):
            crop += ' Wheat, Rice, Cotton and Tobacco \nWith average earning of (₹30-₹154 per kilogram)'
            flag=True
    
    if soil == 'Brown':
        if ( 25 <= rain <= 55):
            crop += ' Corn and Millets \nWith average earning of (₹24-₹89 per kilogram)  '
            flag=True

    if flag == False:
        print('*'*75)
        print('*'*34,'ALERT ', '*'*34)
        print('   CLIMATE OF THIS YEAR IS NOT SUITABLE FOR ANY CROP IN RAJASTHAN !!!')
        crop+= 'NIL, Climate is not suitable this year !!!'
        print('*'*75)
    else:
        print (crop)
    
        
    return crop
