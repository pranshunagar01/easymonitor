from flask import Flask, render_template, flash, request, url_for, redirect, session
from flask_mysqldb import MySQL
import os

app = Flask(__name__)

credentials = ['admin', '12345']

app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'KdWaBSo3YU'
app.config['MYSQL_PASSWORD'] = 'wHEiPHCP2A'
app.config['MYSQL_DB'] = 'KdWaBSo3YU'
app.config['SECRET_KEY'] = os.urandom(12).hex()
mysql = MySQL(app)

def sortfuncID(list):
    data_table = []
    for k in list:
        data_table.append(k)
    for i in range(len(data_table)):
        for j in range(len(data_table)-1):
            if data_table[j][0] > data_table[j+1][0]:
                temp = data_table[j]
                data_table[j] = data_table[j+1]
                data_table[j+1] = temp
    return data_table

def sortfuncName(list):
    data_table = []
    for k in list:
        data_table.append(k)
    for i in range(len(data_table)):
        for j in range(len(data_table)-1):
            if data_table[j][1] > data_table[j+1][1]:
                temp = data_table[j]
                data_table[j] = data_table[j+1]
                data_table[j+1] = temp
    return data_table

def sortfuncAge(list):
    data_table = []
    for k in list:
        data_table.append(k)
    for i in range(len(data_table)):
        for j in range(len(data_table)-1):
            if data_table[j][2] > data_table[j+1][2]:
                temp = data_table[j]
                data_table[j] = data_table[j+1]
                data_table[j+1] = temp
    return data_table


def sortfuncMail(list):
    data_table = []
    for k in list:
        data_table.append(k)
    for i in range(len(data_table)):
        for j in range(len(data_table)-1):
            if data_table[j][3] > data_table[j+1][3]:
                temp = data_table[j]
                data_table[j] = data_table[j+1]
                data_table[j+1] = temp
    return data_table
      


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/loginredirect', methods = ['POST', 'GET'])
def login_redirect():
    if request.form['username'] == "admin" and request.form['password'] == "12345":
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/home')
def home():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM employee")
    if result_value > 0:
        data = cur.fetchall()
    return render_template('home.html', dataEmp = data)

@app.route('/add')
def add():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM employee")
    if result_value > 0:
        data = cur.fetchall()
    return render_template('add.html', dataEmp = data)

@app.route('/addSuccess', methods = ['POST', 'GET'])
def addSuccess():
    cur = mysql.connection.cursor()
    empName = request.form['empName']
    empAge = str(request.form['empAge'])
    empMail = request.form['empMail']
    cur.execute("INSERT INTO employee(employeeName, employeeAge, employeeMail) VALUES (%s, %s, %s)", [empName, empAge, empMail])
    mysql.connection.commit()
    flash("Record successfully Added.") 
    return redirect(url_for('home'))

@app.route('/delete', methods = ['POST', 'GET'])
def delete():
    cur = mysql.connection.cursor()
    empID = str(request.form['delBtn'])
    result_value = cur.execute("SELECT * FROM employee")
    if result_value > 0:
        data = cur.fetchall()
    if len(data) == 1:
        flash("Can't delete the last record.")
        return redirect(url_for('home'))
    cur.execute("DELETE FROM employee WHERE employeeID = %s", [empID])
    mysql.connection.commit()
    flash("Record successfully Deleted.") 
    return redirect(url_for('home'))

@app.route('/modify', methods = ['POST', 'GET'])
def modify():
    cur = mysql.connection.cursor()
    empID = request.form['modBtn']
    empID1 = empID
    result_value = cur.execute("SELECT * FROM employee")
    if result_value > 0:
        data = cur.fetchall()
    return render_template('modify.html', dataEmp = data, empID = empID)

@app.route('/modifySuccess', methods = ['POST', 'GET'])
def modifySuccess():
    cur = mysql.connection.cursor()
    empID = str(request.form['empID'])
    empName = request.form['empName']
    empAge = str(request.form['empAge'])
    empMail = request.form['empMail']
    cur.execute("UPDATE employee SET employeeName = %s, employeeAge = %s, employeeMail = %s WHERE employeeID = %s", [empName, empAge, empMail, empID])
    mysql.connection.commit()
    flash("Record successfully modified.") 
    return redirect(url_for('home'))

@app.route('/sortID')
def sortID():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM employee")
    if result_value > 0:
        data = cur.fetchall()
    data = sortfuncID(data)
    flash("Sorted by ID Successfully.")
    return render_template('home.html', dataEmp = data)
    

@app.route('/sortName')
def sortName():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM employee")
    if result_value > 0:
        data = cur.fetchall()
    data = sortfuncName(data)
    flash("Sorted by Name Successfully.")
    return render_template('home.html', dataEmp = data)

@app.route('/sortAge')
def sortAge():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM employee")
    if result_value > 0:
        data = cur.fetchall()
    data = sortfuncAge(data)
    flash("Sorted by Age Successfully.")
    return render_template('home.html', dataEmp = data)

@app.route('/sortMail')
def sortMail():
    cur = mysql.connection.cursor()
    result_value = cur.execute("SELECT * FROM employee")
    if result_value > 0:
        data = cur.fetchall()
    data = sortfuncMail(data)
    flash("Sorted by Mail Successfully.")
    return render_template('home.html', dataEmp = data)
@app.errorhandler(404)
def page1(e):
    return redirect(url_for('login'))
@app.errorhandler(401)
def page2(e):
    return redirect(url_for('login'))
@app.errorhandler(400)
def page3(e):
    return redirect(url_for('login'))
@app.errorhandler(403)
def page4(e):
    return redirect(url_for('login'))
@app.errorhandler(404)
def page5(e):
    return redirect(url_for('login'))

if(__name__) == "__main__":
    app.debug = True
    app.run(debug = True)