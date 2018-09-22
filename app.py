from flask import Flask,render_template,request
from classes import user
app = Flask(__name__)
"""""""""

student1 = user("olsen matthew","female",3,["Repeating comp1511"],"lazykid")
student2 = user("olsen matthew","female",3,["Repeating comp1511"],"lazykid")

sample_user_tutor = user("jfk","male",4,["Date Science","AI","Java development","COMP 1521"],["You sucks","Nice experience"])
"""
@app.route('/')
def home():
    if request.method == "POST":
        pass
    return render_template("home.html",looking= False);


