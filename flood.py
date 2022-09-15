import requests
from time import sleep as tt
import random 
# payload = {"email":"tunjibaba@gmai.com","pass":"tunjitunji123","token":"30bd215385b8b9ff220582bc478d3169"}
# r= requests.post("https://k1k2.webnode.es/#0.691577106283391",data=payload)

# print(r.json)
def give_mail():
    first = open("first_name.txt","r")
    last = open("last_name.txt","r")
    f_list = []
    l_list = []
    for f in first.readlines():
        f = f.replace("\n","")
        f_list.append(f)
    for l in last.readlines():
        l = l.replace("\n","")
        l_list.append(l)    
    fullname = random.choice(f_list)+random.choice(l_list)+"@gmail.com"
    return fullname

def give_pass():
    passq = open("password_list.txt","r")
    pass_list = []
    for p in passq.readlines():
        p = p.replace("\n","")
        pass_list.append(p)

    password = random.choice(pass_list)
    return password
n_Var = 0
while True:
    payload = {
        "user": "angeelrulay",
        "domain": "https://risasmeme1.webnode.es/risasmeme1/?p=1",
        "empleado": "undefined",
        "email": give_mail(),
        "pass": give_pass(),
        "login": "लॉग इन करो",

        
    
    }
    with requests.Session() as s:
        url = "https://risasmeme1.webnode.es/risasmeme1/"
        header = {
            "user-agent":"Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
        }
        r = s.post(url, data=payload,headers=header)
        tt(2)
        n_Var +=1
        print(r.ok)
        print(str(n_Var)+"\n")
        if n_Var>500:
            print("exitng... 500 posts done")
            break
        else:
            continue


  
