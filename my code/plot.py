from datetime import date,datetime
def calculator_age(birthdate):
    today=date.today()
    years=today.year-birthdate.year
    months=today.month-birthdate.month
    days=today.day-birthdate.day
    if days<0:
        months-=1
        days+=(date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days
    if months<0:
        years-=1
        months+=12

        return years,months,days
    
def main() :
    print("age calculator ") 
    dob=input("enter you date of birth (yyyy-mm-dd):")
    try:
        birthdate=datetime.strptime(dob,"%y-%d-%m").date()
        years,months,days=calculator_age(birthdate)
        print("your age is :")
        print(f"{years} years,{months} months,{days} days old.")
    except ValueError:
if __name__=="__main__":
    main()