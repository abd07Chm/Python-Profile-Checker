name = input("What is your name? ")
age = int(input("What is your age? "))
GPA = float(input("What is your GPA between 0-5 ? "))
f_o_I = input("What is your field of interest? ")
graduation = input("Did you graduate? (Y/N) ")


if age < 25 and GPA >= 3.5 and graduation == "Y":
        print("You are eligible for the scholarship program.")

elif age < 30 and GPA >= 2.5 and graduation == "N":
        print("You are eligible for the internship program.")
  
else:
    print("please try applying again later.")