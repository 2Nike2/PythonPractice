import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.models.todos import Todo as TodoModel
from app.cruds.todos import insert_todo

class Todo(SQLAlchemyObjectType):
    class Meta:
        model = TodoModel
        interface = (relay.Node, )

class TodoConnection(relay.Connection):
    class Meta:
        node = Todo

class InsertTodo(relay.ClientIDMutation):
    class Input:
        user_id = graphene.Int(required=True)
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        deadline = graphene.DateTime(required=True)

    todo = graphene.Field(Todo)

    @classmethod
    def mutate_and_get_payload(cls, root, info, user_id, title, description, deadline):
        todo = insert_todo(user_id, title, description, deadline)
        return InsertTodo(todo)