from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source='user.email')
    book_title = serializers.ReadOnlyField(source='book.title')

    class Meta:
        model = Loan
        fields = [
            'id',
            'user',
            'user_email',
            'book',
            'book_title',
            'borrowed_at',
            'returned_at',
        ]
        read_only_fields = ['user', 'borrowed_at', 'returned_at']
