from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Book
from .serializers import BookSerializer
from core.permissions import IsAdminUserCustom


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all().order_by('-created_at')
    serializer_class = BookSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['author', 'genre', 'is_available']
    search_fields = ['title', 'author', 'isbn', 'genre']

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [AllowAny()]
        return [IsAdminUserCustom()]
