import requests
import json
import os.path
if os.path.exists("courses.json"):
    print("file exists")
    d = open("courses.json","r")
    file = d.read()
    data = json.loads(file)
else:
    print("file not exits")
    a= requests.get("https://api.merakilearn.org/courses")
    url= a.json()
    with open("courses.json","w") as file :
        json.dump(url , file , indent=4)
    q = open("courses.json","r")
    read = q.read()
    data = json.loads(read)
i=0
while i<len(data):
    print(str(i+1)+".",data[i]["name"],data[i]["id"])
    i=i+1
print("")
user_input=int(input("enter the course name:"))
print(data[user_input-1]["name"])
print(user_input)
b=requests.get("https://api.merakilearn.org/courses/"+data[user_input-1]['id']+"/exercises")
d = b.json()
a = data[user_input-1]['name']+"_"+".json"
with open(a,"w") as f:
    json.dump(d,f,indent=4)
s=open(a,"r")
read=s.read()
data=json.loads(read)
i=0
while i<len(data["course"]["exercises"]):
    print(str(i+1),data["course"]["exercises"][i]["name"])
    i=i+1
j=int(input("choose the topic name :"))
print(data["course"]["exercises"][j-1]["name"])
i=1
while i<len(data["course"]["exercises"][j-1]["content"]):
    print(str(i+1),data["course"]["exercises"][j-1]["content"][i]["value"])
    i=i+1
    k =input("previous or next..:")
    if k!="n" and k=="p":
        if k=="previous"and j>1:
            print(data["course"]["exercises"][j-2]["name"])
            i=0
            while i<len(data["course"]["exercises"][j-2]["content"]):
                print(data["course"]["exercises"][j-2]["content"][i]["value"])
                i=i+1
            j=j-1
        else :
            i = 0
            while i < len(data["course"]["exercises"]):
                print(str(i+1),data["course"]["exercises"][i]["name"])
                i+=1    
    elif k != "p" and k == "n":
        if k == "n" and j < len(data["course"]["exercises"]):
                print(data["course"]["exercises"][j]["name"])
                i = 0 
                while i < len(data["course"]["exercises"][j]["content"]):
                    print(data["course"]["exercises"][j]["content"][i]["value"])
                    i+=1
                j=j=1
        if j == len(data["course"]["exercises"]):
            print("topic is completed:")
    else:
        print("wrong user_input ")