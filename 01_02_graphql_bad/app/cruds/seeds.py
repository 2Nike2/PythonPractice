import sys
import pathlib
from datetime import datetime

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append(str(current_dir)+ "/../../")

from app.database import BASE, ENGINE, session_scope
from app.models.users import User
from app.models.todos import Todo

def generate_seed_data():
    BASE.metadata.create_all(ENGINE)
    users = [['Alice'], ['Bob'], ['Charlie']]
    todos = [
        [1, 'Complete project report', 'Finish the final report for the project', datetime(2025, 8, 1)],
        [1, 'Schedule team meeting', 'Arrange a meeting with the project team', datetime(2025, 8, 2)],
        [2, 'Prepare presentation slides', 'Create slides for the upcoming presentation', datetime(2025, 8, 3)],
        [2, 'Review budget plan', 'Examine the budget plan for the next quarter', datetime(2025, 8, 4)],
        [3, 'Update client database', 'Add recent client information to the database', datetime(2025, 8, 5)],
        [3, 'Organize workspace', 'Clean and organize the desk and office area', datetime(2025, 8, 6)]
    ]

    with session_scope() as session:
        for user in users:
            session.add(User(name=user[0]))
        for todo in todos:
            session.add(Todo(
                user_id=todo[0],
                title=todo[1],
                description=todo[2],
                deadline=todo[3]
            ))

if __name__ == '__main__':
    generate_seed_data()