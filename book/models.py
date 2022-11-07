from django.db import models
from student.models import Student
from myuser.models import MyUser
# Create your models here.
class BookCategory(models.Model):
    categoryName = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.categoryName


class Book(models.Model):
    bookname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='book/')
    bookcode = models.CharField(max_length=100,unique=True)
    author = models.CharField(max_length=200,verbose_name="Author Name",help_text="Ram kumar")
    category = models.ForeignKey(BookCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.bookname

class BorrowRequest(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    orderDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.student.user.fullname

class BookIssue(models.Model):
    borrowRequest = models.OneToOneField(BorrowRequest,on_delete=models.CASCADE)
    issuedBy = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    returnDate = models.DateField()

    def __str__(self):
        return self.borrowRequest.book
