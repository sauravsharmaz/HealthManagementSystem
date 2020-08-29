# add search logs functionality
import datetime

# ==================== functions to be executed when user want to log the data ===============
def harry_diet_log():
      print("Hii Harry","\n")
      no_of_fooditem = int(input("How many food items you had eaten today\n"))
      f = open("Harrydiet.txt","a")
      dt = str(datetime.datetime.now())
      f.write("\n---------------\n"+dt+"\n---------------\n")
      i=1
      while i<=no_of_fooditem:
            Harry_diet=str(input("Enter the food item\n"))
            f = open("Harrydiet.txt", "a")
            diet_date = str(Harry_diet+"\n")
            f.write(diet_date)
            f.close()
            i=i+1
      print("ㄍConratulations Harry !"
            "you had successfully saved your Diet logs")
def harry_wrkt_log():
      print("Hii Harry,"
            "\n")
      no_of_exercises = int(input("How many exercises you had done today\n"))
      f = open("Harrywrkt.txt","a")
      dt = str(datetime.datetime.now())
      f.write("\n---------------\n"+dt+"\n---------------\n")
      i=1
      while i<=no_of_exercises:
            Harry_wrkout=str(input("Enter the exercise\n"))
            f = open("Harrywrkt.txt", "a")
            wrkt_date = str(Harry_wrkout+"\n")
            f.write(wrkt_date)
            f.close()
            i=i+1
      print("ㄍConratulations Harry !"
            "you had successfully saved your workout logs")



def hammad_diet_log():
      print("Hii Hammad,"
            "\n")
      no_of_fooditem = int(input("How many food items you had eaten today\n"))
      f = open("Hammaddiet.txt","a")
      dt = str(datetime.datetime.now())
      f.write("\n---------------\n"+dt+"\n---------------\n")
      i=1
      while i<=no_of_fooditem:
            Hammad_diet=str(input("Enter the food item\n"))
            f = open("Hammaddiet.txt", "a")
            diet_date = str(Hammad_diet+"\n")
            f.write(diet_date)
            f.close()
            i=i+1
      print("ㄍConratulations Hammad !"
            "you had successfully saved your Diet logs")
def hammad_wrkt_log():
      print("Hii Hammad,"
            "\n")
      no_of_exercises = int(input("How many exercises you had done today\n"))
      f = open("Hammadwrkt.txt","a")
      dt = str(datetime.datetime.now())
      f.write("\n---------------\n"+dt+"\n---------------\n")
      i=1
      while i<=no_of_exercises:
            Hammad_wrkt=str(input("Enter the exercise\n"))
            f = open("Hammadwrkt.txt", "a")
            wrkt_date = str(Hammad_wrkt+"\n")
            f.write(wrkt_date)
            f.close()
            i=i+1
      print("ㄍConratulations Hammad !"
            "you had successfully saved your workout logs")


def rohan_diet_log():
      print("Hii Rohan,"
            "\n")
      no_of_fooditem = int(input("How many food items you had eaten today\n"))
      f = open("rohandiet.txt","a")
      dt = str(datetime.datetime.now())
      f.write("\n---------------\n"+dt+"\n---------------\n")
      i=1
      while i<=no_of_fooditem:
            rohan_diet=str(input("Enter the food item\n"))
            f = open("rohandiet.txt", "a")
            diet_date = str(rohan_diet+"\n")
            f.write(diet_date)
            f.close()
            i=i+1
      print("ㄍConratulations Rohan !"
            "you had successfully saved your Diet logs")
def rohan_wrkt_log():
      print("Hii Rohan,"
            "\n")
      no_of_exercises = int(input("How many exercises you had done today\n"))
      f = open("rohanwrkt.txt","a")
      dt = str(datetime.datetime.now())
      f.write("\n---------------\n"+dt+"\n---------------\n")
      i=1
      while i<=no_of_exercises:
            rohan_wrkt=str(input("Enter the exercise\n"))
            f = open("rohanwrkt.txt", "a")
            wrkt_date = str(rohan_wrkt+"\n")
            f.write(wrkt_date)
            f.close()
            i=i+1
      print("ㄍConratulations Rohan !"
            "you had successfully saved your workout logs")
# ----------------------------------------------------------------------------------------
# ------------ function for log data ---------------------------------
def log():
      print("you have choosed to log the data\n"
            "Choose User based on the number alloted against each user\n"
            "1. Harry   2. Hammad  3. Rohan\n")
      usr_choice = int(input())
      if usr_choice == 1:
            print("What you want to Log.!"
                  "\n1.Diet  2.Workout\n")
            diet_wrkt_choice = int(input())
            if diet_wrkt_choice == 1:
                  harry_diet_log()
            elif diet_wrkt_choice == 2:
                  harry_wrkt_log()
            else:
                  print("print choose either 1 or 2")
      elif usr_choice == 2:
            print("What you want to Log.!"
                  "\n1.Diet  2.Workout\n")
            diet_wrkt_choice = int(input())
            if diet_wrkt_choice == 1:
                  hammad_diet_log()
            elif diet_wrkt_choice == 2:
                  hammad_wrkt_log()
            else:
                  print("print choose either 1 or 2")

      elif usr_choice == 3:
            print("What you want to Log.!"
                  "\n1.Diet  2.Workout\n")
            diet_wrkt_choice = int(input())
            if diet_wrkt_choice == 1:
                  rohan_diet_log()
            elif diet_wrkt_choice == 2:
                  rohan_wrkt_log()
            else:
                  print("print choose either 1 or 2")

      else:
            print("Please Enter the Number b/w the provided options only!")



# ========================= final program part -1 ==================================

print("----- HEALTH MANAGMENT SYSTEM ----------\n"
      "The program can be used to log & Retrieve the workout and Diet\n"
      "\n"
      "There are 3 person Enrolled currently for the program."
      "\n"
      "\n"
      "Now press \n1.to log  2.to retrieve\n")


# ==================== functions to be executed when user want to retrieve the data ===============
def harry_diet_retrieve():
      f = open("Harrydiet.txt","r")
      hd = f.read()
      print(hd)

def hammad_diet_retrieve():
      f = open("Hammaddiet.txt","r")
      hd = f.read()
      print(hd)

def rohan_diet_retrieve():
      f = open("rohandiet.txt","r")
      hd = f.read()
      print(hd)

def harry_wrkt_retrieve():
      f = open("Harrywrkt.txt","r")
      hd = f.read()
      print(hd)

def hammad_wrkt_retrieve():
      f = open("Hammadwrkt.txt","r")
      hd = f.read()
      print(hd)

def rohan_wrkt_retrieve():
      f = open("rohanwrkt.txt","r")
      hd = f.read()
      print(hd)
# ---------------------------------------------------------------------------------------------
def retrieve():
      print("you have choosed to Retrieve the data\n"
            "Choose User based on the number alloted against each user\n"
            "1. Harry   2. Hammad  3. Rohan\n")
      usr_choice = int(input())
      if usr_choice == 1:
            print("What you want to Retrieve.!"
                  "\n1.Diet  2.Workout\n")
            diet_wrkt_choice = int(input())
            if diet_wrkt_choice == 1:
                  harry_diet_retrieve()
            elif diet_wrkt_choice == 2:
                  harry_wrkt_retrieve()
            else:
                  print("print choose either 1 or 2")
      elif usr_choice == 2:
            print("What you want to Retrieve.!"
                  "\n1.Diet  2.Workout\n")
            diet_wrkt_choice = int(input())
            if diet_wrkt_choice == 1:
                  hammad_diet_retrieve()
            elif diet_wrkt_choice == 2:
                  hammad_wrkt_retrieve()
            else:
                  print("print choose either 1 or 2")

      elif usr_choice == 3:
            print("What you want to Retrieve.!"
                  "\n1.Diet  2.Workout\n")
            diet_wrkt_choice = int(input())
            if diet_wrkt_choice == 1:
                  rohan_diet_retrieve()
            elif diet_wrkt_choice == 2:
                  rohan_wrkt_retrieve()
            else:
                  print("print choose either 1 or 2")

      else:
            print("Please Enter the Number b/w the provided options only!")


# ============================================================================================
# final program part - 2 here
# ============================================================================================
log_ret_choice = int(input())
if log_ret_choice == 1:
    try:
          log()
    except Exception as e:
          print(e)
elif log_ret_choice==2:
      try:
            retrieve()
      except Exception as e:
            print(e)


# some of the functions are not written