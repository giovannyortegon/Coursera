from datetime import datetime
from app import db
# from python terminal
# 
# task no exists 
# from models import db
# db.create_all()
# from models import Task
# from datetime import datetime
# t = Task(title='adfsdf', date=datetime.utcnow())
# t
# db.session.add(t)
# db.session.commit()
# Task.query.all()
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.title} created'