from flask import Flask,render_template,request,url_for
from classes import user
app = Flask(__name__)
"""""""""

student1 = user("olsen matthew","female",3,["Repeating comp1511"],"lazykid")
student2 = user("olsen matthew","female",3,["Repeating comp1511"],"lazykid")

sample_user_tutor = user("jfk","male",4,["Date Science","AI","Java development","COMP 1521"],["You sucks","Nice experience"])
"""
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        return render_template("home.html", looking=True);
    return render_template("home.html",looking= False);
@app.route('/hello')
def hello():
    return "hello world"
@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run( debug=True)