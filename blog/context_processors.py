from blog.models import Announcement, ArticleImg, Carousel, Category, Article, Conf, Friend, Pay, Tag, Comment


def sidebar(request):
	# 所有文章类型
	category_list = Category.objects.all()

	# 文章大头图
	article_img = ArticleImg.objects.all()

	# 文章排行
	blog_top = Article.objects.all().values("id", "title", "view").order_by('-view')[0:6]

	# 标签
	tag_list = Tag.objects.all()

	# 评论
	comment = Comment.objects.all().order_by('-created_at')[0:6]

	# 友链
	friends = Friend.objects.all()

	# 轮播图
	carousel = Carousel.objects.all()

	# 公告
	announcement = Announcement.objects.all()

	return {
		'category_list': category_list,
		'article_img': article_img,
		'blog_top': blog_top,
		'tag_list': tag_list,
		'comment_list': comment,
		'friends': friends,
		'carousel_list': carousel,
		'announcement_list': announcement,
	}


def website_conf(request):
	conf = Conf.objects.first()
	if conf:
		return {
			'main_website': conf.main_website,
			'name': conf.name,
			'chinese_description': conf.chinese_description,
			'english_description': conf.english_description,
			'avatar_link': conf.avatar.url,
			'website_author': conf.website_author,
			'website_author_link': conf.website_author_link,
			'email': conf.email,
			'donate_img': conf.donate_img,
			'website_number': conf.website_number,
			'git': conf.git,
			'website_logo': conf.website_logo
		}
	else:
		return {
			'main_website': '',
			'name': '',
			'chinese_description': '',
			'english_description': '',
			'avatar_link': '',
			'website_author': '',
			'website_author_link': '',
			'email': '',
			'website_number': '',
			'git': '',
			'website_logo': ''
		}


if __name__ == '__main__':
	pass
