from .views import ParentList, ChildrenList
from rest_framework.routers import DefaultRouter
app_name = 'api'

router = DefaultRouter()
router.register('parent', ParentList, basename='parent')
router.register('child', ChildrenList, basename='child')
urlpatterns = router.urls