from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Configuration
from datetime import datetime


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

class Booking(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.Integer)
    street = db.Column(db.String(100))
    number = db.Column(db.Integer)
    city = db.Column(db.String(100))
    postcode = db.Column(db.Integer)
    country = db.Column(db.String(100))
    arrival_date = db.Column(db.DateTime )
    departure_date = db.Column(db.DateTime )
    hotel = db.Column(db.String(100))
    persons = db.Column(db.Integer)
    room = db.Column(db.String(100))
    comment = db.Column(db.String(200))

    def __init__(self,*args,**kwargs):
        super(Booking,self).__init__(*args,**kwargs) #call parent constructor as super is a keyword for parent constructor
    def __repr__(self):
        return '<Booking: %s>'% self.title


@app.route('/', methods = ["GET", "POST"])
def main():
    if request.method == "POST":
        hotel, room = "Hilton" if request.form["hotel"]==0 else "Westin" , "Deluxe" if request.form["room"] == 0 else "Super Deluxe"
        new_entry = Booking(name = request.form["name"],
                            email = request.form["email"],
                            phone = request.form["phone"],
                            street = request.form["street"],
                            number = request.form["street-number"],
                            city = request.form["city"],
                            postcode = request.form["post-code"],
                            country = request.form["country"],
                            arrival_date = datetime.strptime(request.form["arrive"], "%Y-%m-%d"),
                            departure_date = datetime.strptime(request.form["depart"], "%Y-%m-%d"),
                            hotel = hotel,
                            persons =  str(int(request.form["person"])+1),
                            room = room,
                            comment = request.form["comments"])
        db.session.add(new_entry)
        db.session.commit()
        return "Success"
    return render_template('index.html')

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
