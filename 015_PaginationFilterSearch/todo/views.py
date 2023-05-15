from rest_framework.viewsets import ModelViewSet

from .serializers import Todo, TodoSerializer

# from rest_framework.pagination import PageNumberPagination

# PageNumberPagination.page_size = 25
# PageNumberPagination.page_query_param = 'Seite'

from .paginations import (
    CustomPageNumberPagination,
    CustomLimitOffsetPagination,
  CursorPagination
    )

class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = CustomLimitOffsetPagination
    filterset_fields = ['is_done', 'id','priority']
    


    # manuel filtering
    # def get_queryset(self):
    #     title = self.request.query_params.get('title')
    #     if title is None:
    #       return super().get_queryset()
    #     else:    
        
    #       return self.queryset.filter(title__contains='weg')
    