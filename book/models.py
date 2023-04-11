from django.db import models


class BookISBN(models.Model):
    isbn = models.CharField(max_length=50, verbose_name="图书ISBN")

    def __str__(self):
        return self.isbn


class AuthorInfo(models.Model):
    id = models.CharField(max_length=30, verbose_name="身份证号", primary_key=True)
    name = models.CharField(max_length=20, verbose_name="姓名")
    telephone = models.CharField(max_length=20, verbose_name="联系方式")
    age = models.IntegerField(verbose_name="年龄", default=30)
    sex = models.CharField(max_length=2, verbose_name="性别", default="男")

    def __str__(self):
        return self.name


class BookClass(models.Model):
    name = models.CharField(max_length=20, verbose_name='图书类别')

    def __str__(self):
        return self.name


class BookInfoManager(models.Manager):

    def all(self):
        books = super().all()
        books = books.filter(status=True)
        return books

    def create_bookinfo(self, name):
        m = self.model()
        m.name = name
        m.save()
        return m


class BookInfo(models.Model):
    # bookisbn = models.OneToOneField(BookISBN, on_delete=models.CASCADE)
    # authorinfo = models.ManyToManyField(AuthorInfo)
    # bookclass = models.ForeignKey(BookClass, on_delete=models.CASCADE, verbose_name='图书类别', null=True, blank=True)
    # name = models.CharField(max_length=30, verbose_name='图书名称')
    # price = models.IntegerField(default=20, verbose_name='价格')
    # author = models.IntegerField(default=20, verbose_name='价格')
    # image = models.ImageField(upload_to="upload/%Y/%m", default="upload/default.jpg", verbose_name='封面')
    # desc = models.CharField(max_length=200, verbose_name='图书简介', default="")
    # ishot = models.BooleanField(verbose_name='是否畅销', default=True)
    # moredesc = models.TextField(default="", verbose_name='更多介绍')
    name = models.CharField(max_length=30, verbose_name='图书名称')
    price = models.IntegerField(default=20, verbose_name='价格')
    author = models.IntegerField(default=20, verbose_name='价格')
    status = models.BooleanField(default=True)
    objects = BookInfoManager()

    def __str__(self):
        return self.name
