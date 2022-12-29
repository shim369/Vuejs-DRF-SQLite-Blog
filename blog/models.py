from django.db import models

class Category(models.Model):
	name = models.CharField('category', max_length=20)

	def __str__(self):
		return self.name
		
class Article(models.Model):
	title = models.CharField('title', max_length=40)
	description = models.CharField('description', max_length=500, null=True)
	thumbnail = models.ImageField('thumbnail', blank=True, null=True)
	main_text = models.TextField('main_text',blank=True)
	article_body = models.CharField('article_body', max_length=3000, null=True)
	created_at = models.DateTimeField('created_at', auto_now_add=True)
	updated_at = models.DateField('updated_at', auto_now=True)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='category')

	class Meta:
		ordering = ('-created_at',)

	def __str__(self):
		return self.title

	# def get_absolute_url(self):
	# 	return reverse('detail', args=[self.slug])

	# def save(self, *args, **kwargs):
	# 	if not self.slug:
	# 		self.slug = slugify(self.title)
	# 	super(Article, self).save(*args, **kwargs)