from app import db

class User(db.Model):

	id =db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	email = db.Column(db.String(255))
	date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

	def __init__(self, name, email):
		self.name = name
		self.email = email

	def save(self):
		db.session.add(self)
		db.session.commit()

	@staticmethod
	def get_all():
		return User.query.all()

	def delete(self):
		db.session.delete(self)
		db.session.commit()

	def __repr__(self):
		return '<User: {} {}>'.format(self.name, self.email)
