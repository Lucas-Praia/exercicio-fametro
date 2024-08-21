from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class User(AbstractUser, PermissionsMixin):
    username = models.CharField(
        db_column='tx_username',
        max_length=64,
        unique=True,
        verbose_name='Nome de Usuário'
    )
    password = models.CharField(
        db_column='tx_password',
        max_length=104,
        verbose_name='Senha'
    )
    name = models.CharField(
        db_column='tx_name',
        max_length=256,
        null=True,
        blank=True,
        verbose_name='Nome Completo'
    )
    email = models.CharField(
        db_column='tx_email',
        max_length=256,
        null=True,
        blank=True,
        verbose_name='E-mail'
    )
    last_login = models.DateTimeField(
        db_column='dt_last_login',
        null=True,
        verbose_name='Último Login'
    )
    is_active = models.BooleanField(
        db_column='cs_active',
        default=True,
        verbose_name='Ativo'
    )
    is_superuser = models.BooleanField(
        db_column='cs_superuser',
        default=False,
        verbose_name='Superusuário'
    )
    is_staff = models.BooleanField(
        db_column='cs_staff',
        default=False,
        verbose_name='Membro da Equipe'
    )
    is_default = models.BooleanField(
        db_column='cs_default',
        default=False,
        verbose_name='Padrão'
    )

    def __str__(self):
        return self.username

    class Meta:
        managed = True
        db_table = 'auth_user'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['username']

class Brand(models.Model):
    name = models.CharField(
        db_column='tx_name',
        max_length=250,
        verbose_name='Name'
    )
    
    description = models.TextField(
        db_column='tx_description',
        null=True,
        blank=True,
        verbose_name='Description'
    )
    
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        verbose_name='Created at'
    )
    
    updated_at = models.DateTimeField(
        db_column='dt_updated',
        auto_now=True,
        verbose_name='Updated at'
    )
    
    class Meta:
        db_table = 'brand'
        ordering = ['name']
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        db_column='tx_name',
        max_length=250,
        verbose_name='Name'
    )
    
    description = models.TextField(
        db_column='tx_description',
        null=True,
        blank=True,
        verbose_name='Description'
    )
    
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        verbose_name='Created at'
    )
    
    updated_at = models.DateTimeField(
        db_column='dt_updated',
        auto_now=True,
        verbose_name='Updated at'
    )
    
    class Meta:
        db_table = 'category'
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name


class Inflow(models.Model):
    supplier = models.ForeignKey(
        'Supplier',
        on_delete=models.PROTECT,
        related_name='inflows',
        db_column='id_supplier',
        verbose_name='Supplier'
    )
    
    product = models.ForeignKey(
        'Product',
        on_delete=models.PROTECT,
        related_name='inflows',
        db_column='id_product',
        verbose_name='Product'
    )
    
    quantity = models.IntegerField(
        db_column='nu_quantity',
        verbose_name='Quantity'
    )
    
    description = models.TextField(
        db_column='tx_description',
        null=True,
        blank=True,
        verbose_name='Description'
    )
    
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        verbose_name='Created at'
    )
    
    updated_at = models.DateTimeField(
        db_column='dt_updated',
        auto_now=True,
        verbose_name='Updated at'
    )
    
    class Meta:
        db_table = 'inflow'
        #ordenação descendente
        ordering = ['-created_at']
        verbose_name = 'Inflow'
        verbose_name_plural = 'Inflows'
     #retorna como string porque quando nao tiver produto cadastrado ele iria retornar valor nulo e daria conflito com __str__
    def __str__(self):
        return str(self.product)


class Outflow(models.Model):
    product = models.ForeignKey(
        'Product',
        on_delete=models.PROTECT,
        related_name='outflows',
        db_column='id_product',
        verbose_name='Product'
    )
    
    quantity = models.IntegerField(
        db_column='nu_quantity',
        verbose_name='Quantity'
    )
    
    description = models.TextField(
        db_column='tx_description',
        null=True,
        blank=True,
        verbose_name='Description'
    )
    
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        verbose_name='Created at'
    )
    
    updated_at = models.DateTimeField(
        db_column='dt_updated',
        auto_now=True,
        verbose_name='Updated at'
    )
    
    class Meta:
        db_table = 'outflow'
         #ordenação é descendente
        ordering = ['-created_at']
        verbose_name = 'Outflow'
        verbose_name_plural = 'Outflows'
     #retorna como string porque quando nao tiver produto cadastrado ele iria retornar valor nulo e daria conflito com __str__
    def __str__(self):
        return str(self.product)


class Product(models.Model):
    title = models.CharField(
        db_column='tx_title',
        max_length=250,
        verbose_name='Title'
    )
    
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='products',
        db_column='id_category',
        verbose_name='Category'
    )
    
    brand = models.ForeignKey(
        'Brand',
        on_delete=models.PROTECT,
        related_name='products',
        db_column='id_brand',
        verbose_name='Brand'
    )
    
    description = models.TextField(
        db_column='tx_description',
        null=True,
        blank=True,
        verbose_name='Description'
    )
    
    serie_number = models.CharField(
        db_column='tx_serie_number',
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Serie Number'
    )
    
    cost_price = models.DecimalField(
        db_column='nu_cost_price',
        max_digits=20,
        decimal_places=2,
        verbose_name='Cost Price'
    )
    
    selling_price = models.DecimalField(
        db_column='nu_selling_price',
        max_digits=20,
        decimal_places=2,
        verbose_name='Selling Price'
    )
    
    quantity = models.IntegerField(
        db_column='nu_quantity',
        default=0,
        verbose_name='Quantity'
    )
    
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        verbose_name='Created at'
    )
    
    updated_at = models.DateTimeField(
        db_column='dt_updated',
        auto_now=True,
        verbose_name='Updated at'
    )
    
    class Meta:
        db_table = 'product'
        ordering = ['title']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.title


class Supplier(models.Model):
    name = models.CharField(
        db_column='tx_name',
        max_length=250,
        verbose_name='Name'
    )
    
    description = models.TextField(
        db_column='tx_description',
        null=True,
        blank=True,
        verbose_name='Description'
    )
    
    created_at = models.DateTimeField(
        db_column='dt_created',
        auto_now_add=True,
        verbose_name='Created at'
    )
    
    updated_at = models.DateTimeField(
        db_column='dt_updated',
        auto_now=True,
        verbose_name='Updated at'
    )
    
    class Meta:
        db_table = 'supplier'
        ordering = ['name']
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'
    
    def __str__(self):
        return self.name
