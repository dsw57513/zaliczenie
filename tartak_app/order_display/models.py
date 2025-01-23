from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from unidecode import unidecode
from django.urls import reverse
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = Order.Status.PUBLISHED)


class Client(models.Model):
    first_name = models.CharField(max_length=20,blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    phone_number = models.IntegerField(blank = True)
    slug = models.SlugField(max_length=255,blank=True, unique=True)
    
    def __str__(self):
        return self.last_name
    
    def get_absolute_url(self):
        return reverse("client_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            if not Client.objects.all():
                next_id = 1
            else:
                next_id = Client.objects.order_by('-pk').first().pk + 1
            self.slug = slugify(unidecode(f"{next_id}_{self.first_name}_{self.last_name}"))
        super(Client, self).save(*args, **kwargs)


    
    
class Order(models.Model):
    objects = models.Manager()
    published = PublishedManager()
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        FINISHED = 'FI', 'Finished'
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               related_name='order',
                               blank = True)
    created = models.DateField(default = timezone.now)
    due = models.DateField(default = timezone.now, blank=True)
    slug = models.SlugField(max_length=255, blank=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.PUBLISHED)
    adres = models.CharField(max_length=255, blank=True)
    workers = models.ManyToManyField(User)
    def __str__(self):
        return self.status
    
    def get_absolute_url(self):
        return reverse("order_display:order_detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            if not Order.objects.all():
                next_id = 1
            else:
                next_id = Order.objects.order_by('-pk').first().pk + 1
            self.slug = slugify(unidecode(f"{next_id}_{self.due}"))
        super(Order, self).save(*args, **kwargs)
    


class Element(models.Model):
    class Units(models.TextChoices):
        SZTUKI = 'szt'
        M3 = 'm3'
        MB = 'mb'
    class Status(models.TextChoices):
        DONE = 'zrobione'
        IN_PROGRESS = 'do zrobienia'
    name = models.CharField(max_length=20, blank=True)
    width = models.FloatField(blank=True)
    height = models.FloatField(blank=True)
    length = models.FloatField(blank=True)
    count = models.IntegerField(blank=True)
    volume = models.FloatField(blank=True)
    unit = models.CharField(max_length=3,
                              choices=Units.choices,
                              default=Units.M3)
    status = models.CharField(max_length = 12,
                              choices = Status.choices,
                              default = Status.IN_PROGRESS)
    description = models.TextField(blank = True)
    order = models.ForeignKey(Order,
                              on_delete=models.CASCADE,
                              related_name='element')
    slug = models.SlugField(max_length=255)
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("order_display:order_detail", args=[self.slug])
    
    def save(self, *args, **kwargs):
        if self.unit==self.Units.SZTUKI:
            self.volume = self.width*self.height*self.length*self.count/1000000
        elif self.unit==self.Units.MB:
            self.volume = self.width*self.height*self.length*(self.length/self.count)/1000000
        else:
            self.volume = self.count
            
        if not self.slug:
            if not Element.objects.all():
                next_id = 1
            else:
                next_id = Element.objects.order_by('-pk').first().pk + 1
            self.slug = slugify(unidecode(f"{next_id}_{self.name}"))
        
        super(Element, self).save(*args, **kwargs)
    