#input varible
def get_input():
    weight=float(input("Enter your weight(kg) by num: ")) 
    height=float(input("Enter your height(m) by num: "))
    return weight , height
        
#calculat bmi
def bmi_calculator(weight , height):
    bmi = weight/(height*2)
    return bmi

#report of bmi
def bmi_report (bmi):
    if bmi<18.5:
        return "underweight"
    elif 18.5<=bmi<=25:
        return "healthy"
    elif 25<bmi<30:
        return "owerweight"
    else:
        return "obese"

#calculat standard weight
def st_bmi(height):
    low_st_weight = 37*height
    hi_st_weight = 50*height
    return f"your healthy weight beetwin {low_st_weight} to {hi_st_weight}"
#run
def main():
    weight , height = get_input()
    bmi = bmi_calculator(weight , height)
    report = bmi_report(bmi)
    lose_weihgt = weight-(50*height)
    get_weight = (37*height)-weight
    print(f"your bmi is:{bmi}\nit's meen you're {report}")
    if report == "owerweight" or report=="obese":
        print(f"you need lose: {lose_weihgt}kg")
    elif report =="underweight":
        print(f"you need get: {get_weight}kg")
    satndard_weight = st_bmi(height)
    print(satndard_weight)
    print("good luck!")

if __name__=="__main__":
    main()
