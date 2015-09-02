from app import db
from app import User

#create the database and db tables
db.create_all()

# insert
db.session.add(User("student1", "Password"))


# commit the changes
db.session.commit()