from django.db import models
from users.models import Account
from django.shortcuts import reverse
from django.conf import settings
choices = (
    ('Public','Public'),
    ('Private','Private')
)
class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Name = models.CharField(max_length=100,blank=True,null=True)
    Background_Image = models.ImageField(blank=True,null=True)

    Subheading1 = models.CharField(max_length=100,blank=True,null=True)
    Image1 = models.ImageField()# Required Fields
    Description = models.TextField() # Required Fields

    Subheading2 = models.CharField(max_length=100, blank=True, null=True)
    Image2 = models.ImageField(blank=True, null=True)
    Paragraph2 = models.TextField(blank=True,null=True)

    Subheading3 = models.CharField(max_length=100, blank=True, null=True)
    Image3 = models.ImageField(blank=True, null=True)
    Paragraph3 = models.TextField(blank=True,null=True)

    Date = models.DateField(auto_now_add=True,blank=True,null=True)

    Video = models.FileField(blank=True,null=True,upload_to="Videos")

    slug = models.SlugField(blank=True,null=True,unique=True)

    coments = models.ManyToManyField("Comments",blank=True)

    # mode
    Mode = models.CharField(max_length=10,blank=True,null=True,choices=choices,default='Public')
    def get_abs_url(self):
        return reverse(viewname="Blog:BlogView",
                       kwargs={'slug':self.slug}

                       )

# Model to add Comments to Blog
class Comments(models.Model):
    Name = models.CharField(blank=True,null=True,max_length=50)
    Comment = models.TextField()
    Date = models.DateTimeField(auto_now_add=True,blank=True,null=True)

