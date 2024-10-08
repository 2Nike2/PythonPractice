import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType

from app.models.users import User as UserModel
from app.cruds.users import insert_user

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        interface = (relay.Node, )

class UserConnection(relay.Connection):
    class Meta:
        node = User

class InsertUser(relay.ClientIDMutation):
    class Input:
        name =graphene.String(required=True)

    user = graphene.Field(User)

    @classmethod
    def mutate_and_get_payload(cls, root, info, name):
        user = insert_user(name)
        return InsertUser(user)