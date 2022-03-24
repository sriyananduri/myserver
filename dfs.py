import os
from github import Github
import re

sn = "STOKEN"
token = os.environ[sn]

g = Github(token)

sn_r = "shriyananduri/myserver"

repo = g.get_repo(sn_r)
cm = "Automated_update"
m = "main"

def write(path: str, content: bytes):
    global repo, cm, m
    try:
        repo.create_file(path, cm, content, branch=m)
    except:
        delete(path)
        repo.create_file(path, cm, content, branch=m)

def read(path: str):
    global repo, cm, m
    try:
        contents = repo.get_contents(path, ref=m)
        return contents.decoded_content
    except:
        print(f"{path = } does not exist")

def delete(path: str):
    global repo, cm, m
    try:
        contents = repo.get_contents(path, ref=m)
        repo.delete_file(contents.path, cm, contents.sha, branch=m)
    except:
        print(f"{path = } does not exist")

def copy(newpath, oldpath):
    try:
      write(newpath, read(oldpath))
    except:
      print("")

def ls(path: str = ""):
    global repo
    return repo.get_contents(path)

def count(path: str=""):
    return len(repo.get_contents(path))

while True:
  string = input("shriyananduri/myserver: ")
  str_list = re.sub(" ", " ",  string).split()
  length=len(str_list)

  if length>3:
    print("Incorrect Command2")

  elif length==2:
    if (str_list[0]=='delete'):
      if (str_list[1].endswith('.txt')):
        delete(str_list[1])
      else:
        print("Wrong filetype entered")

    elif(str_list[0]=='read'):
      if(str_list[1].endswith('.txt')):
        print(read(str_list[1]))
      else:
        print("Wrong filetype")

    else:
      print("Incorrect Command1")

  elif length==3:
    if(str_list[0]=='copy'):
      if(str_list[1].endswith('.txt')):
        if(str_list[2].endswith('.txt')):
          copy(str_list[1],str_list[2])
        else:
          print("Incorrect filetype")
      else:
        print("Incorrect filetype")

    elif (str_list[0]=='write'):
      if(str_list[1].endswith('.txt')):
        write(str_list[1],str_list[2])

    else:
      print("Incorrect command")

  elif length==1:
    if(str_list[0]=='ls'):
      print(ls())

    elif(str_list[0]=='count'):
      print(count())

    elif(str_list[0]=='exit'):
      break

    else:
      print("Incorrect command")


        
        

    




 






























































































 
