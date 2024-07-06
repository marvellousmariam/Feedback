from flask import Flask,render_template,request 
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
app=Flask(__name__)
ENV='dev'

if ENV=='dev':
    app.debug=True
    app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:adewunmi2020@localhost/tesla'
else:
    app.debug=False
    app.config['SQLALCHEMY_DATABASE_URI']=''
    

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False   
db=SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__='feedback'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(120),unique=True)
    dealer=db.Column(db.String(120))
    rating =db.Column(db.String(120))
    comment=db.Column(db.Text())
    
    def __init__(self,name,dealer,rating,comment) :
        self.name=name
        self.dealer=dealer
        self.rating=rating
        self.comment=comment
# with app.app_context():
#     db.create_all()
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/submit",methods=['POST'])
def submit():
    if request.method=='POST':
        name= request.form["name"]
        dealer= request.form["dealer"]
        rating= request.form["rating"]
        comment= request.form["comment"]
        # print(name,dealer,rating,comment)
        if name=='' and dealer=='':
            return render_template("index.html",message="Please fill required field")
            
        if db.session.query(Feedback).filter(Feedback.name==name).count()==0:
            data=Feedback(name=name,dealer=dealer,rating=rating,comment=comment)
            db.session.add(data)
            db.session.commit()
            send_mail(name,dealer,rating,comment)
            return render_template('success.html')
        return render_template("index.html",message="Already existing user")
if __name__=='__main__':
    app.debug=True
    app.run()