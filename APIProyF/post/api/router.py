from rest_framework.routers import DefaultRouter
from post.api.views import PostApiViewsSet

router_post = DefaultRouter()

router_post.register(prefix='post', basename='post', viewset=PostApiViewsSet)