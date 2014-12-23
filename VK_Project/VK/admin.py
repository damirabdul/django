from django.contrib import admin
from VK.models import UserInfo, Post, Like, DisLike

admin.site.register(Like)
admin.site.register(DisLike)


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_text', 'post_date')
    list_filter = ['post_date']
    search_fields = ['post_text']
    fieldsets = [
        ('Users information', {'fields': ['from_whom', 'to_who']}),
        ('Date information', {'fields': ['post_date'], 'classes': ['collapse']}),
        ('Post information', {'fields': ['post_text']})
    ]


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'sex')
    fieldsets = [
        ('User information', {'fields': ['user'], 'classes': ['collapse']}),
        ('Information', {'fields': ['city', 'birthday', 'interests', 'avatar', 'sex']}),
        ('Friends information', {'fields': ['friends']})
    ]


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(Post,PostAdmin)
