from rest_framework.pagination import PageNumberPagination

class QuestionListPagination(PageNumberPagination):
    page_size=10
    page_size_query_param='record'