from pprint import pprint
from flask import Flask, request, render_template, redirect, url_for, json
import sys, getopt
import json

app = Flask(__name__)

global base_grant_url
base_grant_url = ""
global user_continue_url
user_continue_url = ""
global success_url
success_url = ""
global count
count = 0

@app.route("/click", methods=["GET"])
def get_click():
    global base_grant_url
    global user_continue_url
    global success_url

    host = request.host_url
    base_grant_url = request.args.get('base_grant_url')
    user_continue_url = request.args.get('user_continue_url')
    node_mac = request.args.get('node_mac')
    client_ip = request.args.get('client_ip')
    client_mac = request.args.get('client_mac ')
    splashclick_time = request.args.get('splashclick_time')
    success_url = host + "success"

    if count < 1:
        return render_template("click.html", client_ip=client_ip,
        client_mac=client_mac, node_mac=node_mac,
        user_continue_url=user_continue_url,success_url=success_url)
    else:
        return render_template("social.html", client_ip=client_ip,
        client_mac=client_mac, node_mac=node_mac,
        user_continue_url=user_continue_url,success_url=success_url)


@app.route("/login", methods=["POST"])
def get_login():
    global base_grant_url
    global success_url
    global count

    if count < 1:
        user_email = request.form["user_email_address"]
        user_phone = request.form["user_phone_number"]
        #user_count = 1
        print("User email: " + user_email)
        print("User phone: " + user_phone)
        filestring = user_email + "," + user_phone #+ "," + str(user_count)
        if user_email and user_phone:
            with open('userInfo.txt') as myfile:
                if filestring in myfile.read():
                    print('User already found in database.')
                else:
                    print(filestring)
                    with open("userInfo.txt", "a+") as myfile:
                        myfile.write("----------------------------------------" + "\n")
                        myfile.write(filestring + "\n")
                    #user_count = user_count + 1
                        
            return redirect("http://localhost:5004/success", code=302)
    
    return render_template("click.html", user_continue_url=user_continue_url,success_url=success_url)
    
    
    

    #if count < 1:
    #    count = 1
    #    return redirect("http://localhost:5004/success", code=302)
    #else:
    #    return render_template("social.html", user_email=user_email, user_phone=user_phone)

    #return redirect(base_grant_url+"?continue_url="+success_url, code=302)
    #return redirect("http://localhost:5004/success", code=302)


@app.route("/loginsocial", methods=["POST"])
def get_loginsocial():
    global base_grant_url
    global success_url
    global count

    #user_email = request.form["user_email_address"]
    #user_phone = request.form["user_phone_number"]
    with open("userInfo.txt", "a") as myfile:
        myfile.write("The above user logged in through Facebook" + "\n")
    print("successful fb login")
    

    return redirect("http://localhost:5004/success", code=302)

@app.route("/success",methods=["GET"])
def get_success():
    global user_continue_url
    global count
    
    count = 1
    return render_template("success.html",user_continue_url=user_continue_url)
    #if count < 1:
    #    count = 1
    #    print('yo1')
    #    return render_template("success.html",user_continue_url=user_continue_url)
    #else:
    #    print('yo2')
    #    return render_template("social.html", user_continue_url=user_continue_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=False)
