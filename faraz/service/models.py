from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
# Create your models here.

class person(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    first_name =  models.CharField(max_length= 30 , help_text= _("name"))
    last_name = models.CharField(max_length= 60)
    father_name = models.CharField(max_length= 30 , blank=True)
    birth_day = models.DateField()
    employ_date = models.DateField()
    expire_date = models.DateField()
    mobile_num = models.CharField(max_length= 11)
    phone_num = models.CharField(max_length= 13 , blank=True)
    address = models.CharField(max_length= 200 ,blank=True)
    account_num = models.CharField(max_length= 20 , blank=True)
    img = models.ImageField(blank=True)

    def __str__(self):
        return "{} - {} {}".format(self.user,self.first_name,self.last_name)
    class Meta:
        verbose_name = _('کارمند')
        verbose_name_plural = ('کارمندان')
class customer(models.Model):
    first_name =  models.CharField(max_length= 30 , help_text= _("name"))
    last_name = models.CharField(max_length= 60)
    father_name = models.CharField(max_length= 30 , blank=True , null=True)
    mobile_num = models.CharField(max_length= 11)
    job_name = models.CharField(max_length= 60 , blank=True , null=True)
    birth_day = models.DateField(blank=True , null=True)
    phone_num = models.CharField(max_length= 13 , blank=True , null=True)
    address = models.CharField(max_length= 200 ,blank=True , null=True)
    account_num = models.CharField(max_length= 20 , blank=True , null=True)
    email = models.EmailField(blank=True , null=True)

    def __str__(self):
        return "{} - {} {}".format(self.job_name,self.first_name,self.last_name)
    class Meta:
        verbose_name = _('مشتری')
        verbose_name_plural = ('مشتریان')



class product(models.Model):
    product_name = models.CharField(max_length=30)
    personal_persent = models.IntegerField()

    def __str__(self):
        return self.product_name 

    class Meta:
        verbose_name = _('خدمت')
        verbose_name_plural = ('خدمات')

class contract(models.Model):

    person_name = models.ForeignKey('person' , on_delete=models.SET_DEFAULT , default= 'no person' )
    date = models.DateField ()
    subject = models.CharField(max_length=60)
    customer_name = models.ForeignKey('customer', on_delete=models.PROTECT)
    description = models.TextField()
    transaction = models.BigIntegerField()
    cash_pay = models.BigIntegerField()
    duration = models.DurationField()
    product = models.ForeignKey('product' , on_delete=models.PROTECT)

    def __str__(self):
        return "{} - {} ".format(self.customer_name,self.subject  )
    class Meta:
        verbose_name = _('قرارداد')
        verbose_name_plural = ('قراردادها')

class recive_cheque(models.Model):
    STATUS_CHOICES=(
        ('w','در انتظار وصول'),
        ('p', 'وصول شد'),
        ('i', 'برگشت خورد'),
        ('r', 'در انتظار دریافت')

    )
    customer_name = models.ForeignKey( 'customer',on_delete = models.SET_NULL , null= True )
    contract = models.ForeignKey(contract,on_delete = models.SET_NULL , null= True )
    cheque_amount = models.BigIntegerField(verbose_name ='مبلغ چک',)
    income_date = models.DateField()
    recive_date = models.DateField()
    pay_name = models.CharField(max_length=30)
    status = models.CharField(max_length=1 , choices=STATUS_CHOICES)

    def __str__(self):
        return "{} - {} {}".format(self.customer_name,self.cheque_amount ,self.income_date )
    class Meta:
        verbose_name = _('چک')
        verbose_name_plural = ('چک های دریافتی')

class karbarg(models.Model):
    person_name = models.ForeignKey('person' , on_delete=models.PROTECT)
    job_date = models.DateField()
    contract = models.ForeignKey('contract' , on_delete=models.PROTECT)
    cash_pay = models.BigIntegerField()
    description = models.TextField()
    product_name = models.ForeignKey('product' , on_delete=models.PROTECT)
    def __str__(self):
        return "{}  -  {}  -  {}".format(self.contract , self.product_name , self.cash_pay)
    class Meta:
        verbose_name = _('کاربرگ')
        verbose_name_plural = (' کاربرگ ها')


class msg(models.Model):
    is_replay = models.BooleanField(default=False)
    is_ticket = models.BooleanField(default=False)
    sender = models.CharField(max_length=30)
    reciver = models.CharField(max_length=30)
    datetime = models.DateTimeField()
    subject = models.CharField(max_length=30)
    text = models.TextField()
