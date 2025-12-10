from django.urls import path
from .views import BorrowBookView, ReturnBookView, LoanListView

urlpatterns = [
    path('loans/borrow/', BorrowBookView.as_view(), name='borrow-book'),
    path('loans/return/', ReturnBookView.as_view(), name='return-book'),
    path('loans/list/', LoanListView.as_view(), name='loan-list'),
]
