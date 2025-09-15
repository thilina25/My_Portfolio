from rest_framework import serializers
from .models import About, ContactMessage, Project, ProjectImage, ProjectSubDescription, ProjectTag, SocialLink, Education, Review

class AboutSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(use_url=True)
    class Meta:
        model = About
        fields = "__all__"

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"
        
class ProjectImageSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source="image", use_url=True)
    class Meta:
        model = ProjectImage
        fields = ["id", "image_url"]


class ProjectSubDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSubDescription
        fields = ["id", "text"]


class ProjectTagSerializer(serializers.ModelSerializer):
    path = serializers.ImageField(source="icon", use_url=True)
    class Meta:
        model = ProjectTag
        fields = ["id", "name", "path"]


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)
    subDescriptions = ProjectSubDescriptionSerializer(many=True, read_only=True, source="sub_descriptions")
    tags = ProjectTagSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ["id", "title", "description", "href", "images", "subDescriptions", "tags"]


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