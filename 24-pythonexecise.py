#python coding to find the age of a person days ,months and years 
#Here the input is person age if we live for 90 years then how many days left 

#years=90-43
current_age_person=int(input("please enter the current age"))
Remaing_age=90-current_age_person
Remaining_days=Remaing_age*365
Remaining_weeks=Remaing_age*52
Remaing_months=Remaing_age*12

print(f"you have these many remaing {Remaining_days} days ,{Remaining_weeks} months and {Remaing_months} ")
