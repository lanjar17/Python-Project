#Kasus Body Mass Index (BMI)

def bodyMassIndex():
    beratBadan = float(input('Berat badan(kg) : '))
    tinggiBadan = float(input('Tinggi badan(cm) : '))
    tinggi = tinggiBadan / 100
    
    BMI = beratBadan / (tinggi * tinggi)
    if(BMI < 18):
        print('status berat badan adalah KURUS')
    elif(BMI >= 18) and (BMI < 23):
        print('status berat badan adalah IDEAL')
    elif(BMI >= 23) and (BMI < 27):
        print('status berat badan adalah GEMUK')
    elif(BMI >= 27) and (BMI < 35):
        print('status berat badan adalah OBESITAS')
    elif(BMI >= 35):
        print('status berat badan adalah OBESITAS MORBID')
    else:
        print('Berat badan tidak termasuk dalam kategori')

        
bodyMassIndex()

