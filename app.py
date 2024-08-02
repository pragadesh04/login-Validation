from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///login.db"
db = SQLAlchemy(app)

class login(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    uname = db.Column(db.String(50), nullable = False)
    upass = db.Column(db.String(50), nullable = False)

def __repr__(self) -> str:
    return f"login('{self.uname}', '{self.upass}')"

@app.route("/", methods = ['GET', 'POST'])
def index():

    if request.method == 'POST':
        Uname = request.form.get('uname')
        password = request.form.get('password')
        user = login.query.filter_by(uname=Uname).first()
    print(Uname, password, user)
    
    if user:
        return "Login username exist"
    
    details = login(uname = Uname, upass = password)
    db.session.add(details)
    db.session.commit()

    return render_template("index.html")

@app.route("/hi")
def hi():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)