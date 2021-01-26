import os
import re
import csv
import shutil

os.system('cls')

cd = os.getcwd()
print(cd)

cd = os.path.join(cd, 'grades')
if os.path.isdir(cd):
    shutil.rmtree(cd)

os.mkdir(cd)

grade_map = {'AA': 10, 'AB': 9, 'BB': 8, 'BC': 7,
             'CC': 6, 'CD': 5, 'DD': 4, 'F': 0, 'I': 0}
roll_number_re = re.compile(r'^[0-9]{2}[0-2]{2}[a-zA-Z]{2}[0-9]{2}$')
header_misc = ['sl', 'roll', 'sem', 'year', 'sub_code',
               'total_credits', 'credit_obtained', 'timestamp', 'sub_type']
header_individual = ['Subject', 'Credits', 'Type', 'Grade', 'Sem']
header_overall = ['Semester', 'Semester Credits', 'Semester Credits Cleared',
                  'SPI', 'Total Credits', 'Total Credits Cleared', 'CPI']

with open('acad_res_stud_grades.csv', 'r') as file:
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
            info_file = os.path.join(cd, roll_no+'_individual.csv')
            if not os.path.isfile(info_file):
                with open(info_file, 'w', newline='') as file:
                    data = csv.writer(file)
                    data.writerow(["Roll: "+roll_no])
                    data.writerow(["Semester Wise Details"])
                    data.writerow(header_individual)

            with open(info_file, 'a+', newline='') as file:
                data = csv.writer(file)
                data.writerow(
                    [course, course_credit, sub_typ, grade_obtained, sem_no])

    if len(misc) != 0:
        info_file = os.path.join(cd, 'misc.csv')
        with open(info_file, 'w', newline='') as file:
            data = csv.DictWriter(file, fieldnames=header_misc)
            data.writeheader()
            data.writerows(misc)

individual_files = os.listdir(cd)

for file in individual_files:
    if file != 'misc.csv':
        roll_no = re.split(r'_', file)[0]
        cd1 = os.path.join(cd, file)

        credit_clrd_per_sem = {}  # Dictionary of semester wise credits cleared
        total_credit_per_sem = {}  # Dictionary of semester wise total credits
        grade_obtn_per_sem = {}  # Dictionary of semester wise grade obtained
        corresponding_credit = {}  # Dictionary of semester wise credits corresponding to grade

        with open(cd1, 'r') as f:
            data = csv.reader(f)
            x = 0
            for row in data:
                x = x+1
                if(x > 3):
                    # if particular sem is not in dict then
                    if grade_obtn_per_sem.get(row[4]) == None:
                        # row[4] is a sem number
                        credit_clrd_per_sem[row[4]] = 0
                        total_credit_per_sem[row[4]] = 0
                        grade_obtn_per_sem[row[4]] = []
                        corresponding_credit[row[4]] = []

                    grade_obtn_per_sem[row[4]].append(
                        grade_map[row[3]])  # row[3] is grade to course
                    corresponding_credit[row[4]].append(int(row[1]))
                    total_credit_per_sem[row[4]] += int(row[1])
                    if(row[3] != 'F' and row[3] != 'I'):
                        credit_clrd_per_sem[row[4]] += int(row[1])

        cd1 = os.path.join(cd, roll_no+'_overall.csv')
        tot_credit_clrd = 0  # total credits cleared till that sem
        tot_credits = 0  # total credits till that sem

        with open(cd1, 'w', newline='') as f:
            data = csv.writer(f)
            data.writerow(["Roll: "+roll_no])
            data.writerow(header_overall)

            cpi = 0
            total_sems = int(list(grade_obtn_per_sem.keys())[-1])
            for sem in range(1, total_sems+1):
                spi = 0
                semester = str(sem)
                if grade_obtn_per_sem.get(semester) == None:
                    data.writerow([semester, 0, 0, 0, 0, 0, 0])
                    continue

                for x in range(0, len(grade_obtn_per_sem[semester])):
                    spi = spi + \
                        grade_obtn_per_sem[semester][x] * \
                        corresponding_credit[semester][x]

                spi = spi/total_credit_per_sem[semester]
                cpi = cpi*tot_credits + spi*total_credit_per_sem[semester]
                tot_credits += total_credit_per_sem[semester]
                cpi = cpi/tot_credits
                tot_credit_clrd += credit_clrd_per_sem[semester]
                data.writerow([semester, total_credit_per_sem[semester], credit_clrd_per_sem[semester], round(
                    spi, 2), tot_credits, tot_credit_clrd, round(cpi, 2)])
