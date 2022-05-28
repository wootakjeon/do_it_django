from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Post)
class BoardAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = (
        'title',
        'text',
        'author_id',
        'created_bd',
        'updated_bd',
        'show_ct',
        'photo'
    )
    list_display_links = list_display