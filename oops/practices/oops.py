# # class DemoClass():
# # #Class Name should be titlecase.
# #     def __str__(self):
# #         return "DemoClass" #object representing built-in method
# #         #Note: __str__ or __repr__ is only to represent 
# #     def __repr__(self):
# #         return "Class Object" #represented built-in method
# #     def __add__(self,obj2):
# #         return str(self)+" "+str(obj2)
# #     def __mul__(self,obj2):
# #         return "multiple object"

# # #creating object of class
# # # obj = DemoClass()
# # # print(obj)
# # # print(type(obj))

# # obj1 = DemoClass()
# # obj2 = DemoClass()

# # # print(obj1+obj2)
# # # print(obj1*obj2)

# # #########################################################

# # #Constructors in OOPS

# # class ConstructorDemo():
# #     def __init__(self):     #__init__(self) is constructor and "self" is a object of that class
# #         print("Constructor initialized")

# # #obj1 = ConstructorDemo()

# # class Employee():
# #     def __init__(self,name,salary,designation):
# #         self.name = name
# #         self.salary = salary
# #         self.designation = designation
    
# #     def getName(self):
# #         return self.name
    
# #     def getSalary(self):
# #         return self.salary
    
# #     def getDesignation(self):
# #         return self.designation
    
# #     def getSalaryWithTax(self,tax = 0.15 ):
# #         salary = float(self.salary) if(type(self.salary) == type('str')) else self.salary
# #         return salary+(salary*tax)
    
# #     def __str__(self):
# #         return self.name

# # emp1 = Employee("Rajesh","34000","ASE")
# # emp2 = Employee("Raj","40000","SSE")

# # #print(emp1)

# # # print(emp1.getSalary())
# # # print(emp2.getSalaryWithTax())

# # #############################################

# # #Calling class variables

# # print(emp1.salary)
# # print(emp1.name)
# # print(emp1.designation)
# # #Updating class varibales

# # emp1.salary(50000)
# # print(emp1.getSalary()) # it will update the values already passed hence we have to make the object strict private

# ###############################################
# # Note: by adding __ before class variables,methods or inner class we can hide it from the direct access.
# ###############################################

# class Course():
#     def addCourse(self,course_name,course_fees,course_address):
#         self.__course_name = course_name
#         self.__course_fees = course_fees
#         self.__course_address = course_address
#         columns = {'course_name':self.__course_name,'course_fees':self.__course_fees,'course_address':self.__course_address}
#         return self.__insertIntoDB(tablename ="course",columns = columns)
    
#     def __insertIntoDB(self,tablename,columns,ip = "localhost",uname = "root",password = "04200420",dbname = "oops_practices"):
#         try:
#             import pymysql as sql
#             dbase = sql.connect(ip,uname,password,dbname)
#             cursor = dbase.cursor()
#             a = str(tuple(columns.keys())).replace("'","")
#             #Or we can use
#             # a = "("
#             # for index,i in enumerate(tuple(columns.keys())):
#             #     if(index == len(tuple(columns.keys()))-1):
#             #         a+=i+")"
#             #     else:
#             #         a+=i+","
#             sql = f"insert into {tablename}{a} values {tuple(columns.values())}"
#             cursor.execute(sql)
#             dbase.commit()            
#         except Exception as e:
#             dbase.rollback()
#             raise e
#         else:
#             if(cursor.rowcount>0):
#                 return True
#             else:
#                 return False                
#         finally:
#             dbase.close()
    
   
# c1 = Course()
# if(c1.addCourse("Python",5000,"Kandivli")):
#     print("Inserted Successfully")
# else:
#     print("Something went wrong")

##########################################################################################
##########################################################################################

#Inheritance
# Multiple Inheritance.
#          => Parent 1
#  Child | 
#          => Parent 2
#
#Multilevel Inheritance
#
#  Child | => Parent 1 (if resourse not found) => Parent 2
#

# class Parent():
#     def printMe(self):
#         print("I am in parent")

# class Child(Parent):
#     def printMe(self):
#         print("I am in Child")

# c1 = Child()
# c1.printMe()

#### Multilevel Example####

# class MainParent():
#     def printMe2(self):
#         print("I am in main parent")

# class Parent(MainParent):
#     def printMe(self):
#         print("I am in parent")

# class Child(Parent):
#     def printMe(self):
#         print("I am in child")

# c1 = Child()
# c1.printMe2()

### Multiple Inheritance ###

# class MainParent():
#     def printMe2(self):
#         print("I am in main parent")

# class Parent():
#     def printMe(self):
#         print("I am in parent")

# class Child(Parent,MainParent):
#     def printMe(self):
#         print("I am in child")

# c1 = Child()
# c1.printMe2()



