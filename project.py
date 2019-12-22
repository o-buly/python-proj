#encoding:UTF-8

import random
from os import path

#list
#string
#files
#exceptions
#random
#tuple

MyOrders = ["ofir-order.txt","etty-order.txt"] #list
name = raw_input("enter your user name: ")#string
password = raw_input("enter your password: ")
#MyOrders.append(name + "-order.txt")

def makeOrder(name):#files
    with open(name+"-order.txt", "w") as order:
      input=raw_input("\n-------------\n(TO FINISH THE ORDER ENTER A BLANK LINE)\nenter your order:\n")
      while input!="":
        order.write(input+"\n")
        input=raw_input()
    MyOrders.append(name + "-order.txt")


def readOrder(name):
    try:#exceptions
        with open(name+"-order.txt", "r") as exist:
          print "\nthis is " + name + " order :"
          info = exist.read()
          print info
          exist.close()
    except Exception, description:
        print description

def benefit():
        if(path.exists(name+"-order.txt")):
            benefitVALUES = ("50% הנחה", "90% הנחה", "10% הנחה", "5% הנחה", "ההזמנה עלינו !!!", "75% הנחה", "20% הנחה") #tuple
            number = random.randint(0, len(benefitVALUES)-1)#random
            print "your lucky number is: ", number
            print "your benefit is: ", benefitVALUES[number]
            with open(name + "-order.txt", "a") as orderAppend:
                orderAppend.write("***************\nההטבה שלי :\n" + benefitVALUES[number] + "\n***************")
        else:
         print "Sorry The File Doesn't Exist!!!!"


def readMyOrders():
    for i in range(len(MyOrders)):
        #MyOrders[i].split("-")
        with open(MyOrders[i], 'r') as f:
            print "\nthis is " + MyOrders[i] + " order :"
            info = f.read()
            print info
            f.close()



makeOrder(name)
benefit()
readOrder(name)
readMyOrders()

