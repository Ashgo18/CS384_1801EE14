import tkinter
from tkinter import *
import os
import bcrypt
import csv
import sqlite3
import pandas as pd
import csv
import getpass as gp

sys.setrecursionlimit(15000)


global root
root = Tk()
root.geometry('500x500')
root.title('Quiz Portal')

# conn = sqlite3.connect("project1 quiz cs384.db")
# c = conn.cursor()

# c.execute(""" CREATE TABLE project1_registration:(
#           name text,
#           roll text,
#           phone text,
#           password text
#           )""")
# conn.commit()
# conn.close()

global answers
answers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def file_transfer(answers):
    conn = sqlite3.connect('project1_quiz_cs384.db')
    c = conn.cursor()
    global df, rollnum, quiz_num
    total = [0, 0, 0, 0, 0]
    total_score = 0
    final_score = 0
    for i in range(len(df)):
        total_score += df['marks_correct_ans'][i]
        if int(answers[i]) == 0:
            total[2] += 1
        if int(df['correct_option'][i]) == int(answers[i]):
            total[0] += 1
            final_score += df['marks_correct_ans'][i]
        else:
            total[1] += 1
            if df['compulsory'][i] == 'y':
                final_score += df['marks_wrong_ans'][i]
    total[3] = final_score
    total[4] = total_score
    c.execute('SELECT * FROM project1_marks WHERE roll = ? AND quiz_num= ?',
              [rollnum, quiz_num])
    record = c.fetchall()
    if len(record):
        c.execute("""Update project1_marks SET total_marks = ? WHERE roll = ? AND quiz_num = ?""", [
                  final_score, rollnum, quiz_num])
    else:
        c.execute("INSERT INTO project1_marks values (:roll, :quiz_num, :total_marks)",
                  {
                      'roll': rollnum,
                      'quiz_num': quiz_num,
                      'total_marks': final_score
                  })
    conn.commit()
    conn.close()
    df2 = {}
    df['marked_choice'] = answers
    legends = ['Correct Choices', 'Wrong Choices',
               'Unattempted', 'Marks Obtained', 'Total Quiz Marks']
    df2['Legend'] = legends
    df2['Total'] = total
    df1 = pd.DataFrame(df2)
    df.drop('time', inplace=True, axis=1)
    df = pd.concat([df, df1], ignore_index=True, axis=1)
    file_name = 'q'+str(quiz_num)+'_'+str(rollnum) + '.csv'
    path_dir = os.path.join(os.getcwd(), 'individual_responses')
    file_path = os.path.join(path_dir, file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)
    headerlist = ['ques_no', 'question', 'option1', 'option2', 'option3', 'option4', 'correct_option', 'marks_correct_ans', 'marks_wrong_ans', 'compulsory', 'marked_choice', 'Total', 'Legend'
                  ]
    df.to_csv(file_path, header=headerlist, index=False)
    row = {'Roll': rollnum, 'Total_marks': final_score}
    file_name = 'scores_q'+str(quiz_num) + '.csv'
    path_dir = os.path.join(os.getcwd(), 'quiz_wise_responses')
    file_path = os.path.join(path_dir, file_name)
    if os.path.isfile(file_path):
        with open(file_path, 'a+', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Roll', 'Total_marks'])
            writer.writerow(row)
            file.close()
    else:
        with open(file_path, 'a+', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Roll', 'Total_marks'])
            writer.writeheader()
            writer.writerow(row)
            file.close()
    score_label = Label(
        root, text=f'Congratulations! You have scored {final_score}/{total_score}\nYou can leave this window now. Please press exit')
    score_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    quit_button = Button(root, text='EXIT', command=lambda: root.destroy()).place(
        relx=0.5, rely=0.6, anchor=CENTER)


def final_display():
    global answers
    final = Label(
        root, text='Congratulations! You have completed the quiz. Please press Continue to save the results')
    final.place(relx=0.5, rely=0.5, anchor=CENTER)
    continue_button = Button(root, text='CONTINUE!', command=lambda: [
        final.destroy(), continue_button.destroy(), file_transfer(answers)])
    continue_button.place(relx=0.5, rely=0.65, anchor=CENTER)


def save_responses(answer, n):
    global answers
    if answer:
        answers[n] = answer
        print(answers)


def destroy_button(lst):
    for i in lst:
        i.destroy()
    return


global time_destroyer
time_destroyer = 0


def time_destroy():
    global time_destroyer
    # print(time_destroyer)
    time_destroyer = 1
    # print(time_destroyer)


def time_display(alloted_time):
    global question_label, next_button, prev_button, submit_button, time_label, time_destroyer
    # if alloted_time == -20:
    #     time_label.destroy()
    #     return
    alloted_hours = int(alloted_time/60)
    alloted_mins = int(alloted_time % 60)
    # print(alloted_time, alloted_hours, alloted_mins)
    try:
        if alloted_hours < 10 and alloted_mins < 10 and time_destroyer == 0:
            time_label['text'] = f'0{alloted_hours}:0{alloted_mins}'
        elif alloted_hours < 10 and alloted_mins > 10 and time_destroyer == 0:
            time_label['text'] = f'0{alloted_hours}:{alloted_mins}'
        elif alloted_hours > 10 and alloted_mins > 10 and time_destroyer == 0:
            x = str(alloted_hours) + ':' + str(alloted_mins)
            time_label['text'] = x
        elif alloted_hours > 10 and alloted_mins < 10 and time_destroyer == 0:
            time_label['text'] = f'{alloted_hours}:0{alloted_mins}'
        elif time_destroyer == 1:
            time_label.destroy()
            return
    except:
        pass
    if alloted_time > 0:
        root.after(1000, time_display, alloted_time-1)
    else:
        next_button.destroy()
        prev_button.destroy()
        destroy_button(button_list)
        time_label.destroy()
        question_label.destroy()
        submit_button.destroy()
        final_display()


def submit_confirm(button_list):
    global question_label, next_button, prev_button, submit_button, time_label
    con = Toplevel()
    con.geometry('300x300')
    l = Label(con, text='Are you sure you want to submit?')
    l.place(relx=0.5, rely=0.3, anchor=CENTER)
    y = Button(con, text='YES', command=lambda: [
        final_display(), kill_ques(), con.destroy()])
    y.place(relx=0.3, rely=0.5, width=75, anchor=CENTER)
    n = Button(con, text='NO', command=lambda: con.destroy())
    n.place(relx=0.6, rely=0.5, width=75, anchor=CENTER)


def kill_ques():
    global question_submitter
    question_submitter = 1
    question_display(alloted_time, 1, 1)


global question_submitter
question_submitter = 0


def question_display(alloted_time, n, ch):
    global answers
    global question_submitter
    if question_submitter == 0:
        if n < 10 and n > -1:
            # print(n)
            # print(alloted_time)
            if n == 0 and ch == 0:
                alloted_time = 60*int(alloted_time)
                global time_label
                time_label = Label(root)
                time_label.place(relx=0.8, rely=0.2, anchor=CENTER)
                time_display(alloted_time)
            global question_label, next_button, prev_button, submit_button, button_list
            # for i in range(len(df)):
            question_label = Label(root)
            question_label.place(relx=0.1, rely=0.3, anchor=W)
            question_label['text'] = f"{df['ques_no'][n]}. {df['question'][int(df['ques_no'][n])-1]} [Compulsory : {df['compulsory'][n]}]"
            response = StringVar()
            k = 0.4
            button_list = []
            option = ['1', '2', '3', '4']
            for i in range(5):
                if i < 4:
                    x = 'option'+str(i+1)
                    radio_ques = Radiobutton(
                        root, text=df[x][int(df['ques_no'][n])-1], variable=response, value=i+1, indicatoron=0, width=50)
                    radio_ques.place(relx=0.1, rely=k, anchor=W)
                    # print(answers[int(df['ques_no'][n])-1], i+1)
                    h = i+1
                    if h == int(answers[int(df['ques_no'][n])-1]):
                        # print(answers[int(df['ques_no'][n])-1])
                        radio_ques.select()
                    button_list.append(radio_ques)
                    k += 0.05
                else:
                    radio_ques = Radiobutton(
                        root, text='CLEAR SELECTION', variable=response, value=0, indicatoron=0, width=50)
                    radio_ques.place(relx=0.1, rely=k, anchor=W)
                    button_list.append(radio_ques)

            next_button = Button(root, text='Save and Next', command=lambda: [save_responses(response.get(), n), question_label.destroy(), next_button.destroy(), prev_button.destroy(), submit_button.destroy(), destroy_button(button_list),
                                                                              question_display(alloted_time, n+1, 1)])
            next_button.place(relx=0.6, rely=0.8, anchor=W)
            prev_button = Button(root, text='Save and Previous', command=lambda: [save_responses(response.get(), n), question_label.destroy(), next_button.destroy(), prev_button.destroy(), submit_button.destroy(), destroy_button(button_list),
                                                                                  question_display(alloted_time, n-1, 1)])
            prev_button.place(relx=0.2, rely=0.8, anchor=W)
            submit_button = Button(root, text='Submit Quiz',
                                   command=lambda: submit_confirm(button_list))
            submit_button.place(relx=0.43, rely=0.9, anchor=W, width=75)
        elif n >= 10:
            n = 0
            ch = 1
            question_display(alloted_time, n, 1)
        elif n < 0:
            n = 9
            ch = 1
            question_display(alloted_time, n, 1)
    elif question_submitter == 1:
        next_button.destroy()
        prev_button.destroy()
        submit_button.destroy()
        question_label.destroy()
        destroy_button(button_list)
        time_destroy()
        return


global quiz_num


def commence_quiz(quiz_path, button_list):
    global n, quiz_num
    n = 0
    for i in button_list:
        i.destroy()
    quiz_path_1 = os.path.join(os.getcwd(), 'quiz_wise_questions')
    paper_path = os.path.join(quiz_path_1, quiz_path)
    global df, alloted_time
    df = pd.read_csv(paper_path)
    # print(df['time'][0])
    # global confirm_button
    # confirm_button.destroy
    alloted_time = df['time'][0]
    quiz_num = quiz_path[1:2]
    label_confirm = Label(
        root, text=f'You have picked {quiz_path[:2]}\nAlloted time = {alloted_time}\nClick on BEGIN to begin the quiz')
    label_confirm.place(
        relx=0.5, rely=0.3, anchor=CENTER)
    next_button = Button(root, text='BEGIN!', command=lambda: [
        label_confirm.destroy(), next_button.destroy(), cancel_button.destroy(), question_display(alloted_time, n, 0)])
    next_button.place(relx=0.6, rely=0.5)
    cancel_button = Button(root, text='CANCEL AND QUIT',
                           command=lambda: root.destroy())
    cancel_button.place(relx=0.3, rely=0.5)


def quiz_select(record):
    welcome_label.destroy()
    login_check.destroy()
    register_check.destroy()
    quiz_select_label = Label(
        root, text=f'Welcome {record[0][0]}\nRoll number - {record[0][1]}\nPhone Number - {record[0][2]}\nKindly select the quiz you would like to appear in')
    quiz_select_label.place(relx=0.25, rely=0.2, anchor=W)
    quiz_path = os.path.join(os.getcwd(), 'quiz_wise_questions')
    i = 1
    lst = {}
    response = StringVar()
    for file in os.listdir(quiz_path):
        q = 'quiz_'+str(i)
        lst[q] = file
        i += 1
    print(lst)
    button_list = []
    i = 0.3
    for name, path in lst.items():
        radio_res = Radiobutton(
            root, text=name, variable=response, value=path)
        radio_res.place(relx=0.5, rely=i, anchor=CENTER)
        i += 0.05
        button_list.append(radio_res)
    global confirm_button
    confirm_button = Button(root, text='CONFIRM!', command=lambda: [
        quiz_select_label.destroy(), commence_quiz(response.get(), button_list), confirm_button.destroy()])
    confirm_button.place(relx=0.5, rely=0.5, anchor=CENTER)


def login_verify(top_log, username, password):

    global rollnum
    rollnum = username
    conn = sqlite3.connect('project1_quiz_cs384.db')
    c = conn.cursor()
    c.execute('SELECT * FROM project1_registration WHERE roll = ?',
              [username])
    record = c.fetchall()
    # print(type(record), record[])
    # return
    for rec in record:
        if bcrypt.checkpw(password.encode('utf-8'), rec[3]):
            top_verify = Toplevel()
            top_verify.title('Verified')
            top_verify.geometry('250x250')
            verify_label = Label(top_verify, text='Login Successful!').place(
                relx=0.5, rely=0.5, anchor=CENTER)
            continue_button = Button(top_verify, text='CONTINUE', command=lambda: [top_log.destroy(),
                                                                                   top_verify.destroy(), quiz_select(record)]).place(relx=0.5, rely=0.7, width=75, anchor=CENTER)
            break
    else:
        top_verify = Toplevel()
        top_verify.title('Error')
        top_verify.geometry('300x300')
        verify_label = Label(top_verify, text='Invalid Username or Password!').place(
            relx=0.5, rely=0.3, anchor=CENTER)
        continue_button = Button(top_verify, text='Try Again', command=lambda: [top_log.destroy(), login_user(), top_verify.destroy()]).place(
            relx=0.2, rely=0.5, width=75, anchor=W)
        register_check = Button(top_verify, text='Register',
                                command=lambda: [register_user(), top_log.destroy(), top_verify.destroy()]).place(
            relx=0.5, rely=0.5, width=75, anchor=W)


global rollnum


def register_new(top_reg, username, roll, phone, password):
    hashable_pw = bytes(password, encoding='utf-8')
    hashed_pw = bcrypt.hashpw(hashable_pw, bcrypt.gensalt())
    print(hashable_pw)
    print(hashed_pw)
    global rollnum
    rollnum = roll
    conn = sqlite3.connect('project1_quiz_cs384.db')
    c = conn.cursor()
    c.execute('SELECT * FROM project1_registration WHERE roll = ? AND password = ?',
              [roll, hashed_pw])
    record = c.fetchall()
    if len(record):
        top_verify = Toplevel()
        top_verify.title('Error')
        top_verify.geometry('250x250')
        verify_label = Label(top_verify, text='Username already exists!').place(
            relx=0.5, rely=0.2, anchor=CENTER)
        continue_button = Button(top_verify, text='Try Again', command=lambda: [top_reg.destroy(), top_verify.destroy(), register_user()]).place(
            relx=0.2, rely=0.5, width=75, anchor=CENTER)
        register_check = Button(top_verify, text='Login',
                                command=lambda: [login_user(), top_reg.destroy(), top_verify.destroy()]).place(
            relx=0.6, rely=0.5, width=75, anchor=W)
    else:
        c.execute("INSERT INTO project1_registration VALUES (:name, :roll, :phone, :password)",
                  {
                      'name': username,
                      'roll': roll,
                      'phone': phone,
                      'password': hashed_pw
                  })
        conn.commit()
        conn.close()
        top_verify = Toplevel()
        top_verify.title('Registered!')
        top_verify.geometry('150x150')
        record1 = []
        record1.append(username)
        record1.append(roll)
        record1.append(phone)
        record1.append(password)
        record2 = tuple(record1)
        record = []
        record.append(record2)
        verify_label = Label(top_verify, text='Registration Successful!').place(
            relx=0.5, rely=0.5, anchor=CENTER)
        continue_button = Button(top_verify, text='CONTINUE', command=lambda: [top_reg.destroy(),
                                                                               top_verify.destroy(), quiz_select(record)]).place(relx=0.5, rely=0.7, width=75, anchor=CENTER)


def login_user():
    top_login = Toplevel()
    top_login.title('Login')
    top_login.geometry('400x400')
    user_name_label = Label(top_login, text="User name").place(
        relx=0.2, rely=0.3, anchor=W)
    user_name_entry = Entry(top_login, text='Enter username (Roll no)')
    user_name_entry.place(
        relx=0.4, rely=0.3, anchor=W)
    password_label = Label(top_login, text="Password").place(
        relx=0.2, rely=0.4, anchor=W)
    password_entry = Entry(top_login, show='*')
    password_entry.place(
        relx=0.4, rely=0.4, anchor=W)
    login_button = Button(top_login, text='LOGIN', command=lambda: login_verify(top_login,
                                                                                user_name_entry.get(), password_entry.get())).place(relx=0.3, rely=0.5, width=75, anchor=W)
    cancel_button = Button(top_login, text='CANCEL', command=lambda: top_login.destroy(
    )).place(relx=0.5, rely=0.5, width=75, anchor=W)


def register_user():
    top_reg = Toplevel()
    top_reg.title('Login')
    top_reg.geometry('400x400')
    user_name_label = Label(top_reg, text="Name").place(
        relx=0.15, rely=0.3, anchor=W)
    user_name_entry = Entry(top_reg)
    user_name_entry.place(
        relx=0.4, rely=0.3, anchor=W)
    roll_label = Label(top_reg, text="Roll no(username)").place(
        relx=0.15, rely=0.4, anchor=W)
    roll_entry = Entry(top_reg)
    roll_entry.place(
        relx=0.4, rely=0.4, anchor=W)
    phone_label = Label(top_reg, text="Phone Number").place(
        relx=0.15, rely=0.5, anchor=W)
    phone_entry = Entry(top_reg)
    phone_entry.place(
        relx=0.4, rely=0.5, anchor=W)
    password_label = Label(top_reg, text="Password").place(
        relx=0.15, rely=0.6, anchor=W)
    password_entry = Entry(top_reg)
    password_entry.place(
        relx=0.4, rely=0.6, anchor=W)

    register_button = Button(top_reg, text='REGISTER', command=lambda: register_new(top_reg, user_name_entry.get(
    ), roll_entry.get(), phone_entry.get(), password_entry.get())).place(relx=0.3, rely=0.7, width=75, anchor=W)
    cancel_button = Button(top_reg, text='CANCEL', command=lambda: top_reg.destroy(
    )).place(relx=0.5, rely=0.7, width=75, anchor=W)


welcome_label = Label(
    root, text='Welcome to the Quizzing Portal.\nKindly Login or Register yourself')
welcome_label.place(
    relx=0.5, rely=0.2, anchor=CENTER)

login_check = Button(root, text='Existing user/Login',
                     command=login_user)
login_check.place(relx=0.2, rely=0.4, width=125, height=30, anchor=W)

register_check = Button(root, text='New user/Register',
                        command=register_user)
register_check.place(relx=0.5, rely=0.4, width=125, height=30, anchor=W)


# my_label = Label(root, text='Created By Yuvi Dhelawat').place(
#     relx=0.5, rely=0.9, anchor=CENTER)
root.mainloop()
