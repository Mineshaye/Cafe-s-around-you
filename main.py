from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy




app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db=SQLAlchemy()
db.init_app(app)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/random")
def get_random_cafe():
    result=db.session.execute(db.select(cafe))
    



if __name__=="__main__":
    app.run(debug=True)