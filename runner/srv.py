from flask import Flask, request
import json, traceback
test = Flask("test")

@test.route("/add",  methods=['GET', 'POST'])
def bruh():
    if request.method == "POST":
        print(request)

        print(dir(request.data))
        print(request.data.decode())
        correct = request.data.decode().replace("'", '"')
        print(correct)
        try:

            print(json.loads(correct))
            f = open("session.json", "w")
            session = json.dump(json.loads(correct), fp=f)
            f.close()
            print(session)
        except:
            traceback.print_exc()
        print(type(request.data.decode()))

        #print(json.loads(request.data.decode()))
    return {"status": "OK"}

@test.route("/get_status")
def return_status():
    f = open("session.json", "r")
    return json.load(f)
    f.close()

@test.route("/render_banner")
def render_banner():
    return {"status": "error", "description":"this function is not ready!"}

@test.route("/return_important")
def get_most_important():
    f = open("session.json", "r")
    files = json.load(f)
    f.close()
    important = ["code", "discord", "paint"] #change with your priority list of apps in main.py
    
    for a in important:
        try:
            if files[a]:
                return a 
            
        except:
            pass

test.run(host="0.0.0.0", port=5555)