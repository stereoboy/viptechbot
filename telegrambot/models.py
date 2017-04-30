from django.db import models


#class Pose(models.Model):
#  register_date = models.DateTimeField(auto_now=True)
#  english_name = models.CharField(max_length=256)
#  sanskrit_name = models.CharField(max_length=256, default=None, null=True, blank=True)
#  korean_name = models.CharField(max_length=256, default=None, null=True, blank=True)
#  pose_image = models.ImageField(upload_to='pose_images')
#  parents = models.ManyToManyField('self')
#
#class Author(models.Model):
#  #author_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#  name = models.CharField(max_length=256)
#  nick_name = models.CharField(max_length=256, default='')
#
#class Class(models.Model):
#  #class_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#  author = models.ForeignKey(Author)
#  name = models.CharField(max_length=256)
#
#class Lesson(models.Model):
#  author = models.ForeignKey(Author)
#  yoga_class = models.ForeignKey(Class)
#  name = models.CharField(max_length=256)
#
#class Sequence(models.Model):
#  name = models.CharField(max_length=256)
#  register_date = models.DateTimeField(auto_now=True)
#  author = models.CharField(max_length=256)
#  pose = models.ForeignKey(Pose, default=None)
#
#
