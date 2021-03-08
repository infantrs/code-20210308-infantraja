##Python BMI Calculator challenge


person_details = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]

def cal_bmi(height,weight):
    #To calculate BMI
    
    return weight/height


"""1. Calculate the BMI (Body Mass Index) using Formula 1, BMI Category and Health
risk from Table 1 of the person and add them as 3 new columns"""
def calculate_params(person_details):
    for idx,each_per in enumerate(person_details):
        weight = each_per["WeightKg"]
        height = each_per["HeightCm"]/100 ## height is converted to meters as it is in CM
        
        BMI = cal_bmi(height,weight)
        (person_details[idx])["BMI"] = round(BMI,2)
        
        if BMI <= 18.4:

            (person_details[idx])["BMICategory"] = "Underweight"
            (person_details[idx])["HealthRisk"] = "MalNutritionRisk"
        elif 18.5 <= BMI <=24.9:

            (person_details[idx])["BMICategory"] = "NormalWeight"
            (person_details[idx])["HealthRisk"] = "LowRisk"
            
        elif 25 <= BMI <=29.9:

            (person_details[idx])["BMICategory"] = "OverWeight"
            (person_details[idx])["HealthRisk"] = "EnhancedRisk"
        
        elif 30 <= BMI <=34.9:

            (person_details[idx])["BMICategory"] = "ModeratelyObese"
            (person_details[idx])["HealthRisk"] = "MediumRisk"
        elif 35 <= BMI <=39.9:

            (person_details[idx])["BMICategory"] = "SeverelyObese"
            (person_details[idx])["HealthRisk"] = "HighRisk"
        elif BMI >=40:

            (person_details[idx])["BMICategory"] = "VerySeverelyObese"
            (person_details[idx])["HealthRisk"] = "VeryHighRisk"
        
    return person_details
person_details = calculate_params(person_details)
print(person_details)
        
"""2. Count the total number of overweight people using ranges in the column BMI
Category of Table 1, check this is consistent programmatically and add any other
observations in the documentation"""
def count_of(BMICategory="OverWeight"):
    sorted_list = sorted(person_details,key=lambda x:x["BMICategory"],reverse=False)


    OverWeight = list(filter(lambda x: x["BMICategory"]==BMICategory, sorted_list))
    
    return len(OverWeight)

count_overweight = count_of("OverWeight")
print(count_overweight)


"""3. Create build, tests to make sure the code is working as expected and this can be
added to an automation build / test / deployment pipeline"""

if (calculate_params([{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]))[0]["HealthRisk"] != "VeryHighRisk" or count_of("OverWeight")!=0:
    print("Error in calculating BMI")
else:
    print("Working Fine")
