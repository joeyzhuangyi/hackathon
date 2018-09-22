from flask import Flask
from classes import user

app = Flask(__name__)
student1 = user("olsen matthew","female",3,["Repeating comp1511"],"lazykid")
student2 = user("olsen matthew","female",3,["Repeating comp1511"],"lazykid")

sample_user_tutor = user("jfk","male",4,["Date Science","AI","Java development","COMP 1521"],["You sucks","Nice experience"])

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()


