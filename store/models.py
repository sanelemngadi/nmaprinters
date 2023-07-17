from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

# class ProductImageVariation(models.Model):
#     name = models.CharField(max_length=300)
#     product = models.ForeignKey(Product)

# class ReviewReactions(models.Model):
#     sharp = models.BooleanField()
#     not_sharp = models.BooleanField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product)

#many to many relationship for product
# class ProductReview(models.Model):
#     heading = models.CharField("Review Heading", max_length=100)
#     name = models.CharField("Reviewer", max_length=30)
#     date_reviewed = models.DateTimeField(auto_now_add=True)
#     review = models.TextField()
#     reactions = models.ManyToManyField(ReviewReactions)


# class Category(models.Model):
#     name = models.CharField('Product Category Name')

# class Filter(models.Model):
#     name = models.CharField(max_length=50)

# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.TextField()
#     available = models.BooleanField()
#     price = models.FloatField()
#     ratings = models.FloatField()