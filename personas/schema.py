import graphene
from graphene_django import DjangoObjectType
from .models import Persona

class PersonaType(DjangoObjectType):
    class Meta:
        model = Persona
        fields = ("id", "nombre", "apellido", "edad", "email", "telefono", "ciudad", "fecha_registro")


class Query(graphene.ObjectType):
    personas = graphene.List(PersonaType)
    persona_por_id = graphene.Field(PersonaType, id=graphene.Int(required=True))

    def resolve_personas(root, info):
        return Persona.objects.all()

    def resolve_persona_por_id(root, info, id):
        return Persona.objects.get(pk=id)


class CrearPersona(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        apellido = graphene.String(required=True)
        edad = graphene.Int(required=True)
        email = graphene.String(required=True)
        telefono = graphene.String(required=True)
        ciudad = graphene.String(required=True)

    persona = graphene.Field(PersonaType)

    @classmethod
    def mutate(cls, root, info, nombre, apellido, edad, email, telefono, ciudad):
        persona = Persona.objects.create(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            email=email,
            telefono=telefono,
            ciudad=ciudad
        )
        return CrearPersona(persona=persona)


class ActualizarPersona(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        nombre = graphene.String()
        apellido = graphene.String()
        edad = graphene.Int()
        email = graphene.String()
        telefono = graphene.String()
        ciudad = graphene.String()

    persona = graphene.Field(PersonaType)

    @classmethod
    def mutate(cls, root, info, id, **kwargs):
        persona = Persona.objects.get(pk=id)

        for key, value in kwargs.items():
            setattr(persona, key, value)

        persona.save()
        return ActualizarPersona(persona=persona)


class EliminarPersona(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        persona = Persona.objects.get(pk=id)
        persona.delete()
        return EliminarPersona(ok=True)


class Mutation(graphene.ObjectType):
    crear_persona = CrearPersona.Field()
    actualizar_persona = ActualizarPersona.Field()
    eliminar_persona = EliminarPersona.Field()