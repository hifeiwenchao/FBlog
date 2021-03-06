from django.contrib import admin

# Register your models here.
from django import forms
from import_export.admin import ImportExportModelAdmin
from blog.models import About, Announcement, ArticleImg, Carousel, Friend, SiteUser, Subscription, UserInfo, Tag, \
    Article, Category, \
    Comment, Pay, Conf


# @admin.register(UserInfo)
class UserInfoAdmin(admin.StackedInline):
    model = UserInfo
    fields = (
        'avatar',
        'mobile',
        # 'sex',
        'wechat',
        'qq',
        'blog_address',
        'introduction',
    )


@admin.register(SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
    inlines = [
        UserInfoAdmin,
    ]
    readonly_fields = [
        'username',
        'password',
    ]
    list_display = (
        'username',
        'password',
        'email',
        'time_joined',
    )


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """
    订阅
    """
    list_display = (
        'email',
        'sub_time'
    )


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    """
    关于
    """
    list_display = (
        'contents',
    )


@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    """
    友链
    """
    list_display = (
        'url',
        'title',
        'name'
    )


@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    """
    首页轮播图配置
    """
    list_display = (
        'carousel_title',
        'carousel',
        'img_link_title',
        'img_alt'
    )


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    """
    公告
    """
    list_display = (
        'head_announcement',
        'main_announcement'
    )


class ConfForm(forms.ModelForm):
    website_number = forms.CharField(required=False)

    class Meta:
        model = Conf
        fields = '__all__'


@admin.register(Conf)
class ConfAdmin(ImportExportModelAdmin):
    """
    网站配置信息
    """
    form = ConfForm

    list_display = (
        'main_website',
        'website_number',
        'name',
        'chinese_description',
        'english_description',
        'email',
        'website_logo'
    )
    fieldsets = (
        ('网站配置信息', {
            'fields': (
                'main_website',
                'website_number',
                'donate_img',
                'website_logo'
            )
        }),
        ('作者信息', {
            'fields': (
                'name',
                'chinese_description',
                'english_description',
                'avatar',
                'website_author',
                'website_author_link',
                'email',
                'git'
            )
        }),
    )


@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    """
    文章
    """
    date_hierarchy = 'date_time'
    list_display = (
        'title',
        'category',
        'date_time',
        'content_validity',
        'digest',
        'author',
        'view',
        'comment',
        'picture'
    )
    list_filter = ('category', 'author')
    filter_horizontal = ('tag',)


@admin.register(ArticleImg)
class ArticleImgAdmin(admin.ModelAdmin):
    """
    文章大头图
    """
    list_display = (
        'img_title',
        'url',
        'images',
        'article_img',
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    文章类型
    """
    list_display = (
        'name',
        'created_time',
        'last_mod_time'
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    标签
    """
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    评论
    """
    list_display = (
        'title',
        'comment',
        'user_name',
        'email',
        'url',
        'url_input',
        'create_time',
    )
