import os
import re
import csv

os.system("cls")
# with open("studentinfo_cs384.csv",'r') as file:

print(os.getcwd())

def course():
    # Read csv and process
    cd = os.getcwd() #Directory having studentinfo_cs384.csv file
    with open('studentinfo_cs384.csv','r') as file:
        student_data = csv.DictReader(file)
    
        miscc=[]
        header=['id','full_name','country','email','gender','dob','blood_group','state']
        course_code={'01' : "btech",'11' : "mtech",'12' : "msc",'21' : "phd"}
        roll_number_re = re.compile(r'^[0-9]{2}[0-2]{2}[a-zA-Z]{2}[0-9]{2}$')    
    
        cd+=r'\analytics'
        if not os.path.isdir(cd):
            os.mkdir(cd)
        
        cd+=r'\course'
        if not os.path.isdir(cd):
            os.mkdir(cd)

        for row in student_data:
            roll_no = row['id']
            if not re.match(roll_number_re , roll_no):
                miscc.append(row)
            else:
                year_of_admission = roll_no[0:2]
                course = course_code[roll_no[2:4]]
                branch = (roll_no[4:6]).lower()
                
                cd1=cd
                cd1+="\\"+branch
                if not os.path.isdir(cd1):
                    os.mkdir(cd1)
            
                cd1+="\\"+course
                if not os.path.isdir(cd1):
                    os.mkdir(cd1)

                info_file = cd1 + "\\" + year_of_admission + '' + branch + '' + course + ".csv"

                if not os.path.isfile(info_file):
                    with open(info_file,'w',newline='') as file:
                        data = csv.DictWriter(file,fieldnames=header)
                        data.writeheader()

                with open(info_file,'a+',newline='') as file:
                    data = csv.DictWriter(file,fieldnames=header)
                    data.writerow(row)

        cd+=r'\misc.csv'
        with open(cd,'w',newline='') as file:
            data = csv.DictWriter(file,fieldnames=header)
            data.writeheader()
            data.writerows(miscc)

# def country():
#     # Read csv and process
#     pass


# def email_domain_extract():
#     # Read csv and process
#     pass


# def gender():
#     # Read csv and process
#     pass


# def dob():
#     # Read csv and process
#     pass


# def state():
#     # Read csv and process
#     pass


# def blood_group():
#     # Read csv and process
#     pass


# # Create the new file here and also sort it in this function only.
# def new_file_sort():
#     # Read csv and process
#     pass

# course()