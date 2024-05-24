from app import db, create_app
from app.models import Role

app = create_app()

with app.app_context():
    # Create the database tables if they don't exist
    db.create_all()

    # Add roles to the database
    if not Role.query.filter_by(name='admin').first():
        db.session.add(Role(name='admin'))
    if not Role.query.filter_by(name='user').first():
        db.session.add(Role(name='user'))

    # Commit the changes
    db.session.commit()

    print("Roles added to the database.")
