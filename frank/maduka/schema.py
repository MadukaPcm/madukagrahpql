import graphene
from graphene_django import DjangoObjectType
from . models import Frank,Maduka

class FrankType(DjangoObjectType):
    class Meta:
        model = Frank
        fields = ('id','name')

class MadukaType(DjangoObjectType):
    class Meta:
        model = Maduka

#the data in the above class are translated into graph like
# type Frank{
#     id: id
#     name: String
# }

class Query(graphene.ObjectType):

    all_frank = graphene.List(FrankType)
    all_maduka = graphene.List(MadukaType)

    def resolve_all_frank(root, info):
        return Frank.objects.all()

    def resolve_all_maduka(root, info):
        return Maduka.objects.all()

schema = graphene.Schema(query=Query)
