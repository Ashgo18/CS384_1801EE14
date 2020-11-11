import os
import re
import csv
import shutil

os.system("cls")
def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    cd = os.getcwd()
    cd = os.path.join(cd,'analytics')
    if os.path.isdir(cd):
        shutil.rmtree(cd)


def course():
    # Read csv and process
    cd = os.getcwd() #Directory having studentinfo_cs384.csv file
    with open('studentinfo_cs384.csv','r') as file:
        student_data = csv.DictReader(file)
    
        miscc=[]
        header=['id','full_name','country','email','gender','dob','blood_group','state']
        course_code={'01' : "btech",'11' : "mtech",'12' : "msc",'21' : "phd"}
        roll_number_re = re.compile(r'^[0-9]{2}[0-2]{2}[a-zA-Z]{2}[0-9]{2}$')    
    
        cd = os.path.join(cd,'analytics')
        if not os.path.isdir(cd):
            os.mkdir(cd)
        
        cd = os.path.join(cd,'course')
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
                cd1 = os.path.join(cd1,branch)
                if not os.path.isdir(cd1):
                    os.mkdir(cd1)
            
                cd1 = os.path.join(cd1,course)
                if not os.path.isdir(cd1):
                    os.mkdir(cd1)

                info_file = os.path.join(cd1,year_of_admission + "_" + branch + "_" + course + ".csv")

                if not os.path.isfile(info_file):
                    with open(info_file,'w',newline='') as file:
                        data = csv.DictWriter(file,fieldnames=header)
                        data.writeheader()

                with open(info_file,'a+',newline='') as file:
                    data = csv.DictWriter(file,fieldnames=header)
                    data.writerow(row)

        cd = os.path.join(cd,'misc.csv')
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
    
        cd = os.path.join(cd,'analytics')
        if not os.path.isdir(cd):
            os.mkdir(cd)
        
        cd = os.path.join(cd,'country')
        if not os.path.isdir(cd):
            os.mkdir(cd)

        for row in student_data:
            country = row['country']

            if country == "":
                country = "misc"
            info_file = os.path.join(cd,country.lower() + ".csv")

            if not os.path.isfile(info_file):
                with open(info_file,'w',newline='') as file:
                    data = csv.DictWriter(file,fieldnames=header)
                    data.writeheader()
                
            with open(info_file,'a+',newline='') as file:
                data = csv.DictWriter(file,fieldnames=header)
                data.writerow(row)


def email_domain_extract():
    # Read csv and process
    cd = os.getcwd() #Directory having studentinfo_cs384.csv file
    with open('studentinfo_cs384.csv','r') as file:
        student_data = csv.DictReader(file)
    
        header=['id','full_name','country','email','gender','dob','blood_group','state']
        
        cd = os.path.join(cd,'analytics')
        if not os.path.isdir(cd):
            os.mkdir(cd)
        
        cd = os.path.join(cd,'email_domains')
        if not os.path.isdir(cd):
            os.mkdir(cd)

        for row in student_data:
            email = re.split('@',row['email'])[1]
            email_domain = re.split(r'\.',email)[0]

            if email_domain == "":
                email_domain = "misc"
            info_file = os.path.join(cd ,email_domain.lower() + ".csv")

            if not os.path.isfile(info_file):
                with open(info_file,'w',newline='') as file:
                    data = csv.DictWriter(file,fieldnames=header)
                    data.writeheader()

            with open(info_file,'a+',newline='') as file:
                data = csv.DictWriter(file,fieldnames=header)
                data.writerow(row)


def gender():
    # Read csv and process
    cd = os.getcwd() #Directory having studentinfo_cs384.csv file
    with open('studentinfo_cs384.csv','r') as file:
        student_data = csv.DictReader(file)
    
        header=['id','full_name','country','email','gender','dob','blood_group','state']
        
        cd = os.path.join(cd,'analytics')
        if not os.path.isdir(cd):
            os.mkdir(cd)
        
        cd = os.path.join(cd,'gender')
        if not os.path.isdir(cd):
            os.mkdir(cd)

        for row in student_data:
            gender = row['gender']
            if gender == "":
                gender ="misc"
            info_file = os.path.join(cd ,gender.lower() + ".csv")

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
        
        cd = os.path.join(cd,'analytics')
        if not os.path.isdir(cd):
            os.mkdir(cd)
        
        cd = os.path.join(cd,'dob')
        if not os.path.isdir(cd):
            os.mkdir(cd)

        for row in student_data:
            date_of_birth = row['dob']
            birth_year = re.split('-',date_of_birth)[2]
            
            if birth_year>="1995" and birth_year<="1999":
                info_file = os.path.join(cd ,'bday_1995_1999.csv')
            elif birth_year>="2000" and birth_year<="2004":
                info_file = os.path.join(cd , 'bday_2000_2004.csv')
            elif birth_year>="2005" and birth_year<="2009":
                info_file = os.path.join(cd , 'bday_2005_2009.csv')
            elif birth_year>="2010" and birth_year<="2014":
                info_file = os.path.join(cd , 'bday_2010_2014.csv')
            elif birth_year>="2015" and birth_year<="2020":
                info_file = os.path.join(cd , 'bday_2015_2020.csv')
            else:
                info_file = os.path.join(cd , 'misc.csv')

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
    
        cd = os.path.join(cd , 'analytics')
        if not os.path.isdir(cd):
            os.mkdir(cd)
        
        cd = os.path.join(cd , 'state')
        if not os.path.isdir(cd):
            os.mkdir(cd)

        for row in student_data:
            state = row['state']
            if state == "":
                state = "misc"
            info_file = os.path.join(cd ,state.lower() + ".csv")

            if not os.path.isfile(info_file):
                with open(info_file,'w',newline='') as file:
                    data = csv.DictWriter(file,fieldnames=header)
                    data.writeheader()
                
            with open(info_file,'a+',newline='') as file:
                data = csv.DictWriter(file,fieldnames=header)
                data.writerow(row)


def blood_group():
    # Read csv and process
    cd = os.getcwd()  #Directory having studentinfo_cs384.csv file
    with open('studentinfo_cs384.csv','r') as file:
        student_data = csv.DictReader(file)
    
        header=['id','full_name','country','email','gender','dob','blood_group','state']
    
        cd = os.path.join(cd , 'analytics')
        if not os.path.isdir(cd):
            os.mkdir(cd)
        
        cd = os.path.join(cd ,'blood_group')
        if not os.path.isdir(cd):
            os.mkdir(cd)

        for row in student_data:
            blood_group = row['blood_group']
            if blood_group == "":
                blood_group = "misc"
            info_file = os.path.join(cd , blood_group.lower() + ".csv")

            if not os.path.isfile(info_file):
                with open(info_file,'w',newline='') as file:
                    data = csv.DictWriter(file,fieldnames=header)
                    data.writeheader()
                
            with open(info_file,'a+',newline='') as file:
                data = csv.DictWriter(file,fieldnames=header)
                data.writerow(row)


# # Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    cd = os.getcwd()  #Directory having studentinfo_cs384.csv file
    with open('studentinfo_cs384.csv','r') as file:
        student_data = csv.DictReader(file)
    
        header=['id','first_name','last_name','country','email','gender','dob','blood_group','state']
    
        cd = os.path.join(cd , 'analytics')
        if not os.path.isdir(cd):
            os.mkdir(cd)

        for row in student_data:
            full_name = re.split(' ',row['full_name'],maxsplit=1)
            first_name = full_name[0]
            last_name = full_name[1]
            new_row = row.copy()
            new_row['first_name'] = first_name
            new_row['last_name'] = last_name
            del new_row['full_name']
            
            info_file = os.path.join(cd ,'studentinfo_cs384_names_split.csv')

            if not os.path.isfile(info_file):
                with open(info_file,'w',newline='') as file:
                    data = csv.DictWriter(file,fieldnames=header)
                    data.writeheader()
                
            with open(info_file,'a+',newline='') as file:
                data = csv.DictWriter(file,fieldnames=header)
                data.writerow(new_row)

            sorted_file = os.path.join(cd , 'studentinfo_cs384_names_split_sorted_first_name.csv')

            sorted_list = []
            with open(info_file,'r',newline='') as file:
                data = csv.reader(file)
                sorted_list = sorted(data, key=lambda row: row[1])
            with open(sorted_file,'w',newline='') as file:
                data = csv.writer(file)
                data.writerow(header)
                data.writerows(sorted_list[:-1])
                