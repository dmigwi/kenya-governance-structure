# Deletes the migrations folder if it exists
rm -rf migrations/

# Delete the database.db file
rm database.db

# Creates a migration folder
python manage.py db init

# Generate a migration script
python manage.py db migrate

# Applies the genarated migrations
python manage.py db upgrade