from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AboutViewSet, contact_view, ProjectViewSet, SocialLinkViewSet, EducationViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'about', AboutViewSet)
router.register("projects", ProjectViewSet, basename="projects")
router.register("socials", SocialLinkViewSet, basename="socials")
router.register("education", EducationViewSet, basename="education")
router.register("reviews", ReviewViewSet, basename="reviews")

urlpatterns = [
    path('', include(router.urls)),
    path("contact/", contact_view, name="contact"),
]