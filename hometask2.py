import math

ls_users = [
    ['lori49@gmail.com', 'Victor', 'Webb', '20:07:1996', 'male'],
    ['rodriguezbryan@gmail.com', 'Patrick', 'Logan', '17:08:1998', 'male'],
    ['troyjones@gmail.com', 'Megan', 'Yates', '19:08:1998', 'female'],
    ['shannon51@gmail.com', 'Geoffrey', 'Kent', '16:05:1995', 'male'],
    ['marymills@gmail.com', 'Travis', 'Allen', '12:05:1997', 'male'],
    ['dillon67@gmail.com', 'Courtney', 'Soto', '04:07:1996', 'female'],
    ['kellypalmer@gmail.com', 'Matthew', 'Wright', '05:10:1998', 'male'],
    ['jamesmartha@gmail.com', 'Amy', 'Chavez', '04:04:1998', 'female'],
    ['walshmorgan@gmail.com', 'Jennifer', 'Jones', '11:04:1998', 'female'],
    ['olivia45@gmail.com', 'Paul', 'Santiago', '19:05:1996', 'male'],
    ['dianecantrell@gmail.com', 'Anita', 'Davis', '04:02:1997', 'female'],
    ['courtney10@gmail.com', 'Samuel', 'James', '15:01:1995', 'male'],
    ['diamond36@gmail.com', 'George', 'Barry', '27:03:1996', 'male'],
    ['stephanie54@gmail.com', 'Matthew', 'Montgomery', '03:01:1996', 'male'],
    ['catherinebright@gmail.com', 'Joshua', 'Chang', '07:04:1998', 'male'],
    ['castrobryan@gmail.com', 'Christopher', 'White', '02:11:1996', 'female'],
    ['jessica39@gmail.com', 'Lori', 'Byrd', '10:02:1997', 'female'],
    ['andersondavid@gmail.com', 'Andrew', 'Williams', '19:04:1996', 'male'],
    ['rhall@gmail.com', 'Abigail', 'Peters', '23:08:1995', 'female'],
    ['hlopez@gmail.com', 'Julie', 'Jacobs', '13:07:1996', 'female']
]


def task1():
 manCount = 0
 girlsCount = 0
 for email, name, surname, date, gender in ls_users:
  if gender == 'male':
   manCount = manCount + 1
  else:
   girlsCount = girlsCount + 1

 print('В группе всего', manCount + girlsCount, 'человек, из них', manCount, '- парни,', girlsCount, '- девушки')


def task2():
 for email, name, surname, date, gender in ls_users:
  if gender == 'female' and name[:1] == 'A':
   print(name, surname)

def task3():
 april_list = []
 for email, name, surname, date, gender in ls_users:
  april_list = date.split(':')
  if april_list[1] == '04':
   print(name, surname, date)

def task4():
 today = '01:10:2021'
 format_today = today.split(':')
 age_list = []
 for email, name, surname, date, gender in ls_users:
  date_list = date.split(':')
  age = math.trunc((((int(format_today[2]) - int(date_list[2])) * 365 + (int(date_list[0]) + (int(date_list[1])-1) * 30))) / 365)
  #print(name, surname, age)
  age_list.append([name + ' ' + surname, age])
  #print(((int(format_today[2]) - int(date_list[2])) * 365 + (int(date_list[0]) + (int(date_list[1])-1) * 30)))
  #print(int(format_today[2]))
 for x in age_list:
  print(x)

def task4_1():
 today = '01:10:2021'
 format_today = today.split(':')
 age_list = []

 for email, name, surname, date, gender in ls_users:
  date_list = date.split(':')
  age = math.trunc((((int(format_today[2]) - int(date_list[2])) * 365 + (int(date_list[0]) + (int(date_list[1])-1) * 30))) / 365)
  # print(name, surname, age)
  age_list.append([name + ' ' + surname, age])

 maxAge = 0
 oldStudentList = []

 for name_surname, age in age_list:
  if maxAge < int(age):
   maxAge = int(age)
 #print(maxAge)
 for name_surname, age in age_list:
  if int(age) == maxAge:
   oldStudentList.append([name_surname, age])

 print(oldStudentList)






task4_1()







