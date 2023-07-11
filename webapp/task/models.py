from webapp.db import db
from sqlalchemy.orm import relationship


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    task_date = db.Column(db.Date, nullable=False)
    user = relationship('User', backref='tasks')

    def __repr__(self):
        return f'<Task_id {self.id}, table_id {self.num_week_day}>'
