from django.db import models

class About(models.Model):
    profile_image = models.ImageField(upload_to='about/', blank=True, null=True)
    
    def __str__(self):
        return "About Section"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    href = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="projects/")


class ProjectSubDescription(models.Model):
    project = models.ForeignKey(Project, related_name="sub_descriptions", on_delete=models.CASCADE)
    text = models.TextField()


class ProjectTag(models.Model):
    project = models.ForeignKey(Project, related_name="tags", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to="tags/")  # upload logos/icons

    def __str__(self):
        return f"{self.project.title} - {self.name}"


class SocialLink(models.Model):
    name = models.CharField(max_length=100)
    href = models.URLField(blank=True, null=True)
    icon = models.ImageField(upload_to="socials/")

    def __str__(self):
        return self.name


class Education(models.Model):
    university = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    date = models.CharField(max_length=100)
    contents = models.TextField()

    def __str__(self):
        return f"{self.university} - {self.degree}"


class Review(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True, null=True)
    body = models.TextField()
    img = models.ImageField(upload_to="reviews/")

    def __str__(self):
        return f"{self.name} ({self.username})"