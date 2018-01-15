import pymysql as s
def connectDb():
    db=s.connect("localhost","root","","pybatch")
    cursor=db.cursor()
    return (db,cursor)

def createCourseTable():
    db,cursor=connectDb()
    cursor.execute("create table course(id int primary key,coursename varchar(200),coursefees varchar(200))")
    db.commit()
    db.close()

def createCourseAdmission():
    db,cursor=connectDb()
    cursor.execute("create table courseadmission(id int primary key,courseid varchar(200),customerid varchar(200))")
    db.commit()
    db.close()


def getStudentId(username,password):
    db,cursor=connectDb()
    cursor.execute("select id from customer where username like '"+username+"' and password like '"+password+"'")
    record=cursor.fetchone()
    db.close()
    return(record) 

def getCourseId(coursename):
    db,cursor=connectDb()
    cursor.execute("select id from course where coursename like '"+coursename+"'")
    record=cursor.fetchone()
    db.close()
    return(record) 
    
def feesCalculator(customerid):
    db,cursor=connectDb()
    cursor.execute("select sum(c.coursefees) from course as c inner join courseadmission as a on a.customerid like '"+customerid+"' and c.id like a.courseid ")
    record=cursor.fetchone()
    db.close()
    return(record)