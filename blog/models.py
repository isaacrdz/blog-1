from django.db import models

# Create your models here.
class Post(models.Model):
	header = models.CharField(max_length=50)
	image = models.ImageField(upload_to='blog')
	content = models.TextField()
  	timestamp = models.DateTimeField(auto_now_add=True)
  	slug = models.SlugField(max_length=100, blank=True)
  	

  	def __unicode__(self):
  		return self.header

  	def get_absolute_url(self):
		return '/blog/%s/' % self.slug
