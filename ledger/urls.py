from django.conf.urls import url

from ledger.views import NewExpense, ExpenseDetail, EditExpense, DeleteExpense, ExpenseList
from ledger.models import Expense

urlpatterns = [
    url(r'expenses', ExpenseList.as_view(), name='expenses'),
    url(r'add_item', NewExpense.as_view(), name='add_item'),
    url(r'(?P<pk>\d+)/$', DeleteExpense.as_view(), name='expense_delete'),
]

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'expenses', views.expenses, name='expenses'),
#     url(r'add_item', views.add_expense, name='add_item'),
#     url(r'^(?P<item_id>[0-9]+)/$', views.detail, name='detail'),
# ]
