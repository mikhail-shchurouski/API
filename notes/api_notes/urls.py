from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('notes', NoteViewSet)
urlpatterns = router.urls