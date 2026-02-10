from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'author']
    

    @action(detail=False, methods=['get'])
    def available(self, request):
        books = Book.objects.filter(is_available=True)
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

