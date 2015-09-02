from app import db
from app import *


#create the database and db tables
#db.create_all()

# insert
db.session.add(User("test@example.com", "Password"))


# commit the changes
db.session.commit()