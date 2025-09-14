from rest_framework import serializers
from .models import About, ContactMessage, Project, ProjectImage, ProjectSubDescription, ProjectTag, SocialLink, Education, Review

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'profile_image']

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"
        
class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ["image"]


class ProjectSubDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSubDescription
        fields = ["text"]


class ProjectTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectTag
        fields = ["name", "icon"]


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    sub_descriptions = ProjectSubDescriptionSerializer(many=True, read_only=True)
    tags = ProjectTagSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "title", "description", "href", "images", "sub_descriptions", "tags"]


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = "__all__"


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"