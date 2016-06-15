# -*- coding=utf-8 -*-
from django.contrib import admin
from models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):   #自定义个文章类
#     list_display = ('title','desc','click_count',) #让这些数据在后台默认显示
#     list_display_links = ('title','desc',) #让这些数据可以连接修改
#     list_editable = ('click_count',) #让‘click_count' 可以直接修改
# #
#     # fields = ('title','desc','content')     #让‘文章’在后台只显示‘title’，‘desc'，‘content’选项
#     #exclude = ('title','desc','content')     #让‘文章’在后台不显示‘title’，‘desc'，‘content’选项
#     fieldsets = (   #将‘文章’分类显示
#         (None,{     #将要显示的数据
#             'fields': ('title', 'desc', 'content')
#         }),
#         ('高级设置', {
#             'classes': ('collapse',),   #将数据显示隐藏
#             'fields': ('click_count', 'is_recommend')
#         }),
#     )
#
    class Media:
            js = (
                '/static/js/kindeditor-4.1.10/kindeditor-min.js', #引入主文件
                '/static/js/kindeditor-4.1.10/lang/zh_CN.js',   #引入中文文件
                '/static/js/kindeditor-4.1.10/config.js',   #引入配置文件
            )
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article,ArticleAdmin )  #将ArticleAdmin添加进后台
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
