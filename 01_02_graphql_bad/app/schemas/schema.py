import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from app.cruds.users import fetch_user
from app.cruds.todos import fetch_todo
from app.schemas.users import User, UserConnection, InsertUser
from app.schemas.todos import Todo, TodoConnection, InsertTodo

class Query(graphene.ObjectType):
    node = relay.Node.Field()

    user = graphene.Field(
        lambda x: graphene.List(User),
        id = graphene.Int(required=False),
        name = graphene.String(required=False)
    )

    todo = graphene.Field(
        lambda x: graphene.List(Todo),
        id = graphene.Int(required=False),
        user_id = graphene.Int(required=False),
        title = graphene.String(required=False),
        description = graphene.String(required=False),
        deadline = graphene.DateTime(required=False)
    )

    all_users = SQLAlchemyConnectionField(UserConnection)
    all_todos = SQLAlchemyConnectionField(TodoConnection, sort=None)

    def resolve_user(self, info, id=None, name=None):
        return fetch_user(id, name)
    
    def resolve_todo(self, info, id=None, user_id=None, title=None, description=None, deadline=None):
        return fetch_todo(id, user_id, title, description, deadline)
    
class Mutation(graphene.ObjectType):
    insert_user = InsertUser.Field()
    insert_todo = InsertTodo.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)