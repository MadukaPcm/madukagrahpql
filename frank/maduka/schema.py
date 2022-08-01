import graphene
from graphene_django import DjangoObjectType
from . models import Frank,Maduka

class FrankType(DjangoObjectType):
    class Meta:
        model = Frank
        # fields = ('id','name')

class MadukaType(DjangoObjectType):
    class Meta:
        model = Maduka

#the data in the above class are translated into graph like
# type Frank{
#     id: id
#     name: String
# }

#a mutation class for creating new instance of frank
class CreateFrank(graphene.Mutation):
    frank = graphene.Field(FrankType)

    class Arguments:
        name = graphene.String()

    def mutate(self, info, name):
        datac = Frank(name=name)
        datac.save()
        return CreateFrank(frank=datac)

#a slass instance for creating new instance of maduka.
class CreateMaduka(graphene.Mutation):
    maduka = graphene.Field(MadukaType)

    class Arguments:
        name = graphene.String()
        notes = graphene.String()
        frank_id = graphene.Int()

    def mutate(self, info, name,notes,frank_id):
        datac = Maduka(name=name,notes=notes)
        data = Frank.objects.get(id=frank_id)
        datac.frank = data
        datac.save()

        return CreateMaduka(maduka=datac)

#main mutation class.... for object instance creations.
class Mutation(graphene.ObjectType):
    create_maduka = CreateMaduka.Field()
    create_frank = CreateFrank.Field()


#a class for data querying from our related models...
class Query(graphene.ObjectType):

    all_frank = graphene.List(FrankType)
    all_maduka = graphene.List(MadukaType)

    def resolve_all_frank(root, info):
        return Frank.objects.all()

    def resolve_all_maduka(root, info):
        return Maduka.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
