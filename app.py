from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
#from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
#migrate = Migrate(app,db)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        ndhm_url = request.form['baseURL']
        ndhm_clientID= request.form['client_ID']
        ndhm_secret= request.form['secret']
        url = ndhm_url
        payload = {
            "clientId": "",  
            "clientSecret": ""
            }
        payload["clientId"]= ndhm_clientID
        payload["clientSecret"]= ndhm_secret
        res = requests.post(url, json=payload)
        print(payload)
        print(res)
        output = res.text.encode('utf8')
        print(output)
        
        #new_task = Todo(content=task_content)

        try:
            #db.session.add(new_task)
            #db.session.commit()
            return render_template('index.html', response = output)

        except:
            return 'issue adding the task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html')


""" @app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        task_content = request.form['content']
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')

        except:
            return 'issue adding the task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "issue deleting task"

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "issue updating task"
    else:
        return render_template('update.html', task=task) """

    

if __name__ == "__main__":
    app.run(debug=True)
