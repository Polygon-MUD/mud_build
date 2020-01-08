# my_app/schema.py

import graphene

from graphene_django.types import DjangoObjectType
from .models import Question


class QuestionType(DjangoObjectType):
    class Meta:
        model = Question


class Query:
    questions = graphene.List(QuestionType)
    question = graphene.Field(QuestionType, question_id=graphene.String())

    def resolve_questions(self, info, **kwargs):
        # Querying a list
        return Question.objects.all()

    def resolve_question(self, info, question_id):
        # Querying a single question
        return Question.objects.get(pk=question_id)
