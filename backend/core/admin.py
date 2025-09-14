from django.contrib import admin
from .models import About, ContactMessage, Project, ProjectImage, ProjectSubDescription, ProjectTag, SocialLink, Education, Review


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile_image')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("created_at",)
    
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectSubDescriptionInline(admin.TabularInline):
    model = ProjectSubDescription
    extra = 1


class ProjectTagInline(admin.TabularInline):
    model = ProjectTag
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "href")
    inlines = [ProjectImageInline, ProjectSubDescriptionInline, ProjectTagInline]


admin.site.register(SocialLink)
admin.site.register(Education)
admin.site.register(Review)