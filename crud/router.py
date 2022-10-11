from myapp.viewsets import userViewset
from rest_framework import routers

router= routers.DefaultRouter()
router.register('user',userViewset)