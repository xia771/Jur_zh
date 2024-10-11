from django.contrib import admin

from users.models import User

# Register your models here.
admin.site.site_header='小白的菜鸟客栈'
admin.site.site_title='小白的菜鸟客栈'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'address')  # 显示字段
    search_fields = ('username', 'phone')  # 支持搜索