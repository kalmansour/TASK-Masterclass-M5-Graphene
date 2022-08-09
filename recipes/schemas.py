import graphene

import food.schemas

class Query(food.schemas.FoodQuery, graphene.ObjectType):
    greet = graphene.String(name=graphene.String(default_value="world"))
    
    def resolve_greet(self, info, name):
      return f"Hello {name}!"

class Mutation(food.schemas.FoodMutation,graphene.ObjectType):
  pass

SCHEMA = graphene.Schema(query=Query, mutation=Mutation)