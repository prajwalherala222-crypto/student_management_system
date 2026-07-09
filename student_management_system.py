# 1. Student Management System ⭐⭐⭐


# Concepts: Functions, Lists, Dictionaries, Loops

# Features:

# Add student
# View all students
# Search by roll number
# Update marks
# Delete student
# Calculate average marks
import json

def save_data():
     with open("students.json","w")as file:
          json.dump(details,file,indent=4)
     print("Data saved successfully")


import os
if os.path.exists("students.json"):
     with open("students.json","r") as file:
          details = json.load(file)
else:
     details = []

     



def add_student():
    if details:
         roll_num = details[-1]["roll_num"] +1
    else:
         roll_num = 1

    student_details = {
    "roll_num" : roll_num,
    "name" : input("ENTER THE NAME : "),
    "age" : int(input("ENTER THE AGE : ")),
    "marks" : int(input("ENTER THE MARKS : ")), 
    "course" : input("ENTER THE COURSE NAME :")
    }
    details.append(student_details)
    save_data()
    
    

def average_marks():
    marks = []
    count = 0
    total = 0
    for i in details:
            for j in i:
                aa = i.get("marks")
            marks.append(aa)
            count+= 1
    for j in marks:
         total += j
    print(f" Average marks of students is {total /count}")


def view_all_students():
     if not details:
          print("No students found")
     for student in details:
          print("-"*30)
          print("Roll number -",student["roll_num"])
          print("Name -",student["name"])
          print("Age -",student["age"])
          print("Marks -",student["marks"])
          print("Course -",student["course"])
          print("-"*30)
     
    
        

def delete_student():
    roll_num = int(input("ENTER THE ROLL NUMBER :"))
    for student in details:
        if student.get("roll_num") == roll_num:
             details.remove(student)
             print(details)
             save_data()
             break
    else:
        print("not found")
    
    

def search_by_roll_number():
        roll_number = int(input("Roll number : "))
        for student in details:
               if roll_number == student["roll_num"]:
                    print("-"*30)
                    print("Roll number -",student["roll_num"])
                    print("Name -",student["name"])
                    print("Age -",student["age"])
                    print("Marks -",student["marks"])
                    print("Course -",student["course"])
                    print("-"*30)
                    break
        else:
          print("roll number not exists")
          
              
def update_marks():
    roll_number  = int(input("ENTER THE ROLL NUMBER ACCORDING TO CREDENTIALS : "))
    for i in details:
         if i.get("roll_num") == roll_number:
              new_marks = int(input("ENTER THE UPDATED MARKS : "))
              i["marks"] = new_marks
              print(details)
              save_data()
              break
    else:
        print("student not found")




print("WELCOME TO SCHOOL WEBSITE!!!!")

try:
     school_code = int(input("ENTER THE SCHOOL CODE : "))
     password = input("ENTER THE PASSWORD : ")
     while(school_code != 1111 or password != "luminar"):
          school_code = int(input("ENTER THE SCHOOL CODE : "))
          password = input("ENTER THE PASSWORD : ")
     else:
          print()
          while True:
               print(f"1) Add student\n2) View all students\n3) Search by roll number\n4) Update marks\n5) Delete student\n6) Calculate average marks\n7)Exit")
               print()
               choice = int(input("ENTER THE CHOICE NUMBER : "))
               if choice == 1:
                    add_student()
               elif choice == 2:
                    view_all_students()
                    break
               elif choice == 3:
                    search_by_roll_number()
               elif choice == 4:
                    update_marks()
               elif choice == 5:
                    delete_student()
               elif choice == 6:
                    average_marks()
               elif choice == 7:
                    print("THANK YOU!!!")
                    break
               else:
                    print("invalid choice")
               print()

          else:

               print("INCORRECT SCHOOL_CODE OR PASSWORD")


except ValueError:

     print("enter the correct credentials")