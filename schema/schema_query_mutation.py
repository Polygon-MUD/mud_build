import graphene

import my_app.schema.Query
import my_app.schema.Mutation

class Query(
    my_app.schema.Query, # Add your Query objects here
    graphene.ObjectType
):
    pass

class Mutation(
    my_app.schema.Mutation, # Add your Mutation objects here
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
