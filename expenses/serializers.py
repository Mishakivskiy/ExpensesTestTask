from django.db.models import Sum
from rest_framework.serializers import ModelSerializer, Serializer, CharField, DecimalField

from expenses.models import User, Expense


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class ExpenseByDateRangeSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class CategorySummarySerializer(Serializer):
    category = CharField()
    total_amount = DecimalField(max_digits=10, decimal_places=2)

    @staticmethod
    def get_summary(user, year, month):
        expenses = (
            Expense.objects.filter(user=user, date__year=year, date__month=month)
            .values("category")
            .annotate(total_amount=Sum("amount"))
            .order_by("category")
        )
        return expenses
