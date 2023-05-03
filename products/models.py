from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from django.core.validators import MaxValueValidator, MinValueValidator

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


# Categories
class Categories(MPTTModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
    )
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='catimages/', null=True, blank=True)

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="320" height="240" />'.format(self.image.url))
        return ""

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.name]
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' -> '.join(full_path[::-1])


# Categories Product
class Products(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    mrp = models.DecimalField(default=1, max_digits=16, decimal_places=2)
    sell_price = models.DecimalField(default=0, max_digits=16, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    metatag = models.TextField(null=True, default='', blank=True)
    category = models.ForeignKey('Categories', on_delete=models.DO_NOTHING, related_name='cat_pro', blank=True,
                                 null=True)
    labeltag = models.ForeignKey('LabelTag', on_delete=models.DO_NOTHING, related_name='pro_tags', blank=True,
                                 null=True)
    discount = models.ForeignKey('Discount', null=True, blank=True, related_name='dis_pro', on_delete=models.DO_NOTHING)
    precontent = models.TextField()
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='images/', default='default.png')
    image2 = models.ImageField(upload_to='images/', default='default.png')
    image3 = models.ImageField(upload_to='images/', default='default.png')

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="320" height="240" />'.format(self.image.url))
        return ""

    @property
    def thumbnail_preview2(self):
        if self.image2:
            return mark_safe('<img src="{}" width="320" height="240" />'.format(self.image2.url))
        return ""

    @property
    def thumbnail_preview3(self):
        if self.image3:
            return mark_safe('<img src="{}" width="320" height="240" />'.format(self.image3.url))
        return ""

    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products"
        ordering = ['-created_on']

    def __str__(self):
        return self.name


class Discount(models.Model):
    code = models.CharField(max_length=50,unique=True)
    percent_off = models.PositiveIntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()

    updated_on = models.DateTimeField(blank=True, auto_now=True)
    created_on = models.DateTimeField(blank=True, auto_now_add=True)

    class Meta:
        verbose_name_plural = "Discounts"

    def __str__(self):
        return self.code


# Comments for Products
class Comment(models.Model):
    name = models.CharField(max_length=300, null=True)
    email = models.CharField(max_length=300)
    content = models.TextField()
    product_name = models.ForeignKey('Products', on_delete=models.DO_NOTHING, related_name='product_comments',
                                     blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.name


# label for products
class LabelTag(models.Model):
    name = models.CharField(max_length=300, null=True)
    content = models.TextField()
    product_name = models.ForeignKey('Products', on_delete=models.DO_NOTHING, related_name='product_label',
                                     blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


# Ratings for products
class Ratings(models.Model):
    rating_review = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    username = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='rate_user', blank=True,null=True)
    product_name = models.ForeignKey('Products', on_delete=models.CASCADE, related_name='product_rating',
                                     blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('username', 'product_name')
        verbose_name_plural = 'Ratings'

    def __str__(self):
        return f'{self.username.username} rated {self.product_name.name} {self.rating_review}'
