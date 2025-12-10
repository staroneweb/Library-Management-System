from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = router.urls



"""

"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzY1MzY5ODg4LCJpYXQiOjE3NjUzNjYyODgsImp0aSI6ImEwOTIyOGU0NTBjY
jQxNzA5ZGM1MmM1OTdlMTU2MTc3IiwidXNlcl9pZCI6IjEifQ.5OYP4cRnplJIg2Tf64yz0LDnczTpYp9wvb33OpCdISU"

"""