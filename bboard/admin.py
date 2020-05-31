from django.contrib import admin

from .models import Bb, Rubric, Comment


class BbAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "content",
        "name_author",
        "published",
        "rubric",
    )
    list_display_links = ("title", "content")
    search_fields = ("title", "content")


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric)
admin.site.register(Comment)
