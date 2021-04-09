try:
    import graphene
    import json
    import os
    from pprint import pprint
except ImportError as err:
    print(err)


DATA = [
    {
        "name": "Karel",
        "age": 21
    },
    {
        "name": "Pavel",
        "age": 27
    }
]

class Person(graphene.ObjectType):
    name = graphene.String(value = graphene.String(default_value="Kumarovic kumar"))
    age = graphene.Int()

    # def resolve_name(root, info, value):
    #     return value

    # def resolve_age(root, info):
    #     return 22

class Query(graphene.ObjectType):
    array = graphene.List(Person, size=graphene.Int(default_value=1))

    def resolve_array(root, info, size):
        return DATA[:size]


SCHEMA = graphene.Schema(query=Query)


# ---------   TEST   ------
if __name__ == "__main__":
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