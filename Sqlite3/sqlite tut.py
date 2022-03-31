import sqlite3
from employee import Employee

conn = sqlite3.connect('Employee_DB.sqlite')
curs = conn.cursor()

# create table query
# curs.execute('''create table employees
#                 (
#                     first text,
#                     last text,
#                     pay integer
#                 )''')

# insert into table query
# curs.execute('''insert into employees values
#                 ('Jacqeline', 'Fernandis', 50000)''')


# emp1 = Employee('Neha', 'Dhupia', 20000)
# emp2 = Employee('Lara', 'Dutta', 35000)

# curs.execute('''insert into employees values (?, ?, ?)''', (emp1.first, emp1.last, emp1.pay))
# conn.commit()

# curs.execute('''insert into employees values (:first, :last, :pay)''', {'first' : emp2.first, 'last' : emp2.last, 'pay' : emp2.pay} )
# conn.commit()

# curs.execute('''select * from employees''')
# # print(curs.fetchall())

# rows = curs.fetchall()
# for row in rows:
#      print(row)


def insert_emp(emp):
    with conn:
        curs.execute('''insert into employees values (:first, :last, :pay)''', {'first' : emp.first, 'last' : emp.last, 'pay' : emp.pay} )

def show_table():
    curs.execute('''select * from employees''')
    rows = curs.fetchall()
    for row in rows:
        print(row)

def get_emps_by_lastname(lastname):
    curs.execute('''select * from employees where last = :lastname''', {'lastname' : lastname})
    return curs.fetchall()

def update_pay(emp, pay):
    with conn:
        curs.execute('''update employees set pay = :pay
                        where first = :first and last = :last''', 
                        {'first' : emp.first, 'last' : emp.last, 'pay' : pay})

def remove_emp(emp):
    with conn:
        curs.execute('''delete from employees
                        where first = :first and last = :last''',
                        {'first' : emp.first, 'last' : emp.last})


emp1 = Employee('Katrina', 'Kaif', 70000)
emp2 = Employee('Esha', 'Deol', 40000)

# insert_emp(emp1)
# insert_emp(emp2)

# emps = get_emps_by_lastname('Kaif')
# print(emps)

# update_pay(emp2, 46000)
# show_table()

# remove_emp(emp1)
# show_table()


conn.commit()
conn.close()
