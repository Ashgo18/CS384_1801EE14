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
                if course_code.get(roll_no[2:4]) == None:
                    miscc.append(row)
                    continue
                course = course_code[roll_no[2:4]]
                branch = (roll_no[4:6]).lower()
                
                cd1=cd
                cd1+="\\"+branch
                if not os.path.isdir(cd1):
                    os.mkdir(cd1)
            
                cd1+="\\"+course
                if not os.path.isdir(cd1):
                    os.mkdir(cd1)

                info_file = cd1 + "\\" + year_of_admission + "_" + branch + "_" + course + ".csv"

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

def country():
    # Read csv and process
    cd = os.getcwd()  #Directory having studentinfo_cs384.csv file
    with open('studentinfo_cs384.csv','r') as file:
        student_data = csv.DictReader(file)
    
        header=['id','full_name','country','email','gender','dob','blood_group','state']
    
        cd+=r'\analytics'
        if not os.path.isdir(cd):
            os.mkdir(cd)
        
        cd+=r'\country'
        if not os.path.isdir(cd):
            os.mkdir(cd)

        for row in student_data:
            country = row['country']
            info_file = cd + "\\" + country.lower() + ".csv"

            if not os.path.isfile(info_file):
                with open(info_file,'w',newline='') as file:
                    data = csv.DictWriter(file,fieldnames=header)
                    data.writeheader()
                
            with open(info_file,'a+',newline='') as file:
                data = csv.DictWriter(file,fieldnames=header)
                data.writerow(row)


# def email_domain_extract():
#     # Read csv and process
#     pass


def gender():
    # Read csv and process
    cd = os.getcwd() #Directory having studentinfo_cs384.csv file
    with open('studentinfo_cs384.csv','r') as file:
        student_data = csv.DictReader(file)
    
        header=['id','full_name','country','email','gender','dob','blood_group','state']
        
        cd+=r'\analytics'
        if not os.path.isdir(cd):
            os.mkdir(cd)
        
        cd+=r'\gender'
        if not os.path.isdir(cd):
            os.mkdir(cd)

        for row in student_data:
            gender = row['gender']
            info_file = cd + "\\" + gender.lower() + r'.csv'

            if not os.path.isfile(info_file):
                with open(info_file,'w',newline='') as file:
                    data = csv.DictWriter(file,fieldnames=header)
                    data.writeheader()

            with open(info_file,'a+',newline='') as file:
                data = csv.DictWriter(file,fieldnames=header)
                data.writerow(row)

def dob():
    # Read csv and process
    cd = os.getcwd() #Directory having studentinfo_cs384.csv file
    with open('studentinfo_cs384.csv','r') as file:
        student_data = csv.DictReader(file)
    
        header=['id','full_name','country','email','gender','dob','blood_group','state']
        
        cd+=r'\analytics'
        if not os.path.isdir(cd):
            os.mkdir(cd)
        
        cd+=r'\dob'
        if not os.path.isdir(cd):
            os.mkdir(cd)

        for row in student_data:
            date_of_birth = row['dob']
            birth_year = re.split('-',date_of_birth)[2]
            
            if birth_year>="1995" and birth_year<="1999":
                info_file = cd + r'\bday_1995_1999.csv'
            elif birth_year>="2000" and birth_year<="2004":
                info_file = cd + r'\bday_2000_2004.csv'
            elif birth_year>="2005" and birth_year<="2009":
                info_file = cd + r'\bday_2005_2009.csv'
            elif birth_year>="2010" and birth_year<="2014":
                info_file = cd + r'\bday_2010_2014.csv'
            elif birth_year>="2015" and birth_year<="2020":
                info_file = cd + r'\bday_2015_2020.csv'

            if not os.path.isfile(info_file):
                with open(info_file,'w',newline='') as file:
                    data = csv.DictWriter(file,fieldnames=header)
                    data.writeheader()

            with open(info_file,'a+',newline='') as file:
                data = csv.DictWriter(file,fieldnames=header)
                data.writerow(row)            



def state():
    # Read csv and process
    cd = os.getcwd()  #Directory having studentinfo_cs384.csv file
    with open('studentinfo_cs384.csv','r') as file:
        student_data = csv.DictReader(file)
    
        header=['id','full_name','country','email','gender','dob','blood_group','state']
    
        cd+=r'\analytics'
        if not os.path.isdir(cd):
            os.mkdir(cd)
        
        cd+=r'\state'
        if not os.path.isdir(cd):
            os.mkdir(cd)

        for row in student_data:
            state = row['state']
            info_file = cd + "\\" + state.lower() + ".csv"

            if not os.path.isfile(info_file):
                with open(info_file,'w',newline='') as file:
                    data = csv.DictWriter(file,fieldnames=header)
                    data.writeheader()
                
            with open(info_file,'a+',newline='') as file:
                data = csv.DictWriter(file,fieldnames=header)
                data.writerow(row)


# def blood_group():
#     # Read csv and process
#     pass


# # Create the new file here and also sort it in this function only.
# def new_file_sort():
#     # Read csv and process
#     pass

course()
# dob()
# gender()
# country()
# state()