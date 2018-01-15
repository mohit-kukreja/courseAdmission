from backend import studentOperation as o
import random as r
from random import randrange

    
def login(username,password):
    
    db,cursor=o.connectDb()
    cursor.execute("select * from customer where username like '"+username+"' and password like '"+password+"' ")
    length=len(cursor.fetchall())
    
    if(length>0):
        if(username=="admin" and password=="admin"):
            return(True,999)
        else:
            return(True,000)
        
    else:
        return(False,0)
    db.close()
    
def insertIntoCustomer(**kwargs):
    sql="insert into customer ("
    counter=0
    for key in kwargs.keys():
        if(counter==len(kwargs)-1):
            sql+=key+") values ("
            
        else:
            counter=counter+1
            sql+=key+","
    counter=0
    for key in kwargs.keys():
        if(counter==len(kwargs)-1):
            sql+= "'"+kwargs[key]+"'"+")"
            
        else:
            counter=counter+1
            sql+="'"+kwargs[key]+"'"+","
    
    db,cursor=o.connectDb()
    cursor.execute(sql)
    db.commit()
    db.close()
        

def insertIntoCourse(coursename,coursefees):
    db,cursor=o.connectDb()
    id=randrange(1,1000)
    cursor.execute("insert into course values('"+str(id)+"','"+coursename+"','"+str(coursefees)+"')")
    db.commit()
    db.close()
    
def getAllCourses():
    db,cursor=o.connectDb()
    id=randrange(1,1000)
    cursor.execute("select coursename from course")
    record = cursor.fetchall()
    db.close()
    return(record)
    
def getAdmission(username,password,coursename):    
    db,cursor=o.connectDb()
    id=randrange(1,1000)
    customerid=o.getStudentId(username, password)
    courseid=o.getCourseId(coursename) 
    cursor.execute("insert into courseadmission values('"+str(id)+"','"+str(courseid[0])+"','"+str(customerid[0])+"')")
    db.commit()
    db.close()
     
def receipt_generator(username,password):
    f=open(username+"_receipt.txt","w+")
    id=o.getStudentId(username, password)
    print(id[0])
    fees= o.feesCalculator(str(id[0]))
    f.write("Your Total fees is "+str(fees[0]))
    f.close()
    
    
