from django.urls import path, include
from rest_framework.routers import DefaultRouter
from expenses.views import ExpenseViewSet, UserViewSet, ExpensesByDateRangeView, CategorySummaryView


router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet, basename='expense')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('expenses/date-range/', ExpensesByDateRangeView.as_view(), name='expenses_by_date_range'),
    path('expenses/category-summary/', CategorySummaryView.as_view(), name='category_summary'),
]
