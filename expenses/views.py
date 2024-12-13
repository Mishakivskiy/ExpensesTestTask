from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from expenses.models import Expense, User
from expenses.serializers import (ExpenseByDateRangeSerializer,
                                  CategorySummarySerializer,
                                  UserSerializer,
                                  ExpenseSerializer)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpensesByDateRangeView(ListAPIView):
    serializer_class = ExpenseByDateRangeSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        return Expense.objects.filter(user_id=user_id)


class CategorySummaryView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user_id')
        month = request.query_params.get('month')
        year = request.query_params.get('year')

        if not (user_id and month and year):
            return Response({"error": "user_id, month, and year are required."}, status=400)

        summary = CategorySummarySerializer.get_summary(user_id, year, month)
        serializer = CategorySummarySerializer(summary, many=True)
        return Response(serializer.data)
