import csv
import os
import re
import pandas as pd
import shutil

os.system("cls")

cd = os.getcwd()
cd = os.path.join(cd, 'groups')

if os.path.isdir(cd):
    shutil.rmtree(cd)

os.mkdir(cd)


def group_allocation(filename, number_of_groups):
    # Entire Logic

    # Sorting given file i.e FILENAME
    temp_file = 'tempdata.csv'
    data = pd.read_csv(filename)
    data.set_index('Roll', inplace=True)
    data.sort_values(["Roll"], axis=0, ascending=True, inplace=True)
    data.to_csv(temp_file)

    branch_strength_header = ['BRANCH_CODE', 'STRENGTH']
    branch_header = ['Name', 'Roll', 'Email']
    stats_grouping_header = ['Group', 'Total']
    branch_total = {}
    groups_stats_info = []

    with open(temp_file, 'r') as file:
        data1 = csv.reader(file)
        skip = 1

        for row in data1:
            if skip:
                skip = 0
                continue

            roll = row[0]
            branch = (re.findall(r'\D+', roll)[0]).upper()

            if branch_total.get(branch) == None:
                branch_total[branch] = 0

            branch_total[branch] += 1

            # Creating branch files
            curr_file = os.path.join(cd, branch + '.csv')

            if not os.path.isfile(curr_file):
                with open(curr_file, 'w', newline='') as file:
                    data = csv.writer(file)
                    data.writerow(branch_header)

            with open(curr_file, 'a+', newline='') as file:
                data = csv.writer(file)
                data.writerow(row)

        # Creating Branch_strength file
        branch_total = sorted(branch_total.items(),
                              key=lambda ag: (-ag[1], ag[0]))
        branch_total = dict(branch_total)
        branch_total_tups = branch_total.items()

        cd1 = os.path.join(cd,'branch_strength.csv')
        with open(cd1, 'w', newline='') as file:
            data = csv.writer(file)
            data.writerow(branch_strength_header)
            for i in branch_total_tups:
                data.writerow(list(i))

        # Creating Stats_grouping file
        group_names = []
        groups_total = []

        for key in branch_total:
            stats_grouping_header.append(key)

        for i in range(1, number_of_groups+1):
            groups_total.append(0)

            if i < 10:
                group_names.append("Group_G0" + str(i))
            else:
                group_names.append("Group_G" + str(i))

        present_group = 0
        groups_stats_info.append(group_names)
        groups_stats_info.append(groups_total)

        for key in branch_total:
            temp = []
            total_stud = branch_total[key]
            stud_per_group = total_stud//number_of_groups
            remaining_stud = total_stud - stud_per_group*number_of_groups

            for j in range(number_of_groups):
                temp.append(stud_per_group)
                groups_stats_info[1][j] += stud_per_group

            while remaining_stud:
                temp[present_group] += 1
                groups_stats_info[1][present_group] += 1
                remaining_stud -= 1
                present_group += 1
                present_group %= number_of_groups

            groups_stats_info.append(temp)

        cd1 = os.path.join(cd,'stats_grouping.csv')
        with open(cd1 , 'w', newline='') as file:
            data = csv.writer(file)
            data.writerow(stats_grouping_header)

            for i in range(number_of_groups):
                temp = []

                for j in range(len(groups_stats_info)):
                    temp.append(groups_stats_info[j][i])

                data.writerow(temp)

        # Creating Individual Groups
        temp = 1

        for key in branch_total:
            cdd = os.path.join(cd, key+'.csv')
            with open(cdd, 'r') as file:
                data = csv.reader(file)
                data_list = list(data)
                del data_list[0]

                z = 0
                x = 0
                temp += 1
                for i in range(number_of_groups):
                    curr_file = os.path.join(
                        cd, groups_stats_info[0][i]+'.csv')
                    z += groups_stats_info[temp][i]

                    if not os.path.isfile(curr_file):
                        with open(curr_file, 'w', newline='') as file:
                            data = csv.writer(file)
                            data.writerow(branch_header)

                    with open(curr_file, 'a+', newline='') as file:
                        data = csv.writer(file)
                        while x < z:
                            data.writerow(data_list[x])
                            x += 1

    os.remove(temp_file)


filename = "Btech_2020_master_data.csv"
number_of_groups = int(
    input("Enter the number of groups in which students have to be divided:- "))
group_allocation(filename, number_of_groups)
