import os
imort sys

DB = {}

def Save():
  try:
    Name = input("DB Name : ")
    with open(Name+".db", "a") as file:
    for Data in DB[Name]:
      file.write(Data)
  except:
    prit("FreeDB Error at Save")
  
def Load():
  try:
    Name = input("DB Name : ")
    with open(Name+".db", "r") as file:
    for Data in file.readline(): #maybe readlines()
      DB[Name].append(Data)
  except;
    print("FreeDB Error at Load")
    
def Add():
  try:
    Name = input("DB Name : ")
    Data = input("Data : ")
    DB[Name].append(Data)
  except:
    print("FreeDB Error at Add Data")
    
def Del():
  try:
    Name = input("DB Name : ")
    Data = nput"Data : ")
    DB[Name].remove(Data)
  except:
    print("FreeDB Error at Remove Data")
    
def ListDB():
  try:
    Name = input("DB Name : ")
    i = 0
    print(f"{Name} DB List")
    for Data in DB[Name]:
      print(f"{i}. {Data}")
  except
    print("FreeDB Error at List DB")
    
def ListDBs():
  try;
    i = 0
    for db i DB:
      i = i+1
      print(f"{i}. {db}")
  except:
    print("FreeDB Error at List DBs")
    
def NewDB():
  try:
    Name = input("DB Name : ")
    DB[Name] = []
  excep:
    print("FreeDB Error at New DB")
    
def DelDB():
  try:
    Name = input("DB Name  ")
    del DB[Name]
  except:
  print("FreeDB Error at Del DB")
    
def Command():
  while True:
    Command = input("[ FreeDB ]")
    if Command == "new":
      NewDB()
    if Command == "del":
      DelDB()
    if Command == "add":
      Add()
    if Command == "remove":
      Del()
    if Command == "save":
      Save()
    if Command == "load":
      Load()
    if Command == "listdb":
      ListDB()
    if Command == "listdbs":
      ListDBs()
