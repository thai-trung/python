# implement csv in python

import csv

file = open("phonebook.csv", "a")
name = input("Enter your name: ")
phoneNo = input("Enter your phone number: ")

writer = csv.writer(file)
writer.writerow((name, phoneNo))
file.close()