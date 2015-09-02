from app import db
from models import User

#create the database and db tables
db.create_all()

# insert
db.session.add(User("test@example.com", "Password"))


# commit the changes
db.session.commit()