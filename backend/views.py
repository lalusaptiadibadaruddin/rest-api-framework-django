from .models import Article
from .serializers import ArticleSerializer
from rest_framework import viewsets
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# import permission
from .permissions import IsAuthor


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'

    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]
    # tambahkan permission IsAuthor
    permission_classes = [IsAuthenticated, IsAuthor]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
