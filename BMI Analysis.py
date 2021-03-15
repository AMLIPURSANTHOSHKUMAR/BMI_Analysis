import json
import numpy as np



def range_list(b,s):
    a = []
    for i in np.arange(b,s+0.1, 0.1):
        a.append(round(i,2))
    #print("BMI_list_ranged:", a)
    return a

#calculation of BMI data
def bmi(data,bmi_range):
    #BMI(kg/m) = mass(kg) / height(m)
    height_m = (data['HeightCm']/100)
    bmi_cal = data['WeightKg']/height_m
    data['bmi_cal'] = round(bmi_cal,1)
    print("BMI calculated data:  ",data)
    range_checked_data = range_check(data, bmi_range)
    #print("range_checked_data  :",range_checked_data)
    return range_checked_data

#Checking the range in BMI category
def range_check(data,bmi_range):
    #print("input data for checking the range: ",data)
    total_calculated_data = {}
    a = data['bmi_cal']
    if a<40:
        for k,v in bmi_range.items():
            print("Checking the BMI in particular range  :",k,v)
            for i in v:
                if i == a:
                    #print("found",a,k,v)
                    total_calculated_data['BMI'] = data
                    for l,m in bmi_range_category1.items():
                        if l == k:
                            total_calculated_data['BMI_Category'] = m[1]
                    total_calculated_data['Health_risk'] = k
                    print(total_calculated_data)


            #print("loop:",total_calculated_data)
        return total_calculated_data
        #total_calculated_data_list.append(total_calculated_data)
        #print(total_calculated_data_list)
    else:
        #print("Not Found:", a)
        print(("checking the BMI In particular range seems to be Very high risk"))
        total_calculated_data['BMI'] = data
        total_calculated_data['BMI_Category'] = 'Very severely obese'
        total_calculated_data['Health_risk'] = 'Very high risk'
        return total_calculated_data



#Analaysis of BMI data 
def analaysis_of_data(total_calculated_data_list):
    Underweight_count, Normal_weight_count, Overweight_count, Moderately_obese_count, Severely_obese_count, Very_severely_obese_count = \
        [0, 0, 0, 0, 0, 0]

    for final_data in total_calculated_data_list:
        #print(final_data)
        if final_data['BMI_Category'] == 'Underweight':
            Underweight_count = Underweight_count+1
            total_analysis_data['Underweight']= Underweight_count

        elif final_data['BMI_Category'] == 'Normal weight':
            Normal_weight_count = Normal_weight_count+1
            total_analysis_data['Normal weight'] = Normal_weight_count

        elif final_data['BMI_Category'] == 'Overweight':
            Overweight_count = Overweight_count+1
            total_analysis_data['Overweight'] = Overweight_count

        elif final_data['BMI_Category'] == 'Moderately obese':
            Moderately_obese_count = Moderately_obese_count+1
            total_analysis_data['Moderately obese'] = Moderately_obese_count

        elif final_data['BMI_Category'] == 'Severely obese':
            Severely_obese_count = Severely_obese_count+1
            total_analysis_data['Severely obese'] = Severely_obese_count
        else:
            Very_severely_obese_count = Very_severely_obese_count+1
            total_analysis_data['Very severely obese'] = Very_severely_obese_count




input_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166, "WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
print("user_input_data:",input_data)
total_calculated_data_list = []
bmi_range = {'Malnutrition_risk':range_list(0,18.4),'Low_risk':range_list(18.5,24.9),'Enhanced_risk':range_list(25,29.9),'Medium_risk':range_list(30,34.9),'High_risk':range_list(35,39.9),'Very_high_risk':[40]}
#print("Range:  ",bmi_range)
#bmi_range_category = {'Malnutrition_risk':'18.4','Low_risk':'18.5-24.9','Enhanced_risk':'25-29.9','Medium_risk':'30 - 34.9','High_risk':'35 - 39.9','Very_high_risk':'40 and above'}
#print(bmi_range_category)

bmi_range_category1 = {
                'Malnutrition_risk':['18.4','Underweight'],
                 'Low_risk':['18.5-24.9','Normal weight'],
                 'Enhanced_risk':['25-29.9','Overweight'],
                 'Medium_risk':['30 - 34.9','Moderately obese'],
                 'High_risk':['35 - 39.9','Severely obese'],
                 'Very_high_risk':['40 and above','Very severely obese']}
#print(bmi_range_category1)

total_analysis_data = {}



for i in input_data:
    print("input_data:"  ,i)
    output = bmi(i,bmi_range)
    print("output:  ",output)
    #print("appending to final_data:  ")
    total_calculated_data_list.append(output)
    #print(total_calculated_data_list)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("final_data:",total_calculated_data_list) #printing the consolidated data



mode = input("Enter YES  if you need analaysis   :")
if mode == "YES":
    analaysis_of_data(total_calculated_data_list)
    for key in total_analysis_data:
        if key == 'Overweight':
            print("Count Of Overweight People Are   :",total_analysis_data[key])
    if 'Overweight' not in [i for i in total_analysis_data]:
        print("Overweight People Not Available")
print("Total BMI Category Count Of People Are :",total_analysis_data)



