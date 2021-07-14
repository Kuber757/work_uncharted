from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User Model
    """

    PROFESSION_CHOICE = (
        (None, 'Profession'),
        ('ART', 'Architect'),
        ('ID', 'Interior Designer'),
        ('DTR', 'Distributer'),
        ('HTL', 'Hotel'),
        ('CTR', 'Contractor'),
        ('PNM', 'Press & Media'),
        ('OTH', 'Others'),
    )

    name = models.CharField(
        _('first name'),
        max_length=150,
    )

    email = models.EmailField(
        _('Email'),
        unique=True,
    )

    company_name = models.CharField(
        _('Company Name'),
        max_length=50,
    )

    website_name = models.CharField(
        _('Website Name'),
        max_length=100,
    )

    profession = models.CharField(
        _('Profession'),
        choices=PROFESSION_CHOICE,
        max_length=3,
        null=True,
        blank=True,
    )

    is_staff = models.BooleanField(
        _('Staff Status'),
        default=False,
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name',
    ]

    class Meta:
        ordering = ['-id', ]
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super(self.__class__, self).clean()
        self.email = self.__class__.objects.normalize_email(self.email)

def get_urls(view = "Desktop_View", type = "materials", pk=1, num_img = 5):
    li = ['images/Desktop_View/singapore/' + str(i) + '.jpg' for i in range(1,16)]
    return li

#projects section
class projects:
    def __init__(self, pk, name, num_img, url_list, small_url):
        self.cat = "pro" + str(pk)
        self.pk = pk
        self.name = name
        self.num_img = num_img
        self.url_list = url_list
        self.display = small_url

li = ['images/Desktop_View/singapore/' + str(i) + '.jpg' for i in range(1,16)]
small_url = ['images/Desktop_View/singapore/' + str(i) + '.jpg' for i in range(1,9)]
projects_list = [
    projects(1,'PARK HYATT VIENNAE', 13, li, small_url),
    projects(2,'PRIVATE RESENDENCIES', 5, li, small_url),
    projects(3,'SINGAPORE', 3, li, small_url),
    projects(4,'RIO', 8, li, small_url),
    projects(5,'SHANGHAI', 8, li, small_url),
    projects(6,'PARIS', 6, li, small_url),
    projects(7,'YATCH', 6, li, small_url),
    projects(8,'GRAND HYATT GURGAON', 6, li, small_url),
    projects(9,'CAPETOWN', 6, li, small_url),
    projects(10,'MILAN', 6, li, small_url),
    projects(11,'NEWYORK', 6, li, small_url),
    projects(12,'CLASS 55 YACHT', 6, li, small_url),
    projects(13,'KL WELLNESS CENTER', 6, li, small_url),
    projects(14,'OFFICE', 6, li, small_url),
]


#collections section
class collections:
    def __init__(self, pk, name, num_img, url_list, small_url):
        self.cat = "col" + str(pk)
        self.pk = pk
        self.name = name
        self.num_img = num_img
        self.url_list = url_list
        self.display = small_url

li = ['images/Desktop_View/vases/' + str(i) + '.jpg' for i in range(1,26)]
small_url = ['images/Desktop_View/vases/' + str(i) + '.jpg' for i in range(1,10)]
collections_list = [
    collections(1,'VASES', 13, li, small_url),
    collections(2,'LIGHTS', 13, li, small_url),
    collections(3,'TABLES', 13, li, small_url),
    collections(4,'LAMPS', 13, li, small_url),
    collections(5,'CHAIRS', 13, li, small_url),
    collections(6,'BOWLS', 13, li, small_url),
    collections(7,'CABINS', 13, li, small_url),
    collections(8,'BRASS FURNITURE', 13, li, small_url),
    collections(9,'ACCESSORY SETS', 13, li, small_url),
    collections(10,'BATHROOM SETS', 13, li, small_url),
    collections(11,'BONE & HORN', 13, li, small_url),
    collections(12,'CARPETS', 13, li, small_url),
    collections(13,'CUSHIONS', 13, li, small_url),
    collections(14,'TRAY', 13, li, small_url),
]


#materials section
class materials:
    def __init__(self, pk, name, num_img, url_list,col_list=[],pro_list=[]):
        self.cat = "mat" + str(pk)
        self.pk = pk
        self.name = name
        self.num_img = num_img
        self.url_list = url_list
        self.collections = col_list
        self.projects = pro_list
        self.display = url_list[:8]

li = ['images/Desktop_View/selenite/' + str(i) + '.jpg' for i in range(1,23)]
materials_list = [
    materials(1,'SEMI PRECIOUS STONE', 13, li, [1,3,5], [2,3]),
    materials(2,'STRAW MACQUERTY', 13, li, [2,3], [1,]),
    materials(3,'GLASS', 13, li, [5,], [1,4]),
    materials(4,'MOTHER OF PEARL', 13, li, [6,7], [3,5]),
    materials(5,'STONE', 13, li),
    materials(6,'SELENITE', 13, li),
    materials(7,'STINGRAY', 13, li),
    materials(8,'GRAND HYATT GURGAON', 13, li),
    materials(9,'BRASS', 13, li),
    materials(10,'LEATHER', 13, li),
    materials(11,'WOOD', 13, li),
    materials(12,'PARCHMENT', 13, li),
    materials(13,'BONE', 13, li),
    materials(14,'BONE', 13, li),
    materials(15,'HORN', 13, li),
    materials(16,'LEAFING', 13, li),
    materials(17,'LACQUERWARE', 13, li),
    materials(18,'NATURE MATERIAL', 13, li),
]
