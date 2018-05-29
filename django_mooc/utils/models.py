from django.db import models


class DateTimeBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Slugged(models.Model):
    title = models.CharField(max_length=500)
    slug = models.SlugField(max_length=200, unique=True, null=True,blank=True)


    class Meta:
        abstract = True

    def __unicode__(self):
        return u"%s" % self.title

    def __str__(self):
        return self.title
