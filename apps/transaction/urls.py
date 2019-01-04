from django.urls import path
from .views import TransactionChart

# from .views import MemberList

app_name = "transaction"

urlpatterns = [
    # path('', MemberList.as_view(), name='list'),
    path('chart', TransactionChart.as_view(), name='chart'),
]