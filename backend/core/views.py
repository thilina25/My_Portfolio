from rest_framework import viewsets
from .models import About, ContactMessage, Project, SocialLink, Education, Review
from .serializers import AboutSerializer, ContactMessageSerializer, ProjectSerializer, SocialLinkSerializer, EducationSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

@api_view(['POST'])
def contact_view(request):
    serializer = ContactMessageSerializer(data=request.data)
    if serializer.is_valid():
        # Save message to database
        serializer.save()

        # Prepare email
        visitor_name = serializer.validated_data['name']
        visitor_email = serializer.validated_data['email']
        visitor_message = serializer.validated_data['message']

        subject = f"New message from {visitor_name}"
        message_body = f"""
        You have received a new message from your portfolio contact form.

        Name: {visitor_name}
        Email: {visitor_email}

        Message:
        {visitor_message}
        """

        # Send email from your Gmail account to yourself
        try:
            send_mail(
                subject,
                message_body,
                settings.EMAIL_HOST_USER,      # FROM (your Gmail)
                [settings.EMAIL_HOST_USER],    # TO (your Gmail)
                fail_silently=False,
            )
        except Exception as e:
            # Optional: log error but still return success for the form
            print("Error sending email:", e)

        return Response({"success": "Message received!"}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class SocialLinkViewSet(viewsets.ModelViewSet):
    queryset = SocialLink.objects.all()
    serializer_class = SocialLinkSerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer