from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # Terror, Drama, etc.
    author = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Tempo em minutos
    classification = db.Column(db.String(10), nullable=False)  # Ex: Livre, 16+, etc.
    code = db.Column(db.String(20), unique=True, nullable=False)  # Código único do filme
    synopsis = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Movie {self.name} - {self.category}>"