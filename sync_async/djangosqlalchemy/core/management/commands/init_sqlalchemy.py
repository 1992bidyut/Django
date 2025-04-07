# core/management/commands/init_sqlalchemy.py
from django.core.management.base import BaseCommand
from core.sqlalchemy_models import init_db, Session, SQLAUser


class Command(BaseCommand):
    help = 'Initialize SQLAlchemy database and create sample data'

    def handle(self, *args, **options):
        self.stdout.write('Initializing SQLAlchemy database...')

        # Create tables
        init_db()

        # Add sample data
        session = Session()
        try:
            # Check if we already have users
            existing_users = session.query(SQLAUser).count()
            if existing_users == 0:
                self.stdout.write('Adding sample users...')
                # Add sample users
                users = [
                    SQLAUser(username='user1', email='user1@example.com'),
                    SQLAUser(username='user2', email='user2@example.com'),
                    SQLAUser(username='user3', email='user3@example.com')
                ]
                session.add_all(users)
                session.commit()
                self.stdout.write(self.style.SUCCESS('Sample users added successfully'))
            else:
                self.stdout.write('Sample users already exist')
        except Exception as e:
            session.rollback()
            self.stdout.write(self.style.ERROR(f'Error: {str(e)}'))
        finally:
            session.close()

        self.stdout.write(self.style.SUCCESS('Database initialization complete'))