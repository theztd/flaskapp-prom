import json
from os import path, getenv, uname
from requests import get

try:
    import graphene
    #from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

except ImportError as err:
    print("Install dependencies!!!")
    print(err)
    exit(22)

ENV = getenv("ENV", "devel")
VERSION = "unknown"
INSTANCE = uname()[1]

try:
    with open("./VERSION") as ver:
        VERSION = ver.read().strip()

except IOError as err:
    print("Unable to find VERSION file, but continue...")


DATA = get("http://localhost:5001/api/user/list.json").json()
print(DATA)


class Person(graphene.ObjectType):
    name = graphene.String(value = graphene.String(default_value="Kumarovic kumar"))
    key_length = graphene.Int()
    key = graphene.String()


# register all queries
class Query(graphene.ObjectType):
    users = graphene.List(Person, size=graphene.Int(default_value=1))
    version = graphene.String()
    instance = graphene.String()
    env = graphene.String()

    def resolve_users(root, info, size):
        return DATA[:size]

    def resolve_version(root, info):
        return VERSION

    def resolve_instance(root, info):
        return INSTANCE

    def resolve_env(root, info):
        return ENV

SCHEMA = graphene.Schema(query=Query)


# ---------   TEST   ------
if __name__ == "__main__":
    from pprint import pprint

    print(SCHEMA)
    cq1 = '''
query myquery {
    name: name (value: "karlik")
    age
}
'''

    cq2 = '''
query myquery {
    array (size:5){
        name
        age
    }
}
'''

    r = schema.execute(cq2)
    pprint(r.data)
