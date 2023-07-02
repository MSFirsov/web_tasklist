from webapp.db import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    table_id = db.Column(db.Integer, index=True)

    def __repr__(self):
        return f'<Task_id {self.id}, table_id {self.table_id}>'
