from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
from .models import Bookmark
from .serializers import BookmarkSerializer

# Головна сторінка
def home(request):
    return HttpResponse("Welcome to the Bookmark API!")

# ViewSet для закладок
class BookmarkViewSet(ModelViewSet):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(f"Fetching bookmarks for user: {self.request.user}")
        return Bookmark.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

