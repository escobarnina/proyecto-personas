import graphene
from personas.schema import Query as PersonasQuery
from personas.schema import Mutation as PersonasMutation

class Query(PersonasQuery, graphene.ObjectType):
    pass

class Mutation(PersonasMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
