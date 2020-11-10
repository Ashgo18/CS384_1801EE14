import os
import re
import csv
import shutil

os.system('cls')

cd=os.getcwd()
print(cd)

cd=os.path.join(cd,'grades')
if os.path.isdir(cd):
    shutil.rmtree(cd)

os.mkdir(cd)

grade_map = {'AA':10,'AB':9,'BB':8,'BC':7,'CC':6,'CD':5,'DD':4,'F':0,'I':0}
roll_number_re = re.compile(r'^[0-9]{2}[0-2]{2}[a-zA-Z]{2}[0-9]{2}$')
header_misc = ['sl','roll','sem','year','sub_code','total_credits','credit_obtained','timestamp','sub_type']
header_individual = ['Subject','Credits','Type','Grade','Sem']
header_overall = ['Semester','Semester Credits','Semester Credits Cleared','SPI','Total Credits','Total Credits Cleared','CPI']

with open('acad_res_stud_grades.csv','r') as file:
    students_data = csv.DictReader(file)     
    misc = []

    for row in students_data:
        roll_no = row['roll']
        course = row['sub_code']
        course_credit = row['total_credits']
        grade_obtained = row['credit_obtained']
        sub_typ = row['sub_type']
        sem_no = row['sem']

        if grade_map.get(grade_obtained) == None:
            misc.append(row)
        else:
            info_file = os.path.join(cd,roll_no+'_individual.csv')
            if not os.path.isfile(info_file):
                with open(info_file,'w',newline='') as file:
                    data = csv.writer(file)
                    data.writerow(["Roll: "+roll_no])
                    data.writerow(["Semester Wise Details"])
                    data.writerow(header_individual)

            with open(info_file,'a+',newline='') as file:
                data = csv.writer(file)
                data.writerow([course,course_credit,sub_typ,grade_obtained,sem_no])

    

