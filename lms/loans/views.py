from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from .models import Loan
from .serializers import LoanSerializer
from books.models import Book


class BorrowBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        book_id = request.data.get('book_id')

        if not book_id:
            return Response({"error": "book_id is required"}, status=400)

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)

        if not book.is_available:
            return Response({"error": "Book is already borrowed"}, status=400)

      
        active_loan_exists = Loan.objects.filter(
            user=request.user,
            returned_at__isnull=True
        ).exists()

        if active_loan_exists:
            return Response(
                {"error": "You already have an active borrowed book"},
                status=400
            )

        Loan.objects.create(
            user=request.user,
            book=book
        )

        book.is_available = False
        book.save()

        return Response({"message": "Book borrowed successfully"}, status=201)


class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        book_id = request.data.get('book_id')

        if not book_id:
            return Response({"error": "book_id is required"}, status=400)

        try:
            loan = Loan.objects.get(
                user=request.user,
                book_id=book_id,
                returned_at__isnull=True
            )
        except Loan.DoesNotExist:
            return Response(
                {"error": "No active loan found for this book"},
                status=400
            )

        loan.returned_at = timezone.now()
        loan.save()

        loan.book.is_available = True
        loan.book.save()

        return Response({"message": "Book returned successfully"})


class LoanListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_admin:
            loans = Loan.objects.all().order_by('-borrowed_at')
        else:
            loans = Loan.objects.filter(user=request.user).order_by('-borrowed_at')

        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data)
