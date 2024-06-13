from flask import Flask, render_template, request, redirect, url_for
from models import db, Message

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'  # 데이터베이스 URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/friends', methods=["GET", "POST"])
def friends():
    return render_template("friends.html")

@app.route('/chats', methods=["GET", "POST"])
def chats():
    return render_template("chats.html")

@app.route('/chat', methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        content = request.form.get('content')
        new_message = Message(content=content)
        db.session.add(new_message)
        db.session.commit()
        return redirect(url_for('chat'))

    messages = Message.query.all()
    return render_template("chat.html", messages=messages)

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route('/friends',  methods=["GET","POST"])
# def friends():
#     return render_template("friends.html")

# @app.route('/chats',  methods=["GET","POST"])
# def chats():
#     return render_template("chats.html")

# @app.route('/chat',  methods=["GET","POST"])
# def chat():
#     return render_template("chat.html")

# if __name__ == '__main__':
#     app.run(app, debug=True)