from rest_framework.viewsets import ModelViewSet
from notes.models import Note
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import *


class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
