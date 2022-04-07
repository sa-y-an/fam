from .views import ParentList, ChildrenList
from rest_framework.routers import SimpleRouter
app_name = 'api'

router = SimpleRouter()
router.register('parent', ParentList, basename='parent')
router.register('child', ChildrenList, basename='child')
urlpatterns = router.urls