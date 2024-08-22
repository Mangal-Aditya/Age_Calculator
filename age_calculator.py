import sys

current_date = 21
current_month = 8
current_year = 2004


birth_date = 23
birth_month = 9
birth_year = 2001


if birth_year > current_year :
    print("Congratulation! I think you are greast scientist of all time as you invent time mechine  :) :) ,current year can't be less than your birth year")
    sys.exit()


if  current_month > 12 or birth_month > 12 :
    print("On earth we have 12 month in a year from which planet you are ?  ")
    sys.exit()


if current_date > 32 or birth_date > 32 :
    print("we have 1 to 31 days in our calender please check your one ")
    sys.exit()



days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if birth_date > current_date:
    current_month -= 1  
    current_date += days_in_month[birth_month - 1] 


if birth_month > current_month:
    current_year -= 1  
    current_month += 12

age_years = current_year - birth_year
age_months = current_month - birth_month
age_days = current_date - birth_date


print(f"Present Age: {age_years} Years, {age_months} Months, {age_days} Days")    